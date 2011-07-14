#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 135
#
# Determining the number of solutions of the equation
#     x^2 − y^2 − z^2 = n.
#
# Given the positive integers, x, y, and z, are consecutive terms of
# an arithmetic progression, the least value of the positive integer,
# n, for which the equation, x^2 − y^2 − z^2 = n, has exactly two
# solutions is n = 27:
# 
#     34^2 − 27^2 − 20^2 = 27
#     12^2 − 9^2 − 6^2 = 27
# 
# It turns out that n = 1155 is the least value which has exactly ten
# solutions.
# 
# How many values of n less than one million have exactly ten distinct
# solutions?
#
# Solved ??/??/10
# ??? problems solved
# Position #?? on level 3

# What is the maximum and minimum values of X?
#
# Min value will be when
#     x-2s > 0
# given step size of s, therefore
#     x > 2s
#
# Max value will be when
#     x^2 - (x-s)^2 - (x-2s)^2 >= 1,000,000
# given step size of s, therefore
#     x^2 - (x^2 - 2sx + s^2) - (x^2 - 4sx + 4s^2) > 1,000,000
#     -x^2 + 6sx - 5s^2 > 1,000,000
#     x^2 - 6sx + 5s^2 < 1,000,000
#     (x - 5s) * (x - s) < 1,000,000
# 
# Twelve hours to get to 148,000, which is about 30% finished.  Too slow.


import sys 
import time

start_time = time.clock()

SIZE  = 1000000

n = [0]*(SIZE+1)


for s in range(1,1+SIZE/2):
    min_x = 2*s + 1
    # if x = min_x, then
    # nn = (s/2 + 1)^2

    if ((s % 1000) == 0):
        print "s = {0}, min_x = {1}".format(s, min_x)

    for x in range(min_x, SIZE):
        nn = x**2 - (x-s)**2 - (x-2*s)**2
        #print "nn = {0}, x = {1}, y = {2}, z = {3}".format(nn, x, x-s, x-2*s)
        if (nn < SIZE) & (nn > 0):
            n[nn] += 1
        elif ((x > min_x) & (nn <= 0)):
            #print "Break"
            break

ans = [0]*11
for i in range(1,SIZE+1):
    if (n[i] >= 1) & (n[i] <= 10):
        ans[n[i]] += 1

print "Answer =", ans
print "Answer =", ans[10]
print "Time taken =", time.clock() - start_time, "seconds"
