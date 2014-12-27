#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 304
#
# Primonacci
#
# For any positive integer n the function next_prime(n) returns the
# smallest prime p such that p>n.
#
# The sequence a(n) is defined by:
# a(1)=next_prime(10^14) and a(n)=next_prime(a(n-1)) for n>1.
#
# The fibonacci sequence f(n) is defined by: f(0)=0, f(1)=1 and
# f(n)=f(n-1)+f(n-2) for n>1.
#
# The sequence b(n) is defined as f(a(n)).
#
# Find sum(b(n)) for 1<=n<=100c000. Give your answer mod 1234567891011.
#
# Solved ??/??/14
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

OFFSET = 10**14
#OFFSET = 10**7
MOD = 1234567891011
NN = 100000


############################################################
# Code to calculate Fibonacci numbers efficiently
fib_dict = {}
fib_dict[0] = 0
fib_dict[1] = 1
fib_dict[2] = 1

def fib(n):
    if n in fib_dict:
        return fib_dict[n]

    current_n = 1      # n
    current_f = 1      # fib(n)
    current_f_m_1 = 0  # fib(n-1)

    while (current_n < n):
        # Find the best fib(x-1), fib(x), fib(x+1) from our table to use to get closer to answer
        largest_x = 1
        for x in sorted(fib_dict.keys()):
            if (x < largest_x):
                continue
            if ((x + current_n) > n):
                break
            if (((x+1) in fib_dict) &
                ((x-1) in fib_dict)):
                largest_x = x

        #print("Calculating f({n}) using....".format(n=n))
        #print("    fib[{}] = {}, fib[{}] = {}".format(current_n-1, current_f_m_1, current_n, current_f))
        #print("    fib_dict[{}] = {}, fib_dict[{}] = {}, fib_dict[{}] = {}".format(largest_x-1, fib_dict[largest_x-1],
        #                                                                           largest_x  , fib_dict[largest_x  ],
        #                                                                           largest_x+1, fib_dict[largest_x+1],))

        # f(n+x  ) = f(x+1)*f(n) + f(x  )*f(n-1)
        # f(n+x-1) = f(x  )*f(n) + f(x-1)*f(n-1)
        current_f, current_f_m_1 = (fib_dict[largest_x+1]*current_f + fib_dict[largest_x  ]*current_f_m_1) % MOD, \
                                   (fib_dict[largest_x  ]*current_f + fib_dict[largest_x-1]*current_f_m_1) % MOD
        current_n = current_n + largest_x

        # Insert the new values we've calculated into the dict
        fib_dict[current_n-1] = current_f_m_1
        fib_dict[current_n] = current_f
        #print("    fib_dict[{}] = {}".format(current_n-1, current_f_m_1))
        #print("    fib_dict[{}] = {}".format(current_n, current_f))

        # Calculate one more so that we have a group of 3
        # And insert that into the dict
        fib_dict[current_n+1] = (current_f + current_f_m_1) % MOD
        #print("    fib_dict[{}] = {}".format(current_n+1, (current_f+current_f_m_1) % MOD))

    return current_f


############################################################
# Test code for fibonacci calculation

if (False):
    SIZE = 500
    sfib = [0]*SIZE

    sfib[0] = 0
    sfib[1] = 1
    n = 2
    while n < SIZE:
        sfib[n] = (sfib[n-1]+sfib[n-2]) % MOD
        n += 1

    for n in range(10):
        print("sfib({}) = {}".format(n, sfib[n]))
    for n in [10, 100, 200, 300, 400, 499]:
        print("sfib({}) = {}".format(n, sfib[n]))

    for n in range(10):
        print("fib({}) = {}".format(n, fib(n)))
        if (sfib[n] != fib(n)):
            print("    Error sfib({n}) = {sfib} != fib({n}) = {fib}".format(n=n, sfib=sfib[n], fib=fib(n)))
    for n in [10, 100, 200, 300, 400, 499]:
        print("fib({}) = {}".format(n, fib(n)))
        if (sfib[n] != fib(n)):
            print("    Error sfib({n}) = {sfib} != fib({n}) = {fib}".format(n=n, sfib=sfib[n], fib=fib(n)))

    # Calculate a big fibonacci
    n = 10**14
    for x in range(n, n+10):
        print("fib({}) = {}".format(x, fib(x)))

    print "Time taken = {0} seconds".format(time.clock() - start_time)
    sys.exit(0)


