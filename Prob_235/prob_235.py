#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 235
#
# An Arithmetic Geometric sequence
#
# Given is the arithmetic-geometric sequence u(k) = (900-3k)r^(k-1).
#
# Let s(n) = sum(u(1), u(2), ..., u(k)).
#
# Find the value of r for which s(5000) = -600,000,000,000.
#
# Give your answer rounded to 12 places behind the decimal point.
#
# Solved 05/14/11
# 138 problems solved
# Position #254 on level 3


def u(k,r):
    return (900-3*k) * r**(k-1)

def s(n,r):
    result = 0.0
    for i in range(n):
        result += u(i+1, r)
    return result

target = -600000000000.0

print target
r = 1.0
print s(5000, r)

for ri in range(-10,10):
    r = 1.00232210863287 + ri * 0.000000000000001
    res = s(5000,r)
    print "s(5000, {0}) = {1}, {2}".format(r, res-target, (r-1.0)*100)

