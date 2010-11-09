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
# Answer:

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

##def find_chain(len, n, chain, start):
##    i = (n % 100) * 100
##
##    if (len > 10):
##        print "ERROR: Length too long"
##        return False
##
##    found = False
##    if (i > 1000):
##        for j in range(i, i+100):
##            if j in la:
##                found = True
##                if (j == start):
##                    print "{0}    LOOP  chain length = {1}".format(chain, len)
##                    return True
##                else:
##                    find_chain(len+1, j, chain + [j], start)
##
##    if (found == False):
##        print "{0}    chain length = {1}".format(chain, len)
##
##    return True
        


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
##    if ((p6(i) > 999) & (p6(i) < 10000) & ((p6(i) % 100) >= 10)):
##        l6.append(p6(i))
##        la.append(p6(i))
##    if ((p7(i) > 999) & (p7(i) < 10000) & ((p7(i) % 100) >= 10)):
##        l7.append(p7(i))
##        la.append(p7(i))
##    if ((p8(i) > 999) & (p8(i) < 10000) & ((p8(i) % 100) >= 10)):
##        l8.append(p8(i))
##        la.append(p8(i))


print "There are {0} 4-digit p(3,n) numbers".format(len(l3))
print "There are {0} 4-digit p(4,n) numbers".format(len(l4))
print "There are {0} 4-digit p(5,n) numbers".format(len(l5))
##print "There are {0} 4-digit p(6,n) numbers".format(len(l6))
##print "There are {0} 4-digit p(7,n) numbers".format(len(l7))
##print "There are {0} 4-digit p(8,n) numbers".format(len(l8))
##dup = len(l3) + len(l4) + len(l5) + len(l6) + len(l7) + len(l8) - len(la)
dup = len(l3) + len(l4) + len(l5) - len(la)
print "{0} 4-digit numbers total (not counting {1} duplicates)".format(len(la), dup)

##find_chain(1,1045,[1045],1045)

##for i in l8:
##    chain = [i]
##    find_chain(1, i, chain, i)

for i0 in l5:
    t0 = 'p(5,n)'
    b1 = (i0 % 100) * 100
    
    for i1 in range(b1, b1+100):
        if (i1 in la):
            if (i1 in l3):
                t1 = 'p(3,n)'
            elif (i1 in l4):
                t1 = 'p(4,n)'
            elif (i1 in l5):
                t1 = 'p(5,n)'

            b2 = (i1 % 100) * 100

            for i2 in range(b2, b2+100):
                if (i2 in la):
                    if (i2 in l3):
                        t2 = 'p(3,n)'
                    elif (i2 in l4):
                        t2 = 'p(4,n)'
                    elif (i2 in l5):
                        t2 = 'p(5,n)'

                    b3 = (i2 % 100) * 100

                    for i3 in range(b3, b3+100):
                        if (i3 == i0):
                            if (('p(3,n)' in [t0, t1, t2]) & ('p(4,n)' in [t0, t1, t2]) & ('p(5,n)' in [t0, t1, t2])):
                                print "Found: {3} = {0}, {4} = {1}, {5} = {2}".format(i0,i1,i2, t0, t1, t2)
