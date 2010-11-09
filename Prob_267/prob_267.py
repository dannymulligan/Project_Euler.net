#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 267
#
# Billionaire
#
# You are given a unique investment opportunity.
# 
# Starting with £1 of capital, you can choose a fixed proportion, f,
# of your capital to bet on a fair coin toss repeatedly for 1000
# tosses.
# 
# Your return is double your bet for heads and you lose your bet for
# tails.
# 
# For example, if f = 1/4, for the first toss you bet £0.25, and if
# heads comes up you win £0.5 and so then have £1.5. You then bet
# £0.375 and if the second toss is tails, you have £1.125.
# 
# Choosing f to maximize your chances of having at least
# £1,000,000,000 after 1,000 flips, what is the chance that you become
# a billionaire?
# 
# All computations are assumed to be exact (no rounding), but give
# your answer rounded to 12 digits behind the decimal point in the
# form 0.abcdefghijkl.
#
# Answer: 
# Solved 12/18/09
# 109 problems solved
# Position #886 on level 3


# The outcome depends only on the number of heads, not the order in
# which heads and tails arrive.  For a given number of heads N, the
# outcome will be...
#
#    O(N) = (1+2f)^N * (1-f)^(1000-N)
#
# We need to find the smallest N for which a solution for f exists
# that yields O(N) >= 1,000,000,000.  If we work with logs, the match
# becomes a little simpler...
#
#    Ol(N) = N*ln(1+2f) + (1000-N)*ln(1-f)
#
# Now, we need to find the smallest N for which a solution for f
# exists that yields Ol(N) >= ln(1,000,000,000).  First we need to
# find the first derivative of Ol(N)...
#
#              N     d(1+2f)    (1000-N)   d(1-f)
#   Ol'(N) = ----- * -------  + -------- * ------
#            1+2*f     df         1-f        df
#
#             2*N    (1000-N)
#   Ol'(N) = ----- - --------
#            1+2*f     1-f
#
# The maximum or minimum value of Ol(N) will occur when...
#
#   Ol'(N) = 0
#
# or...
#
#    2*N    (1000-N)
#   ----- = --------
#   1+2*f     1-f
#
#    2*N*(1-f) = (1000-N)*(1+2*f)
#    2*N - 2*N*f = (1000-N) + (1000-N)*2*f
#    2*N - 2*N*f = 1000 - N + 2000*f - 2*N*f
#    2*N = 1000 - N + 2000*f
#    3*N = 1000 + 2000*f
#    2000*f = 3*N - 1000
#    f = (3*N - 1000)/2000
#
# Is this point a minimum or maximum?  We need to calculate the 2nd
# derivative...
#
#   Ol'(N) = 2*N*(1+2*f)^-1 - (1000-N)*(1-f)^-1
#
#   Ol''(N) = -4*N*(1+2*f)^-2 - (1000-N)*-1*(1-f)^-2*-1
#
#   Ol''(N) = -4*N*(1+2*f)^-2 - (1000-N)*(1-f)^-2
#
#               -4*N        -(1000-N)
#   Ol''(N) = ---------  +  ---------
#             (1+2*f)^2      (1-f)^2
#
# since, N<=1000, this is always negative, therefore the Ol'(N) = 0
# point calculated above will always be a maximum.  So we need to
# calculate the value of Ol(N) with f = N/500 -1, and see if it is
# greater than ln(1,000,000,000).
#

import math

# Ol(N) = N*ln(1+2*f) + (1000-N)*ln(1-f)
def Ol(N,f):
    if (N == 1000):  return N*math.log(1.0+2.0*f)
    elif (N == 0):   return                         (1000.0-N)*math.log(1.0-f)
    else:            return N*math.log(1.0+2.0*f) + (1000.0-N)*math.log(1.0-f)

def max_Ol(N):
    f = (3.0*N - 1000.0)/2000.0
    print "With N =", N, "the optimum f =", f
    if (f > 0.0):  return Ol(N,f)
    else:          return 0

def solution_exists(N):
    if max_Ol(N) > math.log(10**9):
        return True
    else:
        return False

def solution_count(N):
    return (math.factorial(1000)/(math.factorial(1000-N)*math.factorial(N)))


solutions = 0
for N in range(1000,0,-1):
    if solution_exists(N):
        solutions += solution_count(N)
    else:
        print "No solution found with N =", N
        break

fsolutions = float(solutions)/float(2**1000)
print "The solution is", fsolutions
