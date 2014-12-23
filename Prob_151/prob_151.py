#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 151
#
# Paper sheets of standard sizes: an expected-value problem.
#
# A printing shop runs 16 batches (jobs) every week and each batch
# requires a sheet of special colour-proofing paper of size A5.
#
# Every Monday morning, the foreman opens a new envelope, containing a
# large sheet of the special paper with size A1.
#
# He proceeds to cut it in half, thus getting two sheets of size
# A2. Then he cuts one of them in half to get two sheets of size A3
# and so on until he obtains the A5-size sheet needed for the first
# batch of the week.
#
# All the unused sheets are placed back in the envelope.
#
#      +-------------+-------------+
#      |             |             |
#      |             |     A3      |
#      |             |             |
#      |     A2      +------+------+
#      |             |      |  A5  |
#      |             |  A4  +------+
#      |             |      |  A5  |
#      +-------------+------+------+
#
# At the beginning of each subsequent batch, he takes from the
# envelope one sheet of paper at random. If it is of size A5, he uses
# it. If it is larger, he repeats the 'cut-in-half' procedure until he
# has what he needs and any remaining sheets are always placed back in
# the envelope.
#
# Excluding the first and last batch of the week, find the expected
# number of times (during each week) that the foreman finds a single
# sheet of paper in the envelope.
#
# Give your answer rounded to six decimal places using the format
# x.xxxxxx .
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

answer = 0.0
inventory = []
inventory.append({(1,0,0,0,0): 1.000})  # Start off with a single sheet of A1

for round in range(1,16):
    print("==== Round {} ========".format(round))
    for config in inventory[round-1].keys():
        prob = inventory[round-1][config]
        inventory.append(dict())
        lconfig = list(config)

        for i in range(5):
            if (lconfig[i] != 0):
                nprob = prob * lconfig[i]/sum(lconfig)
                print("Printer randomly selects an A{} sheet from configuration {} with probability {}".format(i+1, config, nprob)),
                nconfig = list(lconfig)
                nconfig[i] -= 1
                for j in range(i+1,5):
                    nconfig[j] += 1
                print("and ends up with configuration {} with probability {}".format(tuple(nconfig), nprob))

                if tuple(nconfig) in inventory[round]:
                    inventory[round][tuple(nconfig)] += nprob
                else:
                    inventory[round][tuple(nconfig)] = nprob

    print("---- End result is as follows ----")
    for config in inventory[round].keys():
        if (sum(config) == 1):
            print("--> configuration {} with probability {} <-- single sheet".format(config, inventory[round][config]))
            answer += inventory[round][config]
        else:
            print("    configuration {} with probability {}".format(config, inventory[round][config]))

print("Answer = {:0.6f}".format(answer - 1.0))  # Subtract 2 to account for the 1.0 answer in round 15

print "Time taken = {0} seconds".format(time.clock() - start_time)


# State will be of form A1, A2, A3, A4, A5.
#
# For round 1, we have the following possibilities
#    1.000  1, 0, 0, 0, 0  <- single sheet
# Total = 16*A5 remaining
#
# For round 2, we have the following possibilities
#    1.000  0, 1, 1, 1, 1
# Total = 15*A5 remaining
#
# For round 3, we have the following possibilities
#    0.250  0, 1, 1, 1, 0
#    0.250  0, 1, 1, 0, 2
#    0.250  0, 1, 0, 2, 2
#    0.250  0, 0, 2, 2, 2
# Total = 14*A5 remaining
#
# For round 4, we have the following possibilities
#    0.250  0, 1, 1, 1, 0
#    0.250  0, 1, 1, 0, 2
#    0.250  0, 1, 0, 2, 2
#    0.250  0, 0, 2, 2, 2
# Total = 13*A5 remaining
