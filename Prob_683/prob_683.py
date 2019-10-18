#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 683
#
# The Chase II
#
# Consider the following variant of "The Chase" game. This game is
# played between n players sitting around a circular table using two
# dice. It consists of n−1 rounds, and at the end of each round one
# player is eliminated and has to pay a certain amount of money into a
# pot. The last player remaining is the winner and receives the entire
# contents of the pot.
#
# At the beginning of a round, each die is given to a randomly
# selected player. A round then consists of a number of turns.
#
# During each turn, each of the two players with a die rolls it. If a
# player rolls a 1 or a 2, she passes the die to her neighbour on the
# left; if she rolls a 5 or a 6, she passes the die to her neighbour
# on the right; otherwise, she keeps the die for the next turn.
#
# The round ends when one player has both dice at the beginning of a
# turn. The turn is aborted, that player is eliminated, and she has to
# pay s^2 where s is the number of completed turns in this round. Note
# that if both dice happen to be handed to the same player at the
# beginning of a round, then no turns are completed, so the player is
# eliminated without having to pay any money into the pot.
#
# Let G(n) be the expected amount that the winner will receive. For
# example G(5) is approximately 96.544, and G(50) is 2.82491788e6 in
# scientific notation rounded to 9 significant digits.
#
# Find G(500), giving your answer in scientific notation rounded to 9
# significant digits.


import sys
import time
start_time = time.clock()

DEBUG = False

if DEBUG:
    print(sys.version)


###############################################################################

def pot(nplayers, tolerance):
    prev_probs = [1.0/nplayers] * nplayers
    if DEBUG:
        print()
        print("pot(nplayers={}, tolerance={})".format(nplayers, tolerance))
        print(prev_probs)
    prev_probs[0] = 0

    done = False
    expected_pot = 0.0
    round = 0
    while not done:
        # Calculate the next round of probabilities
        round += 1
        next_probs = [0.0] * nplayers
        for n in range(nplayers):
            next_probs[n] += 1/9 * prev_probs[(nplayers + n - 2) % nplayers]
            next_probs[n] += 2/9 * prev_probs[(nplayers + n - 1) % nplayers]
            next_probs[n] += 3/9 * prev_probs[(nplayers + n    ) % nplayers]
            next_probs[n] += 2/9 * prev_probs[(nplayers + n + 1) % nplayers]
            next_probs[n] += 1/9 * prev_probs[(nplayers + n + 2) % nplayers]

        # Calculate the contribution to the pot
        pot_contribution = round**2 * next_probs[0]
        done = (pot_contribution < tolerance)
        expected_pot += pot_contribution
        if DEBUG:
            print(round, next_probs, pot_contribution)

        prev_probs = next_probs
        prev_probs[0] = 0.0

    return expected_pot


###############################################################################
g = 0.0
tol = 2e-14
tolerance = 1.0 * tol
prev_time = start_time
for n in range(2,51):
    result = pot(nplayers=n, tolerance=tolerance)
    g += result
    now = time.clock()
    time_taken = now - prev_time
    prev_time = now
    print("pot(nplayers={}, tolerance={:.6e}) = {}, G({}) = {:.8e}, time taken {:.3} seconds".format(n, tolerance, result, n, g, time_taken))
    tolerance = g * tol

print("Answer = {:.8e}".format(g))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
