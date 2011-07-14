#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 307
#
# Chip Defects
#
# 20,000 defects are randomly distributed amongst the 1,000,000
# integrated-circuit chips produced by a factory (any number of
# defects may be found on a chip).
#
# Find the probability that there is a chip with at least 3 defects.
#
# Give your answer rounded to 10 decimal places in the form
# 0.abcdefghij
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

#                (3)... ...(3)=>(3)=>(3)=>(3)=>(3)
#              //   ... ...   //   //   //   //
#           (2)=>(2)... ...(2)=>(2)=>(2)=>(2)=>(2)
#         //   //   ... ...   //   //   //   //
#      (1)=>(1)=>(1)... ...(1)=>(1)=>(1)=>(1)=>(1)
#    //   //   //   ... ...   //   //   //   //
# (0)=>(0)=>(0)=>(0)... ...(0)=>(0)=>(0)=>(0)=>(0)

from fractions import Fraction

chips   = 1000000
defects = 20000

p0 = Fraction(1,1)
p1 = Fraction(0,1)
p2 = Fraction(0,1)
good   = Fraction(chips-defects, chips)
defect = Fraction(defects, chips)

for n in range(defects):
    p2 = (p2 * good) + (p1 * defect)
    p1 = (p1 * good) + (p0 * defect)
    p0 = (p0 * good)
    if ((n % 100) == 0):
        print "n = {0}, p0 = {1:.10f}, p1 = {2:.10f}, p2 = {3:.10f}".format(n, float(p0), float(p1), float(p2))

answer = 1 - (p0 + p1 + p2)
print answer
print "{0}".format(float(answer))
print "{0:.10f}".format(float(answer))
