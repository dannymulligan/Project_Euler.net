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
# Solved 07/02/13
# 178 problems solved
# Position #360 on level 7

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
    (1,1): {Fraction(1,1): '1'},
    (2,2): {Fraction(2,1): '2'},
    (3,3): {Fraction(3,1): '3'},
    (4,4): {Fraction(4,1): '4'},
    (5,5): {Fraction(5,1): '5'},
    (6,6): {Fraction(6,1): '6'},
    (7,7): {Fraction(7,1): '7'},
    (8,8): {Fraction(8,1): '8'},
    (9,9): {Fraction(9,1): '9'},
}

########################################

def reachable(lnum, rnum):
    #print "reachable({},{})".format(lnum,rnum)

    # Save time if we've already calculated this one
    if reachable_cache.has_key((lnum,rnum)):
        return reachable_cache[(lnum,rnum)]

    # Don't have to handle the case with only a single digit,
    #   taken care of in cache initiatization

    # Concationation
    result = {}
    txt = ''
    num = 0
    for i in range(lnum, rnum+1):
        txt += "{}".format(i)
        num = 10*num + i
    result[num] = txt
    #print "{}-{}    {} = {}".format(lnum,rnum, num, txt)
    
    # Divide and conquer
    length = (rnum - lnum)
    for i in range(0,length):
        lreachable = reachable(lnum, lnum+i)
        rreachable = reachable(lnum+i+1, rnum)
        #print "lreachable =", lreachable
        #print "rreachable =", rreachable
        for lkey in lreachable:
            lstr = lreachable[lkey]
            for rkey in rreachable:
                rstr = rreachable[rkey]
                
                if not((lkey + rkey) in result):
                    result[lkey + rkey] = '(' + lstr + '+' + rstr + ')'
                    #print "{}-{}    {} = {}".format(lnum,rnum, (lkey + rkey), '(' + lstr + '+' + rstr + ')')

                if not((lkey + rkey) in result):
                    result[lkey + rkey] = '(' + lstr + '+' + rstr + ')'
                    #print "{}-{}    {} = {}".format(lnum,rnum, (lkey + rkey), '(' + lstr + '+' + rstr + ')')

                if not((lkey - rkey) in result):
                    result[lkey - rkey] = '(' + lstr + '-' + rstr + ')'
                    #print "{}-{}    {} = {}".format(lnum,rnum, (lkey - rkey), '(' + lstr + '-' + rstr + ')')

                if not((lkey * rkey) in result):
                    result[lkey * rkey] = '(' + lstr + '*' + rstr + ')'
                    #print "{}-{}    {} = {}".format(lnum,rnum, (lkey * rkey), '(' + lstr + '*' + rstr + ')')

                if (rkey == 0):
                    continue
                if not((lkey / rkey) in result):
                    result[lkey / rkey] = '(' + lstr + '/' + rstr + ')'
                    #print "{}-{}    {} = {}".format(lnum,rnum, (lkey / rkey), '(' + lstr + '/' + rstr + ')')

    reachable_cache[(lnum,rnum)] = result
    #print "result for reachable({},{}) = {}".format(lnum, rnum, result)
    return result


top = 9
print "Calculating reachable(1,{})".format(top)
results = reachable(1,top)
print "len(results) =", len(results)
#print "results =", results

reachable_set = set()

for rkey in results:
    if (rkey.denominator != 1):
        continue
    if (rkey <= 0):
        continue
    reachable_set.add(rkey.numerator)

print "len(reachable_set) =", len(reachable_set)
#print reachable_set

print "Answer =", sum(reachable_set)

print "Time taken = {0} seconds".format(time.clock() - start_time)
