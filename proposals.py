"""Code handling solution proposals."""

from typing import Iterator, Self
import codes
import verifiers



class Verifier:
    def __init__(self, verifier_card: int, option: int):
        self.verifier_card = verifier_card
        self.option = option

    def __repr__(self):
        return f"Verifier(verifier_card={self.verifier_card}, option={self.option})"

    def check(self, code: codes.Code) -> bool:
        return verifiers.VERIFIER_CARDS[self.verifier_card](code, self.option)


class Proposal:
    def __init__(
        self, verifiers_cards: list[int], options: list[int]):
        assert len(verifiers_cards) == len(options)
        self.verifiers: list[Verifier] = [
            Verifier(verifier_card, option)
            for verifier_card, option in zip(verifiers_cards, options)
        ]
        self._accepted_codes = None

    def __repr__(self):
        return f"Proposal(verifiers={self.verifiers}, accepted_codes={self.accepted_codes()})"

    def check(self, code: codes.Code) -> bool:
        return all(verifier.check(code) for verifier in self.verifiers)

    def accepted_codes(self):
        if  self._accepted_codes is None:
            self._accepted_codes = [
                code
                for code in codes.generate_codes()
                if self.check(code)
            ]
        return self._accepted_codes

    def drop_verifier(self, verifier_card_index: int) -> Self:
        assert verifier_card_index < len(self.verifiers)
        verifiers = self.verifiers[:verifier_card_index] + self.verifiers[verifier_card_index + 1:]
        cards = [v.verifier_card for v in verifiers]
        options = [v.option for v in verifiers]
        return type(self)(cards, options)

    def is_solvable(self) -> bool:
        num_accepted = 0
        for code in codes.generate_codes():
            if self.check(code):
                num_accepted += 1
            if num_accepted > 1:
                break
        return num_accepted == 1

    def consistent_with_verifiers(self, verifiers: list[list[Verifier]]) -> bool:
        """Whether this proposal's options are within the allowed set."""
        assert len(verifiers) == len(self.verifiers)
        for v1, v_options in zip(self.verifiers, verifiers):
            assert v1.verifier_card == v_options[0].verifier_card
            options = set([v. option for v in v_options])
            if v1.option not in options:
                return False
        return True

def generate_proposals(verifier_cards: list[int]) -> Iterator[Proposal]:
    """Generates all possible proposals."""
    if not verifier_cards:
        yield Proposal([], [])
        return
    for option in range(verifiers.VERIFIER_CARD_SIZE[verifier_cards[0]]):
        for proposal in generate_proposals(verifier_cards[1:]):
            options = [v.option for v in proposal.verifiers]
            yield Proposal(verifier_cards, [option] + options)

def filter_unsolvable(proposals: list[Proposal]) -> list[Proposal]:
    """Filters out proposals that are not solvable."""
    solvable = []
    for proposal in proposals:
        if proposal.is_solvable():
            solvable.append(proposal)
    return solvable

def filter_redundant(proposals: list[Proposal]) -> list[Proposal]:
    """Filters out proposals that are redundant."""
    non_redundant = []
    for proposal in proposals:
        for i in range(len(proposal.verifiers)):
            if proposal.drop_verifier(i).is_solvable():
                break
        else:
            non_redundant.append(proposal)
    return non_redundant
