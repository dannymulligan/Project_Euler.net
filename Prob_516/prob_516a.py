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

# Answer is S(  1,000,000) = 2,236,471,777, Required  3,720 results from products_less_than(), Time taken =  3.09 seconds
# Answer is S(100,000,000) = 3,620,613,805, Required 38,406 results from products_less_than(), Time taken = 99.32 seconds
#
# Deleted the parts of products_less_than() that pass around a list of the primes that multiplied together
# to generate the result being returned.
#
# Answer is S(  1,000,000) = 2,236,471,777, Required  3,720 results from products_less_than(), Time taken =   2.22 seconds
# Answer is S(100,000,000) = 3,620,613,805, Required 38,406 results from products_less_than(), Time taken =  72.66 seconds
# Answer is S(500,000,000) = 4,179,987,535, Required 83,360 results from products_less_than(), Time taken = 235.40 seconds

# Reversed the order of the prime_hamming_table, makes products_less_than() generator run much faster
# because larger initial numbers mean less depth of recursion up and down.
#
# Answer is S(        1,000,000) = 2,236,471,777, Required     3,720 results from products_less_than(), Time taken =   0.13 seconds
# Answer is S(      100,000,000) = 3,620,613,805, Required    38,406 results from products_less_than(), Time taken =   1.42 seconds
# Answer is S(      500,000,000) = 4,179,987,535, Required    83,360 results from products_less_than(), Time taken =   3.32 seconds
# Answer is S(    1,000,000,000) =   964,002,218, Required   115,646 results from products_less_than(), Time taken =   4.76 seconds
# Answer is S(   10,000,000,000) = 3,546,796,075, Required   336,907 results from products_less_than(), Time taken =  15.83 seconds
# Answer is S(  100,000,000,000) = 3,340,605,175, Required   950,489 results from products_less_than(), Time taken =  52.28 seconds
# Answer is S(1,000,000,000,000) =   xxx,xxx,xxx, Required 2,609,415 results from products_less_than(), Time taken = 164.31 seconds


import time
start_time = time.clock()

LIMIT_PRIMES = 10**4
LIMIT_CHALLENGE = 10**12

import primes
prime_table, prime_list = primes.calculate_primes(LIMIT_PRIMES)

p2limit = 1
while 2**p2limit < LIMIT_CHALLENGE:
    p2limit += 1

p3limit = 1
while 3**p3limit < LIMIT_CHALLENGE:
    p3limit += 1

p5limit = 1
while 5**p5limit < LIMIT_CHALLENGE:
    p5limit += 1

print("largest possible power of 2 is 2**{} = {:,}".format(p2limit, 2**p2limit))
print("largest possible power of 3 is 3**{} = {:,}".format(p3limit, 3**p3limit))
print("largest possible power of 5 is 5**{} = {:,}".format(p5limit, 5**p5limit))

hamming_table = dict()
for p2 in range(p2limit):
    for p3 in range(p3limit):
            for p5 in range(p5limit):
                x = 2**p2 * 3**p3 * 5**p5
                if x <= LIMIT_CHALLENGE:
                    hamming_table[x] = (p2, p3, p5)

print("There are {} hamming numbers less than or equal to LIMIT_CHALLENGE = {:,}".format(len(hamming_table), LIMIT_CHALLENGE))
#print(sorted(hamming_table.keys()))

multiplier_table = []
cum_multiplier = 0
for x in sorted(hamming_table.keys()):
    cum_multiplier += x
    multiplier_table.append((x, cum_multiplier))
    #print("{} = {}, cumulative = {}".format(x, hamming_table[x], cum_multiplier))
#print(multiplier_table)


def max_mult(num, multiplier_table, limit):
    bot = 0
    top = len(multiplier_table)
    while (top - bot) > 1:
        mid = (top + bot) // 2
        mult, cum = multiplier_table[mid]
        if mult*num <= limit:
            bot = mid
        else:
            top = mid
    return multiplier_table[bot]

prime_hamming_table = dict()
for entry in hamming_table:
    if primes.is_prime(entry+1, prime_table):
        prime_hamming_table[entry+1] = hamming_table[entry]

prime_hamming_table = sorted(prime_hamming_table)
prime_hamming_table = prime_hamming_table[3:]  # Delete 2, 3, 5 from the list
prime_hamming_table.sort(reverse=True)
print("There are {} primes less than or equal to LIMIT_CHALLENGE = {:,}, with hamming totient numbers".format(len(prime_hamming_table), LIMIT_CHALLENGE))
#print(prime_hamming_table)

def products_less_than(curr, nums, limit, debug):
    if debug:
        print("products_less_than({}, {}, {}, {})".format(curr, nums, limit, debug))
    if len(nums) == 1:
        if curr * nums[0] <= limit:
            if debug:
                print("    terminal case a -> {}, {}".format(nums[0], nums))
            yield nums[0]
        if debug:
            print("    terminal case b -> {}, {}".format(1, []))
        return 1, []
    else:
        if curr*nums[0] <= limit:
            for number in products_less_than(curr*nums[0], nums[1:], limit, debug):
                if curr * nums[0] * number <= limit:
                    if debug:
                        print("    multiply {} by {} and recurse -> {}, {}".format(nlist, nums[0], nums[0]*number, [nums[0]] + nlist))
                    yield nums[0] * number

        if curr <= limit:
            for number in products_less_than(curr, nums[1:], limit, debug):
                if number <= limit:
                    if debug:
                        print("    multiply {} by {} and recurse -> {}, {}".format(nlist, 1, number, nlist))
                    yield number

        if nums[0] <= limit:
            if debug:
                print("    {} by itself -> {}, {}".format(nums[0], nums[0], [nums[0]]))
            yield nums[0]  # num[0] alone

if False:
    nlist = [2, 3, 4, 5, 6]
    limit = 25
    debug = False
    print()
    print("limit = {}, nlist = {}, debug = {}".format(limit, nlist, debug))
    print()
    for x, l in products_less_than(1, nlist, limit, debug):
        print(x, l)

if False:
    nlist = prime_hamming_table[:12]
    limit = 150
    print()
    print("limit = {}, nlist = {}".format(limit, nlist))
    print()
    for x, l in products_less_than(1, nlist, limit, False):
        print(x, l)

answer = 0
mult, sum = max_mult(1, multiplier_table, LIMIT_CHALLENGE)
answer += sum
count = 1
for product in products_less_than(1, prime_hamming_table, LIMIT_CHALLENGE, False):
    count += 1
    mult, sum = max_mult(product, multiplier_table, LIMIT_CHALLENGE)
    answer = (answer + sum*product) % 2**32
    if not (count % 25000):
        print("calcualted {:,} products after {:.2f} seconds".format(count, time.clock() - start_time))
print("Answer is S({:,}) = {:,}".format(LIMIT_CHALLENGE, answer))
print("Required {:,} results from products_less_than()".format(count))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
