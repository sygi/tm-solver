# Info

This is a solver for the [Turing Machine](turingmachine.info) board game.

The main entrypoint is `solve.solve_puzzle`, which takes a list of ids of verifier cards.

It finds a best (ie. making as little queries as possible) solution to the most difficult game that
could be defined with these verifier cards (note that we're only passing verifier card ids, not verifiers
that fully specify the game/code).

It returns a tuple of two things:
1. a list of questions to ask, in the form of: code, verifier card id, what answer we can expect from the game for the most difficult game.
2. the code defined by the sequence of questions and answers.

# Algorithm

The algorithm used is a simple min-max search, cutting the branch off once
its depth is greater than the best solution found so far.

## TODOs

One could improve the repository by:
- changing the optimization criterium to minimize the number of rounds (with at most 3 queries per round)
  of the same code), instead of ignoring whether the queries use the same code or not.
- Use the lower bound on the length of the best solution: log_2(number of candidate codes)
  as a heuristic, doing an A-star search.
- Include the actual verifiers, to make the sequence of answers match what would happen
  in a particular game (note that, in principle, the solution for a particular game
  could be slightly shorter than for the most-difficult game with the given verifiers,
  but I haven't played such a game yet).
