#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 206
#
# Concealed Square
#
# Find the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.
#
# Answer: 
# Solved 07/11/10
# 113 problems solved
# Position #927 on level 3

# Notes:
# Call the number we're looking for N, and its square NN
#
# The last digit is 0, therefore N[-1] must be 0
# This means that NN[-2] must be 0, so NN is actually 1_2_3_4_5_6_7_8_900
#
# NN[-3:] are 900, therefore N[-2:] must be 30
#
# NN[-5] is 8, by trial and error, this means that N[-4:] must be one
# of 0430, 0530, 0830, 2930, 3030, 3330, 5430, 5530, 5830, 7930, 8030,
# or 8330, a total of 12 possibilities out of 10k for the last 4
# digits of N.
#
# N^2 is somewhere between 1020304050607080900 and 192939495969798900, thus
# N is somewhere between 1010101010 and 1389026623, which is a range of 378925613
# 
# Given that we only have to test 12 possibilities out of each 10k, a
# brute force approach would require us to check about 454k possibilities.

import math
import string

print "Testing for last possible 4 digits of N"
poss_ends = []
cnt = 0
for i in range(10000):
    n = i
    nn = n * n
    nns = '{0}'.format(nn)
    if (len(nns) < 5):
        continue
    nt = nns[-5] + nns[-3] + nns[-1]
    if (nt == '890'):
        print '>', n, nn
        cnt += 1
        poss_ends.append(n)
print 'poss_ends =', poss_ends
print 'len(poss_ends) =', len(poss_ends)

#   nn = 1_2_3_4_5_6_7_8_9_0
max_nn = 1929394959697989900
min_nn = 1020304050607080900

max_n = int(math.sqrt(max_nn)/10000)
min_n = int(math.sqrt(min_nn)/10000)
print max_n, min_n
print "Need to check", len(poss_ends)*(max_n-min_n) ,"possibilities"

for i in range(min_n, max_n):
    for j in poss_ends:
        n = i * 10000 + j
        nn = n * n
        nns = '{0}'.format(nn)
        nt = nns[0] + nns[2] + nns[4] + nns[6] + nns[8] + nns[10] + nns[12] + nns[14] + nns[16] + nns[18]
        #print "Checking, n=", n, "n^2=", nn, "nt=", nt
        if (nt != '1234567890'):
            continue
        print "Result found, n=", n, "n^2=", nn
