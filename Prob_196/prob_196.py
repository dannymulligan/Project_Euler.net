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


def is_prime_range(bot, top, prime_table):
    '''Return a list like prime_table but starting with a defined offset'''
    assert bot <= top
    assert top <= (len(prime_table)-1)**2, \
        "Error: prime_table needs to be bigger, result will cover {} to {}, len(prime_table) = {}, needs to be {}" \
        .format(bot, top, len(prime_table), integer_square_root(top))
    offset_prime_table = [1] * (top - bot + 1)

    # special case for multiples of 2
    n = bot - (bot % 2)
    while n <= top:
        offset_prime_table[n - bot] = 2
        n += 2

    # iterate through primes >= 3
    for p in range(3, len(prime_table)):
        if prime_table[p] != 1:
            continue  # p is not a prime

        n = bot - (bot % (2*p)) + p  # n = the first odd multiple of p that is >= bot
        while n <= top:
            if bot <= n <= top:
                offset_prime_table[n - bot] = p
            n += p*2
        if p ** 2 > top:
            break

    return offset_prime_table


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

    offset_prime_table = is_prime_range(row_l_min, row_p_max, prime_table)

    def prime_1_0(n):
        if offset_prime_table[n - row_l_min] == 1:
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
    # The above code doesn't cover this case correctly
    # Row M:  0, 1, 0, 0, 0
    # Row N:  1, 0, 1, 0, 0
    # Row O:  0, 0, 0, 0, 0
    # So look for it explicitly
    for n in range(len(row_n_prime)-2):
        if row_n_prime[n] and row_n_prime[n+2]:
            if row_m_prime[n+1] or row_o_prime[n+1]:
                row_n_prime[n] += 1
                row_n_prime[n+2] += 1


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
TARGET1 = 5678027
TARGET2 = 7208785
TARGET = TARGET1 + TARGET2 + 100

row_min, row_max = triangle_row_range(TARGET)
print("Row {} is from {} to {}".format(TARGET, row_min, row_max))

min_needed, _ = triangle_row_range(TARGET-2)
_, max_needed = triangle_row_range(TARGET+2)
print("Need to know primes from {:,} to {:,}".format(min_needed, max_needed))

max_prime_table = integer_square_root(max_needed) + 1
print("Generating a table of primes < {:,}".format(max_prime_table))
print("This will allow us to check primes < {:,}".format(max_prime_table**2))

import primes
prime_table, prime_list = primes.calculate_primes(max_prime_table+1)

#answer1 = S(41, debug=True)
#print("S({:,}) = {:,}".format(41, answer1))
#sys.exit()

#            (       n,              S(n)),

#            (       n,              S(n)),
TestCases = [(       8,                 60),  # Given in the problem statement
             (       9,                 37),  # Given in the problem statement
             (      40,                797),
             (      50,               3709),
             (      60,               5399),
             (     100,               9938),
             (    1000,            3500211),
             (    1010,            8162514),
             (   10000,          950007619),  # Given in the problem statement
             (   25000,        11250007474),
             (   50000,       232499865696),
             (   75000,       975937610571),
             (  100000,       549999566882),
             (  250000,      8749999468456),
             (  500000,     98375000264623),
             ( 1000000,    463999977061648)]

# before using is_prime_range()...
#
# Testing - verifying S(8) = 60, ran in 0.000 seconds
# Testing - verifying S(9) = 37, ran in 0.000 seconds
# Testing - verifying S(1000) = 3500211, ran in 0.041 seconds
# Testing - verifying S(10000) = 950007619, ran in 0.397 seconds
# Testing - verifying S(25000) = 11250007474, ran in 0.924 seconds
# Testing - verifying S(50000) = 176249823503, ran in 2.081 seconds
# Testing - verifying S(75000) = 776250028962, ran in 3.380 seconds
# Testing - verifying S(100000) = 549999566882, ran in 4.510 seconds
# Testing - verifying S(125000) = 2000000444988, ran in 5.748 seconds
# Testing - verifying S(150000) = 5141250480315, ran in 7.093 seconds
# Testing - verifying S(200000) = 6620000729143, ran in 9.331 seconds
# Testing - verifying S(250000) = 8749999468456, ran in 11.922 seconds
#
# after using is_prime_range()...
#
# Testing - verifying S(8) = 60, ran in 0.000 seconds
# Testing - verifying S(9) = 37, ran in 0.000 seconds
# Testing - verifying S(1000) = 3500211, ran in 0.003 seconds
# Testing - verifying S(10000) = 950007619, ran in 0.033 seconds
# Testing - verifying S(25000) = 11250007474, ran in 0.083 seconds
# Testing - verifying S(50000) = 176249823503, ran in 0.179 seconds
# Testing - verifying S(75000) = 776250028962, ran in 0.245 seconds
# Testing - verifying S(100000) = 549999566882, ran in 0.337 seconds
# Testing - verifying S(125000) = 2000000444988, ran in 0.417 seconds
# Testing - verifying S(150000) = 5141250480315, ran in 0.508 seconds
# Testing - verifying S(200000) = 6620000729143, ran in 0.679 seconds
# Testing - verifying S(250000) = 8749999468456, ran in 0.908 seconds

if False:
    for Test in TestCases:
        (n, expect) = Test
        print("Testing - verifying S({:,}) = {:,}".format(n, expect), end='')
        start_time = time.clock()
        answer = S(n)
        print(", ran in {:.3f} seconds".format(time.clock() - start_time))
        #assert answer == expect, "S({:,}) should be {:,} but got {:,}".format(n, expect, answer)
        if not answer == expect:
            print("S({:,}) should be {:,} but got {:,}".format(n, expect, answer))
    sys.exit()

start_time = time.clock()
answer1 = S(TARGET1)
print("S({:,}) = {:,}".format(TARGET1, answer1))
answer2 = S(TARGET2)
print("S({:,}) = {:,}".format(TARGET2, answer2))

print("Answer = {:,}".format(answer1 + answer2))

print("Time taken = {:.3f} seconds".format(time.clock() - start_time))
