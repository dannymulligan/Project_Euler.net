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
# similarily for X=-2, X=-3, etc.  So...
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



#
# Any Pn with D(0)=0 will have Pn(0)=0, and so all values of N of the form
#
#     xxxx xxxx xxxx xxx0    has a integer root, because P(0) = 0
#
# Any Pn where the highest non-zero D(n) term is for an odd n will
# have a value for large negative X where D(n)*X^(n) will be more
# negative than any of the other terms, so these Pn's will have an
# integer root.
#
#     0000 0000 0000 00xx    always has a integer root, because (D(1)*X^1)<0 for X<0
#     0000 0000 0000 xxxx    always has a integer root, because (D(3)*X^3)<0 for X<0
#     0000 0000 00xx xxxx    always has a integer root, because (D(5)*X^5)<0 for X<0
#     0000 0000 xxxx xxxx    always has a integer root, because (D(7)*X^7)<0 for X<0
#     0000 00xx xxxx xxxx    always has a integer root, because (D(9)*X^9)<0 for X<0
#     0000 xxxx xxxx xxxx    always has a integer root, because (D(11)*X^11)<0 for X<0
#     00xx xxxx xxxx xxxx    always has a integer root, because (D(13)*X^13)<0 for X<0
#     xxxx xxxx xxxx xxxx    always has a integer root, because (D(15)*X^15)<0 for X<0
#
# The remaining cases have the have an even power of X as their largest
# coefficient, which means that for X<-10 this term will be positive
# and will dominate the lesser powers.
#
#
#     0000 0000 0000 000x    has a integer root if D(0)=0

#    Pn = D(n)*X^(n) + D(n-1)*X^(n-1) + ... + D(1)*X + D(0)
#    d(Pn)/ds = Pn' = n*D(n)*X^(n-1) + (n-1)D(n-1)*X^(n-2) + ... + D(1)


#     0000 0000 000x xxxx    has a integer root, because Pn(-10) < 0
#     0000 0000 0xxx xxxx    has a integer root, because Pn(-10) < 0
#     0000 000x xxxx xxxx    has a integer root, because Pn(-10) < 0
#     0000 0xxx xxxx xxxx    has a integer root, because Pn(-10) < 0
#     000x xxxx xxxx xxxx    has a integer root, because Pn(-10) < 0
#     0xxx xxxx xxxx xxxx    has a integer root, because Pn(-10) < 0

