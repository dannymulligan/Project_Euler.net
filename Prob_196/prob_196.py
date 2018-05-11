#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 196
#
# Prime triplets
#
# Build a triangle from all positive integers in the following way:
#
#    1:    1
#    2:   <2>  <3>
#    3:    4   <5>   6
#    4:   <7>   8    9   10
#    5:  <11>  12  <13>  14   15
#    6:   16  <17>  18  <19>  20   21
#    7:   22  <23>  24   25   26   27   28
#    8:  <29>  30  <31>  32   33   34   35   36
#    9:  <37>  38   39   40  <41>  42  <43>  44  45
#   10:   46  <47>  48   49   50   51   52  <53> 54  55
#   11:   56   57   58  <59>  60  <61>  62   63  64  65  66
#      . . .
#
# Each positive integer has up to eight neighbours in the triangle.
#
# A set of three primes is called a prime triplet if one of the three
# primes has the other two as neighbours in the triangle.
#
# For example, in the second row, the prime numbers 2 and 3 are
# elements of some prime triplet.
#
# If row 8 is considered, it contains two primes which are elements of
# some prime triplet, i.e. 29 and 31.
# If row 9 is considered, it contains only one prime which is an
# element of some prime triplet: 37.
#
# Define S(n) as the sum of the primes in row n which are elements of
# any prime triplet.  Then S(8)=60 and S(9)=37.
#
# You are given that S(10000)=950007619.
#
# Find S(5678027) + S(7208785).
#
# Solved ??/??/14
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

########################################
def triangle(n):
    return n*(n+1)//2

def triangle_row_range(n):
    return triangle(n-1)+1, triangle(n)+1

def integer_square_root(n):
    '''Return largest m where m**2 <= n'''
    m = 1
    while m**2 <= n:
        m += 1
    return m-1


def S(target_row, debug=False):
    if debug:
        print("S({:,}, debug={})".format(target_row, debug))
    ########################################
    # Calculate rows l, m, n, o, p
    if debug:
        print("Calculate rows l, m, n, o, p")

    row_l_min, row_l_max = triangle_row_range(target_row-2)
    row_m_min, row_m_max = triangle_row_range(target_row-1)
    row_n_min, row_n_max = triangle_row_range(target_row)
    row_o_min, row_o_max = triangle_row_range(target_row+1)
    row_p_min, row_p_max = triangle_row_range(target_row+2)

    row_l_value = [n for n in range(row_l_min, row_l_max)]
    row_m_value = [n for n in range(row_m_min, row_m_max)]
    row_n_value = [n for n in range(row_n_min, row_n_max)]
    row_o_value = [n for n in range(row_o_min, row_o_max)]
    row_p_value = [n for n in range(row_p_min, row_p_max)]

    def prime_1_0(n):
        if primes.is_prime(n, prime_table):
            return 1
        else:
            return 0

    row_l_prime = [prime_1_0(n) for n in row_l_value]
    row_m_prime = [prime_1_0(n) for n in row_m_value]
    row_n_prime = [prime_1_0(n) for n in row_n_value]
    row_o_prime = [prime_1_0(n) for n in row_o_value]
    row_p_prime = [prime_1_0(n) for n in row_p_value]


    ########################################
    # Count adjacent primes in row m
    if debug:
        print("Count adjacent primes in row m")

    for n in range(len(row_m_prime)):
        if row_m_prime[n]:
            a, b = n-1, n+1
            a = max(0, a)
            b = min(b, len(row_l_prime))
            adjacent_l = sum(row_l_prime[a:b+1])
            if adjacent_l == 1:
                row_m_prime[n] = 2
            elif adjacent_l == 2:
                row_m_prime[n] = 3


    ########################################
    # Count adjacent primes in row o
    if debug:
        print("Count adjacent primes in row o")

    for n in range(len(row_o_prime)):
        if row_o_prime[n]:
            a, b = n-1, n+1
            a = max(0, a)
            adjacent_p = sum(row_p_prime[a:b+1])
            if adjacent_p == 1:
                row_o_prime[n] = 2
            elif adjacent_p == 2:
                row_o_prime[n] = 3


    ########################################
    # Count adjacent primes in row n
    if debug:
        print("Count adjacent primes in row n")

    for n in range(len(row_n_prime)):
        if row_n_prime[n]:
            a, b = n-1, n+1
            a = max(0, a)
            b = min(b, len(row_m_prime))
            adjacent_m = sum(row_m_prime[a:b+1])

            a, b = n-1, n+1
            a = max(0, a)
            adjacent_o = sum(row_o_prime[a:b+1])

            row_n_prime[n] += adjacent_m + adjacent_o


    ########################################
    # Generate count of triplets in row n
    if debug:
        print("Count count of triplets in row n")
    answer = 0
    for n in range(len(row_n_prime)):
        if row_n_prime[n] >= 3:
            answer += row_n_value[n]

    if debug and (n < 100):
        print("row_l_prime = {}".format(row_l_prime))
        print("row_m_prime = {}".format(row_m_prime))
        print("row_n_prime = {}".format(row_n_prime))
        print("row_o_prime = {}".format(row_o_prime))
        print("row_p_prime = {}".format(row_p_prime))

    return answer


########################################
TARGET = 100
#TARGET = 5678027
#TARGET = 7208785

row_min, row_max = triangle_row_range(TARGET)
print("Row {} is from {} to {}".format(TARGET, row_min, row_max))

min_needed, _ = triangle_row_range(TARGET-2)
_, max_needed = triangle_row_range(TARGET+2)
print("Need to know primes from {:,} to {:,}".format(min_needed, max_needed))

max_prime_table = integer_square_root(max_needed) + 1
print("Generating a table of primes < {:,}".format(max_prime_table))
print("This will allow us to check primes < {:,}".format(max_prime_table**2))

import primes
prime_table, prime_list = primes.calculate_primes(max_prime_table)


if False:
    answer, expect = S(8), 60
    assert answer == expect, "S(8) == {:,} given in the problem statement, but we got {:,}".format(expect, answer)
    answer, expect = S(9), 37
    assert answer == expect, "S(9) == {:,} given in the problem statement, but we got {:,}".format(expect, answer)
    answer, expect = S(1000), 3500211
    assert answer == expect, "S(1000) == {:,} calculated from earlier version of code, but we got {:,}".format(expect, answer)
    answer, expect = S(10000), 950007619
    assert answer == expect, "S(10000) == {:,} given in the problem statement, but we got {:,}".format(expect, answer)
    answer, expect = S(100000), 549999566882
    assert answer == expect, "S(100000) == {:,} calculated from earlier version of code, but we got {:,}".format(expect, answer)

import cProfile
start_time = time.clock()

n = 5678027
n = 10000
cProfile.run('S(n, debug=True)')
#print("S({}) = {}".format(n, S(n, debug=True)))

print("Time taken = {:.3f} seconds".format(time.clock() - start_time))
