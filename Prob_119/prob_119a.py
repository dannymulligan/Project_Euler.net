#!/usr/bin/python
#
# Project Euler.net Problem 119
# 
# The number 512 is interesting because it is equal to the sum of its
# digits raised to some power: 5 + 1 + 2 = 8, and 8^(3) = 512. Another
# example of a number with this property is 614656 = 28^(4).
# 
# We shall define a_(n) to be the nth term of this sequence and insist
# that a number must contain at least two digits to have a sum.
# 
# You are given that a_(2) = 512 and a_(10) = 614656.
# 
# Find a_(30).
#
# Solved 11/10/09
# 103 solved
# Position #1114 on level 3

solutions = []
for x in range(2,100):
    for y in range(1,25):
        n = x**y
        digits = map(lambda x: int(x), list(str(n)))
        b = reduce(lambda x, y: x+y, digits)
        if ((b == x) & (n >= 10)):
            print "{0} = {1}^{2}".format(n,x,y)
            solutions.append((n,x,y))
solutions.sort()
for i in range(30):
    (n,x,y) = solutions[i]
    print "{3}: {0} = {1}^{2}".format(n,x,y, i+1)
