#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 169
#
# Exploring the number of different ways a number can be expressed as
# a sum of powers of 2.
#
# Define f(0)=1 and f(n) to be the number of different ways n can be
# expressed as a sum of integer powers of 2 using each power no more
# than twice.
#
# For example, f(10)=5 since there are five different ways to express
# 10:
#
#     1 + 1 + 8
#     1 + 1 + 4 + 4
#     1 + 1 + 2 + 2 + 4
#     2 + 4 + 4
#     2 + 8
#
# What is f(10^25)?
#
# Solved 04/20/2014
# 191 problems solved
# Position #153 on level 7

import sys
import time
start_time = time.clock()


def Decimal2List(n):
    result = list()
    while n > 0:
        if (n % 2):
            n -= 1
            result = [1] + result
        else:
            result = [0] + result
        n /= 2
    if result == []:
        result = [0]
    return result

def List2Decimal(l):
    result = 0
    for n in l:
        result *= 2
        result += n
    return result


def f(n):
    print("Calling f({})".format(n))
    ln = Decimal2List(n)
    return fl(ln)

def SubR(ln):
    # Subtract 0...01b from l
    if ln == [0] * len(ln):
        return ln[:-1] + [-1]

    if ln[-1] == 0:
        return SubR(ln[:-1]) + [1]
    else:
        return ln[:-1] + [ln[-1] - 1]

def fl(ln):
    #print("Calling fl({})".format(ln))
    if len(ln) <= 2:
        if   ln ==    [0]:  return 1
        elif ln ==    [1]:  return 1
        elif ln ==    [2]:  return 1
        elif ln == [0, 0]:  return 1
        elif ln == [0, 1]:  return 1
        elif ln == [0, 2]:  return 1
        elif ln == [1, 0]:  return 2  # [1, 0] & [0, 2]
        elif ln == [1, 1]:  return 1
        elif ln == [1, 2]:  return 1
        elif ln == [2, 0]:  return 2  # [2, 0] & [1, 2]
        elif ln == [2, 1]:  return 1
        elif ln == [2, 2]:  return 1
        elif ln == [3, 0]:  return 1  # [2, 2]
        else:              return 0
    else:
        # Split the list in half
        la, ra = ln[:len(ln)/2], ln[len(ln)/2:]
        #print("Splitting the list {} into {} & {}".format(ln, la, ra))

        # Calculate f(left) * f(right) + f(left - 0..01b) * f(right + 20..0b)
        fl_la = fl(la)

        fl_ra = fl(ra)

        lb = SubR(la)
        if (lb[-1] == -1):
            fl_lb = 0
        else:
            fl_lb = fl(lb)

        rb = [ra[0] + 2] + ra[1:]
        fl_rb = fl(rb)
        print("    fl({}) = fl({})*fl({}) + fl({})*fl({}) = {}*{} + {}*{} = {}".format(
            ln, la, ra, lb, rb, fl_la, fl_ra, fl_lb, fl_rb, fl_la*fl_ra + fl_lb*fl_rb))
        return fl_la*fl_ra + fl_lb*fl_rb

#print("f(10) = {}".format(f(10)))
#print("f(20) = {}".format(f(20)))
#print("f(100) = {}".format(f(100)))

answer = f(10**25)
print "Answer =", answer
print "Time taken = {0} seconds".format(time.clock() - start_time)
