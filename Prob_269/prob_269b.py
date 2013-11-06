#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 269
#
# Polynomials with at least one integer root
#
# A root or zero of a polynomial P(x) is a solution to the equation
# P(x) = 0.  Define Pn as the polynomial whose coefficients are the
# digits of n.  For example, P5703(x) = 5x^3 + 7x^2 + 3.
#
# We can see that:
#
#     * Pn(0) is the last digit of n,
#     * Pn(1) is the sum of the digits of n,
#     * Pn(10) is n itself.
#
# Define Z(k) as the number of positive integers, n, not exceeding k
# for which the polynomial Pn has at least one integer root.
#
# It can be verified that Z(100,000) is 14696.
#
# What is Z(10^16)?
#
# Solved ??/??/09
# ?? problems solved
# Position #??? on level ?

# Notes from my own discoveries...
#
# "for which the polynomial has at least one integer root" means an
# integer value of X such that Pn(X) = 0.  A non integer X that solves
# Pn(X) = 0 doesn't count.
#
# P0 is not a polynomial
#
# Z(10) = 1
# Z(100) = 33
# Z(1,000) = 172
# Z(10,000) = 1,754
# Z(100,000) = 14,696
# Z(1,000,000) = 152,960
# Z(10,000,000) = 1,393,262

# For a polynomial...
#
#    Pn = D(n)*X^(n) + D(n-1)*X^(n-1) + ... + D(1)*X + D(0)
#
# Pn(X) is always > 0 for X>0, so there are no roots for X>0
#
# For X<=-10, the highest term will always be larger than all previous
# terms combined, so it is not possible to have any roots for X<=-10
#
# Pn(0)=0 if (D[0]==0)
# For X=-1, Pn(-1)=D[n]*(-1^n) + D[n-1]*(-1^(n-1)) + ... + D[1]*(-1^1) + D[0]*(-1^0)
#     so Pn(-1)=0 if (D[n]*(-1^n) + D[n-1]*(-1^(n-1)) + ... + D[1]*(-1^1) + D[0]*(-1^0)) == 0)
# similarly for X=-2, X=-3, etc.  So...
#
# Pn(0)=0  if (D[0] == 0):
# Pn(-1)=0 if (((D[n]*-1**n) + (D[n-1]*-1**(n-1)) + ... + D[1]*-1**1 + D[0]*-1**0) == 0)
# Pn(-2)=0 if (((D[n]*-2**n) + (D[n-1]*-2**(n-1)) + ... + D[1]*-2**1 + D[0]*-2**0) == 0)
# Pn(-3)=0 if (((D[n]*-3**n) + (D[n-1]*-3**(n-1)) + ... + D[1]*-3**1 + D[0]*-3**0) == 0)
# Pn(-4)=0 if (((D[n]*-4**n) + (D[n-1]*-4**(n-1)) + ... + D[1]*-4**1 + D[0]*-4**0) == 0)
# Pn(-5)=0 if (((D[n]*-5**n) + (D[n-1]*-5**(n-1)) + ... + D[1]*-5**1 + D[0]*-5**0) == 0)
# Pn(-6)=0 if (((D[n]*-6**n) + (D[n-1]*-6**(n-1)) + ... + D[1]*-6**1 + D[0]*-6**0) == 0)
# Pn(-7)=0 if (((D[n]*-7**n) + (D[n-1]*-7**(n-1)) + ... + D[1]*-7**1 + D[0]*-7**0) == 0)
# Pn(-8)=0 if (((D[n]*-8**n) + (D[n-1]*-8**(n-1)) + ... + D[1]*-8**1 + D[0]*-8**0) == 0)
# Pn(-9)=0 if (((D[n]*-9**n) + (D[n-1]*-9**(n-1)) + ... + D[1]*-9**1 + D[0]*-9**0) == 0)
# 
# So we need to count each of the above cases, then adjust for overlaps
#
# Experimentally, for Z(10,000,000), there are 2 Pn's that have roots
# at 4 values of X.  They are...
#          10 9 8 7 6 5 4 3 2 1 0
# P1561560                R R R R  (Roots at X=-3, X=-2, X=-1, & X=0)
# P1681680              R   R R R  (Roots at X=-4, X=-2, X=-1, & X=0)
#
# For Z(10,000,000), there are 313 Pn's that have roots at 3 values of X
# For Z(10,000,000), there are 59,199 Pn's that have roots at 2 values of X






def p(X, D):
    res = 0
    pow = len(D)-1
    for i in D:
        res += i*(X**pow)
        pow -= 1
        #print pow, i*(X**pow), res
    return res

