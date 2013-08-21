#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 286
#
# Scoring probabilities
#
# Barbara is a mathematician and a basketball player. She has found
# that the probability of scoring a point when shooting from a
# distance x is exactly (1 - x/q), where q is a real constant greater
# than 50.
#
# During each practice run, she takes shots from distances x = 1,
# x = 2, ..., x = 50 and, according to her records, she has precisely
# a 2 % chance to score a total of exactly 20 points.
#
# Find q and give your answer rounded to 10 decimal places.
#
# Solved 08/21/13
# 180 problems solved
# Position #321 on level 7

#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import math
import sys
import time
start_time = time.clock()

########################################

def prob(n, q):
    # Probability of scoring n points out of 50 attempts,
    # when probability of scoring each shot is (1-x/q) for x = 1 .. 50
    bin_table = []
    curr_line = [1.0]
    bin_table.append(curr_line)

    for x in range(1,51):
        prev_line = curr_line
        curr_line = []

        p = (1.0 - 1.0*x/q)

        for i in range(len(prev_line)+1):
            if (i == 0):
                from_l = 0.0
                from_r = prev_line[i] * (1-p)
            elif (i == len(prev_line)):
                from_l = prev_line[i-1] * p
                from_r = 0.0
            else:
                from_l = prev_line[i-1] * p
                from_r = prev_line[i] * (1-p)

            curr_line.append(from_l + from_r)
        bin_table.append(curr_line)

    return bin_table[50][n]

target = 0.02
error_tolerance = 1.0e-14

upper_point = 60.0
upper_result = prob(20, upper_point)

lower_point = 50.0
lower_result = prob(20, lower_point)

mid_point = (upper_point + lower_point)/2.0
mid_result = prob(20, mid_point)

error = abs(mid_result - target)

while (error > error_tolerance):
    if (mid_result < target):
        upper_point = mid_point
        upper_result = prob(20, upper_point)
    else:
        lower_point = mid_point
        lower_result = prob(20, lower_point)
        
    mid_point = (upper_point + lower_point)/2.0
    mid_result = prob(20, mid_point)
    error = abs(mid_result - target)
    
    print "When q = {:2.14f}, probability of scoring 20 points is {:16}, error is {}".format(mid_point, mid_result, error),
    print "U:L = {:14}:{:14} probs = {:16}:{:16}".format(upper_point, lower_point, upper_result, lower_result)

q = mid_point    
print "q = {} (This is the answer to the problem)".format(q)
print "With q = {}, the probability of scoring 20 points is {}".format(q, prob(20, q))
    
print "Time taken = {0} seconds".format(time.clock() - start_time)
