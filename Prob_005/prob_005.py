#!/usr/bin/python
#
# Project Euler.net Problem 5
#
# What is the smallest number divisible by each of the numbers 1 to 20?
#
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest number that is evenly divisible by all of the
# numbers from 1 to 20?
#

# Number  Factors  Answer
#   1      1        1
#   2      2        2
#   3      3        3x2
#   4      2x2      3x2x2 
#   5      5        5x3x2x2
#   6      3x2      5x3x2x2
#   7      7        7x5x3x2x2
#   8      2x2x2    7x5x3x2x2x2
#   9      3x3      7x5x3x3x2x2x2
#  10      5x2      7x5x3x3x2x2x2
#  11      11       11x7x5x3x3x2x2x2
#  12      3x2x2    11x7x5x3x3x2x2x2
#  13      13       13x11x7x5x3x3x2x2x2
#  14      7x2      13x11x7x5x3x3x2x2x2
#  15      5x3      13x11x7x5x3x3x2x2x2
#  16      2x2x2x2  13x11x7x5x3x3x2x2x2x2
#  17      17       17x13x11x7x5x3x3x2x2x2x2
#  18      3x3x2    17x13x11x7x5x3x3x2x2x2x2
#  19      19       19x17x13x11x7x5x3x3x2x2x2x2
#  20      5x2x2    19x17x13x11x7x5x3x3x2x2x2x2

answer = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 3 * 2 * 2 * 2 * 2
print "Answer is", answer
