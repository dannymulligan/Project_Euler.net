#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 132
#
# Determining the first forty prime factors of a very large repunit.
#
# A number consisting entirely of ones is called a repunit. We shall
# define R(k) to be a repunit of length k.
#
# For example, R(10) = 1111111111 = 11 x 41 x 271 x 9091, and the sum
# of these prime factors is 9414.
#
# Find the sum of the first forty prime factors of R(10^9).
#
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?


# Modulus 3:
# 1, length 1, repeated 2x2x2x2x2 x 5x5x5x5x5 times
# 11, length 2, repeated 2x2x2x2 x 5x5x5x5x5 times
#   mod 3
# 2, length 2, repeated 2x2x2x2 x 5x5x5x5x5 times
# 202, length 4, repeated 2x2x2 x 5x5x5x5x5 times
#   mod 3
# 1, length 4, repeated 2x2x2 x 5x5x5x5x5 times
# 10001, length 8, repeated 2x2 x 5x5x5x5x5 times
#   mod 3
# 2, length 8, repeated 2x2 x 5x5x5x5x5 times
# 200000002, length 16, repeated 2 x 5x5x5x5x5 times
#   mod 3
# 200000002, length 16, repeated 2 x 5x5x5x5x5 times
# 1, length 16, repeated 2 x 5x5x5x5x5 times
# 10000000000000001, length 32, repeated 5x5x5x5x5 times
#   mod 3
# 2, length 32, repeated 5x5x5x5x5 times
# etc...

# R(10) = 1111111111 = 11 x 41 x 271 x 9091
repundit = (1, 1, [2, 5])


#
# Find the sum of the first forty prime factors of R(10^9).
