#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 225
#
# Tribonacci non-divisors
#
# The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201, ...
# is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.
#
# It can be shown that 27 does not divide any terms of this sequence.
# In fact, 27 is the first odd number with this property.
#
# Find the 124th odd number that does not divide any terms of the above sequence.
#
# Solved 06/26/13
# 176 problems solved
# Position #419 on level 7

#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import sys
import time
start_time = time.clock()

########################################

def tribonacci(mod):
    a = 1
    b = 1
    c = 1
    yield a
    yield b
    yield c

    (a, b, c) = (b, c, (a+b+c)%mod)
    yield c
    
    (a, b, c) = (b, c, (a+b+c)%mod)
    yield c
    
    (a, b, c) = (b, c, (a+b+c)%mod)
    yield c
    
    looped = False
    while (not looped):
        (a, b, c) = (b, c, (a+b+c)%mod)
        looped = ((a == 3) & (b == 5) & (c == 9))
        yield c

    
matches = []
for mod in range(3, 20000, 2):
    count = 0
    divisible = False
    for n in tribonacci(mod):
        count += 1
        if (n == 0):
            divisible = True
            break

    if divisible:    
        #print "The tribonacci sequence is divisible by {} at element {}".format(mod, count)
        pass
    else:
        print "{}: The tribonacci sequence contains no elements divisible by {}".format(len(matches) + 1, mod)
        matches.append(mod)

    if (len(matches) == 124):
        break

print "Found {} matches".format(len(matches))        
print "matches =", matches        
print "The answer is", matches[123]

print "Time taken = {0} seconds".format(time.clock() - start_time)