# ############################################################
# # Number of possibilities
#
# # Possibilities in the range: 0000 0000 0000 0000
# p_0000_0000_0000_0000 = 1
#
# # Possibilities in the range: 0000 0000 0000 000x
# p_0000_0000_0000_000x = 9
# # Possibilities in the range: 0000 0000 0000 00xx
# p_0000_0000_0000_00xx = 90
# # Possibilities in the range: 0000 0000 0000 0xxx
# p_0000_0000_0000_0xxx = 900
# # Possibilities in the range: 0000 0000 0000 xxxx
# p_0000_0000_0000_xxxx = 9000
#
# # Possibilities in the range: 0000 0000 000x xxxx
# p_0000_0000_000x_xxxx = 90000
# # Possibilities in the range: 0000 0000 00xx xxxx
# p_0000_0000_00xx_xxxx = 900000
# # Possibilities in the range: 0000 0000 0xxx xxxx
# p_0000_0000_0xxx_xxxx = 9000000
# # Possibilities in the range: 0000 0000 xxxx xxxx
# p_0000_0000_xxxx_xxxx = 90000000
#
# # Possibilities in the range: 0000 000x xxxx xxxx
# p_0000_000x_xxxx_xxxx = 900000000
# # Possibilities in the range: 0000 00xx xxxx xxxx
# p_0000_00xx_xxxx_xxxx = 9000000000
# # Possibilities in the range: 0000 0xxx xxxx xxxx
# p_0000_0xxx_xxxx_xxxx = 90000000000
# # Possibilities in the range: 0000 xxxx xxxx xxxx
# p_0000_xxxx_xxxx_xxxx = 900000000000
#
# # Possibilities in the range: 000x xxxx xxxx xxxx
# p_000x_xxxx_xxxx_xxxx = 9000000000000
# # Possibilities in the range: 00xx xxxx xxxx xxxx
# p_00xx_xxxx_xxxx_xxxx = 90000000000000
# # Possibilities in the range: 0xxx xxxx xxxx xxxx
# p_0xxx_xxxx_xxxx_xxxx = 900000000000000
# # Possibilities in the range: xxxx xxxx xxxx xxxx
# p_xxxx_xxxx_xxxx_xxxx = 9000000000000000
#
#
# ############################################################
# # Print the number of possibilities
# print "p_0000_0000_0000_0000 =", p_0000_0000_0000_0000
#
# print "p_0000_0000_0000_000x =", p_0000_0000_0000_000x
# print "p_0000_0000_0000_00xx =", p_0000_0000_0000_00xx
# print "p_0000_0000_0000_0xxx =", p_0000_0000_0000_0xxx
# print "p_0000_0000_0000_xxxx =", p_0000_0000_0000_xxxx
#
# print "p_0000_0000_000x_xxxx =", p_0000_0000_000x_xxxx
# print "p_0000_0000_00xx_xxxx =", p_0000_0000_00xx_xxxx
# print "p_0000_0000_0xxx_xxxx =", p_0000_0000_0xxx_xxxx
# print "p_0000_0000_xxxx_xxxx =", p_0000_0000_xxxx_xxxx
#
# print "p_0000_000x_xxxx_xxxx =", p_0000_000x_xxxx_xxxx
# print "p_0000_00xx_xxxx_xxxx =", p_0000_00xx_xxxx_xxxx
# print "p_0000_0xxx_xxxx_xxxx =", p_0000_0xxx_xxxx_xxxx
# print "p_0000_xxxx_xxxx_xxxx =", p_0000_xxxx_xxxx_xxxx
#
# print "p_000x_xxxx_xxxx_xxxx =", p_000x_xxxx_xxxx_xxxx
# print "p_00xx_xxxx_xxxx_xxxx =", p_00xx_xxxx_xxxx_xxxx
# print "p_0xxx_xxxx_xxxx_xxxx =", p_0xxx_xxxx_xxxx_xxxx
# print "p_xxxx_xxxx_xxxx_xxxx =", p_xxxx_xxxx_xxxx_xxxx
#
#
# ############################################################
# # Number of roots
#
# # Roots in the range: 0000 0000 0000 0000
# r_0000_0000_0000_0000 = p_0000_0000_0000_0000
# # If P0 is allowed, then it has a root
# # But might not be allowed, need to check both possibilities
#
# # Roots in the range: 0000 0000 0000 000x
# r_0000_0000_0000_000x = 0
# # if D(0) > 0, then no root possible
#
# # Roots in the range: 0000 0000 0000 00xx
# r_0000_0000_0000_00xx = p_0000_0000_0000_00xx
#
# # Roots in the range: 0000 0000 0000 0xxx
# r_0000_0000_0000_0xxx = 10+20+30+40+50+60+70+80+90
# # 0000_0000_0000_010x are root = 10
# # 0000_0000_0000_021x +
# # 0000_0000_0000_020x are root = 20
# # ...etc...
# # 0000_0000_0000_098x +
# # 0000_0000_0000_097x +
# # 0000_0000_0000_096x +
# # 0000_0000_0000_095x +
# # 0000_0000_0000_094x +
# # 0000_0000_0000_093x +
# # 0000_0000_0000_092x +
# # 0000_0000_0000_091x +
# # 0000_0000_0000_090x are root = 90
# r_0000_0000_0000_0xxx += 9+8+7+6+5+4+3+2+1
# # 10% of 0000_0000_0000_011x to 0000_0000_0000_019x are root = 9
# # 10% of 0000_0000_0000_022x to 0000_0000_0000_029x are root = 8
# # 10% of 0000_0000_0000_033x to 0000_0000_0000_039x are root = 7
# # 10% of 0000_0000_0000_044x to 0000_0000_0000_049x are root = 6
# # 10% of 0000_0000_0000_055x to 0000_0000_0000_059x are root = 5
# # 10% of 0000_0000_0000_066x to 0000_0000_0000_069x are root = 4
# # 10% of 0000_0000_0000_077x to 0000_0000_0000_079x are root = 3
# # 10% of 0000_0000_0000_088x to 0000_0000_0000_089x are root = 2
# # 10% of 0000_0000_0000_099x are root = 1
#
# # Roots in the range: 0000 0000 0000 xxxx
# r_0000_0000_0000_xxxx = p_0000_0000_0000_xxxx
#
# # Roots in the range: 0000 0000 000x xxxx
# r_0000_0000_000x_xxxx = 1000+2000+3000+4000+5000+6000+7000+8000+9000
# # 0000_0000_0001_0xxx are root = 1000
# # 0000_0000_0002_1xxx +
# # 0000_0000_0002_0xxx are root = 2000
# # ...etc...
# # 0000_0000_0009_8xxx +
# # 0000_0000_0009_7xxx +
# # 0000_0000_0009_6xxx +
# # 0000_0000_0009_5xxx +
# # 0000_0000_0009_4xxx +
# # 0000_0000_0009_3xxx +
# # 0000_0000_0009_2xxx +
# # 0000_0000_0009_1xxx +
# # 0000_0000_0009_0xxx are root = 9000
# r_0000_0000_0000_0xxx += 900+800+700+600+500+400+300+200+100
# # 10% of 0000_0000_0001_1xxx to 0000_0000_0001_9xxx are root = 900
# # 10% of 0000_0000_0002_2xxx to 0000_0000_0002_9xxx are root = 800
# # 10% of 0000_0000_0003_3xxx to 0000_0000_0003_9xxx are root = 700
# # 10% of 0000_0000_0004_4xxx to 0000_0000_0004_9xxx are root = 600
# # 10% of 0000_0000_0005_5xxx to 0000_0000_0005_9xxx are root = 500
# # 10% of 0000_0000_0006_6xxx to 0000_0000_0006_9xxx are root = 400
# # 10% of 0000_0000_0007_7xxx to 0000_0000_0007_9xxx are root = 300
# # 10% of 0000_0000_0008_8xxx to 0000_0000_0008_9xxx are root = 200
# # 10% of 0000_0000_0009_9xxx are root = 100
#
# # Roots in the range: 0000 0000 00xx xxxx
# r_0000_0000_00xx_xxxx = p_0000_0000_00xx_xxxx
#
# # Roots in the range: 0000 0000 0xxx xxxx
# r_0000_0000_0xxx_xxxx = 0
#
# # Roots in the range: 0000 0000 xxxx xxxx
# r_0000_0000_xxxx_xxxx = p_0000_0000_xxxx_xxxx
#
# # Roots in the range: 0000 000x xxxx xxxx
# r_0000_000x_xxxx_xxxx = 0
# # Roots in the range: 0000 00xx xxxx xxxx
# r_0000_00xx_xxxx_xxxx = p_0000_00xx_xxxx_xxxx
# # Roots in the range: 0000 0xxx xxxx xxxx
# r_0000_0xxx_xxxx_xxxx = 0
# # Roots in the range: 0000 xxxx xxxx xxxx
# r_0000_xxxx_xxxx_xxxx = p_0000_xxxx_xxxx_xxxx
#
# # Roots in the range: 000x xxxx xxxx xxxx
# r_000x_xxxx_xxxx_xxxx = 0
# # Roots in the range: 00xx xxxx xxxx xxxx
# r_00xx_xxxx_xxxx_xxxx = p_00xx_xxxx_xxxx_xxxx
# # Roots in the range: 0xxx xxxx xxxx xxxx
# r_0xxx_xxxx_xxxx_xxxx = 0
# # Roots in the range: xxxx xxxx xxxx xxxx
# r_xxxx_xxxx_xxxx_xxxx = p_xxxx_xxxx_xxxx_xxxx
#
#
# ############################################################
# # Print the number of roots
# print "r_0000_0000_0000_0000 =", r_0000_0000_0000_0000
#
# print "r_0000_0000_0000_000x =", r_0000_0000_0000_000x
# print "r_0000_0000_0000_00xx =", r_0000_0000_0000_00xx
# print "r_0000_0000_0000_0xxx =", r_0000_0000_0000_0xxx
# print "r_0000_0000_0000_xxxx =", r_0000_0000_0000_xxxx
#
# print "r_0000_0000_000x_xxxx =", r_0000_0000_000x_xxxx
# print "r_0000_0000_00xx_xxxx =", r_0000_0000_00xx_xxxx
# print "r_0000_0000_0xxx_xxxx =", r_0000_0000_0xxx_xxxx
# print "r_0000_0000_xxxx_xxxx =", r_0000_0000_xxxx_xxxx
#
# print "r_0000_000x_xxxx_xxxx =", r_0000_000x_xxxx_xxxx
# print "r_0000_00xx_xxxx_xxxx =", r_0000_00xx_xxxx_xxxx
# print "r_0000_0xxx_xxxx_xxxx =", r_0000_0xxx_xxxx_xxxx
# print "r_0000_xxxx_xxxx_xxxx =", r_0000_xxxx_xxxx_xxxx
#
# print "r_000x_xxxx_xxxx_xxxx =", r_000x_xxxx_xxxx_xxxx
# print "r_00xx_xxxx_xxxx_xxxx =", r_00xx_xxxx_xxxx_xxxx
# print "r_0xxx_xxxx_xxxx_xxxx =", r_0xxx_xxxx_xxxx_xxxx
# print "r_xxxx_xxxx_xxxx_xxxx =", r_xxxx_xxxx_xxxx_xxxx
#
#
# ############################################################
# # Calculate the answer
#
# # Reduced problem
# reduced_answer  = r_0000_0000_0000_0000
# reduced_answer += r_0000_0000_0000_000x + r_0000_0000_0000_00xx + r_0000_0000_0000_0xxx + r_0000_0000_0000_xxxx
# reduced_answer += r_0000_0000_000x_xxxx
# reduced_answer += 1  # Add one extra because 10^5 has a root
# print "It can be verified that Z(100,000) is 14696."
# print "Z(100,000) =", reduced_answer
# print "Error =", 14696-reduced_answer
#
# # Full size problem
# full_answer  = r_0000_0000_0000_0000
# full_answer += r_0000_0000_0000_000x + r_0000_0000_0000_00xx + r_0000_0000_0000_0xxx + r_0000_0000_0000_xxxx
# full_answer += r_0000_0000_000x_xxxx + r_0000_0000_00xx_xxxx + r_0000_0000_0xxx_xxxx + r_0000_0000_xxxx_xxxx
# full_answer += r_0000_000x_xxxx_xxxx + r_0000_00xx_xxxx_xxxx + r_0000_0xxx_xxxx_xxxx + r_0000_xxxx_xxxx_xxxx
# full_answer += r_000x_xxxx_xxxx_xxxx + r_00xx_xxxx_xxxx_xxxx + r_0xxx_xxxx_xxxx_xxxx + r_xxxx_xxxx_xxxx_xxxx
# # Don't add one extra because 10^16 does not have a root
# print "Z(10^16) =", full_answer




