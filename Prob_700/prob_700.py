#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 700
#
# Eulercoin
#
# Leonhard Euler was born on 15 April 1707.
#
# Consider the sequence 1504170715041707n mod 4503599627370517.
#
# An element of this sequence is defined to be an Eulercoin if it is
# strictly smaller than all previously found Eulercoins.
#
# For example, the first term is 1504170715041707 which is the first
# Eulercoin. The second term is 3008341430083414 which is greater than
# 1504170715041707 so is not an Eulercoin. However, the third term is
# 8912517754604 which is small enough to be a new Eulercoin.
#
# The sum of the first 2 Eulercoins is therefore 1513083232796311.
#
# Find the sum of all Eulercoins.


import sys
#print(sys.version)
import time
start_time = time.clock()

###############################################################################

A = 1504170715041707  # = 17 * 1249 * 12043 * 5882353
B = 4503599627370517  # prime
def sequence():
    '''
    sequence[n] = ((A * n) % B)
    '''
    n = 0
    while True:
        n += 1
        yield n, (A * n) % B

answer = 0
current_limit = A + 1
i = 0
for n, e in sequence():
    if e < current_limit:
        current_limit = e
        answer += e
        i += 1
        print("{}: sequence[{:,}] = {:,}".format(i, n, e))
    if n == 4000000000:
        break

print("After {:,} items, answer = {:,}".format(i, answer))


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
