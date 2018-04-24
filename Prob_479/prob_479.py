#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 479
#
# Roots on the Rise
#
# Let ak, bk, and ck represent the three solutions (real or complex
# numbers) to the expression 1/x = (k/x)2(k+x2) - kx.
#
# For instance, for k = 5, we see that {a5, b5, c5} is approximately
# {5.727244, -0.363622+2.057397i, -0.363622-2.057397i}.
#
# Let S(n) = Σ (ak+bk)p(bk+ck)p(ck+ak)p for all integers p, k such
# that 1 <= p, k <= n.
#
# Interestingly, S(n) is always an integer. For example, S(4) = 51160.
#
# Find S(10^6) modulo 1 000 000 007.


import sys
#print(sys.version)
import time
start_time = time.clock()

########################################


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
