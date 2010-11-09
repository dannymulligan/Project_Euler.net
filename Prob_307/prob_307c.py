#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 307
#
# Chip Defects
#
# 20,000 defects are randomly distributed amongst the 1,000,000
# integrated-circuit chips produced by a factory (any number of
# defects may be found on a chip).
#
# Find the probability that there is a chip with at least 3 defects.
#
# Give your answer rounded to 10 decimal places in the form
# 0.abcdefghij
#
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time
import random

start = time.clock()
chips   = 1000000
defects =   20000

def simulate():
    wafer = [0]*chips
    for defect in range(defects):
        victim = random.randint(0,chips-1)
        wafer[victim] += 1
        if wafer[victim] >= 3:
            return True
    return False

f3 = 0
tot = 0
for i in range(1000000):
    tot += 1
    if (simulate()):
        f3 += 1
    if ((i % 100) == 0):
        print "{0:10g}: result = {1:.12f}".format(i, 1.0*f3/tot)

sys.exit()

     24000: result = 0.728927961335
     24100: result = 0.728890917389
     24200: result = 0.728978141399
     24300: result = 0.729064647545
     24400: result = 0.729273390435
     24500: result = 0.729357985388
     24600: result = 0.729441892606
     24700: result = 0.729241731104
     24800: result = 0.729285109471
     24900: result = 0.729488775551
     25000: result = 0.729170833167
