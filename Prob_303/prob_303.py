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

def digit(n, x):
    '''Return digit n of number x'''
    return ((x/10**n) % 10)

def fn_backup(x):
    # Only works for cases where x = 99, 999, 9999
    n = 1
    power = 0
    while True:
        while True:
            #print("n={}, x={}, n*x={}, digit({}, {})={}".format(n, x, n*x, power, n*x, digit(power, n*x)))
            valid, msd, xxx = test_012(n*x)
            if valid:
                return n
            if (digit(power, n*x) <= 2):
                break
            n += 10**power
        power += 1
        if power > 20:
            return

def small_digit_recurse(top, digits):
    if top and (digits == 1):
        yield 1
        yield 2
    elif top and (digits > 1):
        for n in small_digit_recurse(top=False, digits=digits-1):
            yield 1*(10**(digits-1)) + n
        for n in small_digit_recurse(top=False, digits=digits-1):
            yield 2*(10**(digits-1)) + n
    elif (digits == 1):
        yield 0
        yield 1
        yield 2
    else:
        for n in small_digit_recurse(top=False, digits=digits-1):
            yield                      n
        for n in small_digit_recurse(top=False, digits=digits-1):
            yield 1*(10**(digits-1)) + n
        for n in small_digit_recurse(top=False, digits=digits-1):
            yield 2*(10**(digits-1)) + n

def small_digit_num(digits):
    '''Generate numbers up to digits in length
    that only use digits <= 2'''
    for d in range(1, digits+1):
        for n in small_digit_recurse(top=True, digits=d):
            yield n


def fn(x):
    if ((x == 99)
     or (x == 999)
     or (x == 9999)):
        return fn_backup(x)

    for n in small_digit_num(30):
        #print("n={n}, x={x}, {n}%{x}={r}".format(n=n, x=x, r=n%x))
        if ((n % x) == 0):
            #print("fn({x}) = {d}, because {d}*{x}={n}".format(n=n, x=x, d=n/x))
            return n/x


start_time = time.clock()
answer = 0
biggest = 0
for n in range(1,10001):
    result = fn(n)
    answer += result
    if (result > biggest):
        biggest = result
        print(">>> fn({}) = {}".format(n, result))
    else:
        print("fn({}) = {}".format(n, result))

print("Answer = {}".format(answer))
print("Calculated in {:.3f} seconds".format(time.clock()-start_time))


# This solution is too slow (~2 hours), but the vast majority of the
# time is spent on fn(9999), and to a lesser degree, on fn(999), &
# fn(99).
#
# With a hack that uses a different method for fn(99), fn(999), &
# fn(9999), I'm able to run the program in a little over 7 minutes,
# which is good enough for me.  Moving on...
