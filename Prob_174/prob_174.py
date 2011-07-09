#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 174
#
# Counting the number of "hollow" square laminae that can form one,
# two, three, ... distinct arrangements.
#
# We shall define a square lamina to be a square outline with a square
# "hole" so that the shape possesses vertical and horizontal symmetry.
#
# Given eight tiles it is possible to form a lamina in only one way:
# 3x3 square with a 1x1 hole in the middle. However, using thirty-two
# tiles it is possible to form two distinct laminae.
#
#     * * * * * *    * * * * * * * * *
#     * * * * * *    * . . . . . . . *    32 = 6^2 - 2^2
#     * * . . * *    * . . . . . . . *
#     * * . . * *    * . . . . . . . *    32 = 9^2 - 7^2
#     * * * * * *    * . . . . . . . *
#     * * * * * *    * . . . . . . . *
#                    * . . . . . . . *
#                    * . . . . . . . *
#                    * * * * * * * * *
#
# If t represents the number of tiles used, we shall say that t = 8 is
# type L(1) and t = 32 is type L(2).
#
# Let N(n) be the number of t <= 1,000,000 such that t is type L(n);
# for example, N(15) = 832.
#
# What is sum(N(n)) for 1 <= n <= 10?
#
# Answer: 209566
# Solved 07/09/10
# 147 problems solved
# Position #56 on level 3


# The number of squares in a X by X square with a Y by Y hole is
#     X^2 - Y^2
# the maximum value of Y is X-2, at which point the number of squares is
#     X^2 - (X-2)^2 = X^2 - (X^2 - 4X + 4) = 4X - 4 = 4(X-1)
# Therefore the maximum number of X we need to consider is when
#     4(X-1) = SIZE
# or
#     X = SIZE/4 + 1
#
# In order for the lamina to be symmetric, X-Y must be even
#
# When X is known, then the we have
#    X^2 - Y^2 <= SIZE
#    X^2 - SIZE <= Y^2
#    Y >= sqrt(X^2 - SIZE)

import sys 
import time

start_time = time.clock()

SIZE  = 1000000

n = [0]*(SIZE+1)

def odd(n):
    return ((n % 2) == 1)

def even(n):
    return ((n % 2) == 0)

for x in range(3,SIZE/4+2):

    min_y2 = x**2 - SIZE
    if ((min_y2 < 0) & even(x)):
        min_y = 2
    elif ((min_y2 < 0) & odd(x)):
        min_y = 1
    else:
        min_y = int(min_y2**.5)
        if ((min_y % 2) != (x % 2)):
            min_y += 1
    
    for y in range(min_y, x, 2):
        c = x**2 - y**2
        #print "n = {2}, x = {0}, y = {1}".format(x,y,c)
        if (c <= SIZE):
            #print "{2} = {0} {1}".format(x,y,c)
            n[c] += 1

#print "n[8] = ", n[8]
#print "n[32] = ", n[32]
#print n[0:25]

ans = [0]*21
for i in range(1,SIZE+1):
    if ((n[i] >= 1) & (n[i] <= 20)):
        ans[(n[i])] += 1

for i in range(11):
    print "ans[{0}] = {1}".format(i, ans[i])

print "Answer =", sum(ans[1:11])
print "Time taken =", time.clock() - start_time, "seconds"
