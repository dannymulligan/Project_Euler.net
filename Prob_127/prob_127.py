#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 127
#
# Investigating the number of abc-hits below a given limit.
#
# The radical of n, rad(n), is the product of distinct prime factors
# of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.
#
# We shall define the triplet of positive integers (a, b, c) to be an
# abc-hit if:
#
#    GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
#    a < b
#    a + b = c
#    rad(abc) < c
#
# For example, (5, 27, 32) is an abc-hit, because:
#
#    GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
#    5 < 27
#    5 + 27 = 32
#    rad(4320) = 30 < 32
#
# It turns out that abc-hits are quite rare and there are only
# thirty-one abc-hits for c < 1000, with sum(c) = 12523.
#
# Find sum(c) for c < 120000.
#
# Note: This problem has been changed recently, please check that you
# are using the right parameters.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?
