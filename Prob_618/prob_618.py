#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 618
#
# Numbers with a given prime factor sum
#
# Consider the numbers 15, 16 and 18:
#     15=3×5 and 3+5=8.
#     16=2×2×2×2 and 2+2+2+2=8.
#     18=2×3×3 and 2+3+3=8
#
# 15, 16 and 18 are the only numbers that have 8 as sum of the prime
# factors (counted with multiplicity).
#
# We define S(k) to be the sum of all numbers n where the sum of the
# prime factors (with multiplicity) of n is k.
#
# Hence S(8)=15+16+18=49.  Other examples: S(1)=0, S(2)=2, S(3)=3,
# S(5)=5+6=11
#
# The Fibonacci sequence is F1=1, F2=1, F3=2, F4=3, F5=5, ....
#                               24
# Find the last nine digits of sum S(Fk)
#                               k=2

SIZE = 24

import sys
#print(sys.version)
import time
start_time = time.clock()

########################################
def fibonacci(limit):
    a, b, n = 1, 1, 2
    yield a
    yield b
    while n < limit:
        a, b = b, a + b
        n += 1
        yield b


########################################
def S(n):
    if n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 5:
        return 11
    else:
        return 0

########################################
answer = 0
for n, f in enumerate(fibonacci(SIZE)):
    partial_answer = S(f)
    print(n+1, f, partial_answer)
    answer += partial_answer

print()
print("Answer = {:,}".format(answer))
print()
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
