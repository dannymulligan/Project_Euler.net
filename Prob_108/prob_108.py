#!/usr/bin/python
#
# Project Euler.net Problem 108
# 
# In the following equation x, y, and n are positive integers.
#
#     1     1     1
#    --- + --- = ---
#     x     y     n
# 
# For n = 4 there are exactly three distinct solutions:
#
#     1      1     1
#    --- + ---- = ---
#     5     20     4
#
#     1      1     1
#    --- + ---- = ---
#     6     12     4
#
#     1     1     1
#    --- + --- = ---
#     8     8     4
# 
# What is the least value of n for which the number of distinct
# solutions exceeds one-thousand?
# 
# NOTE: This problem is an easier version of problem 110; it is
# strongly advised that you solve this one first.
#
# Solved: 07/03/11
# 143 problems solved
# Position #139 on level 3

#     1     1     1
#    --- + --- = ---
#     x     y     n
# 
# Therefore
#
#      y      x     1
#    ---- + ---- = ---
#     xy     xy     n
# 
#    x + y    1
#    ----- = ---
#     xy      n
#
#          xy
#    n = -----
#        x + y
#
#    n(x + y) = xy
#
#    nx + ny = xy
#
#    nx = (x-n)y
#
#         nx
#    y = -----
#        x - n

import sys

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

mcnt = 0
for n in range(135000,1000000):
    x = n + 1
    done = False
    acnt = 0
    while not done:
        #num = (n*x)/gcd(n*x, x-n)
        div = (x-n)/gcd(n*x, x-n)
        if (div == 1):
            acnt += 1
            #y = n*x/(x-n)
            #print "    1/{0} + 1/{1} = 1/{2}".format(x, y, n)
            if (x >= n*2):
                done = True
        x += 1

    if ((n % 1000) == 0):
        print "Searching with n = {0}".format(n)

    if (acnt > mcnt):
        mcnt = acnt
        print "{0} answers found with n = {1}".format(acnt, n)

    if (acnt > 1100):
        sys.exit()
