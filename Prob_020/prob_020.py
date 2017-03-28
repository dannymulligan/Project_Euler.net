#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 20
#
# Factorial digit sum
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import math
import sys
import time
start_time = time.clock()

N = 100

Factorial = math.factorial(N)

# Convert to digits
Answer = 0
while (Factorial > 0):
    Answer += Factorial % 10
    Factorial -= Factorial % 10
    Factorial = Factorial//10
    #print("Answer = {}, Factorial = {}".format(Answer, Factorial))

print("Answer = {}".format(Answer))
print("Time taken = {:.3f} seconds".format(time.clock() - start_time))

