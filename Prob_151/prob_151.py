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

import time
import random

ICNT = 100000000
start_time = time.clock()

count = 0
for i in range(ICNT):
    # Assumes the first batch already done
    A2 = 1
    A3 = 1
    A4 = 1
    A5 = 1

    for j in range(14):
        # Check for single sheet of paper
        if ((A2 + A3 + A4 + A5) == 1):
            count += 1

        # Pick a piece of paper from the envelope
        choice = random.randint(1,(A2+A3+A4+A5))
        if    (choice                 <= A2):  piece = 2
        elif ((choice - A2          ) <= A3):  piece = 3
        elif ((choice - A2 - A3     ) <= A4):  piece = 4
        else:                                  piece = 5

        # Process that piece of paper
        if (piece == 2):
            A2 -= 1
            A3 += 1
            A4 += 1
            A5 += 1
            #print "Chose an A2 sheet, A2 = {0}, A3 = {1}, A4 = {2}, A5 = {3}, total sheets = {4}".format(A2,A3,A4,A5, (A2+A3+A4+A5))
        elif (piece == 3):
            A3 -= 1
            A4 += 1
            A5 += 1
            #print "Chose an A3 sheet, A2 = {0}, A3 = {1}, A4 = {2}, A5 = {3}, total sheets = {4}".format(A2,A3,A4,A5, (A2+A3+A4+A5))
        elif (piece == 4):
            A4 -= 1
            A5 += 1
            #print "Chose an A4 sheet, A2 = {0}, A3 = {1}, A4 = {2}, A5 = {3}, total sheets = {4}".format(A2,A3,A4,A5, (A2+A3+A4+A5))
        elif (piece == 5):
            A5 -= 1
            #print "Chose an A5 sheet, A2 = {0}, A3 = {1}, A4 = {2}, A5 = {3}, total sheets = {4}".format(A2,A3,A4,A5, (A2+A3+A4+A5))

    if (((i+1) % 100000) == 0):
        print "Answer = {0:12.10f}, count = {1}, iterations = {2}, time = {3}".format((float(count)/float(i+1)), count, (i+1), (time.clock() - start_time))
