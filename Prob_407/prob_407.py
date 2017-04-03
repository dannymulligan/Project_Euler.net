#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 407
#
# Idempotents
#
# If we calculate a^2 mod 6 for 0 <= a <= 5 we get: 0,1,4,3,4,1.
#
# The largest value of a such that a^2 ≡ a mod 6 is 4.
#
# Let's call M(n) the largest value of a < n such that a2 === a (mod n).
# So M(6) = 4.
#
# Find sum(M(n)) for 1 <= n <= 10^7.


import sys
import time
start_time = time.clock()


########################################
def res(a,n):
    return (a**2) % n


########################################
def M(n):
    for a in range(n, 0, -1):
        r = res(a, n)
        if a == r:
            return a
    return 1


########################################
if False:
    for n in range(1,10):
        print("")
        print("="*60)
        print("n = {}, M({}) = {}".format(n, n, M(n)))
        print("-"*60)
        for a in range(n):
            r = res(a, n)
            if a == r:
                print(" >> a = {}, r = {} <<".format(a,r))
            else:
                print("    a = {}, r = {}".format(a,r))
    sys.exit()

########################################
for SIZE in [10**1, 10**2, 10**3, 10**4]:
    start_time = time.clock()
    Answer = 0
    for n in range(1, SIZE+1):
        mm = M(n)
        #print("M({}) = {}".format(n, mm))
        Answer += mm
        
    print("When SIZE = {:,}, answer is {:,} (calculated in {:.2f} seconds)".format(SIZE, Answer, time.clock() - start_time))
#print("Time taken = {:.2f} seconds".format(time.clock() - start_time))

# When SIZE = 10, answer is 18 (calculated in 0.00 seconds)
# When SIZE = 100, answer is 2,550 (calculated in 0.00 seconds)
# When SIZE = 1,000, answer is 314,035 (calculated in 0.22 seconds)
# When SIZE = 10,000, answer is 34,981,570 (calculated in 21.69 seconds)
