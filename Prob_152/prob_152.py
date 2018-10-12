#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 152
#
# Writing 1/2 as a sum of inverse squares
#
# There are several ways to write the number 1/2 as a sum of inverse
# squares using distinct integers.
#
# For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:
#
# In fact, only using integers between 2 and 45 inclusive, there are
# exactly three ways to do it, the remaining two being:
# {2,3,4,6,7,9,10,20,28,35,36,45} and
# {2,3,4,6,7,9,12,15,28,30,35,36,45}.
#
# How many ways are there to write the number 1/2 as a sum of inverse
# squares using distinct integers between 2 and 80 inclusive?

import sys
import time
start_time = time.clock()


###############################################################################
SIZE = 45
print("Calculating the solution using integers up to {}".format(SIZE))

import primes
nums = [n for n in range(2, SIZE+1)]
lcm = primes.lcm(nums)
print("LCM = {}".format(lcm))


###############################################################################

def fractional_value(x_s):
    value = fractions.Fraction(0, 1)
    for x in x_s:
        value += fractions.Fraction(1, x**2)
    return value

if False:
    testcases = [
        ([2, 3, 4, 5, 7, 12, 15, 20, 28, 35], fractions.Fraction(1,2)),
        ([2, 3, 4, 6, 7, 9, 10, 20, 28, 35, 36, 45], fractions.Fraction(1,2)),
        ([2, 3, 4, 5, 7, 9, 12, 15, 28, 30, 35, 36, 45], fractions.Fraction(461,900)),
        ([2, 3, 4, 6, 7, 9, 12, 15, 28, 30, 35, 36, 45], fractions.Fraction(1,2)),
        ]
    for (x_s, answer) in testcases:
        result = fractional_value(x_s)
        assert result == answer, \
            "value({}) = {} but expecting 1/2".format(x_s, result)
    print("Test of verify() passed")
    sys.exit()


###############################################################################

def precalc_values(n_min, n_max):
    print("precalc_values({},{})".format(n_min, n_max))
    max_solutions = 1
    lookup_table = dict()
    for i in range(2**(n_max - n_min + 1)):
        x_s = []
        x = n_min
        n = i
        value = 0.0
        while x <= n_max:
            if (n % 2) == 1:
                x_s.append(x)
                value += 1/(x**2)
            n = n // 2
            x += 1
        if value in lookup_table:
            lookup_table[value].append(x_s)
            max_solutions = max(max_solutions, len(lookup_table[value]))
            #print("{} solutions for {}".format(len(lookup_table[value]), value))
        else:
            lookup_table[value] = [x_s]
    return lookup_table


###############################################################################

def calc_values(n_min, n_max):
    print("calc({},{})".format(n_min, n_max))
    for i in range(2**(n_max - n_min + 1)):
        x_s = []
        x = n_min
        n = i
        value = 0.0
        while x <= n_max:
            if (n % 2) == 1:
                x_s.append(x)
                value += 1/(x**2)
            n = n // 2
            x += 1
        yield value, x_s


###############################################################################

def find_solution(value, x_s, target_value):
    #print("find_solution({}, {}, {})".format(value, x_s, target_value))
    global values
    global value_table
    global resolution
    solutions = 0
    i_max = len(values) - 1

    v_min = 0.5 - value - resolution
    v_max = 0.5 - value + resolution
    #print("          v_min = {},       v_max = {}".format(v_min, v_max))

    i_min_a = 0
    i_min_b = 1
    while (values[i_min_b] < v_min) and (i_min_b < i_max):
        i_min_a, i_min_b = i_min_b, i_min_b*2
        i_min_b = min(i_max, i_min_b)

    while (values[i_min_a] < v_min) and  (values[i_min_b] > v_min) and (i_min_b - i_min_a > 1):
        i_min_c = (i_min_a + i_min_b) // 2
        if values[i_min_c] > v_min:
            i_min_b = i_min_c
        else:
            i_min_a = i_min_c

    i_max_a = i_min_a
    i_max_b = i_max
    while (values[i_max_a] < v_max) and  (values[i_max_b] > v_max) and (i_max_b - i_max_a > 1):
        i_max_c = (i_max_a + i_max_b) // 2
        if values[i_max_c] > v_max:
            i_max_b = i_max_c
        else:
            i_max_a = i_max_c

    #print("min values[{}] = {}, values[{}] = {}".format(
    #    i_min_a, values[i_min_a], i_min_b, values[i_min_b]))
    #print("max values[{}] = {}, values[{}] = {}".format(
    #    i_max_a, values[i_max_a], i_max_b, values[i_max_b]))

    for i in range(i_min_b, i_max_b):
        value = values[i]
        for possible in value_table[value]:
            answer = x_s + possible
            f_value = fractional_value(answer)
            print("    Attempted solution {} = {} = {}".format(answer, float(f_value), f_value))
            if fractional_value(answer) == target:
                print("Solution found = {}".format(answer))
                solutions += 1

    return solutions


#value = fractional_value([2, 3, 4, 5, 7, 12, 15])
#print(value, float(value), 0.5 - float(value))


###############################################################################

answer = 0
split = 24
value_table = precalc_values(SIZE - split, SIZE)
values = [value for value in sorted(value_table)]
max_value = values[-1]
print("max_value = {}".format(max_value))
print("len(values) = {}".format(len(values)))
#print("values[:20] = {}".format(values[:20]))
print("Finished pre-calculating values after {:.2f} seconds".format(time.clock() - start_time))
print("")

n_max = SIZE - split - 1
n_min = 2
target = fractions.Fraction(1,2)
upper_limit = 0.5 + resolution
lower_limit = 0.5 - max_value - resolution
print(lower_limit, upper_limit)
for i in range(2**(n_max - n_min + 1)):

    x_s = []
    x = n_max
    n = i
    value = 0.0
    while x >= n_min:
        if (n % 2) == 1:
            x_s.append(x)
            value += 1/(x**2)
        n = n // 2
        x -= 1

    x_s = sorted(x_s)
    #print(i, x_s, value)
    if (value > lower_limit) and (value < upper_limit):
        # Test this value to see if it is a solution
        attempt = 0
        answer += find_solution(value, x_s, target)

print("{:,} solutions found".format(answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
