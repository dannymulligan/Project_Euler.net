#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 154
#
# Exploring Pascal's pyramid
#
# A triangular pyramid is constructed using spherical balls so that
# each ball rests on exactly three balls of the next lower level.
#
#    n = 0:                1
#
#    n = 1:                1
#                        1   1
#
#    n = 2:                1
#                        2   2
#                      1   2   1
#
#    n = 3:                1
#                        3   3
#                      3   6   3
#                    1   3   3   1
#
# Then, we calculate the number of paths leading from the apex to each
# position:
#
# A path starts at the apex and progresses downwards to any of the
# three spheres directly below the current position.
#
# Consequently, the number of paths to reach a certain position is the
# sum of the numbers immediately above it (depending on the position,
# there are up to three numbers above it).
#
# The result is Pascal's pyramid and the numbers at each level n are
# the coefficients of the trinomial expansion (x + y + z)^n.
#
# How many coefficients in the expansion of (x + y + z)^200000 are
# multiples of 10^12?

# When the modulus is 10**12, this is approximately 2**40.  A 64-bit
# integer is big enough to store this, but a 32 bit integer is not.

(MOD_POWER, POWER) = (3, 30)
# debug_answers[(MOD_POWER, POWER)] = answer
debug_answers = {(2, 10): 3,
                 (2, 20): 33,
                 (2, 30): 270,
                 (3, 30): 30,
                 (3, 50): 390,
                 (4, 50): 69}

print("Running with MOD_POWER = {:,}, POWER = {:,}".format(MOD_POWER, POWER))

import sys
#print(sys.version)
import time
start_time = time.clock()
import numpy as np
import math

modulus = 10**MOD_POWER

########################################

n_factorial_power_2 = [0] * (POWER+1)

power_2 = 0
for p in range(2, POWER+1):
    n = p
    while (n % 2) == 0:
        power_2 += 1
        n /= 2
    n_factorial_power_2[p] = power_2

n_factorial_power_5 = [0] * (POWER+1)

power_5 = 0
for p in range(2, POWER+1):
    n = p
    while (n % 5) == 0:
        power_5 += 1
        n /= 5
    n_factorial_power_5[p] = power_5

print("n_factorial_power_2[:10] = {}".format(n_factorial_power_2[:10]))
print("n_factorial_power_5[:10] = {}".format(n_factorial_power_5[:10]))

print("n_factorial_power_2[{}] = {:,}".format(POWER, n_factorial_power_2[POWER]))
print("n_factorial_power_5[{}] = {:,}".format(POWER, n_factorial_power_5[POWER]))

max_power_2 = n_factorial_power_2[POWER] - MOD_POWER
max_power_5 = n_factorial_power_5[POWER] - MOD_POWER

print("max_power_2 = {:,}".format(max_power_2))
print("max_power_5 = {:,}".format(max_power_5))


########################################

def gen_valid_triplets(limit):
    min_x_value = (limit+2)//3
    max_x_value = limit
    while n_factorial_power_2[max_x_value] > max_power_2:
        max_x_value -= 1
    while n_factorial_power_2[max_x_value] > max_power_2:
        max_x_value -= 1

    for x in range(max_x_value, min_x_value-1, -1):
        max_z_value = (limit - min_x_value)//2
        for z in range(0, max_z_value+1):
            y = limit - x - z
            if (x >= y >= z):
                yield (x, y, z)


########################################


def gen_triplets(limit):
    lowest_x_value = (limit+2)//3
    for x in range(limit, lowest_x_value-1, -1):
        largest_z_value = (limit - lowest_x_value)//2
        for z in range(0, largest_z_value+1):
            y = limit - x - z
            if (x >= y >= z):
                yield (x, y, z)

def trio_multiplier(trio):
    (x, y, z) = trio
    if x == y == z:
        return 1
    elif (x == y) or (y == z) or (z == x):
        return 3
    else:
        return 6

def trinomial_coefficient(n, trio):
    (x, y, z) = trio
    result = math.factorial(n) // (math.factorial(x) * math.factorial(y) * math.factorial(z))
    return result


prev_time = start_time
count = 0
sum = 0
answer = 0
#for trio in gen_triplets(POWER):
for trio in gen_valid_triplets(POWER):
    m = trio_multiplier(trio)
    sum += m
    count += 1
    c = trinomial_coefficient(POWER, trio)
    if (c % modulus) == 0:
        answer += m
        print ("{} x {} = {} x {} -> answer = {}".format(m, trio, m, c, answer))
    else:
        print ("{} x {} = {} x {}".format(m, trio, m, c, m))

    if (count % 1000000) == 0:
        print("{:,} terms, {:.2f} seconds delta, {:.2f} seconds total".format(
            count, time.clock() - prev_time, time.clock() - start_time))
        prev_time = time.clock()

print("{:,} terms calculated out of {:,} total in triangle".format(count, sum))

print()
print("With MOD_POWER = {:,}, POWER = {:,}, answer = {:,}".format(MOD_POWER, POWER, answer))

if (MOD_POWER, POWER) in debug_answers:
    expected_answer = debug_answers[(MOD_POWER, POWER)]
    assert answer == expected_answer, "ERROR, expected answer = {:,}, actual answer = {:,}".format(expected_answer, answer)

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