############################################################
# Code to calculate primes
import random

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


############################################################
# Calculate the answer
i = OFFSET + 1
f_i = fib(i)
f_i_m_1 = fib(i-1)

count = 0
answer = 0
prev_time = time.clock()
while (count < NN):
    if is_prime(i):
        answer = (answer + f_i) % MOD
        count += 1
        if ((count % 1000) == 0):
            print("count = {}, fib({}) = {}, answer = {}, time = {}".format(count, i, f_i, answer, time.clock()-prev_time))
            prev_time = time.clock()
    i += 1
    f_i, f_i_m_1 = (f_i + f_i_m_1) % MOD, f_i
    i += 1
    f_i, f_i_m_1 = (f_i + f_i_m_1) % MOD, f_i

print "Answer =", answer

print "Time taken = {0} seconds".format(time.clock() - start_time)


# Ways to accelerate fibonacci sequence
#
# f(0) = 1
# f(1) = 1
# f(2) = f(1) + f(0)
# f(3) = f(1) + f(1)
#
# f( 0) = 0
# f( 1) = 1
# f( 2) = 1
# f( 3) = 2
# f( 4) = 3
# f( 5) = 5
# f( 6) = 8
# f( 7) = 13
# f( 8) = 21
# f( 9) = 34
# f(10) = 55
# f(11) = 89
#
# f(n+1)  =  f(n  ) + f(n-1)                                                 =    1*f(n) +   1*f(n-1)  =  f( 2)*f(n) + f( 1)*f(n-1)
# f(n+2)  =  f(n+1) + f(n  )  =  1*f(n) +  1*f(n-1)  +   1*f(n)              =    2*f(n) +   1*f(n-1)  =  f( 3)*f(n) + f( 2)*f(n-1)
# f(n+3)  =  f(n+2) + f(n+1)  =  2*f(n) +  1*f(n-1)  +   1*f(n) +  1*f(n-1)  =    3*f(n) +   2*f(n-1)  =  f( 4)*f(n) + f( 3)*f(n-1)
# f(n+4)  =  f(n+3) + f(n+2)  =  3*f(n) +  2*f(n-1)  +   2*f(n) +  1*f(n-1)  =    5*f(n) +   3*f(n-1)  =  f( 5)*f(n) + f( 4)*f(n-1)
# f(n+5)  =  f(n+4) + f(n+3)  =  5*f(n) +  3*f(n-1)  +   3*f(n) +  2*f(n-1)  =    8*f(n) +   5*f(n-1)  =  f( 6)*f(n) + f( 5)*f(n-1)
# f(n+6)  =  f(n+5) + f(n+4)  =  8*f(n) +  5*f(n-1)  +   5*f(n) +  3*f(n-1)  =   13*f(n) +   8*f(n-1)  =  f( 7)*f(n) + f( 6)*f(n-1)
# f(n+7)  =  f(n+6) + f(n+5)  = 13*f(n) +  8*f(n-1)  +   8*f(n) +  5*f(n-1)  =   21*f(n) +  13*f(n-1)  =  f( 8)*f(n) + f( 7)*f(n-1)
# f(n+8)  =  f(n+7) + f(n+6)  = 21*f(n) + 13*f(n-1)  +  13*f(n) +  8*f(n-1)  =   34*f(n) +  21*f(n-1)  =  f( 9)*f(n) + f( 8)*f(n-1)
# f(n+9)  =  f(n+8) + f(n+7)  = 34*f(n) + 21*f(n-1)  +  21*f(n) + 13*f(n-1)  =   55*f(n) +  34*f(n-1)  =  f(10)*f(n) + f( 9)*f(n-1)
# f(n+10) =                                                                  =   89*f(n) +  55*f(n-1)  =  f(11)*f(n) + f(10)*f(n-1)
# f(n+11) =                                                                  =  144*f(n) +  89*f(n-1)  =  f(12)*f(n) + f(11)*f(n-1)
#
# f(n+x-2) = f(x-1)*f(n) + f(x-2)*f(n-1)
# f(n+x-1) = f(x  )*f(n) + f(x-1)*f(n-1)
# f(n+x  ) = f(x+1)*f(n) + f(x  )*f(n-1)
#
