#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 99
#
# Largest exponential
#
# Comparing two numbers written in index form like 2**11 and 3**7 is
# not difficult, as any calculator would confirm that 2**11 = 2048 <
# 3**7 = 2187.
#
# However, confirming that 632382**518061 > 519432**525806 would be
# much more difficult, as both numbers contain over three million
# digits.
#
# Using base_exp.txt, a 22K text file containing one thousand lines
# with a base/exponent pair on each line, determine which line number
# has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the
# example given above.
#
# Solved 08/08/16
# ?? problems solved
# Position #??? on level ?

import csv
import math
import time
start_time = time.clock()

########################################

BiggestIndex = 0
BiggestLogN = 0.0

with open('base_exp.txt', 'r') as CSVFile:
    CSVReader = csv.reader(CSVFile)
    for N, Line in enumerate(CSVReader):
        Base = int(Line[0])
        Exponent = int(Line[1])
        LogNumber = math.log(Base) * Exponent
        if LogNumber > BiggestLogN:
            BiggestLogN = LogNumber
            BiggestIndex = N
            print(N, Base, Exponent, LogNumber)

# N is indexed from 0, but line numbers start from 1
BiggestIndex += 1

print()
print("Answer = {}".format(BiggestIndex))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
