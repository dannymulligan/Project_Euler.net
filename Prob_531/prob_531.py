#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 531
#
# Chinese leftovers
#
# Let g(a,n,b,m) be the smallest non-negative solution x to the
# system:
#
# x = a mod n
# x = b mod m
#
# if such a solution exists, otherwise 0.
#
# E.g. g(2,4,4,6)=10, but g(3,4,4,6)=0.
#
# Let phi(n) be Euler's totient function.
#
# Let f(n,m)=g(phi(n),n,phi(m),m)
#
# Find sum(f(n,m)) for 1000000 <= n < m < 1005000


import sys
#print(sys.version)
import time
start_time = time.clock()

########################################


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
