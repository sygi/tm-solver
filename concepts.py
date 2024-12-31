"""Semi-natural language description of concepts."""

# 1. verifier: a single function taking a code and returning a boolean
# 2. verifier card: a set of verifiers, takes a code and returns a boolean
#    according to one of the verifiers, that is called "active".
# 3. code: described by a list[int]. When a verifier returns true on a code,
#    we say it accepts it.
# 4. proposal: a set of verifiers, one from each card.

# Initially, we minimize the number of code checks on verifier cards, without
# taking into account the number of times a given code is being checked (ie. number of rounds).
#
# Initially, we don't take into account the particular code (ie. which of the verifiers is active
# in each card). Instead, we minimize the pessimistic number of checks we could take for
# the worst code.
#
# Order of operations:
# 1. check every potential proposal, and keep the ones which only have
#    one possible code (ie. for which the problem is solvable).
# 2. for each of the remaining proposals, check if removal of any of the verifiers
#    leads to increase of the number of accepted codes. We only keep the proposals
#    where removal of any of the verifiers leads to increase of the number of accepted codes
#    (ie. there are no redundant verifiers).
