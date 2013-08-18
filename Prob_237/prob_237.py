#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 237
#
# Problem summary
#
# Let T(n) be the number of tours over a 4 x n playing board such
# that:
# - The tour starts in the top left corner.
# - The tour consists of moves that are up, down, left, or right one
#       square. The tour visits each square exactly once.
# - The tour ends in the bottom left corner.
#
# The diagram shows one tour over a 4 x 10 board:
#
#   +---+---+---+---+---+---+---+---+---+---+
#   | X******** | ***************** | ***** |
#   +---+---+-*-+-*-+---+---+---+-*-+-*-+-*-+
#   | ***** | ***** | ************* | * | * |
#   +-*-+-*-+---+---+-*-+---+---+---+-*-+-*-+
#   | * | * | ***** | ***************** | * |
#   +-*-+-*-+-*-+-*-+---+---+---+---+---+-*-+
#   | X | ***** | ************************* |
#   +---+---+---+---+---+---+---+---+---+---+
#
# T(10) is 2329. What is T(10^12) modulo 10^8?
#
# Solved ??/??/13
# ?? problems solved
# Position #??? on level ?

# Interfaces between rows can be one of the following...
#
#    A     B     C     D     E
#   -+-   -+-   -+-   -+-   -+-
#   >>>   >>>   >>>    |     |
#   -+-   -+-   -+-   -+-   -+-
#    |    <<<   <<<   >>>    |
#   -+-   -+-   -+-   -+-   -+-
#    |    >>>    |    <<<   >>>
#   -+-   -+-   -+-   -+-   -+-
#   <<<   <<<    |     |    <<<
#   -+-   -+-   -+-   -+-   -+-
#
# For a 4xN board, there are N-1 interfaces
#
# The 1st interface can be one of
#
# The last interface can be one of
#
# A can go to
# B1 can go to
# B2 can go to
# B3 can go to
# C can go to
# D can go to
# E can go to
#
# This will be a 'divide and conquer' algorithm


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

M = 10**8
#M = 0

########################################

def is_power_of_2(n):
    return ((n & (n - 1)) == 0)
    # Doesn't handle corner case of n == 0 correctly, but we don't care

def partition(n):
    x = 1
    while (x < n):
        x *= 2
    return x/2


########################################

