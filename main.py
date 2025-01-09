import codes
import proposals
import solve
import verifiers
# TODO: load up a problem, ideally in a json format consistent with
# https://boardgamegeek.com/thread/3067566/no-spoiler-helper-software-beatmachine

if __name__ == "__main__":
    verifier_cards = [4, 9, 11, 14]  # problem 1
    print(solve.solve_puzzle(verifier_cards))
