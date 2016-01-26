#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 323
#
# Bitwise-OR operations on random integers
#
# Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
# (i.e. 0 ≤ yi < 232, every value equally likely).
#
# For the sequence xi the following recursion is given:
#
#    x0 = 0 and
#    xi = xi-1| yi-1, for i > 0. ( | is the bitwise-OR operator)
#
# It can be seen that eventually there will be an index N such that xi
# = 232 -1 (a bit-pattern of all ones) for all i ≥ N.
#
# Find the expected value of N.
# Give your answer rounded to 10 digits after the decimal point.
#

import sys
import time
start_time = time.clock()

########################################
SIZE = 32
RESOLUTION = 10**-13  # the resolution we're looking for
PROB_FLIP = 0.5  # probability that a bit will go to 1 on any round if it is currently 0

print("SIZE = {}".format(SIZE))
print("RESOLUTION = {:12.10g}".format(RESOLUTION))
print("PROB_FLIP  = {:12.10g}".format(PROB_FLIP))


round = 1
answer = 0.0
prev_prob_ones = 0.0
curr_prob_ones = 0.0
delta = 1.0

while (delta > RESOLUTION):
    prev_prob_ones = curr_prob_ones
    curr_prob_ones = (1.0 - PROB_FLIP**round)**SIZE
    delta = curr_prob_ones - prev_prob_ones
    answer += delta * round
    print("round={} prev_prob_ones={}, curr_prob_ones={}, delta={} answer={:14.12f}".format(round, prev_prob_ones, curr_prob_ones, delta, answer))
    round += 1


print("Answer = {:12.10f}".format(answer))
print("Time taken = {0} seconds".format(time.clock() - start_time))
