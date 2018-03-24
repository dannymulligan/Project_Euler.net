#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 407
#
# Idempotents
#
# If we calculate a^2 mod 6 for 0 <= a <= 5 we get: 0,1,4,3,4,1.
#
# The largest value of a such that a^2 ≡ a mod 6 is 4.
#
# Let's call M(n) the largest value of a < n such that a2 === a (mod n).
# So M(6) = 4.
#
# Find sum(M(n)) for 1 <= n <= 10^7.

# This is a brute force solution, which takes 12364 seconds = 206 minutes = 3.5 hours to run
# Some people in the forums have solved it in Python in ~3 mins, or 60x faster, so clearly
# there are some optimizations I'm missing.

import sys
import time
start_time = time.clock()

SIZE = 100
SIZE = int(sys.argv[1])
SizeLimit = SIZE

############################################################
import primes
LIMIT_PRIME = SIZE
prime_table = [1]*LIMIT_PRIME  # table of largest factor
prime_list = []
primes.calculate_primes(LIMIT_PRIME, prime_table, prime_list)

import itertools
import operator
import functools
def divisors(factors0, factors1):
    factors = sorted(factors0 + factors1)
    for l in range(1, len(factors)):
        for c in itertools.combinations(factors, l):
            yield functools.reduce(operator.mul, c)


############################################################

print("Calculating M(n) for n in 1..{:,}".format(SIZE))
m = [1] * (SIZE+1)
m[1] = 0
answer = 0

prev_factors = [2]
prev_time = time.clock()
for a in range(3, SIZE):
    if (a % 25000) == 0:
        print("Calculating M(?) = {:,} with {:.2f} seconds elapsed, {:.3f} seconds delta".format(a, time.clock() - start_time, time.clock() - prev_time))
        prev_time = time.clock()
    
    aam1 = a * (a - 1)
    curr_factors = primes.factors(a, prime_table)
    #print("    a={a}, a*(a-1)={aam1}, prev_factors={p}, curr_factors={c}".format(a=a, aam1=aam1, p=prev_factors, c=curr_factors))
    for d in divisors(prev_factors, curr_factors):
        n = aam1 // d
        if a >= n:
            continue
        if n <=SIZE:
            #print("        M({n}) = {a}".format(n=n, a=a))
            #print("M({n}) = {a}".format(n=n, a=a), end='')
            #print("    a={a}, a*(a-1)={aam1} = {n}*{d}".format(a=a, aam1=aam1, d=d, n=n))
            m[n] = a
    prev_factors = curr_factors

for n in range(1, SIZE+1):
    answer += m[n]
    #print("M({:2}) = {:2}".format(n, m[n]))

print("When SizeLimit = {:,}, answer is {:,} (calculated in {:.2f} seconds)".format(SizeLimit, answer, time.clock() - start_time))
