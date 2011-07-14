#!/usr/bin/python
#
# Project Euler.net Problem 72
#
# Consider the fraction, n/d, where n and d are positive integers. If
# n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# 
# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:
# 
#     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
#         5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 
# It can be seen that there are 21 elements in this set.
# 
# How many elements would be contained in the set of reduced proper
# fractions for d <= 1,000,000?
# 
#
# Solved 
# ?? problems solved
# Position #??? on level ?

#       D      Answer
#       8          21
#      10          31
#      50         773
#     100       3,043
#     500      76,115
#   1,000     304,191
#   5,000   7,600,457
#  10,000  30,397,485

LIMIT_D =     8
LIMIT_D =    10
LIMIT_D =    50
LIMIT_D =   100
LIMIT_D =   500
LIMIT_D =  1000
LIMIT_D =  5000
LIMIT_D = 10000
#LIMIT_D = 50000

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

print "LIMIT_D =", LIMIT_D

answer = 0
for d in range(2,LIMIT_D+1):
    for n in range(1,d):
        if (gcd(n,d) == 1):
            answer += 1
            if ((answer % 5000000) == 0):
                print "Found {0}M answers so far, latest one is {1}/{2}, d={3}, n={4}".format(answer/1000000, n/gcd(n,d), d/gcd(n,d), d, n)
    

print "Answer = ", answer
