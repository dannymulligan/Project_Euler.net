#!/usr/bin/python
#
# Project Euler.net Problem 216
#
# Investigating the primality of numbers of the form 2n^2-1
#
# Consider numbers t(n) of the form t(n) = 2n^(2)-1 with n > 1.
# The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
# It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
# For n <= 10000 there are 2202 numbers t(n) that are prime.
# 
# How many numbers t(n) are prime for n <= 50,000,000 ?
#
# Solved 12/25/10
# 135 problems solved
# Position #304 on level 3

import sys
import time
import random

## with k = 10
#N = 9        # Answer should be 6
#N = 100      # Answer = 45 out of 100, total time taken = 0.00509 seconds
#N = 10000    # Answer = 2202 out of 10000, total time taken = 0.59515 seconds
#N = 100000   # Answer = 17185 out of 100000, total time taken = 10.657583 seconds
#N = 1000000  # Answer = 141444 out of 1000000, total time taken = 146.7798 seconds
#N = 50000000
## with k = 5
#N = 100      # Answer = 45 out of 100, total time taken = 0.003023 seconds
#N = 10000    # Answer = 2202 out of 10000, total time taken = 0.392527 seconds
#N = 100000   # Answer = 17185 out of 100000, total time taken = 7.261346 seconds
#N = 1000000  # Answer = 141444 out of 1000000, total time taken = 103.105436 seconds
#N = 50000000

## with k = 4
#N = 10000    # Answer = 2202 out of 10000, total time taken = 0.351582 seconds
#N = 100000   # Answer = 17185 out of 100000, total time taken = 6.576682 seconds
#N = 1000000  # Answer = 141444 out of 1000000, total time taken = 94.130468 seconds

# Add heurstic optimization
#N = 10000    # Answer = 2202 out of 10000, total time taken = 0.350081 seconds
#N = 100000   # Answer = 17185 out of 100000, total time taken = 6.477365 seconds
#N = 1000000  # Answer = 141444 out of 1000000, total time taken = 91.037437 seconds

# Add quick prime tests up to 11
#N = 10000    # Answer = 2202 out of 10000, total time taken = 0.294139 seconds
#N = 100000   # Answer = 17185 out of 100000, total time taken = 5.27628 seconds
#N = 1000000  # Answer = 141444 out of 1000000, total time taken = 73.184803 seconds

N = 50000000  # Answer = 5437849 out of 50000000, total time taken = 4790.242245 seconds
# 4790 seconds = 79 minutes 50 seconds

def exp_by_sq(x,y,z):
    # return (x**y % z)
    if (y == 1):
        # y is 1
        ans = x
    elif ((y % 2) == 0):
        # y is even
        ans = exp_by_sq(x,y/2,z)
        ans = (ans * ans) % z
    else:
        # l is odd
        ans = exp_by_sq(x,(y-1)/2,z)
        ans = (ans * ans) % z
        ans = (x * ans) % z
    return ans


def miller_rabin_primality_test(n,s,d,k):
    # True  = n might be prime
    # False = n not prime
    #
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    for kk in xrange(k):
        a = random.randint(2,n-2)
        x = exp_by_sq(a,d,n)
        if ((x == 1) or (x == n-1)):
            continue
        for r in xrange(1,s):
            x = ((x*x) % n)
            if (x == 1):  return False
            if (x == n-1):  break
        if (x != n-1):  return False
    return True

def is_prime(n):
    s = 0
    d = n - 1
    while ((d % 2) == 0):
        d /= 2
        s += 1
    # n-1 = (2**s)*d
    return miller_rabin_primality_test(n,s,d,4)

def t(n):
    return 2*n*n-1

start_time = time.clock()

answer = 0
prev_time = time.clock()
for i in xrange(2,N+1):
    n = t(i)

    # Optimization based on quick prime tests
    if (n == 7) or (n == 17) or (n == 31) or (n == 71):
        answer += 1
        continue
    if (n%3 == 0) or (n%5 == 0) or (n%7 == 0) or (n%11 == 0):
        continue

    # Optimization based on looking at previous runs, not sure why this works
    if (n%10 == 3):
        continue

    if (is_prime(n)):
        answer += 1
    if ((i % 50000) == 0):
        curr_time = time.clock()
        print "Calculating {0}, {1} solutions found, last 50,000 numbers took {2} seconds.".format(i, answer, curr_time-prev_time)
        prev_time = curr_time

print "Answer = {0} out of {1}, total time taken = {2} seconds".format(answer, i, time.clock() - start_time)
