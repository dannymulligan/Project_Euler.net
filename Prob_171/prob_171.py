#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 171
#
# Finding numbers for which the sum of the squares of the digits is a square
#
# For a positive integer n, let f(n) be the sum of the squares of the
# digits (in base 10) of n, e.g.
#
#    f(3) = 3^2 = 9,
#    f(25) = 2^2 + 5^2 = 4 + 25 = 29,
#    f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36
#
# Find the last nine digits of the sum of all n, 0 < n < 10^20, such
# that f(n) is a perfect square.

import sys
#print(sys.version)
import time
start_time = time.clock()


############################################################
# If 10^20 is all "9"s, then the maximum that f(n) could be is 20*9^2
# or 1,620.  Since we are looking for n < 10^20, this means that f(n)
# must be a perfect square less than 1,620, which gives us 40
# possibilities for f(n).
#
#     f(n) = 2^2 = 4
#     f(n) = 3^3 = 9
#     ...
#     f(n) = 40^2 = 1,600
#
# f(n) = 41^2 = 1,681 is larger than is possible with n < 10^20, so we
# don't need to check this high.
#
# Each valid f(n) value must be made up from the sum of digits
# squared.  Finding a valid partition gives us the digits in n.  We
# then enumerate all possible combinations of those digits, along with
# as many 0's as can fit, to find the solution.

########################################
possible_fn_values = [n**2 for n in range(1, 41)]
print(possible_fn_values)

possible_fn_parts = [n**2 for n in range(0, 10)]
print(possible_fn_parts)


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
