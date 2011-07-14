#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 188
#
# The hyperexponentiation of a number
#
# The hyperexponentiation or tetration of a number a by a positive
# integer b, denoted by a^^b or ^(b)a, is recursively defined by:
#
#     a^^1 = a,
#     a^^(k+1) = a^(a^^k).
#
# Thus we have e.g. 3^^2 = 3^3 = 27, hence 3^^3 = 3^27 = 7625597484987
# and 3^^4 is roughly 10^(3.6383346400240996*10^12).
#
# Find the last 8 digits of 1777^^1855.
#
# Solved 11/26/10
# 133 problems solved
# Position #350 on level 3

# 1777 = prime
# 1855 = 5 x 7 x 53
#
# 1,777^10,000,000 = xxx,821,600,000,001
#
# This means that 1777^(x mod 10**7) = 1777^x if we only care
# about the last 8 digits of the result



import sys
import time

start_time = time.clock()
SIZE =  5000
BASE = 1777
POWER = 1855

factor_table = [1]*(1+SIZE)  # largest factor, 1 means this number is prime
def calculate_factor_table():
    i = 2
    while (i <= (SIZE/2)):
        if (factor_table[i] == 1):
            j = i*2
            while (j <= SIZE):
                factor_table[j] = i
                #print "factor_table[{0}] = {1}".format(j, i)
                j += i
        i += 1

def calculate_factors(n):
    factors = []
    while (factor_table[n] != 1):
        print "n = {0}, factors = {1}".format(n, factors)
        factors.append(factor_table[n])
        n /= factor_table[n]
    factors.append(n)
    return factors

# print "Calculating factor_table with SIZE = {0}".format(SIZE)
# calculate_factor_table()
# print "Factors of {0} are {1}".format(BASE, calculate_factors(BASE))
# print "Factors of {0} are {1}".format(POWER, calculate_factors(POWER))

# answer = 1
# for i in xrange(1,10000001):
#     answer = answer * BASE
#     answer = (answer % 10**9)
#     if (answer % 10000000) == 1:
#         print "{0}^{1} = {2:8}".format(BASE, i, answer)
#     if (answer % 1000000000) == 1:
#         print "{0}^{1} = {2:8}".format(BASE, i, answer)

answer = POWER
for p in xrange(POWER):
    print "Depth {0:4}: calculating {1}^{2}".format(p, BASE, answer)
    pow = answer
    answer = 1
    for i in xrange(pow):
        answer *= BASE
        answer = answer % 10**9
    print "            answer = {0}".format(answer)
    answer = answer % 10**7    

print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()
