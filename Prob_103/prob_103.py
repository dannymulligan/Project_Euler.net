#!/usr/bin/python
#
# Project Euler.net Problem 103
# 
# Let S(A) represent the sum of elements in set A of size n. We shall
# call it a special sum set if for any two non-empty disjoint subsets,
# B and C, the following properties are true:
# 
#    1. S(B) != S(C); that is, sums of subsets cannot be equal.
#    2. If B contains more elements than C then S(B) > S(C).
# 
# If S(A) is minimised for a given n, we shall call it an optimum
# special sum set. The first five optimum special sum sets are given
# below.
# 
#     n = 1: {1}
#     n = 2: {1, 2}
#     n = 3: {2, 3, 4}
#     n = 4: {3, 5, 6, 7}
#     n = 5: {6, 9, 11, 12, 13}
# 
# It seems that for a given optimum set, A = {a_(1), a_(2), ... ,
# a_(n)}, the next optimum set is of the form B = {b, a_(1)+b,
# a_(2)+b, ... ,a_(n)+b}, where b is the "middle" element on the
# previous row.
# 
# By applying this "rule" we would expect the optimum set for n = 6 to
# be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is
# not the optimum set, as we have merely applied an algorithm to
# provide a near optimum set. The optimum set for n = 6 is A = {11,
# 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string:
# 111819202225.
# 
# Given that A is an optimum special sum set for n = 7, find its set string.
# 
# NOTE: This problem is related to problems 105 and 106.
#
# Solved:
# ? problems solved
# Position #??? on level ?

import sys
import itertools
import time

start_time = time.clock()

########################################
def check_properties(sA):
    lA = len(sA)
    for x in itertools.product('ABC', repeat=lA):
        (lB,lC) = (0,0)
        (tB,tC) = (0,0)
        (sB,sC) = ([],[])
        for i in range(lA):
            if x[i] == 'B':
               lB += 1
               tB += sA[i]
               sB.append(sA[i])
            if x[i] == 'C':
               lC += 1
               tC += sA[i]
               sC.append(sA[i])
        if (lB == 0) | (lC == 0):  continue

        if (((lB == lC) & (tB == tC))
          | ((lB >  lC) & (tB <= tC))
          | ((lB <  lC) & (tB >= tC))):
            #print "    Fail", sB, sC
            return False

    return True


########################################
#should_fail = [81, 88, 75, 42, 87, 84, 86, 65]
#should_pass = [157, 150, 164, 119, 79, 159, 161, 139, 158]
#print check_properties(should_fail)
#print check_properties(should_pass)

########################################
#A6init = [ 11, 17, 20, 22, 23, 24 ]  # S(A) = 117
##A6best = [ 11, 18, 19, 20, 22, 25 ]  # S(A) = 115
#
#print "Starting with", A6init, "sum =", sum(A6init)
#
#count = 0
#A6best = list(A6init)
#for a0 in range(-3,3):
#    for a1 in range(-3,3):
#        if ((A6init[1]+a1) < (A6init[0]+a0)):  continue
#        for a2 in range(-3,3):
#            if ((A6init[2]+a2) < (A6init[1]+a1)):  continue
#            for a3 in range(-3,3):
#                if ((A6init[3]+a3) < (A6init[2]+a2)):  continue
#                for a4 in range(-3,3):
#                    if ((A6init[4]+a4) < (A6init[3]+a3)):  continue
#                    for a5 in range(-3,3):
#                        if ((A6init[5]+a5) < (A6init[4]+a4)):  continue
#                        A6try = [A6init[0]+a0, A6init[1]+a1, A6init[2]+a2, A6init[3]+a3, A6init[4]+a4, A6init[5]+a5]
#                        if (sum(A6try) < sum(A6best)):
#                            count += 1
#                            if (check_properties(A6try)):
#                                A6best = list(A6try)
#                                print A6try, sum(A6try), a0, a1, a2, a3, a4, a5, "(Best so far)", "Count =", count, "Time =", time.clock() - start_time
#print A6best, "= best found"


########################################
#A7 = [ 20, 20+11, 20+18, 20+19, 20+20, 20+22, 20+25 ]
A7init = [20, 31, 38, 39, 40, 42, 45]  # S(A) = 255

print "Starting with", A7init, "sum =", sum(A7init)

count = 0
A7best = list(A7init)
for a0 in range(-10,9):
    for a1 in range(-10,9):
        if ((A7init[1]+a1) < (A7init[0]+a0)):  continue
        for a2 in range(-10,9):
            if ((A7init[2]+a2) < (A7init[1]+a1)):  continue
            for a3 in range(-10,9):
                if ((A7init[3]+a3) < (A7init[2]+a2)):  continue
                for a4 in range(-10,9):
                    if ((A7init[4]+a4) < (A7init[3]+a3)):  continue
                    for a5 in range(-10,9):
                        if ((A7init[5]+a5) < (A7init[4]+a4)):  continue
                        for a6 in range(-10,9):
                            if ((A7init[6]+a6) < (A7init[5]+a5)):  continue
                            A7try = [A7init[0]+a0, A7init[1]+a1, A7init[2]+a2, A7init[3]+a3, A7init[4]+a4, A7init[5]+a5, A7init[6]+a6]
                            if (sum(A7try) < sum(A7best)):
                                count += 1
                                if ((count % 1000) == 0):
                                    print "Testing A7try =", A7try, "sum =", sum(A7try), "count =", count, "Time =", time.clock() - start_time
                                if (check_properties(A7try)):
                                    A7best = list(A7try)
                                    print A7try, sum(A7try), a0, a1, a2, a3, a4, a5, a6, "Best so far)"
print A7best, "= best found"
# Searched to (-10,9)

########################################
end_time = time.clock()
print "Run time =", end_time - start_time, "seconds"
print "count =", count

# Starting with [20, 31, 38, 39, 40, 42, 45] sum = 255
# Run time = 6681.346595 seconds
