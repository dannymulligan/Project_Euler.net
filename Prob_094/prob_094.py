#!/usr/bin/python
#
# Project Euler.net Problem 94
#
# It is easily proved that no equilateral triangle exists with
# integral length sides and integral area. However, the almost
# equilateral triangle 5-5-6 has an area of 12 square units.
# 
# We shall define an almost equilateral triangle to be a triangle for
# which two sides are equal and the third differs by no more than one
# unit.
# 
# Find the sum of the perimeters of all almost equilateral triangles
# with integral side lengths and area and whose perimeters do not
# exceed one billion (1,000,000,000).
#

# From http://en.wikipedia.org/wiki/Triangle
#
# Area of a triangle with sides of length A, B, & C
#     S = sqrt(s * (s - A) * (s - B) * (s - C))
# where s = (A + B + C)/2
#
# From: http://en.wikipedia.org/wiki/Heronian_triangle
#
# The following formulas generate all Heronian triangles:
# 
#     a = n * (m^2 + k^2)
#     b = m * (n^2 + k^2)
#     c = (m + n) * (m * n - k^2)
# 
# where m,n, and k are rational numbers, and where a, b and c are now the side lengths [1]
#
# From: http://mathworld.wolfram.com/HeronianTriangle.html
#
# A Heronian triangle is a triangle having rational side lengths and
# rational area. The triangles are so named because such triangles are
# related to Heron's formula
#
#     Delta=sqrt(s(s-a)(s-b)(s-c))      
# 
# giving a triangle area Delta in terms of its side lengths a, b, c
# and semiperimeter s=(a+b+c)/2. Finding a Heronian triangle is
# therefore equivalent to solving the Diophantine equation
#
#     Delta^2=s(s-a)(s-b)(s-c).
# 
# The complete set of solutions for integer Heronian triangles (the
# three side lengths and area can be multiplied by their least common
# multiple to make them all integers) were found by Euler (Buchholz
# 1992; Dickson 2005, p. 193), and parametric versions were given by
# Brahmagupta and Carmichael (1952) as
#
#     a     = n * (m^2 + k^2)      
#     b     = m * (n^2 + k^2)      
#     c     = (m + n) * (mn - k^2)   
#     s     = mn * (m + n) 
#     Delta = kmn * (m + n) * (mn - k^2).       
# 
# This produces one member of each similarity class of Heronian
# triangles for any integers m, n, and k such that GCD(m,n,k)=1,
# mn>k^2>=m^2n/(2m+n), and m>=n>=1 (Buchholz 1992).
#
# Heronian Triangles
# 
# The first few integer Heronian triangles sorted by increasing
# maximal side lengths, are ((3, 4, 5), (5, 5, 6), (5, 5, 8), (6, 8,
# 10), (10, 10, 12), (5, 12, 13), (10, 13, 13), (9, 12, 15), (4, 13,
# 15), (13, 14, 15), (10, 10, 16), ... (Sloane's A055594, A055593, and
# A055592), having areas 6, 12, 12, 24, 48, 30, 60, 54, ... (Sloane's
# A055595).
#
# From: http://www.research.att.com/~njas/sequences/A102341
#
#     (5, 5, 6)               perimeter = 
#     (17, 17, 16)            perimeter =
#     (65, 65, 66)            perimeter =
#     (241, 241, 240)         perimeter =
#     (901, 901, 902)         perimeter =
#     (46816, 46817, 46817)   perimeter =
#     (174725, 174725, 174726)
#     (652080, 652081, 652081)
#     (2433601, 2433601, 2433602)
#

def gcd2 (a, b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

def gcd3 (a, b, c):
    return gcd2(gcd2(a,b), c)

def area(a,b,c):
    s = (a + b + c)/2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return int(area)


LIMIT = 50

for m in range(1,LIMIT):
    for n in range(1,LIMIT):
        for k in range(1,LIMIT):
            print "{0}".format((m,n,k)),
            if (gcd3(m,n,k) != 1):
                print "Failed GCD test - gcd3{0} = {1}".format((m,n,k),gcd3(m,n,k))
                continue
            if ~(m*n > k*k >= m*m*n/(2*m+n)):
                print "Failed comparision test - {0} > {1} >= {2}".format(m*n, k*k, m*m*n/(2*m+n))
                continue
            a = n * (m*m + k*k)
            b = m * (n*n + k*k)
            c = (m + n) * (m * n - k*k)
            print "(m,n,k) = {0}, (a,b,c) = {1}, area = {2}".format((m,n,k), (a,b,c), area(a,b,c))