def perm (left, right, length):
    if (length > 1):
        #print "perm('{}', '{}', {})".format(left, right, length)
        answer = 0

        split_point = partition(length)

        left_perm = perm(left, 'A', split_point)
        if (left_perm != 0):
            right_perm = perm('A', right, length - split_point)
            answer += left_perm * right_perm
            #print "    split on A: left_perm = {}, right_perm = {}, answer = {}".format(left_perm, right_perm, answer)

        left_perm = perm(left, 'B1', split_point)
        if (left_perm != 0):
            right_perm = perm('B1', right, length - split_point)
            answer += left_perm * right_perm
            #print "    split on B1: left_perm = {}, right_perm = {}, answer = {}".format(left_perm, right_perm, answer)

        left_perm = perm(left, 'B2', split_point)
        if (left_perm != 0):
            right_perm = perm('B2', right, length - split_point)
            answer += left_perm * right_perm
            #print "    split on B2: left_perm = {}, right_perm = {}, answer = {}".format(left_perm, right_perm, answer)

        left_perm = perm(left, 'B3', split_point)
        if (left_perm != 0):
            right_perm = perm('B3', right, length - split_point)
            answer += left_perm * right_perm
            #print "    split on B3: left_perm = {}, right_perm = {}, answer = {}".format(left_perm, right_perm, answer)

        left_perm = perm(left, 'C', split_point)
        if (left_perm != 0):
            right_perm = perm('C', right, length - split_point)
            answer += left_perm * right_perm
            #print "    split on C: left_perm = {}, right_perm = {}, answer = {}".format(left_perm, right_perm, answer)

        left_perm = perm(left, 'D', split_point)
        if (left_perm != 0):
            right_perm = perm('D', right, length - split_point)
            answer += left_perm * right_perm
            #print "    split on D: left_perm = {}, right_perm = {}, answer = {}".format(left_perm, right_perm, answer)

        left_perm = perm(left, 'E', split_point)
        if (left_perm != 0):
            right_perm = perm('E', right, length - split_point)
            answer += left_perm * right_perm
            #print "    split on E: left_perm = {}, right_perm = {}, answer = {}".format(left_perm, right_perm, answer)

        if (M == 0):
            return answer
        else:
            return answer % M
    elif (length == 1):
        if   (left == 'A'):
            if   (right == 'A'):   return 0
            elif (right == 'B1'):  return 1
            elif (right == 'B2'):  return 0
            elif (right == 'B3'):  return 0
            elif (right == 'C'):   return 1
            elif (right == 'D'):   return 1
            elif (right == 'E'):   return 1
            else:
                print "Error"
                raise AssertionError
        elif (left == 'B1'):
            if   (right == 'A'):   return 0
            elif (right == 'B1'):  return 1
            elif (right == 'B2'):  return 0
            elif (right == 'B3'):  return 0
            elif (right == 'C'):   return 1
            elif (right == 'D'):   return 0
            elif (right == 'E'):   return 1
            else:
                print "Error"
                raise AssertionError
        elif (left == 'B2'):
            if   (right == 'A'):   return 1
            elif (right == 'B1'):  return 0
            elif (right == 'B2'):  return 1
            elif (right == 'B3'):  return 0
            elif (right == 'C'):   return 0
            elif (right == 'D'):   return 0
            elif (right == 'E'):   return 0
            else:
                print "Error"
                raise AssertionError
        elif (left == 'B3'):
            if   (right == 'A'):   return 1
            elif (right == 'B1'):  return 0
            elif (right == 'B2'):  return 0
            elif (right == 'B3'):  return 1
            elif (right == 'C'):   return 0
            elif (right == 'D'):   return 0
            elif (right == 'E'):   return 0
            else:
                print "Error"
                raise AssertionError
        elif (left == 'C'):
            if   (right == 'A'):   return 1
            elif (right == 'B1'):  return 0
            elif (right == 'B2'):  return 1
            elif (right == 'B3'):  return 0
            elif (right == 'C'):   return 0
            elif (right == 'D'):   return 0
            elif (right == 'E'):   return 0
            else:
                print "Error"
                raise AssertionError
        elif (left == 'D'):
            if   (right == 'A'):   return 1
            elif (right == 'B1'):  return 0
            elif (right == 'B2'):  return 0
            elif (right == 'B3'):  return 0
            elif (right == 'C'):   return 0
            elif (right == 'D'):   return 0
            elif (right == 'E'):   return 0
            else:
                print "Error"
                raise AssertionError
        elif (left == 'E'):
            if   (right == 'A'):   return 1
            elif (right == 'B1'):  return 0
            elif (right == 'B2'):  return 0
            elif (right == 'B3'):  return 1
            elif (right == 'C'):   return 0
            elif (right == 'D'):   return 0
            elif (right == 'E'):   return 0
            else:
                print "Error"
                raise AssertionError
    else:
        print "Error"
        raise AssertionError


########################################

len = 10
i = len - 2
print "For len =", len

ending_in_A = perm('B1', 'A',  i) + perm('C', 'A',  i) + perm('D', 'A',  i) + perm('E', 'A',  i)
if (M != 0):
    ending_in_A = ending_in_A % M
print "{} solutions end in A".format(ending_in_A)

ending_in_B1 = perm('B1', 'B1', i) + perm('C', 'B1', i) + perm('D', 'B1', i) + perm('E', 'B1', i)
if (M != 0):
    ending_in_B1 = ending_in_B1 % M
print "{} solutions end in B1".format(ending_in_B1)

answer = ending_in_A + ending_in_B1
if (M != 0):
    answer = answer % M
print "Answer =", answer

#print "perm('B1', 'A',  {}) = {}".format(i, perm('B1', 'A',  i))
#print "perm('C',  'A',  {}) = {}".format(i, perm('C',  'A',  i))
#print "perm('D',  'A',  {}) = {}".format(i, perm('D',  'A',  i))
#print "perm('E',  'A',  {}) = {}".format(i, perm('E',  'A',  i))
#print "perm('B1', 'B1', {}) = {}".format(i, perm('B1', 'B1', i))
#print "perm('C',  'B1', {}) = {}".format(i, perm('C',  'B1', i))
#print "perm('D',  'B1', {}) = {}".format(i, perm('D',  'B1', i))
#print "perm('E',  'B1', {}) = {}".format(i, perm('E',  'B1', i))


print "Time taken = {0} seconds".format(time.clock() - start_time)
