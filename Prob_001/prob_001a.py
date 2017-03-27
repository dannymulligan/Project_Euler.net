#!/usr/bin/python
#
# Project Euler.net Problem 1
#
# Add all the natural numbers below one thousand that are multiples of 3 or 5.
#
# If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 100 billion.


def sum_n (n):
    return n*(n+1)/2

LIMIT = 100000000000

answer  =  3 * sum_n((LIMIT-1)/3)
answer +=  5 * sum_n((LIMIT-1)/5)
answer -= 15 * sum_n((LIMIT-1)/15)

print("Answer =".format(answer))
