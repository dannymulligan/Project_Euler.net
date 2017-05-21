#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 429
#
# Sum of squares of unitary divisors
#
# A unitary divisor d of a number n is a divisor of n that has the
# property gcd(d, n/d) = 1.
#
# The unitary divisors of 4! = 24 are 1, 3, 8 and 24.
#
# The sum of their squares is 12 + 32 + 82 + 242 = 650.
#
# Let S(n) represent the sum of the squares of the unitary divisors of
# n. Thus S(4!)=650.
#
# Find S(100000000!) modulo 1000000009.

import sys
#print(sys.version)
import time
start_time = time.clock()

MODULO = 1000000009
TARGET = 10**8

LIMIT_PRIME = TARGET+1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

############################################################
def calculate_primes(limit=LIMIT_PRIME):
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    primes.append(i)
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 2
    print("There are {} primes less than {}, calculated in {:.2f} seconds".format(len(primes), limit, (time.clock() - start_time)))

calculate_primes(LIMIT_PRIME)


############################################################
factorial = [0]*LIMIT_PRIME

for i in range(2,TARGET+1):
    n = i
    while n > 1:
        factor = prime_table[n]
        if factor == 1:
            factorial[n] += 1
            n = 1
        else:
            factorial[factor] += 1
            n = n // factor

#print("factorial =", factorial)


############################################################
squares = [0]*LIMIT_PRIME

for i in range(2,TARGET+1):
    if factorial[i] == 0:
        continue

    s = 1
    for power in range(factorial[i]*2):
        s = (s * i) % MODULO

    squares[i] = s

#print("squares =", squares)


############################################################
answer = 1  # 1^2

for i in range(2,TARGET+1):
    if factorial[i] == 0:
        continue
    answer = (answer * (1 + squares[i])) % MODULO

print("Answer =", answer)

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
