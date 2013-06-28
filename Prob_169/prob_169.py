#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 169
#
# Exploring the number of different ways a number can be expressed as
# a sum of powers of 2.
#
# Define f(0)=1 and f(n) to be the number of different ways n can be
# expressed as a sum of integer powers of 2 using each power no more
# than twice.
#
# For example, f(10)=5 since there are five different ways to express
# 10:
#
#     1 + 1 + 8
#     1 + 1 + 4 + 4
#     1 + 1 + 2 + 2 + 4
#     2 + 4 + 4
#     2 + 8
#
# What is f(10^25)?
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

########################################
NUM = 10**25
#NUM = 10**6
#NUM = 10

num_array = []
n = NUM
while (n > 0):
    if ((n % 2) == 1):
        num_array.append(1)
        n -= 1
    else:
        num_array.append(0)
    n /= 2

print "num_array = ",
for i in xrange(len(num_array)):
    if (num_array[i] == 1):
        print "2^{0}".format(i),
print

#answer = collapse(num_array)
#print "Answer =", answer

print "Time taken = {0} seconds".format(time.clock() - start_time)


########################################
#def collapse(num_array):
#    i = 0
#    while (num_array[i] == 0):
#        i += 1
#    n = 


# if num_array = [0, 0, 0, 0, 1, ..., x, y, z]
# then we can collapse to...
#     [0, 0, 0, 0, 1, ..., x, y, z]
#     [0, 0, 0, 2, 0, ..., x, y, z]
#     [0, 0, 2, 1, 0, ..., x, y, z]
#     [0, 2, 1, 1, 0, ..., x, y, z]
#     [2, 1, 1, 1, 0, ..., x, y, z]
# if num_array = [0, 0, 0, 0, 2, ..., x, y, z]
# then we can collapse to...
#     [0, 0, 0, 0, 2, ..., x, y, z]
#     [0, 0, 0, 2, 1, ..., x, y, z]
#     [0, 0, 2, 1, 1, ..., x, y, z]
#     [0, 2, 1, 1, 1, ..., x, y, z]
#     [2, 1, 1, 1, 1, ..., x, y, z]
