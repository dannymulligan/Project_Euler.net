#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 512
#
# Sums of totients of powers
#
# Let phi(n) be Euler's totient function.
#
# Let f(n) = (sum from i=1 to n of phi(n^i)) mod (n+1)
#
# Let g(n) = sum from i=1 to n of f(i)
#
# g(100)=2007
#
# Find g(5×10^8)

import sys
#print(sys.version)
import time
start_time = time.clock()

########################################


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
