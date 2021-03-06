#!/usr/bin/python
#
# Project Euler.net Problem 61
#
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal
# numbers are all figurate (polygonal) numbers and are generated by
# the following formulae:
#
#     Triangle      P(3,n) = n(n+1)/2     1, 3, 6, 10, 15, ...
#     Square        P(4,n) = n^(2)        1, 4, 9, 16, 25, ...
#     Pentagonal    P(5,n) = n(3n-1)/2    1, 5, 12, 22, 35, ...
#     Hexagonal     P(6,n) = n(2n-1)      1, 6, 15, 28, 45, ...
#     Heptagonal    P(7,n) = n(5n-3)/2    1, 7, 18, 34, 55, ...
#     Octagonal     P(8,n) = n(3n-2)      1, 8, 21, 40, 65, ...
#
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has
# three interesting properties.
#
# 1. The set is cyclic, in that the last two digits of each number is
# the first two digits of the next number (including the last number
# with the first).
#
#  2. Each polygonal type: triangle (P(3,127)=8128), square
# (P(4,91)=8281), and pentagonal (P(5,44)=2882), is represented by a
# different number in the set.
#
# 3. This is the only set of 4-digit numbers with this property.
#
# Find the sum of the only ordered set of six cyclic 4-digit numbers
# for which each polygonal type: triangle, square, pentagonal,
# hexagonal, heptagonal, and octagonal, is represented by a different
# number in the set.
#

import sys

def p3 (n):
    return n*(n+1)/2
def p4 (n):
    return n**2
def p5 (n):
    return n*(3*n-1)/2
def p6 (n):
    return n*(2*n-1)
def p7 (n):
    return n*(5*n-3)/2
def p8 (n):
    return n*(3*n-2)

def self_test():
    print "Running self_test()"

    s3 = s4 = s5 = s6 = s7 = s8 = ""
    for i in range (1,6):
        if (i > 1):
            s3 += ", "
            s4 += ", "
            s5 += ", "
            s6 += ", "
            s7 += ", "
            s8 += ", "
        s3 += "{0}".format(p3(i))
        s4 += "{0}".format(p4(i))
        s5 += "{0}".format(p5(i))
        s6 += "{0}".format(p6(i))
        s7 += "{0}".format(p7(i))
        s8 += "{0}".format(p8(i))
    s3 += ", ..."
    s4 += ", ..."
    s5 += ", ..."
    s6 += ", ..."
    s7 += ", ..."
    s8 += ", ..."

    failed = False
    if (s3 == "1, 3, 6, 10, 15, ..." ):
        print "P(3,n) = {0}".format(s3)
    else:
        print "ERROR: Self test failed check of p3()"
        failed = True

    if (s4 == "1, 4, 9, 16, 25, ..." ):
        print "P(4,n) = {0}".format(s4)
    else:
        print "ERROR: Self test failed check of p4()"
        failed = True

    if (s5 == "1, 5, 12, 22, 35, ..."):
        print "P(5,n) = {0}".format(s5)
    else:
        print "ERROR: Self test failed check of p5()"
        failed = True

    if (s6 == "1, 6, 15, 28, 45, ..."):
        print "P(6,n) = {0}".format(s6)
    else:
        print "ERROR: Self test failed check of p6()"
        failed = True

    if (s7 == "1, 7, 18, 34, 55, ..."):
        print "P(7,n) = {0}".format(s7)
    else:
        print "ERROR: Self test failed check of p7()"
        failed = True

    if (s8 == "1, 8, 21, 40, 65, ..."):
        print "P(8,n) = {0}".format(s8)
    else:
        print "ERROR: Self test failed check of p8()"
        failed = True

    if (failed):
        print "ERROR: self_test() failed"
    else:
        print "self_test() passed"


self_test()

# Make list of all of the 4 digit numbers
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
la = []
for i in range(150):
    if ((p3(i) > 999) & (p3(i) < 10000) & ((p3(i) % 100) >= 10)):
        l3.append(p3(i))
        la.append(p3(i))
    if ((p4(i) > 999) & (p4(i) < 10000) & ((p4(i) % 100) >= 10)):
        l4.append(p4(i))
        la.append(p4(i))
    if ((p5(i) > 999) & (p5(i) < 10000) & ((p5(i) % 100) >= 10)):
        l5.append(p5(i))
        la.append(p5(i))
    if ((p6(i) > 999) & (p6(i) < 10000) & ((p6(i) % 100) >= 10)):
        l6.append(p6(i))
        la.append(p6(i))
    if ((p7(i) > 999) & (p7(i) < 10000) & ((p7(i) % 100) >= 10)):
        l7.append(p7(i))
        la.append(p7(i))
    if ((p8(i) > 999) & (p8(i) < 10000) & ((p8(i) % 100) >= 10)):
        l8.append(p8(i))
        la.append(p8(i))


