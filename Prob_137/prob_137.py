#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 137
#
# Determining the value of infinite polynomial series for which the
# coefficients are Fibonacci numbers.
#
# Consider the infinite polynomial series AF(x) = xF(1) + x^2F(2) +
# x^3F(3) + ..., where F(k) is the kth term in the Fibonacci sequence:
# 1, 1, 2, 3, 5, 8, ... ; that is, F(k) = F(k-1) + F(k−2), F(1) = 1
# and F(2) = 1.
#
# For this problem we shall be interested in values of x for which
# AF(x) is a positive integer.
#
# Surprisingly AF(1/2) = (1/2)*1 + (1/2)^2*1 + (1/2)^3*2 + (1/2)^4*3 +
# (1/2)^5*5 + ...
#         = 1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
#         = 2
#
# The corresponding values of x for the first five natural numbers are
# shown below.
#
#       x              AF(x)
#     sqrt(2)-1         1
#     1/2               2
#     (sqrt(13)-2)/3    3
#     (sqrt(89)-5)/8    4
#     (sqrt(34)-3)/5    5
#
# We shall call AF(x) a golden nugget if x is rational, because they
# become increasingly rarer; for example, the 10th golden nugget is
# 74049690.
#
# Find the 15th golden nugget.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?
