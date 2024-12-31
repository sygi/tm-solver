import codes
import proposals
import solve
import verifiers
# TODO: load up a problem, ideally in a json format consistent with
# https://boardgamegeek.com/thread/3067566/no-spoiler-helper-software-beatmachine

if __name__ == "__main__":
    for code in codes.generate_codes():
        print(code)
    verifier_cards = [4, 9, 11, 14]  # problem 1
    verifier_cards = [3, 7, 10, 14]  # problem 2
    #verifier_cards = [4, 9, 18, 20]  # problem 12
    all_props = []
    for proposal in proposals.generate_proposals(verifier_cards):
        all_props.append(proposal)
    print("total proposals:", len(all_props))
    solvable_proposals = proposals.filter_unsolvable(all_props)
    print("solvable proposals:", len(solvable_proposals))
    non_redundant = proposals.filter_redundant(solvable_proposals)
    print("non-redundant proposals:", len(non_redundant))
    for proposal in non_redundant:
        print(proposal)
    print(solve.solve(non_redundant)[0])
