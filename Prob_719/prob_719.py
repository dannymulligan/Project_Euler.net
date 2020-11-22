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

def ssplit(s):
    #print("ssplit({})".format(s))
    '''Return all of the possible splits of string s'''
    yield [int(s)]
    for x in range(1,len(s)):
        for y in ssplit(s[x:]):
            yield [int(s[:x])] + y

def S(n):
    '''Note: n is the square root of the n used in the problem description'''
    snum = "{}".format(n**2)
    for split in ssplit(snum):
        if sum(split) == n:
            print("sqrt({:,}) = {} = {:,}".format(n**2, split, n))
            return True

def T(nums):
    solution = 0
    for n in nums:
        if S(n):
            solution += n**2
    return solution


optimization = 3
if optimization >= 1:
    # Eliminate recursion if no solution is possible
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
        '''Note: n is the square root of the n used in the problem description'''
        snum = "{}".format(n**2)
        for split in ssplit(snum, n):
            if sum(split) == n:
                print("sqrt({:,}) = {} = {:,}".format(n**2, split, n))
                return True

if optimization >= 2:
    # Our number splitting technique preserves the digit sum
    # n % 9 calculates the digit sum of n modulo 0
    # if (n % 9) doesn't equal (n**2 % 9) then no possibility of an S-number
    def S(n):
        '''Note: n is the square root of the n used in the problem description'''
        #if (n % 9) != (n**2 % 9):
        #    return False
        if (n % 9) != (n**2 % 9):
            return False
        snum = "{}".format(n**2)
        for split in ssplit(snum, n):
            if sum(split) == n:
                print("sqrt({:,}) = {} = {:,}".format(n**2, split, n))
                return True

    def T(nums):
        solution = 0
        for n in nums:
            if (n % 9) > 1:
                continue
            if S(n):
                solution += n**2
        return solution

if optimization >= 3:
    # Our number splitting technique preserves the digit sum
    # n % 9 calculates the digit sum of n modulo 0
    # If (n % 9) doesn't equal 0 or 1 then no possibility of an S-number
    # Using a appropriate range generator eliminates a lot of work
    def S(n):
        '''Note: n is the square root of the n used in the problem description'''
        snum = "{}".format(n**2)
        for split in ssplit(snum, n):
            if sum(split) == n:
                print("sqrt({:,}) = {} = {:,}".format(n**2, split, n))
                return True

    def T(nums):
        solution = 0
        for n in nums:
            if S(n):
                solution += n**2
            if S(n+1):
                solution += (n+1)**2
        return solution

    nums, solution = range(9, 10**5 + 1, 9),  499984803177  # Calculated in 129.13,  16.42,  17.17 seconds


check_given_examples = False
if check_given_examples:
    nums = [9, 82, 91, 99]
    for n in nums:
        print("S({}) == {}".format(n, S(n), n**2))
        assert S(n)

    nums = range(2, 10**2 + 1)
    solution = 41333
    result = T(nums)
    print("T({}) = {:,}".format(nums, result))
    assert result == solution
else:
    # Run time given                                              optimization = 0,    = 1,    = 2
    nums, solution = range(2, 10**3 + 1),         10804656  # Calculated in   0.06,   0.03,   0.00 seconds
    nums, solution = range(2, 10**4 + 1),       2818842841  # Calculated in   2.74,   0.68,   0.00 seconds
    nums, solution = range(2, 12500 + 1),       3078722269  # Calculated in   4.56,   0.99,   0.00 seconds
    nums, solution = range(2, 15000 + 1),       3240698798  # Calculated in   6.41,   1.32,   0.00 seconds
    nums, solution = range(2, 10**4 * 2),       3839800575  # Calculated in  10.39,   1.96,   0.00 seconds
    nums, solution = range(2, 10**4 * 3),       6222187932  # Calculated in  17.44,   3.34,   3.29 seconds
    nums, solution = range(2, 10**5 + 1),     499984803177  # Calculated in 129.13,  16.42,  17.17 seconds
#    nums, solution = range(2, 10**5 * 2),     831602531877  # Calculated in ???.??,  50.37,  47.84 seconds
#    nums, solution = range(2, 10**5 * 4),    5117390432505  # Calculated in ???.??, 131.34, 133.85 seconds
    nums, solution = range(2, 10**6 + 1),                0  # Calcualted in ???.??, 447.22, 413.22 seconds

    # These versions set nums to where (n % 9) == 0 for optimization = 3
    # They rely on the T function also calculating the (n % 9) == 1 case by adding 1 to n
    nums, solution = range(9, 10**5 + 1, 9),  499984803177  # Calculated in  3.81 seconds
    nums, solution = range(9, 10**6 + 1, 9),             0  # Calcualted in 89.60 seconds

Answer = T(nums)

if solution == 0:
    print("Answer is {:,}".format(Answer))
elif Answer == solution:
    print("Answer is {:,} which matches the expected solution".format(Answer))
else:
    print("ERROR: Answer is {:,} which does not match the expected solution of {:,}".format(Answer, solution))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
