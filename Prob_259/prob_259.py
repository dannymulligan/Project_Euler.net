#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 259
#
# Reachable Numbers
#
# A positive integer will be called reachable if it can result from an
# arithmetic expression obeying the following rules:
#
# - Uses the digits 1 through 9, in that order and exactly once each.
# - Any successive digits can be concatenated (for example, using the
#   digits 2, 3 and 4 we obtain the number 234).
# - Only the four usual binary arithmetic operations (addition,
#   subtraction, multiplication and division) are allowed.
# - Each operation can be used any number of times, or not at all.
# - Unary minus is not allowed.
# - Any number of (possibly nested) parentheses may be used to define
#   the order of operations.
#
# For example, 42 is reachable, since (1/23) * ((4*5)-6) * (78-9) = 42.
# 
# What is the sum of all positive reachable integers?
#
# Solved ??/??/12
# ?? problems solved
# Position #??? on level ?

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
from fractions import Fraction

reachable_cache = {
    (1,1): {'1': Fraction(1,1)}, 
    (2,2): {'2': Fraction(2,1)},
    (3,3): {'3': Fraction(3,1)}, 
    (4,4): {'4': Fraction(4,1)},
    (5,5): {'5': Fraction(5,1)}, 
    (6,6): {'6': Fraction(6,1)},
    (7,7): {'7': Fraction(7,1)}, 
    (8,8): {'8': Fraction(8,1)},
    (9,9): {'9': Fraction(9,1)},
}

########################################

def reachable(lnum, rnum):
    #print "reachable({},{})".format(lnum,rnum)
    
    # Save time if we've already calculated this one
    if reachable_cache.has_key((lnum,rnum)):
        return reachable_cache[(lnum,rnum)]

    # Don't have to handle the case with only a single digit,
    #   taken care of in cache initiatization

    # Divide and conquer
    length = (rnum - lnum)
    result = {}
    for i in range(0,length):
        lreachable = reachable(lnum, lnum+i)
        rreachable = reachable(lnum+i+1, rnum)
        #print "lreachable =", lreachable
        #print "rreachable =", rreachable
        for lkey in lreachable:
            lres = lreachable[lkey]
            for rkey in rreachable:
                rres = rreachable[rkey]
                result['(' + lkey + '+' + rkey + ')'] = (lres + rres)
                result['(' + lkey + '-' + rkey + ')'] = (lres - rres)
                result['(' + lkey + '*' + rkey + ')'] = (lres * rres)
                if (rres != 0):
                    result['(' + lkey + '/' + rkey + ')'] = (lres / rres)

    reachable_cache[(lnum,rnum)] = result            
    return result

    
top = 8
print "Calculating reachable(1,{})".format(top)    
results = reachable(1,top)
print "len(results) =", len(results)

reachable_set = set()

for rkey in results:
    res = results[rkey]
    if (res.denominator != 1):
        continue
    if (res <= 0):
        continue
    reachable_set.add(res.numerator)

print reachable_set
print "Answer =", sum(reachable_set)

print "Time taken = {0} seconds".format(time.clock() - start_time)

