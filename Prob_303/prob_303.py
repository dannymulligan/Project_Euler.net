#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 303
#
# Multiples with small digits
#
# For a positive integer n, define f(n) as the least positive multiple
# of n that, written in base 10, uses only digits <= 2.
#
# Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.
#
# Also, the sum of n from 1 to 100 of f(n)/n is 11363107.
#
# Find the sum of n from 1 to 10,000 of f(n)/n.
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

########################################

def test_012(n):
    valid = True
    msd = 0
    power = 0
    while (n > 0):
        msd = n
        if ((n % 10) > 2):
            valid = False
        n = n / 10
        power += 1
    return valid, msd, power-1

assert test_012( 1221) == (True, 1, 3)
assert test_012(11021) == (True, 1, 4)
assert test_012(  221) == (True, 2, 2)
assert test_012(50021) == (False, 5, 4)

########################################

def fn(n):
    x = 0
    if   ((n % 10) == 0):  rep = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    elif ((n % 10) == 1):  rep = [1, 1, 8]
    elif ((n % 10) == 2):  rep = [1, 4, 1, 4]
    elif ((n % 10) == 3):  rep = [4, 3, 3]
    elif ((n % 10) == 4):  rep = [3, 2, 3, 2]
    elif ((n % 10) == 5):  rep = [2, 2, 2, 2, 2]
    elif ((n % 10) == 6):  rep = [2, 3, 2, 3]
    elif ((n % 10) == 7):  rep = [3, 3, 4]
    elif ((n % 10) == 8):  rep = [4, 1, 4, 1]
    elif ((n % 10) == 9):  rep = [8, 1, 1]

    #print("startup x={}, rep={}".format(x, rep))
    while True:
        for dx in rep:
            x += dx
            nx = n*x % 10
            (valid, msd, power) = test_012(n*x)
            #print("x={}, n={}, n*x={}, valid={}".format(x, n, n*x, valid))
            if valid:
                return x

        # Skip ahead if we can
        if (msd > 2):
            # Skip x ahead so that n*x is at least 10**(power+1)
            #print("    skipping ahead msd={}, x={}, n={}, n*x={}".format(msd, x, n, n*x))
            x = 10**(power+1)/n

            # Check values of x until we can use fancy skipping logic again
            x = x - (x % 10)
            (valid, msd, power) = test_012(n*x)
            #print("x={}, n={}, n*x={}, valid={}".format(x, n, n*x, valid))
            if valid:
                return x

            for dx in rep:
                x += dx
                nx = n*x % 10
                (valid, msd, power) = test_012(n*x)
                #print("x={}, n={}, n*x={}, valid={}".format(x, n, n*x, valid))
                if valid:
                    return x
            #print("    skipped ahead x = {}/{} = {}".format(10**(power+1), n, x))


start_time = time.clock()
assert fn(  2) ==  1  # 2*1=2
assert fn(  3) ==  4  # 3*4=12
assert fn(  7) ==  3  # 7*3=21
assert fn( 42) ==  5  # 42*5 = 210
assert fn( 89) == 12598  # 89*12598=1121222
assert fn( 99) == 11335578  # 99*11335578=1122222222
assert fn(495) == 22671156  # 495*22671156=11222222220


print("Starting")
start_time = time.clock()
answer = 0
biggest = 0
for n in range(1,101):
    #if ((n % 25) == 0):
    #    print("n={}".format(n))
    result = fn(n)
    answer += result
    if (result > biggest):
        biggest = result
        print("fn({}) = {}, {}*{}={}".format(n, result, n, result, n*result))

print answer
print("Calculated in {:.3f} seconds".format(time.clock()-start_time))
assert answer == 11363107
