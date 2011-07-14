#!/usr/bin/python
#
# Project Euler.net Problem 120
# 
# Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.
# 
# For example, if a = 7 and n = 3, then
#
#     r = 42: 6^3 + 8^3 = 728 == 42 mod 49.
#
# And as n varies, so too will r, but for a = 7 it turns out that
# max(r) = 42.
# 
# For 3 <= a <= 1000, find sum(max(r)).
#
# Solved 09/11/10
# 124 problems solved
# Position #607 on level 3

############################################################
#
# If n is even, then, by the binomial expansion...
#
#     (a-1)^n = a^n - C(1,n)*a^(n-1) + C(2,n)*a^(n-2) - ... + C(n-2,n)*a^2 - C(n-1,n)*a + 1
#     (a+1)^n = a^n + C(1,n)*a^(n-1) + C(2,n)*a^(n-2) - ... + C(n-2,n)*a^2 + C(n-1,n)*a + 1
#
# so
#
#     (a-1)^n + (a-1)^n = 2*(a^n + C(2,n)a^(n-2) + ... + C(n-2,n)*a^2 + 1)
#
# and
#
#     ((a-1)^n + (a-1)^n) modulus a^2 = 2
#
# If n is odd, then, by the binomial expansion...
#
#     (a-1)^n = a^n - C(1,n)*a^(n-1) + C(2,n)*a^(n-2) - ... - C(n-2,n)*a^2 + C(n-1,n)*a - 1
#     (a+1)^n = a^n + C(1,n)*a^(n-1) + C(2,n)*a^(n-2) - ... + C(n-2,n)*a^2 + C(n-1,n)*a + 1
#
# so
#
#     (a-1)^n + (a-1)^n = 2*(a^n + C(2,n)a^(n-2) + ... + C(n-3,n)*a^3 + C(n-1,n)*a)
#
# and
#
#     ((a-1)^n + (a-1)^n) modulus a^2 = (2a*(1 + B(2,n) + ... + B(n-3,n) + B(n-1,n))) modulus a^2
#
# I'm not sure how to prove it, but by experimentation...
#
#     (a-1)^2a modulus a^2 = 1
#     (a+1)^2a modulus a^2 = 1
# so
#     (a-1)^(2a+n) modulus a^2 = (a-1)^2a modulus a^2 * (a-1)^n modulus a^2
#                              = (a-1)^n modulus a^2
# and similarily
#     (a+1)^(2a+n) modulus a^2 = (a-1)^n modulus a^2
#
# So we don't need to check n = multiples of 2, as r is always = 2
# and we dont' need to check n > 2a, as these are just repeats of n <= 2a

MAX = 1000

answer = 0
for a in range(3, MAX+1):
    rmax = 0 
    print "a = {0}:".format(a)
    for n in range(1, a*2, 2):
        r = ((a-1)**n + (a+1)**n) % (a**2)
        if (r > rmax):  rmax = r
        #print "    n = {1}, r = {2}, rmax = {3}".format(a, n, r, rmax)
    answer += rmax


print "(MAX = {0}) answer = {1}".format(MAX, answer)

#for a in range(3, 100):
#    print "a = {0}: ((a-1)^2a) % a^2 = {1}, ((a+1)^2a) % a^2 = {2}".format(a, (a-1)**(2*a)%(a**2), (a+1)**(2*a)%(a**2))
    