print "There are {0} 4-digit p(3,n) numbers that can chain.".format(len(l3))
print "There are {0} 4-digit p(4,n) numbers that can chain.".format(len(l4))
print "There are {0} 4-digit p(5,n) numbers that can chain.".format(len(l5))
print "There are {0} 4-digit p(6,n) numbers that can chain.".format(len(l6))
print "There are {0} 4-digit p(7,n) numbers that can chain.".format(len(l7))
print "There are {0} 4-digit p(8,n) numbers that can chain.".format(len(l8))
dup = len(l3) + len(l4) + len(l5) + len(l6) + len(l7) + len(l8) - len(la)
print "{0} 4-digit numbers total (not counting {1} duplicates)".format(len(la), dup)

for i0 in l8:
    t0 = 'p8'
    b1 = (i0 % 100) * 100

    for i1 in range(b1, b1+100):
        if (i1 in la):
            if   (i1 in l8):  t1 = 'p8'
            elif (i1 in l7):  t1 = 'p7'
            elif (i1 in l6):  t1 = 'p6'
            elif (i1 in l5):  t1 = 'p5'
            elif (i1 in l4):  t1 = 'p4'
            elif (i1 in l3):  t1 = 'p3'

            #print "-22-: {0}={1}, {2}={3}".format(t0,i0, t1,i1)
            b2 = (i1 % 100) * 100

            for i2 in range(b2, b2+100):
                if (i2 in la):
                    if   (i2 in l8):  t2 = 'p8'
                    elif (i2 in l7):  t2 = 'p7'
                    elif (i2 in l6):  t2 = 'p6'
                    elif (i2 in l5):  t2 = 'p5'
                    elif (i2 in l4):  t2 = 'p4'
                    elif (i2 in l3):  t2 = 'p3'

                    #print "-333-: {0}={1}, {2}={3}, {4}={5}".format(t0,i0, t1,i1, t2,i2)
                    b3 = (i2 % 100) * 100

                    for i3 in range(b3, b3+100):
                        if (i3 in la):
                            if   (i3 in l8):  t3 = 'p8'
                            elif (i3 in l7):  t3 = 'p7'
                            elif (i3 in l6):  t3 = 'p6'
                            elif (i3 in l5):  t3 = 'p5'
                            elif (i3 in l4):  t3 = 'p4'
                            elif (i3 in l3):  t3 = 'p3'

                            #print "-4444-: {0}={1}, {2}={3}, {4}={5}, {6}={7}".format(t0,i0, t1,i1, t2,i2, t3,i3)
                            b4 = (i3 % 100) * 100

                            for i4 in range(b4, b4+100):
                                if (i4 in la):
                                    if   (i4 in l8):  t4 = 'p8'
                                    elif (i4 in l7):  t4 = 'p7'
                                    elif (i4 in l6):  t4 = 'p6'
                                    elif (i4 in l5):  t4 = 'p5'
                                    elif (i4 in l4):  t4 = 'p4'
                                    elif (i4 in l3):  t4 = 'p3'

                                    #print "-55555-: {0}={1}, {2}={3}, {4}={5}, {6}={7}, {8}={9}".format(t0,i0, t1,i1, t2,i2, t3,i3, t4,i4)
                                    b5 = (i4 % 100) * 100

                                    for i5 in range(b5, b5+100):
                                        if (i5 in la):
                                            if   (i5 in l8):  t5 = 'p8'
                                            elif (i5 in l7):  t5 = 'p7'
                                            elif (i5 in l6):  t5 = 'p6'
                                            elif (i5 in l5):  t5 = 'p5'
                                            elif (i5 in l4):  t5 = 'p4'
                                            elif (i5 in l3):  t5 = 'p3'

                                            b6 = (i5 % 100) * 100

                                            for i6 in range(b6, b6+100):
                                                if (i6 == i0):
                                                    temp = [t0, t1, t2, t3, t4, t5]  # t0 already known to be 'p(8,n)'
                                                    if (('p7' in temp) & ('p6' in temp) & ('p5' in temp) & ('p4' in temp) & ('p3' in temp)):
                                                        print "Found: {0}={1}, {2}={3}, {4}={5}, {6}={7}, {8}={9}, {10}={11}, sum={12}".format(t0,i0, t1,i1, t2,i2, t3,i3, t4,i4, t5,i5, (i0+i1+i2+i3+i4+i5))
                                                        sys.exit(0)
