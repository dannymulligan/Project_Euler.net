#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 172
#
# Investigating numbers with few repeated digits.
#
# How many 18-digit numbers n (without leading zeros) are there such
# that no digit occurs more than three times in n?
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

# Recursive solution doesn't run close to quickly enough.  Here are
# results from running...
# 
# Checked 6 digit numbers, answer = 8754480, time taken = 0.13527
# Checked 7 digit numbers, answer = 85480920, time taken = 1.330127
# Checked 8 digit numbers, answer = 825234480, time taken = 13.154628
# Checked 9 digit numbers, answer = 7857440640, time taken = 126.074299
#
# Each extra digit makes the run time about 10x longer.  Adding
# another 9 digits to get to 18 will make the simulation take about
# 4,000 years.  Need a better approach.

import time
import sys

start_time = time.clock()

LEN_LIM = 3
NUM_LEN = 7

def poss(digits, a, b, c, d, e, f, g, h, i, j):
    ans = 0
    if (digits == 1):
        if (a < LEN_LIM):  ans += 1  # Can we add a 0 to the end of the number
        if (b < LEN_LIM):  ans += 1  # Can we add a 1 to the end of the number
        if (c < LEN_LIM):  ans += 1  # Can we add a 2 to the end of the number
        if (d < LEN_LIM):  ans += 1  # Can we add a 3 to the end of the number
        if (e < LEN_LIM):  ans += 1  # Can we add a 4 to the end of the number
        if (f < LEN_LIM):  ans += 1  # Can we add a 5 to the end of the number
        if (g < LEN_LIM):  ans += 1  # Can we add a 6 to the end of the number
        if (h < LEN_LIM):  ans += 1  # Can we add a 7 to the end of the number
        if (i < LEN_LIM):  ans += 1  # Can we add a 8 to the end of the number
        if (j < LEN_LIM):  ans += 1  # Can we add a 9 to the end of the number
    else:
        if (a < LEN_LIM):  ans += poss(digits-1, a+1, b, c, d, e, f, g, h, i, j)  # Can we add a 0 to the end of the number
        if (b < LEN_LIM):  ans += poss(digits-1, a, b+1, c, d, e, f, g, h, i, j)  # Can we add a 1 to the end of the number
        if (c < LEN_LIM):  ans += poss(digits-1, a, b, c+1, d, e, f, g, h, i, j)  # Can we add a 2 to the end of the number
        if (d < LEN_LIM):  ans += poss(digits-1, a, b, c, d+1, e, f, g, h, i, j)  # Can we add a 3 to the end of the number
        if (e < LEN_LIM):  ans += poss(digits-1, a, b, c, d, e+1, f, g, h, i, j)  # Can we add a 4 to the end of the number
        if (f < LEN_LIM):  ans += poss(digits-1, a, b, c, d, e, f+1, g, h, i, j)  # Can we add a 5 to the end of the number
        if (g < LEN_LIM):  ans += poss(digits-1, a, b, c, d, e, f, g+1, h, i, j)  # Can we add a 6 to the end of the number
        if (h < LEN_LIM):  ans += poss(digits-1, a, b, c, d, e, f, g, h+1, i, j)  # Can we add a 7 to the end of the number
        if (i < LEN_LIM):  ans += poss(digits-1, a, b, c, d, e, f, g, h, i+1, j)  # Can we add a 8 to the end of the number
        if (j < LEN_LIM):  ans += poss(digits-1, a, b, c, d, e, f, g, h, i, j+1)  # Can we add a 9 to the end of the number
    return ans

prev_time = time.clock()
ans = 9*poss(6, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
print "Checking {0} digit numbers, answer = {1}, CPU time taken = {2} seconds".format(6, ans, time.clock() - prev_time)

prev_time = time.clock()
ans = 9*poss(7, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
print "Checking {0} digit numbers, answer = {1}, CPU time taken = {2} seconds".format(7, ans, time.clock() - prev_time)

prev_time = time.clock()
ans = 9*poss(8, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
print "Checking {0} digit numbers, answer = {1}, CPU time taken = {2} seconds".format(8, ans, time.clock() - prev_time)

prev_time = time.clock()
ans = 9*poss(9, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
print "Checking {0} digit numbers, answer = {1}, CPU time taken = {2} seconds".format(9, ans, time.clock() - prev_time)


sys.exit()

print "Answer =", ans
print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()
