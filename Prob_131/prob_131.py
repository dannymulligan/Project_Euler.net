#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 131
#
# Determining primes, p, for which n^3 + p*n^2 is a perfect cube.
#
# There are some prime values, p, for which there exists a positive
# integer, n, such that the expression n^3 + p*n^2 is a perfect cube.
#
# For example, when p = 19, 83 + 82×19 = 123.
#
# What is perhaps most surprising is that for each prime with this
# property the value of n is unique, and there are only four such
# primes below one-hundred.
#
# How many primes below one million have this remarkable property?
#
# Solved 02/09/14
# 189 problems solved
# Position #191 on level 7

import time
start_time = time.clock()

LIMIT_PRIME = 1000000  # There are 78,498 primes less than 1,000,000
#LIMIT_PRIME = 100000   # There are 9,592 primes less than 100,000
#LIMIT_PRIME = 10000    # There are 1,229 primes less than 10,000
#LIMIT_PRIME = 1000     # There are 168 primes less than 1,000
#LIMIT_PRIME = 100      # There are 25 primes less than 100
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

def calculate_primes():
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1
    while (i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 1


calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME


#     N^3 + P * N^2 = M^3
#
#           (    P)
#  => N^3 * (1 + -) = M^3
#           (    N)
#
#           (N + P)
#  => N^3 * (-----) = M^3
#           (  N  )
#
# Take the cube root of each side
#             _____
#            /N + P
#  => N *   / ----- = M
#        \3/    N
#
# Therefore
#
# Since M is an integer, then
#              ______
#           \3/ N + P
# must be an integer, therefore N+P is a perfect cube, say N+P = X^3
#
# Similarily
#              ___
#           \3/ N
# must be an integer, therefore N is a perfect cube, say N = Y^3
#
# Thus P = X^3 - Y^3 = (X - Y) * (X^2 + XY + Y^2)
#
# Then, since P is prime, (X - Y) has to be 1
#
# So we must search for results where P =  X^3 - Y^3 is prime, with X = Y + 1
#
# Beautiful solution from: http://www.mathblog.dk/project-euler-131-primes-perfect-cube/

def int_cube_root(x3):
    #print "find_p(m={m}, n={n})".format(m=m, n=n)
    min_x = 1
    max_x = x3
    while ((max_x - min_x) > 1):
        x = (min_x + max_x)/2
        if (x**3 == x3):
            return x
        elif (x**3 < x3):
            min_x = x
        else:
            max_x = x
    x = max_x
    if (x**3 == x3):
        return x
    else:
        return 0

assert int_cube_root(9) == 0
assert int_cube_root(8) == 2


answer = 0

for x in range(2, LIMIT_PRIME):
    y = x - 1
    p = x**3 - y**3
    n = y**3

    if (p > LIMIT_PRIME):
        print "Terminating with X={x}, Y={y}, N={n}, P={p}, M={m}".format(x=x, y=y, m=m, n=n, p=p)
        break

    if p in primes:
        m = int_cube_root(n**3 + p * n**2)
        print "    N={n}, P={p}, M={m}: {n}^3 + {p}*{n}^2 = {m}^3  (VALID SOLUTION)".format(m=m, n=n, p=p)
        answer += 1

print "The answer is", answer
print "Time taken =", time.clock() - start_time, "seconds"
