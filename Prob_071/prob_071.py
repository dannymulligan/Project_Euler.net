#!/usr/bin/python
#
# Project Euler.net Problem 71
#
# Consider the fraction, n/d, where n and d are positive integers. If
# n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# 
# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:
# 
#     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
#         5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 
# It can be seen that 2/5 is the fraction immediately to the left of
# 3/7.
#
# By listing the set of reduced proper fractions for d <= 1,000,000 in
# ascending order of size, find the numerator of the fraction
# immediately to the left of 3/7.
#
#
# Solved 10/24/09
# 86 problems solved
# Position #209 on level 2

LIMIT_D = 8
LIMIT_D = 1000
LIMIT_D = 1000000

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

bn = 1
bd = LIMIT_D
for d in range(1,LIMIT_D+1):
    if ((d % 7) == 0):
        n = ((3*d) / 7) - 1
    else:
        n = ((3*d) / 7)

    if (gcd(n,d) != 1): continue  # Eliminate because HCF(n,d) != 1

    # is n/d > bn/bd?
    # is (n)/(d) > (bn)/(bd)?
    # is (n*bd)/(d*bd) > (bn)/(bd)?
    # is (n*bd)/(d*bd) > (d*bn)/(d*bd)?
    # is (n*bd) > (d*bn)?
    if ((n*bd) > (d*bn)):
        (bn,bd) = (n,d)
        #print "Found {0}/{1}".format(n/gcd(n,d), d/gcd(n,d))

print "Answer = {0}/{1}".format(bn/gcd(bn,bd), bd/gcd(bn,bd))
