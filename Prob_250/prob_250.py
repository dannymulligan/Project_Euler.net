#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 250
#
# 250250
#
# Find the number of non-empty subsets of {1^(1), 2^(2), 3^(3),...,
# 250250^(250250)}, the sum of whose elements is divisible by
# 250. Enter the rightmost 16 digits as your answer.
#
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time

SIZE =  250251

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

def factors(n):
    factors = []
    while (factor_table[n] != 1):
        #print "n = {0}, factors = {1}".format(n, factors)
        factors.append(factor_table[n])
        n /= factor_table[n]
    factors.append(n)
    return factors

def pow_simple(a,b):
    result = 1
    base = a % 250
    for n in xrange(b):
        result *= a
        result = result % 250
    return result

def pow(a,b,m):
    result = 1
    base = a % m
    for x in factors(b):
        result = 1
        for y in xrange(x):
            result *= base
            result = result % m
        base = result
    return result

start_time = time.clock()
calculate_factor_table()

print "factors(25025) = {0}".format(factors(25025))
print "pow({0},{1},{2}) = {3}".format(2, 25025, 10**16, pow(2,25025,10**16))

results = [0]*250
for i in xrange(1,250251):
    if ((i % 1000) == 0):
        print "Calculating item {0} at time {1} seconds".format(i, time.clock())
    x = pow(i,i,250)
    results[x] += 1

print results
# results = [25025, 1001, 0, 1001, 1001,
#        0, 3003, 1002, 0, 1001, 0, 1001, 0, 1001, 1000,
#        0, 3002, 1002, 0, 1001, 0, 1001, 0, 1001, 1000, 
#        0, 3002, 1001, 0, 1001, 0, 1001, 0, 1000, 1000,
#        0, 3002, 1001, 0, 1001, 0, 1001, 0, 1001, 1000,
#        0, 3003, 1002, 0, 1001, 0, 1001, 0, 1002, 1002,
#        0, 3003, 1001, 0, 1001, 0, 1001, 0, 1001, 1001,
#        0, 3004, 1001, 0, 1001, 0, 1001, 0, 1000, 1001,
#        0, 3003, 1001, 0, 1001, 0, 1001, 0, 1001, 1001,
#        0, 3004, 1001, 0, 1001, 0, 1001, 0, 1001, 1001,
#        0, 3003, 1001, 0, 1001, 0, 1001, 0, 1002, 1001,
#        0, 3003, 1000, 0, 1001, 0, 1001, 0, 1002, 1002,
#        0, 3002, 1000, 0, 1001, 0, 1001, 0, 1001, 1001,
#    25025, 3003, 1001, 0, 1001, 0, 1001, 0, 1002, 1002,
#        0, 3002, 1000, 0, 1001, 0, 1001, 0, 1002, 1001,
#        0, 3003, 1000, 0, 1001, 0, 1001, 0, 1001, 1001,
#        0, 3003, 1001, 0, 1001, 0, 1001, 0, 1001, 1000,
#        0, 3003, 1001, 0, 1001, 0, 1001, 0, 1001, 1001,
#        0, 3003, 1002, 0, 1001, 0, 1001, 0, 1001, 1000,
#        0, 3003, 1001, 0, 1001, 0, 1001, 0, 1001, 1001,
#        0, 3002, 1000, 0, 1001, 0, 1001, 0, 1000, 1001,
#        0, 3004, 1001, 0, 1001, 0, 1001, 0, 1001, 1002,
#        0, 3004, 1002, 0, 1001, 0, 1001, 0, 1001, 1002,
#        0, 3004, 1001, 0, 1001, 0, 1001, 0, 1000, 1002,
#        0, 3004, 1001, 0, 1001, 0, 1001, 0, 1000, 1001,
#        0, 3003, 1001, 0, 1001]


print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()