possible_count = 0
total_root_count = 0
root_count = 0
root_count2 = 0
root_count3 = 0
root_count4 = 0
line_count = 11
for i in range(1,1001):
    possible_count += 1
    Ds = list(str(i))
    D = []
    for j in Ds:
        D.append(int(j))

    D0 = D1 = D2 = D3 = D4 = D5 = D6 = D7 = D8 = D9 = 0
    D0 = D[-1]
    if (len(D) > 1):  D1 = D[-2]
    if (len(D) > 2):  D2 = D[-3]
    if (len(D) > 3):  D3 = D[-4]
    if (len(D) > 4):  D4 = D[-5]
    if (len(D) > 5):  D5 = D[-6]
    if (len(D) > 6):  D6 = D[-7]
    if (len(D) > 7):  D7 = D[-8]
    if (len(D) > 8):  D8 = D[-9]
    if (len(D) > 9):  D9 = D[-9]
    if (len(D) > 10):
        print "Error"
        raise AssertionError

    root_known = False
    root_count = 0
    if ((i % 10) == 0):
        root_known = True  # Root at X=0
        root_count += 1
    if ((D0*1**0 - D1*1**1 + D2*1**2 - D3*1**3 + D4*1**4 - D5*1**5 + D6*1**6 - D7*1**7 + D8*1**8 - D9*1**9) == 0):
        root_known = True  # Root at X=-1
        root_count += 1
    if ((D0*2**0 - D1*2**1 + D2*2**2 - D3*2**3 + D4*2**4 - D5*2**5 + D6*2**6 - D7*2**7 + D8*2**8 - D9*2**9) == 0):
        root_known = True  # Root at X=-2
        root_count += 1
    if ((D0*3**0 - D1*3**1 + D2*3**2 - D3*3**3 + D4*3**4 - D5*3**5 + D6*3**6 - D7*3**7 + D8*3**8 - D9*3**9) == 0):
        root_known = True  # Root at X=-3
        root_count += 1
    if ((D0*4**0 - D1*4**1 + D2*4**2 - D3*4**3 + D4*4**4 - D5*4**5 + D6*4**6 - D7*4**7 + D8*4**8 - D9*4**9) == 0):
        root_known = True  # Root at X=-4
        root_count += 1
    if ((D0*5**0 - D1*5**1 + D2*5**2 - D3*5**3 + D4*5**4 - D5*5**5 + D6*5**6 - D7*5**7 + D8*5**8 - D9*5**9) == 0):
        root_known = True  # Root at X=-5
        root_count += 1
    if ((D0*6**0 - D1*6**1 + D2*6**2 - D3*6**3 + D4*6**4 - D5*6**5 + D6*6**6 - D7*6**7 + D8*6**8 - D9*6**9) == 0):
        root_known = True  # Root at X=-6
        root_count += 1
    if ((D0*7**0 - D1*7**1 + D2*7**2 - D3*7**3 + D4*7**4 - D5*7**5 + D6*7**6 - D7*7**7 + D8*7**8 - D9*7**9) == 0):
        root_known = True  # Root at X=-7
        root_count += 1
    if ((D0*8**0 - D1*8**1 + D2*8**2 - D3*8**3 + D4*8**4 - D5*8**5 + D6*8**6 - D7*8**7 + D8*8**8 - D9*8**9) == 0):
        root_known = True  # Root at X=-8
        root_count += 1
    if ((D0*9**0 - D1*9**1 + D2*9**2 - D3*9**3 + D4*9**4 - D5*9**5 + D6*9**6 - D7*9**7 + D8*9**8 - D9*9**9) == 0):
        root_known = True  # Root at X=-9
        root_count += 1


    if (root_known):  total_root_count += 1

    if (root_count > 1):
        if (root_count == 2):  root_count2 += 1
        if (root_count == 3):  root_count3 += 1
        if (root_count > 3):   root_count4 += 1
        print "For P{0:-5} ".format(i),
        for j in range(-10,1):
            if (p(j,D) == 0):
                print -j,
            else:
                print " ",
        print

print "Total roots found =", total_root_count
print "out of a possible", possible_count
print "Functions that have a root at 2 X values =", root_count2
print "Functions that have a root at 3 X values =", root_count3
print "Functions that have a root at >3 X values =", root_count4


## Calculate Pns from 1 to 10,
## Calculate Z 
#def Z(s, e, eqns):
#    # Return count of numbers between s[] and e[] inclusive
#    # for which one or more of the eqns are equal to 0
#    # s = list of digits, s[0] = least significant, s[n] = most significant
#    # e = list of digits, s[0] = least significant, s[n] = most significant
#    # eqns = list of eqn
#    # eqn = list of coefficients, eqn[0] = coeff to X^0, eqn[N] = coeff to X^N
#
#
#eqn0 = []
#
#z_100000 = Z([1], [0]*5+[1], [eqn0, eqn1, eqn2, eqn3, eqn4, eqn5, eqn6, eqn7, eqn8, eqn9])
