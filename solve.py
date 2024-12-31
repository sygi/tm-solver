"""Tries to solve a given problem."""

from typing import Self
import codes
import proposals as props

class Query:
    def __init__(self, code: codes.Code, verifier_card_index: int, num_verifier_cards: int):
        self.code = code
        self.verifier_card_index = verifier_card_index
        self.num_verifier_cards = num_verifier_cards

    def __repr__(self) -> str:
        return f"{self.code=} {self.verifier_card_index=} {self.num_verifier_cards=}"

    def next_query(self) -> Self | None:
        if self.verifier_card_index != self.num_verifier_cards - 1:
            return type(self)(self.code, self.verifier_card_index + 1, self.num_verifier_cards)
        else:
            return self.next_code()

    def next_code(self) -> Self | None:
        next_code = self.code.next_code()
        if next_code is None:
            return None
        return type(self)(next_code, 0, self.num_verifier_cards)

def distinguishes(code: codes.Code, verifiers: list[props.Verifier]) -> bool:
    """Whether code distinguishes between some of the verifiers."""
    acceptance = [v.check(code) for v in verifiers]
    return len(set(acceptance)) > 1

def solve(
    proposals: list[props.Proposal], next_to_check=None, depth=0, best_so_far=10000) -> None | tuple[list[tuple[codes.Code, int, bool]], codes.Code]:
    """The shortest sequence of moves to solve the problem and the solution."""
    if depth >= best_so_far:
        # Not worth looking so far from the tree: we already have a better solution.
        return None
    # TODO: store both code and the verifier card to check next.
    if len(proposals) == 1:
        return [], proposals[0].accepted_codes()[0]
    next_to_check = next_to_check or Query(codes.Code(111), 0, len(proposals[0].verifiers))
    plausible_options = []
    verifier_cards = []
    for v in zip(*[p.verifiers for p in proposals], strict=True):
        # v = all kth verifiers across proposals
        plausible_options.append(set([kth_v.option for kth_v in v]))
        verifier_cards.append(v[0].verifier_card)
        assert all([kth.verifier_card == verifier_cards[-1] for kth in v])

    remaining_verifiers = []
    for i, options in enumerate(plausible_options):
        # TODO: move verifiers to verifiers module
        remaining_verifiers.append(
            [props.Verifier(verifier_cards[i], o) for o in options]
        )

    best = None
    while next_to_check is not None:
        v_i = next_to_check.verifier_card_index
        if not distinguishes(next_to_check.code, remaining_verifiers[v_i]):
            next_to_check = next_to_check.next_query()
            continue
        new_true_verifiers, new_false_verifiers = [], []
        for v in remaining_verifiers[v_i]:
            if v.check(next_to_check.code):
                new_true_verifiers.append(v)
            else:
                new_false_verifiers.append(v)

        assert next_to_check is not None  # for type checker
        new_verifiers = remaining_verifiers[:v_i] + [new_true_verifiers] + remaining_verifiers[v_i + 1:]
        new_proposals = [
            p for p in proposals if p.consistent_with_verifiers(new_verifiers)
        ]
        # Note: we don't need to check for solvability nor redundancy, all new
        # proposals are a subset of old proposals and we already checked them.
        assert len(new_proposals) < len(proposals)
        current_best = len(best) if best is not None else 10_000
        solution1 = solve(new_proposals, next_to_check, depth+1, current_best)

        new_verifiers = remaining_verifiers[:v_i] + [new_false_verifiers] + remaining_verifiers[v_i + 1:]
        new_proposals = [
            p for p in proposals if p.consistent_with_verifiers(new_verifiers)
        ]
        assert len(new_proposals) < len(proposals)
        solution2 = solve(new_proposals, next_to_check, depth+1, current_best)

        if solution1 is None or solution2 is None:
            next_to_check = next_to_check.next_query()
            continue
        # We are looking for the shortest solution to the most difficult problem.
        true_branch = len(solution1[0]) > len(solution2[0])
        worse_branch = solution1[0] if true_branch else solution2[0]
        the_code = solution1[1] if true_branch else solution2[1]

        if best is None or len(worse_branch) + 1 < len(best[0]):
            best = [(next_to_check.code, new_verifiers[v_i][0].verifier_card, true_branch)] + worse_branch, the_code

        next_to_check = next_to_check.next_query()

    if best is not None:
        assert 2**len(best[0]) >= len(proposals)
    return best
