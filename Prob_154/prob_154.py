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

# For layer N, the addresses of the values are (x, y, z) or (x, N-x-z,
# z).  There is symmetry in these values, and the value at (x, y, z)
# is identical to the 5 values at (x, z, y), (y, x, z), (y, z, x), (z,
# x, y), and (z, y, x).  This allows us to only calculate the cases
# where x >= y >= z, then we multiply by 6 if x, y, & z are all
# different, by 3 if two of the three values are identical and by 1 if
# all three are identical.
#
# The value of at (x, y, z) is given by C(x, y, z) = N! / (x! * y! * z!)
#
# For this to be divisible by 10**M = 2**M * 5**M, we calculate the
# power of 2 and power of 5 in N! = T and F, then subtract M from each
# one to calculate the maximum powers of 2 and 5 in (x! * y! * z!).
#
# This in turn allows us to limit the values that we consider as valid
# values of (x, y, z).
#
# This solution runs in about an hour, but other solutions in the
# forum are well under 1 minute.  I choose to not spend any more time
# optimizing the run time from here.

(MOD_POWER, POWER) = (12, 200000)
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

def pre_calculations(n, mod_power, power):
    n_factorial_power = [0] * (power+1)

    power_n = 0
    for p in range(2, power+1):
        x = p
        while (x % n) == 0:
            power_n += 1
            x /= n
        n_factorial_power[p] = power_n

    max_power = n_factorial_power[power] - mod_power
    return max_power, n_factorial_power



########################################

def gen_valid_triplets(limit):
    max_power_2, n_factorial_power_2 = pre_calculations(2, MOD_POWER, POWER)
    max_power_5, n_factorial_power_5 = pre_calculations(5, MOD_POWER, POWER)
    print(" max_power_2 = {:,}".format(max_power_2))
    print(" n_factorial_power_2[:11] = {}".format(n_factorial_power_2[:11]))
    print(" max_power_5 = {:,}".format(max_power_5))
    print(" n_factorial_power_5[:11] = {}".format(n_factorial_power_5[:11]))

    min_x = (limit+2)//3

    max_x = limit
    while n_factorial_power_2[max_x] > max_power_2:
        max_x -= 1
    while n_factorial_power_5[max_x] > max_power_5:
        max_x -= 1

    for x in range(max_x, min_x-1, -1):
        max_z = (limit - min_x)//2
        while n_factorial_power_2[x] + n_factorial_power_2[max_z] > max_power_2:
            max_z -= 1
        while n_factorial_power_5[x] + n_factorial_power_5[max_z] > max_power_5:
            max_z -= 1

        for z in range(0, max_z+1):
            y = limit - x - z
            if (x >= y >= z):
                power_2 = n_factorial_power_2[x] + n_factorial_power_2[y] + n_factorial_power_2[z]
                power_5 = n_factorial_power_5[x] + n_factorial_power_5[y] + n_factorial_power_5[z]
                if (power_2 <= max_power_2) and (power_5 <= max_power_5):
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

def prob_154(mod_power, power):
    prev_time = time.clock()
    count = 0
    sum = 0
    answer = 0
    #for trio in gen_triplets(power):
    for trio in gen_valid_triplets(power):
        m = trio_multiplier(trio)
        sum += m
        count += 1
        #c = trinomial_coefficient(power, trio)
        answer += m

        if (count % 100000) == 0:
            print("{}: {:,} terms, {:.2f} seconds delta, {:.2f} seconds total".format(
                trio, count, time.clock() - prev_time, time.clock() - start_time))
            prev_time = time.clock()

    print("{:,} terms calculated out of {:,} total in triangle".format(count, sum))
    return answer


answer = prob_154(MOD_POWER, POWER)
print()
print("With MOD_POWER = {:,}, POWER = {:,}, answer = {:,}".format(MOD_POWER, POWER, answer))

if (MOD_POWER, POWER) in debug_answers:
    expected_answer = debug_answers[(MOD_POWER, POWER)]
    assert answer == expected_answer, "ERROR, expected answer = {:,}, actual answer = {:,}".format(expected_answer, answer)

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
