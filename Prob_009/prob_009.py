#!/usr/bin/python
#
# Project Euler.net Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^(2) + b^(2) = c^(2)
#
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#

MAX = 1000

for a in range(MAX/3):
    for b in range(a+1, (MAX-a)/2):
        for c in range(b+1, MAX):
            if ((a+b+c) == MAX):
                if ((a*a) + (b*b) == (c*c)):
                    print "a = {0}, b = {1}, c = {2}, a*b*c = {3}\n".format(a, b, c, (a*b*c))
