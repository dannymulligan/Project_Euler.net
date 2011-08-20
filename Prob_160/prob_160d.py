#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 160
#
# Problem summary
#
# For any N, let f(N) be the last five digits before the trailing
# zeroes in N!. For example,
#
#     9! = 362880 so f(9)=36288
#     10! = 3628800 so f(10)=36288
#     20! = 2432902008176640000 so f(20)=17664
#
# Find f(1,000,000,000,000)
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level 4

import sys
import time
start_time = time.clock()

MAX = 10**12
ROUND = 100000
fact = []

def precalc_f():
    f = 1
    for i in xrange(ROUND+1):
        if (((i % 2) == 0) or ((i % 5) == 0)):
            pass
        else:
            f = (f * i) % ROUND
        fact.append(f)


########################################
def log2(n):
    ans = 0
    while (n>=2):
        n /= 2
        ans += 1
    return ans


########################################
def log5(n):
    ans = 0
    while (n>=5):
        n /= 5
        ans += 1
    return ans

########################################
def cnt(n):
    ans = 4*(n/10)
    n = n % 10
    if   (n >= 9):  ans += 4  # 9
    elif (n >= 7):  ans += 3  # 7 (8 is skipped)
    elif (n >= 3):  ans += 2  # 3 (4,5,6 are skipped)
    elif (n >= 1):  ans += 1  # 1 (2 is skipped)
    return ans


########################################
def f_ex25(n):
    if (n <= ROUND):
        return fact[n]
    else:
        # if n = p * ROUND + r
        # then answer = fact[ROUND]^p * fact[r]
        p = n / ROUND
        r = n % ROUND
        ans = (fact[ROUND]**p) % ROUND
        ans = (ans*fact[r]) % ROUND
        return ans


########################################
def odd(n):
    if (n % 2):  return True
    else:        return False


########################################
def power(n,x):
    np = n
    a = 1
    while x:
        if odd(x):
            x -= 1
            a = (a*np) % ROUND
        else:
            np = np**2 % ROUND
            x /= 2
    return a


########################################
def expand(n,n2,n5):
    np = 2
    while n2:
        if odd(n2):
            n2 -= 1
            n = (n*np) % ROUND
        else:
            np = np**2 % ROUND
            n2 /= 2
    np = 5
    while n5:
        if odd(n5):
            n5 -= 1
            n = (n*np) % ROUND
        else:
            np = np**2 % ROUND
            n5 /= 2
    return (n,n2,n5)


print "########################################"
print "Fancy calculation method"

precalc_f()

(ans,ans2,ans5) = (1,0,0)
for b in xrange(1+log2(MAX)):
    for c in xrange(1+log5(MAX)):
        div = (2**b) * (5**c)
        if (div > MAX):  continue


        amax = MAX / ((2**b) * (5**c))
        (n, n2, n5) = (f_ex25(amax), b*cnt(amax), c*cnt(amax))

        print "Factorial(N * 2^{0} * 5^{1}) where N = 1..{2} excluding all multiples of 2 and 5, {3} numbers total".format(b,c,amax, cnt(amax))
        #print "..  n = {0} * 2^{1} * 5^{2},  ans = {3} * 2^{4} * 5^{5}".format(n, n2, n5, ans, ans2, ans5)
        ans = (ans * n) % ROUND
        ans2 += n2
        ans5 += n5
        #print ".   n = {0} * 2^{1} * 5^{2},  ans = {3} * 2^{4} * 5^{5}".format(n, n2, n5, ans, ans2, ans5)
        m = min(ans2,ans5)
        ans2 -= m
        ans5 -= m
        #print "    n = {0} * 2^{1} * 5^{2},  ans = {3} * 2^{4} * 5^{5}".format(n, n2, n5, ans, ans2, ans5)

print "a={0} * 2^{1} * 5^{2}".format(ans,ans2,ans5)
(ans,ans2,ans5) = expand(ans,ans2,ans5)
print "a={0} * 2^{1} * 5^{2}".format(ans,ans2,ans5)
print "Answer =", ans
print "Time taken = {0} seconds".format(time.clock() - start_time)
start_time = time.clock()

sys.exit()

print "########################################"
print "Simple calculation method"
(s,s2,s5) = (1,0,0)
for i in xrange(1,MAX+1):
    ii = i

    while ((ii % 2) == 0):
        ii /= 2
        s2 += 1

    while ((ii % 5) == 0):
        ii /= 5
        s5 += 1

    s = s*ii
    s = s % ROUND
print "s={0} * 2^{1} * 5^{2}".format(s,s2,s5)
m = min(s2,s5)
(s2,s5) = (s2-m,s5-m)
print "s={0} * 2^{1} * 5^{2}".format(s,s2,s5)
(s,s2,s5) = expand(s,s2,s5)
print "a={0} * 2^{1} * 5^{2}".format(s,s2,s5)
print "Answer =", s
print "Time taken = {0} seconds".format(time.clock() - start_time)
