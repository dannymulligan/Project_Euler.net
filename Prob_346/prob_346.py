#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 346
#
# Strong Repunits
#
# The number 7 is special, because 7 is 111 written in base 2, and 11
# written in base 6 (i.e. base10(7) = base6(11) = base2(111)). In
# other words, 7 is a repunit in at least two bases b > 1.
#
# We shall call a positive integer with this property a strong
# repunit. It can be verified that there are 8 strong repunits below
# 50: {1,7,13,15,21,31,40,43}.
#
# Furthermore, the sum of all strong repunits below 1000 equals 15864.
#
# Find the sum of all strong repunits below 10^12.
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()
MAX = 50

########################################

repunits = []
repunits.append([]) # repunits[0]
repunits.append([]) # repunits[1]
for b in xrange(2,MAX):
    r = []
    n = 1
    while (n < MAX):
        r.append(n)
        n = n*b + 1
    repunits.append(r)

print repunits   

answer = []
for i in xrange(1,MAX):
    cnt = 0
    for j in xrange(2,MAX):
        if (i in repunits[j]):
            cnt += 1
            if (cnt >= 2):
                answer.append(i)
                break

print answer
print "Time taken = {0} seconds".format(time.clock() - start_time)

