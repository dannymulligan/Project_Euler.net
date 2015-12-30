#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 196
#
# Prime triplets
#
# Build a triangle from all positive integers in the following way:
#
#    1:     1
#    2:   <2>  <3>
#    3:    4   <5>   6
#    4:   <7>   8    9   10
#    5:  <11>  12  <13>  14   15
#    6:   16  <17>  18  <19>  20   21
#    7:   22  <23>  24   25   26   27   28
#    8:  <29>  30  <31>  32   33   34   35   36
#    9:  <37>  38   39   40  <41>  42  <43>  44  45
#   10:   46  <47>  48   49   50   51   52  <53> 54  55
#   11:   56   57   58  <59>  60  <61>  62   63  64  65  66
#      . . .
#
# Each positive integer has up to eight neighbours in the triangle.
#
# A set of three primes is called a prime triplet if one of the three
# primes has the other two as neighbours in the triangle.
#
# For example, in the second row, the prime numbers 2 and 3 are
# elements of some prime triplet.
#
# If row 8 is considered, it contains two primes which are elements of
# some prime triplet, i.e. 29 and 31.
# If row 9 is considered, it contains only one prime which is an
# element of some prime triplet: 37.
#
# Define S(n) as the sum of the primes in row n which are elements of
# any prime triplet.  Then S(8)=60 and S(9)=37.
#
# You are given that S(10000)=950007619.
#
# Find S(5678027) + S(7208785).
#
# Solved ??/??/14
# ?? problems solved
# Position #??? on level ?

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
def triangle(n):
    return n*(n+1)/2

def triangle_row_range(n):
    return triangle(n-1)+1, triangle(n)

for i in range(10):
    print("triangle({}) = {}".format(i, triangle(i)))

for i in range(1,12):
    print("row({}) covers {}".format(i, triangle_row_range(i)))

for i in [10000, 5678027, 7208785, 7208786, 7208787]:
    print("row({}) covers {}".format(i, triangle_row_range(i)))

for i in [9999, 10000, 5678027, 5678026, 7208784, 7208785, 7208786, 7208787]:
    print("triangle({}) = {}".format(i, triangle(i)))

# Row 7208785 covers 25983286983721 to 25983294192505
# We'd possibly need to check the next two rows too, up to 7208787
# Row 7208786 covers 25983294192506 to 25983301401291
# Row 7208787 covers 25983301401292 to 25983308610078
# log2(25983308610078) = 44.56
# 25983308610078 = 2.6E13
# So we can't build a table of primes that big

print "Time taken = {0} seconds".format(time.clock() - start_time)
