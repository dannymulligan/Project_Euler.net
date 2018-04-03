#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 516
#
# 5-smooth totients
#
# 5-smooth numbers are numbers whose largest prime factor doesn't
# exceed 5.
#
# 5-smooth numbers are also called Hamming numbers.
#
# Let S(L) be the sum of the numbers n not exceeding L such that
# Euler's totient function φ(n) is a Hamming number.
#
# S(100)=3728.
#
# Find S(10^12). Give your answer modulo 2^32.

#
# S(100) = 3,728
#
# S(1,000) = 203,813 after 1.01 seconds
# S(2,000) = 657,877 after 4.01 seconds
# S(3,000) = 1,296,476 after 9.03 seconds
# S(4,000) = 2,105,735 after 16.09 seconds
# S(5,000) = 3,054,007 after 25.15 seconds
# S(6,000) = 4,092,790 after 36.24 seconds
# S(7,000) = 5,320,420 after 49.38 seconds
# S(8,000) = 6,588,178 after 64.44 seconds
# S(9,000) = 8,011,764 after 81.65 seconds
# S(10,000) = 9,586,559 after 100.87 seconds
# S(11,000) = 11,170,609 after 122.09 seconds
# S(12,000) = 12,825,261 after 145.34 seconds
# S(13,000) = 14,648,753 after 170.68 seconds
# S(14,000) = 16,512,096 after 197.97 seconds
# S(15,000) = 18,441,249 after 227.59 seconds
# S(16,000) = 20,515,942 after 259.09 seconds
# S(17,000) = 22,757,252 after 292.52 seconds
# S(18,000) = 24,894,340 after 327.97 seconds
# S(19,000) = 27,185,005 after 365.55 seconds
# S(20,000) = 29,679,566 after 405.33 seconds


SIZE = 20000

import sys
#print(sys.version)
import time
start_time = time.clock()


############################################################
import fractions
def phi_slow(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount


############################################################
import primes
prime_table, prime_list = primes.calculate_primes(SIZE+1)

def phi(n):
    factors = primes.factors(n, prime_table)

    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

if False:
    phi_reference = [ 1,  1,  2,  2,  4,  2,  6,  4,  6,
                      4, 10,  4, 12,  6,  8,  8, 16,  6, 18,
                      8, 12, 10, 22,  8, 20, 12, 18, 12, 28,
                      8, 30, 16, 20, 16, 24, 12, 36, 18, 24,
                     16, 40, 12, 42, 20, 24, 22, 46, 16, 42,
                     20, 32, 24, 52, 18, 40, 24, 36, 28, 58,
                     16, 60, 30, 36, 32, 48, 20, 66, 32, 44,
                     24, 70, 24, 72, 36, 40, 36, 60, 24, 78,
                     32, 54, 40, 82, 24, 64, 42, 56, 40, 88,
                     24, 72, 44, 60, 46, 72, 32, 96, 42, 60, ]

    phi_check = [phi_slow(n) for n in range(1, 100)]

    print(phi_check)
    print(phi_reference)
    print(phi_check == phi_reference)


############################################################

def is_hamming(n):
    while (n % 2) == 0:
        n /= 2
    while (n % 3) == 0:
        n /= 3
    while (n % 5) == 0:
        n /= 5
    return n == 1

if False:
    hamming_numbers = [13, 17, 19, 31, 37, 41, 61, 73, 97, 101, 109, 151, 163, 181, 193, 241, 251, 257, 271, 401, 433]

    for number in hamming_numbers:
        print(number-1)
        assert is_hamming(number-1)
        assert not is_hamming(number)


############################################################
answer = 0
for n in range(1, SIZE+1):
    if is_hamming(phi(n)):
        answer = (answer + n) % 2**32
        #print("phi({}) = {}".format(n, phi(n)))
    if not (n % 1000):
        print("S({:,}) = {:,} after {:.2f} seconds".format(n, answer, time.clock() - start_time))

print("Answer S({:,}) = {:,}".format(n, answer))



print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
