#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 491
#
# Double pandigital number divisible by 11
#
# We call a positive integer double pandigital if it uses all the
# digits 0 to 9 exactly twice (with no leading zero). For example,
# 40561817703823564929 is one such number.
#
# How many double pandigital numbers are divisible by 11?
#

import itertools
import math
import sys
import time
start_time = time.clock()

DIGITS = 7
numbers = [x for x in range(DIGITS)]*2

answer = 0

# From: https://stackoverflow.com/questions/6284396/permutations-with-unique-values
def unique_permutations(elements):
    if len(elements) == 1:
        yield (elements[0],)
    else:
        unique_elements = set(elements)
        for first_element in unique_elements:
            remaining_elements = list(elements)
            remaining_elements.remove(first_element)
            for sub_permutation in unique_permutations(remaining_elements):
                yield (first_element,) + sub_permutation
                

for i in unique_permutations(numbers):
    if i[0] == 0:
        continue

    even = []
    odd = []
    for n in range(len(numbers)):
        if ((n % 2) == 1):
            odd.append(i[n])
        else:
            even.append(i[n])


    if sum(odd) != sum(even):
        continue
    
    answer += 1
    if (answer % 10000) == 0:
        number = 0
        for d in i:
            number *= 10
            number += d
        print(i, number, even, odd)
        #print("odd ", sorted(odd), odd)
        #print("even ", sorted(even), even)

print("Answer for DIGITS = {} is {:,}".format(DIGITS, answer))

# Answer for DIGITS = 3 is 24
# Answer for DIGITS = 4 is 486
# Answer for DIGITS = 5 is 15,840
# Answer for DIGITS = 6 is 810,000
# Answer for DIGITS = 7 is 59,194,800
