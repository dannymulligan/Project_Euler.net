#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 686
#
# Powers of Two
#
# 2^7=128 is the first power of two whose leading digits are "12".
# The next power of two whose leading digits are "12" is 2^80.
#
# Define p(L,n) to be the nth-smallest value of j such that the base
# 10 representation of 2^j begins with the digits of L.
#
# So p(12,1) = 7 and p(12,2) = 80.
#
# You are also given that p(123,45) = 12710.
#
# Find p(123,678910).

import sys
#print(sys.version)
import time
start_time = time.clock()

###############################################################################
def p(L, n):
    L_str = "{}".format(L)
    target_str = L_str[0] + "." + L_str[1:]
    target_len = len(target_str)
    ans, i = 2.0, 1
    found = 0
    prev_i = 1
    min_delta_i, max_delta_i = 10000, 0
    while (found < n):
        ans_str = "{:15.13e}".format(ans)
        if ans_str[:target_len] == target_str:
            found += 1
            delta_i, prev_i = i-prev_i, i
            max_delta_i = max(max_delta_i, delta_i)
            min_delta_i = min(min_delta_i, delta_i)
            if (found % 10000) == 0:
                print("Found 2^{} = {:15.13e}, item {}".format(i, ans, found), end='')
                print(", delta_i min/last/max = {}/{}/{}".format(min_delta_i, delta_i, max_delta_i))
                min_delta_i, max_delta_i = 10000, 0
            # Based on the observed minimum delta between solutions, we're not going to find another match
            # before we've multiplied the answer by 2^196.  We could skip forward by 2^180 or so and save
            # a significant amount of processing and speed up our calculations here.
        ans *= 2
        if ans > 1e10:
            ans /= 1e10
        i += 1
        #print(" 2^{} = {:e}".format(i, ans))
    return i-1

if False:
    assert p(12,1) == 7
    assert p(12,2) == 80
    assert p(123,45) == 12710

L = 123
n = 678910
result = p(L=L, n=n)
print("p(L={}, n={}) = {}".format(L, n, result))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
