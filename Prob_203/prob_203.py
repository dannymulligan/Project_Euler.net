#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 203
#
# Squarefree Binomial Coefficients
#
# The binomial coefficients C(n,k) can be arranged in triangular form,
# Pascal's triangle, like this:
#
#                   1       
#                 1   1       
#               1   2   1       
#             1   3   3   1       
#           1   4   6   4   1       
#         1   5  10  10   5   1       
#       1   6  15  20  15   6   1       
#     1   7  21  35  35  21   7   1
#              ..........
# 
# It can be seen that the first eight rows of Pascal's triangle
# contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21
# and 35.
# 
# A positive integer n is called squarefree if no square of a prime
# divides n. Of the twelve distinct numbers in the first eight rows of
# Pascal's triangle, all except 4 and 20 are squarefree. The sum of
# the distinct squarefree numbers in the first eight rows is 105.
# 
# Find the sum of the distinct squarefree numbers in the first 51 rows
# of Pascal's triangle.
#
# Answer: 34029210557338
# Solved 08/09/10
# 117 problems solved
# Position #793 on level 3 (previously #825 on level 3)

import math

#DEPTH = 8
DEPTH = 51

print "Calculating Pascal's triange of depth", DEPTH

pascal = [[1]]
pset = set()
prev = pascal[0]
for i in range(1,DEPTH):
    j0 = 0
    new = []
    for j in prev:
        new.append(j0+j)
        pset.add(j0+j)
        j0=j
    new.append(j)
    pascal.append(new)
    prev = new

pmax = 0
for j in pascal:
    print j
    #print j[0], j[len(j)/2]
    pmax = max(pmax,max(j))

print "Set is", pset
print "Length of pset is", len(pset)

print "Maximum is", pmax
print "Biggest prime we need to check is", math.pow(pmax,0.25)

limit_prime = 1 + int(math.pow(pmax,0.25))
print "limit_prime is", limit_prime

prime_table = [1]*limit_prime  # table of smallest factor
primes = []
tried = []

def calculate_primes():
    i = 2
    while (i < (limit_prime/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i*2
            while (j < limit_prime):
                prime_table[j] = i
                j += i
        i += 1
    while (i < limit_prime):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 1

calculate_primes()

print "There are", len(primes), "primes less than", limit_prime
print "They are", primes
print "The highest prime is", primes[-1]
    
prime_sq = []
for prime in primes:
    prime_sq.append(prime**2)
print "There are", len(prime_sq), "squared primes"
print "They are prime_sq =", prime_sq

ns_set = []
sq_set = []
for n in pset:
    found = False
    for p in prime_sq:
        if ((n % p) == 0):
            sq_set.append(n)
            found = True
            break
    if (found == False):
        ns_set.append(n)

print "Number of square free results is", len(ns_set)
print "Square free results are", ns_set
print "Number of square results is", len(sq_set)
print "Square results are", sq_set

answer = 0
for n in ns_set:
    answer += n

print "Answer to PE203 =", answer


