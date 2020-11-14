#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 719
#
# Number Splitting
#
# We define an S-number to be a natural number, n, that is a perfect
# square and its square root can be obtained by splitting the decimal
# representation of into 2 or more numbers then adding the numbers.
#
# For example, 81 is an S-number because sqrt(81) = 8 + 1 = 9
# 6724 is an S-number: sqrt(6724) = 6 + 72 + 4 = 82
# 8281 is an S-number: sqrt(8281) = 8 + 2 + 81 = 91
# 9801 is an S-number: sqrt(9801) = 98 + 0 + 1 = 99
#
# Further we define T(N) to be the sum of all S numbers n<N. You are
# given T(10^4) = 41333.
#
# Find T(10^12)

import sys
#print(sys.version)
import time
start_time = time.clock()

###############################################################################

def split(n):
    '''Return all of the possible splits of integer n'''
    yield [n]
    for x in range(1,n):
        for y in split(n-x):
            yield [x] + y
if False:
    for s in split(4):
        print(s)


Optimize = True
if Optimize:
    def ssplit(s, need):
        #print("ssplit({}, {})".format(s, need))
        '''Return all of the possible splits of string s'''
        yield [int(s)]
        for x in range(1,len(s)):
            prefix = int(s[:x])
            if prefix + int(s[x:]) >= need:
                for y in ssplit(s[x:], need - prefix):
                    yield [prefix] + y

    def S(n):
        snum = "{}".format(n**2)
        for split in ssplit(snum, n):
            if sum(split) == n:
                print("sqrt({:,}) = {} = {:,}".format(n**2, split, n))
                return True
else:
    def ssplit(s):
        print("ssplit({})".format(s))
        '''Return all of the possible splits of string s'''
        yield [int(s)]
        for x in range(1,len(s)):
            for y in ssplit(s[x:]):
                yield [int(s[:x])] + y

    def S(n):
        snum = "{}".format(n**2)
        for split in ssplit(snum):
            if sum(split) == n:
                print("sqrt({:,}) = {} = {:,}".format(n**2, split, n))
                return True

debug = False
if debug:
    nums, solution = [2, 9, 12, 82, 91, 99], 0
else:
   nums, solution = range(2, 10**2 + 1),         41333  # Calculated in   0.00 seconds ->   0.00 seconds
   nums, solution = range(2, 10**3 + 1),      10804656  # Calculated in   0.06 seconds ->   0.03 seconds
   nums, solution = range(2, 10**4 + 1),    2818842841  # Calculated in   2.74 seconds ->   0.68 seconds
   nums, solution = range(2, 12500 + 1),    3078722269  # Calculated in   4.56 seconds ->   0.99 seconds
   nums, solution = range(2, 15000 + 1),    3240698798  # Calculated in   6.41 seconds ->   1.32 seconds
   nums, solution = range(2, 10**4 * 2),    3839800575  # Calculated in  10.39 seconds ->   1.96 seconds
   nums, solution = range(2, 10**4 * 3),    6222187932  # Calculated in  17.44 seconds ->   3.34 seconds
   nums, solution = range(2, 10**5 + 1),  499984803177  # Calculated in 129.13 seconds ->  16.42 seconds
   nums, solution = range(2, 10**5 * 2),  831602531877  # Calculated in ???.?? seconds ->  49.53 seconds
   nums, solution = range(2, 10**5 * 4), 5117390432505  # Calculated in ???.?? seconds -> 131.34 seconds
   nums, solution = range(2, 10**6 + 1), 0   # Calcualted in 447.22 seconds


Answer = 0
for n in nums:
    if S(n):
        Answer += n**2

if solution == 0:
    print("Answer is {:,}".format(Answer))
elif Answer == solution:
    print("Answer is {:,} which matches the expected solution".format(Answer))
else:
    print("ERROR: Answer is {:,} which does not match the expected solution of {:,}".format(Answer, solution))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))


# sqrt(81) = [8, 1] = 9
# sqrt(100) = [10, 0] = 10
# sqrt(1,296) = [1, 29, 6] = 36
# sqrt(2,025) = [20, 25] = 45
# sqrt(3,025) = [30, 25] = 55
# sqrt(6,724) = [6, 72, 4] = 82
# sqrt(8,281) = [8, 2, 81] = 91
# sqrt(9,801) = [98, 1] = 99
# sqrt(10,000) = [100, 0] = 100
# Answer is 41,333 which matches the expected solution
