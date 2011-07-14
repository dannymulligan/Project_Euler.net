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
import sys
import time

start = time.clock()
chips   = 1000000
defects =   20000

p0 = Fraction(1,1)  # probability of 0 defects in this chip
p1 = Fraction(0,1)  # probability of 1 defects in this chip
p2 = Fraction(0,1)  # probability of 2 defects in this chip
s1_add0 = Fraction(chips-1, chips)  # probability of a new defect adding 0 defects in this chip
s1_add1 = Fraction(1, chips)        # probability of a new defect adding 1 defects in this chip
s1_add2 = Fraction(0, chips)        # probability of a new defect adding 2 defects in this chip

for n in range(0,10):
    p2 = (p2 * s1_add0) + (p1 * s1_add1) + (p0 * s1_add2)
    p1 = (p1 * s1_add0) + (p0 * s1_add1)
    p0 = (p0 * s1_add0)

print "10 steps: p0 = {0}, p1 = {1}, p2 = {2}".format(float(p0), float(p1), float(p2))
p_012 = (p0 + p1 + p2)
print "p_012 =", float(p_012), p_012
#print "time =", time.clock() - start

p2 = p2.limit_denominator(2**1024)
p1 = p1.limit_denominator(2**1024)
p0 = p0.limit_denominator(2**1024)

s10_add2 = p2
s10_add1 = p1
s10_add0 = p0

for n in range(1,10):
    p2 = (p2 * s10_add0) + (p1 * s10_add1) + (p0 * s10_add2)
    p1 = (p1 * s10_add0) + (p0 * s10_add1)
    p0 = (p0 * s10_add0)

print "100 steps: p0 = {0}, p1 = {1}, p2 = {2}".format(float(p0), float(p1), float(p2))
p_012 = (p0 + p1 + p2)
print "p_012 =", float(p_012)
#print "time =", time.clock() - start

p2 = p2.limit_denominator(2**1024)
p1 = p1.limit_denominator(2**1024)
p0 = p0.limit_denominator(2**1024)

s100_add2 = p2
s100_add1 = p1
s100_add0 = p0

for n in range(1,10):
    p2 = (p2 * s100_add0) + (p1 * s100_add1) + (p0 * s100_add2)
    p1 = (p1 * s100_add0) + (p0 * s100_add1)
    p0 = (p0 * s100_add0)

print "1,000 steps: p0 = {0}, p1 = {1}, p2 = {2}".format(float(p0), float(p1), float(p2))
p_012 = (p0 + p1 + p2)
print "p_012 =", float(p_012)
#print "time =", time.clock() - start

p2 = p2.limit_denominator(2**1024)
p1 = p1.limit_denominator(2**1024)
p0 = p0.limit_denominator(2**1024)

s1000_add2 = p2
s1000_add1 = p1
s1000_add0 = p0

for n in range(1,5):
    p2 = (p2 * s1000_add0) + (p1 * s1000_add1) + (p0 * s1000_add2)
    p1 = (p1 * s1000_add0) + (p0 * s1000_add1)
    p0 = (p0 * s1000_add0)
    print "{3} steps: p0 = {0}, p1 = {1}, p2 = {2}".format(float(p0), float(p1), float(p2), (n+1)*1000)
    p_012 = (p0 + p1 + p2)
    print "p_012 =", float(p_012)
    #print "time =", time.clock() - start

p2 = p2.limit_denominator(2**1024)
p1 = p1.limit_denominator(2**1024)
p0 = p0.limit_denominator(2**1024)

s5000_add2 = p2
s5000_add1 = p1
s5000_add0 = p0

for n in range(1,4):
    p2 = (p2 * s5000_add0) + (p1 * s5000_add1) + (p0 * s5000_add2)
    p1 = (p1 * s5000_add0) + (p0 * s5000_add1)
    p0 = (p0 * s5000_add0)
    print "{3} steps: p0 = {0}, p1 = {1}, p2 = {2}".format(float(p0), float(p1), float(p2), (n+1)*5000)
    p_012 = (p0 + p1 + p2)
    print "p_012 =", float(p_012)

p2 = p2.limit_denominator(2**1024)
p1 = p1.limit_denominator(2**1024)
p0 = p0.limit_denominator(2**1024)

s20000_add2 = p2
s20000_add1 = p1
s20000_add0 = p0


ans = p_012.limit_denominator(2**1024)
p1_012 = p_012.limit_denominator(2**1024)
print "p1_012 =", float(p1_012)

for n in range(1,10):
    ans *= p1_012

ans = ans.limit_denominator(2**1024)
p10_012 = ans
print "p10_012 =", float(p10_012)

for n in range(1,10):
    ans *= p10_012

ans = ans.limit_denominator(2**1024)
p100_012 = ans
print "p100_012 =", float(p100_012)

for n in range(1,10):
    ans *= p100_012

ans = ans.limit_denominator(2**1024)
p1000_012 = ans
print "p1000_012 =", float(p1000_012)

for n in range(1,10):
    ans *= p1000_012

ans = ans.limit_denominator(2**1024)
p10000_012 = ans
print "p10000_012 =", float(p10000_012)

for n in range(1,10):
    ans *= p10000_012

ans = ans.limit_denominator(2**1024)
p100000_012 = ans
print "p100000_012 =", float(p100000_012)

for n in range(1,10):
    ans *= p100000_012

ans = ans.limit_denominator(2**1024)
p1000000_012 = ans
print "p1000000_012 =", float(p1000000_012)

answer = 1 - ans
print "Answer =", float(answer), answer
print "Answer = {0:.10f}".format(float(answer))

sys.exit()