def p(X, D):
    res = 0
    pow = len(D)-1
    for i in D:
        res += i*(X**pow)
        pow -= 1
        #print pow, i*(X**pow), res
    return res

# root_count = 0
# for i in range(0,100000):
#     Ds = list(str(i))
#     D = []
#     for j in Ds:
#         D.append(int(j))
#     p_m10 = p(-10,D)
#     p_0 = p(0,D)
#     p_p10  = p(10,D)
#     root_exists1 = (((p_m10 <= 0) and (p_p10 > 0)) or (p_0 == 0))
#     if (root_exists1):
#         root_count += 1
#         print "For P{0}, P{0}(-10)={1}, P{0}(0)={2}, P{0}(10)={3}, root_count={4}".format(i, p_m10, p_0, p_p10, root_count)
#
# print "Total roots found =", root_count
# print

possible_count = 0
total_root_count = 0
root_count = 0
root_count2 = 0
root_count3 = 0
root_count4 = 0
line_count = 11
for i in range(1,10000001):
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


    if ((line_count % 11) == 0):
        print "           10 9 8 7 6 5 4 3 2 1 0"
        line_count = 1

    if (root_known):  total_root_count += 1

    if (root_count > 1):
        if (root_count == 2):  root_count2 += 1
        if (root_count == 3):  root_count3 += 1
        if (root_count > 3):   root_count4 += 1
        line_count += 1
        print "For P{0:-5} ".format(i),
        for j in range(-10,1):
            if (p(j,D) == 0):
                print "R",
            else:
                print " ",
        print

print "Total roots found =", total_root_count
print "out of a possible", possible_count
print "Functions that have a root at 2 X values =", root_count2
print "Functions that have a root at 3 X values =", root_count3
print "Functions that have a root at >3 X values =", root_count4

# # Find differences
# diff_count = 0
# for i in range(0,100000):
#     Ds = list(str(i))
#     D = []
#     for j in Ds:
#         D.append(int(j))
#
#     p_m10 = p(-10,D)
#     p_0 = p(0,D)
#     p_p10  = p(10,D)
#     root_exists1 = (((p_m10 <= 0) and (p_p10 > 0)) or (p_0 == 0))
#
#     root_exists2 = False
#     for j in range(-10,11):
#         if (p(j,D) == 0):
#             root_exists2 = True
#             root = j
#             break
#
#     if (root_exists1 & ~root_exists2):
#         print "1: Difference found for P{0} root_exists1 & ~root_exists2".format(i)
#         diff_count += 1
#
# print "Total differences =", diff_count
