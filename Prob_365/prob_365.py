#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 365
#
# A huge binomial coefficient
#
# The binomial coefficient C(10^18,10^9) is a number with more than 9
# billion (9x10^9) digits.
#
# Let M(n,k,m) denote the binomial coefficient C(n,k) modulo m.
#
# Calculate M(10^18,10^9,p*q*r) for 1000<p<q<r<5000 and p,q,r prime.
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?


#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

from fractions import gcd
import sys
import time
start_time = time.clock()

POW_n = 18  # n = 10^18
POW_k = 9   # k = 10^9
TOP_m = 5000
BOT_m = 1000

########################################
LIMIT_PRIME = TOP_m
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
pqr = []

def calculate_primes():
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            if ((i > BOT_m) & (i < TOP_m)):
                pqr.append(i)
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1
    while (i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            primes.append(i)
            if ((i > BOT_m) & (i < TOP_m)):
                pqr.append(i)
        i += 1

calculate_primes()
print "There are", len(primes), "primes less than", TOP_m
#print "They are", primes
print "There are", len(pqr), "primes greater than", BOT_m, "and less than", TOP_m
#print "They are", pqr

print "We will have {0} different cases to consider".format(len(pqr)*(len(pqr)-1)*(len(pqr)-2)/(3*2*1))


########################################
def XPowYModM(x,y,m):
    ans = 1
    mul = x
    while (y > 0):
        if (y % 2):
            ans = (ans * mul) % m
            y = (y - 1)
        y = y/2
        mul = (mul * mul) % m
    return ans

## Test data for XPowYModM(x,y,m)
#(x,y,m,e) = ( 5,  1,   3,  2);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = ( 5,  2,   3,  1);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = ( 2,  5,   5,  2);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = ( 3,  7,  19,  2);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = ( 3,  7, 100, 87);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = (10, 10,   5,  0);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = (10,  8,   7,  2);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = (10,  9, 117, 64);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = (64,  2, 117,  1);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#(x,y,m,e) = (10, 18, 117,  1);  print "XPowYModM({0},{1},{2}) = {3} ({4})".format(x,y,m,XPowYModM(x,y,m),(e==XPowYModM(x,y,m)))
#sys.exit()


########################################
def ExtendedEuclidian(a,b):
    """
    Find the solution to xa + yb = gcd(a,b) = 1
    We assume a & b are co-prime to each other
    We also assume a & b are > 0, and a > b
    x is the multiplicative inverse of a mod b
    y is the multiplicative inverse of b mod a
    """
    (x,lastx) = (0,1)
    (y,lasty) = (1,0)
    while (b != 0):
        q = a / b
        (a,b) = (b, a % b)
        (x, lastx) = (lastx-q*x, x)
        (y, lasty) = (lasty-q*y, y)
    return (lastx,lasty)

## Test data for ExtendedEuclidian(a,b)
#(a,b,e) = ( 120,  23, ( -9, 47));  ans = ExtendedEuclidian(a,b); print "ExtendedEuclidian({0},{1}) = {2} ({3})".format(a,b,ans,(e==ans))
#(a,b,e) = (  13,   8, ( -3,  5));  ans = ExtendedEuclidian(a,b); print "ExtendedEuclidian({0},{1}) = {2} ({3})".format(a,b,ans,(e==ans))
#(a,b,e) = (  65,  40, ( -3,  5));  ans = ExtendedEuclidian(a,b); print "ExtendedEuclidian({0},{1}) = {2} ({3})".format(a,b,ans,(e==ans))
#(a,b,e) = (  59,  35, (-16, 27));  ans = ExtendedEuclidian(a,b); print "ExtendedEuclidian({0},{1}) = {2} ({3})".format(a,b,ans,(e==ans))
#(a,b,e) = (1239, 735, (-16, 27));  ans = ExtendedEuclidian(a,b); print "ExtendedEuclidian({0},{1}) = {2} ({3})".format(a,b,ans,(e==ans))
#sys.exit()


########################################
def InvMod(a,b):
    """
    Return x such that a*x mod b = 1
    Assumes a & b are co-prime to each other
    """
    g = gcd(a,b)
    #print g, a, b
    while (g != 1):
        (a,b) = (a/g,b/g)
        g = gcd(a,b)
        #print g, a, b

    if (b == 1):
        return 1
    else:
        (x,y) = ExtendedEuclidian(a,b)
        return (x+b) % b

## Test data for InvMod(a,b)
#(a,b) = ( 120,  23);  x = InvMod(a,b); print "InvMod({0},{1}) = {2} ({3})".format(a,b,x,(((a*x)%b)==1))
#(a,b) = (  13,   8);  x = InvMod(a,b); print "InvMod({0},{1}) = {2} ({3})".format(a,b,x,(((a*x)%b)==1))
#(a,b) = (  59,  35);  x = InvMod(a,b); print "InvMod({0},{1}) = {2} ({3})".format(a,b,x,(((a*x)%b)==1))
#(a,b) = ( 237, 731);  x = InvMod(a,b); print "InvMod({0},{1}) = {2} ({3})".format(a,b,x,(((a*x)%b)==1))
#sys.exit()


########################################
def binomial(n,k):
    """
    Calculate C(n,k), using a simple but slow algorithm
    """
    (num,den) = (1,1)
    for i in xrange(k):
        num = (num * (n-i))
        den = (den * (k-i))
        c = gcd(num,den)
        num /= c
        den /= c
    ans = num / den
    return ans

## Test data for binomial(n,k)
#(n,k,e) = (3, 2,  3);  x = binomial(n,k); print "binomial({0},{1}) = {2} ({3})".format(n,k,x,(x==e))
#(n,k,e) = (4, 2,  6);  x = binomial(n,k); print "binomial({0},{1}) = {2} ({3})".format(n,k,x,(x==e))
#(n,k,e) = (6, 3, 20);  x = binomial(n,k); print "binomial({0},{1}) = {2} ({3})".format(n,k,x,(x==e))
#(n,k,e) = (8, 3, 56);  x = binomial(n,k); print "binomial({0},{1}) = {2} ({3})".format(n,k,x,(x==e))
#sys.exit()


########################################
def func_m(n,k,m):
    """
    Calculate C(n,k) mod m
    """

    # Minor simplification... C(n,k) = C(n,(n-k))
    # if n-k is smaller than k, we save work by calculating C(n,(n-k))
    if ((n-k) < k):
        k = n-k

    #               n!       n * (n-1) * ... * (n-k+2) * (n-k+1)
    # C(n,k) = ----------- = -----------------------------------
    #          k! * (n-k)!   k * (k-1) * ... *    2    *    1
    #
    # Some of the numbers in the numerator and denominator will be
    # multiples of m.
    #
    # If there are an equal number of powers of m in the numerator and
    # denominator, then the cancel each other out, in which case we
    # need to divide them out of the numbers in the numerator and
    # denominator before we can calculate the result (done below).
    #
    # If there are more factors of m in the numerator than in the
    # denominator, then the resulting binomial coefficient will be a
    # multiple of m, and applying modulo m to the result will cause
    # this function to be 0.
    #
    # It is not possible for the denominator to have more factors of m
    # than the numerator.  The numbers in the denominator start with
    # 1, which is as far as possible away from m, m^2, m^3, ..., etc.
    # The numbers in the denominator can start anywhere relative to
    # the nearest m, m^2, m^3, ..., etc, so there will always be at
    # least as many factors of m in the numerator as in the
    # denominator.
    #
    # We have to look for factors of m, m^2, etc.
    for i in xrange(1,8):
        if ((m**i) <= k):
            # There is at least one multiple of m^i in the denominator
            # Check if there are more in the numerator than in the denominator
            if ((n % (m**i)) < (k % (m**i))):
                return 0
        else:
            # There are no multiples of m^i in the denominator
            # Check if there are any in the numerator
            if ((n % (m**i)) < k):
                return 0


    # Since the calculation will repeat every m iterations,
    # and k = l * m + r, we're going to run a loop of m, take the
    # result to the power of l, and multiply by the result of a loop
    # of r
    (l, r) = (k / m, k % m)
    #print "l = ", l, "r =", r, "m =", m

    c = 1
    for i in xrange(r):
        num = n-i
        den = k-i
        while ((num % m) == 0):
            num = num / m
        while ((den % m) == 0):
            den = den / m

        #print "{0}: c * {1} / {2}".format(i,num,den)

        c = (c * num) % m
        #print "    c = c * {0} = {1}".format(num,c)

        c = (c * InvMod(den,m)) % m
        #print "    c = c * {0} = {1} ".format(InvMod(den,m),c)
    c_r = c
    #print "c_r =", c_r

    if (l == 0):
        c_m = 1
    else:
        for i in xrange(r,m):
            num = n-i
            den = k-i
            while ((num % m) == 0):
                num = num / m
            while ((den % m) == 0):
                den = den / m

            #print "{0}: c * {1} / {2}".format(i,num,den)

            c = (c * num) % m
            #print "    c = c * {0} = {1}".format(num,c)

            c = (c * InvMod(den,m)) % m
            #print "    c = c * {0} = {1}".format(InvMod(den,m),c)
        c_m = c
    #print "c_m =", c_m

    ans = XPowYModM(c_m,l,m)
    ans = (ans * c_r) % m
    return ans

#for i in xrange(16):
#    print "InvMod({0},5) = {1}".format(i, InvMod(i,5))
#i = 120; print "InvMod({0},5) = {1}".format(i, InvMod(i,5))
#i = 24; print "InvMod({0},5) = {1}".format(i, InvMod(i,5))

## Test data for func_m(n,k)
#(n,k,m) = ( 4, 2,   3);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#(n,k,m) = ( 4, 3,   3);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#(n,k,m) = (12, 5, 997);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#(n,k,m) = (12, 7, 997);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#(n,k,m) = (12, 5,   5);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#(n,k,m) = (19, 7, 719);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#(n,k,m) = (19, 7, 137);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#(n,k,m) = (19, 9, 307);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#
#for i in primes[20:300]:
#    (n,k,m) = (19,  9, i);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#    (n,k,m) = (37, 12, i);  x = func_m(n,k,m);  e = (binomial(n,k) % m);  print "func_m({0},{1},{2}) = {3} ({4} {5})".format(n,k,m,x,(x==e),e)
#
#print "{0}".format(False)

n = 10**POW_n
k = 10**POW_k

c_n_k_m = []
non_zero = 0
for m in pqr:
    x = func_m(n,k,m)
    c_n_k_m.append(x)
    if (x != 0):
        non_zero += 1
        print "func_m({0},{1},{2}) = {3}".format(n,k,m,x)
print "Found {0} non-zero M(n,k,m) results".format(non_zero)


########################################
poss = 0
ans = 0
for ri in range(2,len(pqr)):
    if ((ri % 100) == 0):
        print "ri =", ri
    if (c_n_k_m[ri] == 0):
        continue
    for qi in range(1,ri):
        if (c_n_k_m[qi] == 0):
            continue
        for pi in range(0,qi):
            if (c_n_k_m[pi] == 0):
                continue
            poss += 1

            x = (c_n_k_m[pi] * pqr[qi]*pqr[ri] * InvMod(pqr[qi]*pqr[ri],pqr[pi])) \
              + (c_n_k_m[qi] * pqr[pi]*pqr[ri] * InvMod(pqr[pi]*pqr[ri],pqr[qi])) \
              + (c_n_k_m[ri] * pqr[pi]*pqr[qi] * InvMod(pqr[pi]*pqr[qi],pqr[ri]))
            x = x % (pqr[pi]*pqr[qi]*pqr[ri])
            ans += x

            #print "{0}-{1}-{2} = {3} * {4} * {5} = {6}".format(pi,qi,ri, pqr[pi],pqr[qi],pqr[ri], pqr[pi]*pqr[qi]*pqr[ri])

            #print "M(10^18,10^9,{0}) = {1}, ".format(pqr[pi], c_n_k_m[pi]),
            #print "M(10^18,10^9,{0}) = {1}, ".format(pqr[qi], c_n_k_m[qi]),
            #print "M(10^18,10^9,{0}) = {1} => ".format(pqr[ri], c_n_k_m[ri]),
            #print "M(10^18,10^9,{0}) = {1} ".format(pqr[pi]*pqr[qi]*pqr[ri], x)

            #print "x = {0} * {1} * {2}".format(c_n_k_m[pi], pqr[qi]*pqr[ri], InvMod(pqr[qi]*pqr[ri],pqr[pi])),
            #print  " + {0} * {1} * {2}".format(c_n_k_m[qi], pqr[pi]*pqr[ri], InvMod(pqr[pi]*pqr[ri],pqr[qi])),
            #print  " + {0} * {1} * {2}".format(c_n_k_m[ri], pqr[pi]*pqr[qi], InvMod(pqr[pi]*pqr[qi],pqr[ri])),
            #print " = {0}".format(x)
 

print "We considered {0} possibilities".format(poss)
print "Answer = {0}".format(ans)
print "Time taken = {0} seconds".format(time.clock() - start_time)

