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
# Solved 09/12/11
# 170 problems solved
# Position #362 on level 4

# {1,7,13,15,21,31,40,43}.
#  1 = 1_B2  (and 1_B3, 1_B4, 1_B5, ...1_Bn)
#  3 = 11_B2
#  7 = 111_B2
# 15 = 1111_B2
# 31 = 11111_B2
#  4 = 11_B3
# 13 = 111_B3
# 40 = 1111_B3
#  5 = 11_B4
# 21 = 111_B4
#  6 = 11_B5
# 31 = 111_B5
#  7 = 11_B6
# 43 = 111_B6
#  8 = 11_B7
#  9 = 11_B8
# 11 = 11_B10
# 12 = 11_B11
# 13 = 11_B12
# 14 = 11_B13
# 15 = 11_B14
# 16 = 11_B15
# 17 = 11_B16
# 18 = 11_B17
# 19 = 11_B18
# 20 = 11_B19
# 21 = 11_B20
# 22 = 11_B21
# 23 = 11_B22
# 24 = 11_B23
# 25 = 11_B24
# 26 = 11_B25
# 27 = 11_B26
# 28 = 11_B27
# 29 = 11_B28
# 30 = 11_B29
# 31 = 11_B30
# 32 = 11_B31
# 33 = 11_B32
# 34 = 11_B33
# 35 = 11_B34
# 36 = 11_B35
# 37 = 11_B36
# 38 = 11_B37
# 39 = 11_B38
# 40 = 11_B39
# 41 = 11_B40
# 42 = 11_B41
# 43 = 11_B42
# 44 = 11_B43
# 45 = 11_B44
# 46 = 11_B45
# 47 = 11_B46
# 48 = 11_B47
# 49 = 11_B48

#  1 = 1_B2  (and 1_B3, 1_B4, 1_B5, ...1_BN)
#  7 = 111_B2
#  7 = 11_B6
# 13 = 111_B3
# 13 = 11_B12
# 15 = 1111_B2
# 15 = 11_B14
# 21 = 111_B4
# 21 = 11_B20
# 31 = 11111_B2
# 31 = 111_B5
# 31 = 11_B30
# 43 = 111_B6
# 43 = 11_B42

# Observation: every repunit with three or more 1's (e.g. 111_Bx) will
# be a strong repunit, since there is a repunit with two 1's
# (e.g. 11_By) for every possible number below MAX.
#
# We do still need to watch for duplicates in our list of strong
# repunits, for example, 31 = 11111_B2 = 111_B5 = 11_B30.  If we make
# a list of all strong repunits, 31 would be listed twice.  Therefore
# we need to trim our list of strong repunits for duplicates before we
# sum it to find the answer

import sys
import time
start_time = time.clock()
MAX = 50
MAX = int(1e12)
print "Running with MAX={0}".format(MAX)

########################################

w_answer = [1]
answer   = [1]  # 1 is a repunit in any base

# max_b is determined by MAX > max_b*max_b + max_b + 1
# so MAX > max_b(max_b + 1)
# so max_b ~= sqrt MAX
max_b = int(MAX**.5)
print "Maximum base = {0}".format(max_b)

for b in xrange(2,max_b+1):
    n = b*b + b + 1  # start with 111_Bb
    while (n < MAX):
        #if not(n in answer):
        #    answer.append(n)
        answer.append(n)
        n = n*b + 1

#print "answer =", answer
#print "Answer = ", sum(answer)

# answer will contain duplicates, but we need to exclude these.  The
# following is a fast way to create a new list without the duplicates
# From: http://www.peterbe.com/plog/uniqifiers-benchmark
# Note: this approach does not preserve the order of the list, but we
# don't care about that
c_answer = {}.fromkeys(answer).keys()
# {}.fromkeys(answer) creates a dictionary from the list answer
# .keys() creates a list from the keys in that dictionary

# Turns out that there are only 2 strong repunits that are duplicated
# in our answer list, they are 31 and 8191.  These are the only
# numbers that are repunits in more than 2 bases.  There are no
# numbers that are repunits in more than 3 bases.

print "Answer =", sum(c_answer)
print "Time taken = {0} seconds".format(time.clock() - start_time)
