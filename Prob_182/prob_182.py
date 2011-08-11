#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 182
#
# RSA encryption
#
# The RSA encryption is based on the following procedure:
# 
# Generate two distinct primes p and q.
# Compute n = pq and phi = (p-1)(q-1).
# Find an integer e, 1 < e < phi, such that gcd(e,phi) = 1.
# 
# A message in this system is a number in the interval [0,n-1].
# A text to be encrypted is then somehow converted to messages
# (numbers in the interval [0,n-1]).
# To encrypt the text, for each message, m, c = m^e mod n is
# calculated.
# 
# To decrypt the text, the following procedure is needed: calculate d
# such that ed = 1 mod phi, then for each encrypted message, c,
# calculate m = c^d mod n.
#
# There exist values of e and m such that m^e mod n = m.
# We call messages m for which m^e mod n = m unconcealed messages.
#
# An issue when choosing e is that there should not be too many
# unconcealed messages.
# For instance, let p = 19 and q = 37.
# Then n = 19*37 = 703 and phi = 18*36 = 648.
# If we choose e = 181, then, although gcd(181,648) = 1 it turns out
# that all possible messages m (0 <= m <= n-1) are unconcealed when
# calculating me mod n.
#
# For any valid choice of e there exist some unconcealed messages.
# It's important that the number of unconcealed messages is at a
# minimum.
#
# Choose p = 1009 and q = 3643.
# Find the sum of all values of e, 1 < e < phi(1009,3643) and
# gcd(e,phi) = 1, so that the number of unconcealed messages for this
# value of e is at a minimum.
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

########################################
def odd(n):
    if (n % 2):  return True
    else:        return False

########################################
def gcd(a,b):
    if (b > a):
        a,b = b,a
    while b:
        a, b = b, a%b
    return a

########################################
def encrypt(m,e,n):
    m_e = 1
    while e:
        if odd(e):
            m_e = (m_e * m) % n
            e -= 1
        else:
            m = (m*m)%n
            e /= 2
    return m_e

########################################
p,q = 1009,3643
n = p*q
phi = (p-1)*(q-1)

best_unconcealed = n
best_count = 0
answer = 0
print "best_unconcealed = {0}".format(best_unconcealed)

for e in xrange(2,phi/10000):
    if (gcd(e,phi) != 1):  continue

    print "(p,q) = ({0},{1}), n={2}, phi={3}, e={4}".format(p,q,n,phi,e),

    unconcealed = 0
    for m in xrange(n):
        if (encrypt(m,e,n) == m):
            unconcealed += 1
        if (unconcealed > best_unconcealed):
            break

    if (unconcealed == best_unconcealed):
        best_count += 1
        answer += e
        print "    unconcealed={0}, match previous best, count={1}, answer={2}".format(unconcealed, best_count, answer)
    elif (unconcealed < best_unconcealed):
        best_count = 1
        best_unconcealed = unconcealed
        answer = e
        print "    unconcealed={0}, new best, count={1}, answer={2}".format(unconcealed, best_count, answer)
    else:
        print "    unconcealed={0}".format(unconcealed)

print "Answer =", answer
print "Time taken = {0} seconds".format(time.clock() - start_time)
