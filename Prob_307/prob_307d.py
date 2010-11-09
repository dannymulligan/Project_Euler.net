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
# Answer: 0.7310686772
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
#chips   = 1000000
#defects =   20000
#f_chips = [5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2]
#f_defects = [5, 2, 5, 2, 5, 2, 5, 2, 2]
chips   = 10
defects =   3
f_chips = [2, 5]
f_defects = [3]

################################################################################
# Calculate the probability of 0, 1, or 2 defects in any one chip
p0 = Fraction(1,1)  # probability of 0 defects in this chip
p1 = Fraction(0,1)  # probability of 1 defects in this chip
p2 = Fraction(0,1)  # probability of 2 defects in this chip
add0 = Fraction(chips-1, chips)  # probability of a new defect adding 0 defects in this chip
add1 = Fraction(1, chips)        # probability of a new defect adding 1 defects in this chip
add2 = Fraction(0, chips)        # probability of a new defect adding 2 defects in this chip
#print "add0 =", add0, "add1 =", add1

p2 = (p2 * add0) + (p1 * add1) + (p0 * add2)
p1 = (p1 * add0) + (p0 * add1)
p0 = (p0 * add0)

nn = 1
nnp = 1
for i in f_defects:
    np0 = p0
    np1 = p1
    np2 = p2
    nnp = nn

    for j in range(i-1):
        np2 = (np2 * add0) + (np1 * add1) + (np0 * add2)
        np1 = (np1 * add0) + (np0 * add1)
        np0 = (np0 * add0)
        nnp += nn
        print "{0} steps: p0 = {1}, p1 = {2}, p2 = {3}".format(nnp, float(np0), float(np1), float(np2))
        #print "{0} steps: p0 = {1:.10f}, p1 = {2:.10f}, p2 = {3:.10f}".format(nnp, float(np0), float(np1), float(np2))
        #print "{0} steps: p0 = {1}, p1 = {2}, p2 = {3}".format(nnp, np0, np1, np2)

    p2 = np2.limit_denominator(2**1024)
    p1 = np1.limit_denominator(2**1024)
    p0 = np0.limit_denominator(2**1024)
    add2 = p2
    add1 = p1
    add0 = p0
    nn = nnp


################################################################################
# Calculate the probability of 0, 1, or 2 defects in all chips
p012 = p0 + p1 + p2
prob = p012
prob_prev = p012
pn = 1
ppn = 1
print "p012^{0} = {1}".format(pn, float(prob))

for i in f_chips:
    for j in range(i-1):
        prob *= prob_prev
        pn += ppn
        print "p012^{0} = {1}".format(pn, float(prob))
    prob = prob.limit_denominator(2**1024)
    prob_prev = prob
    ppn = pn

answer = 1 - prob
print "Answer =", float(answer)


sys.exit()
