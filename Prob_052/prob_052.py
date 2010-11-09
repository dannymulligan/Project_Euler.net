#!/usr/bin/python
#
# Project Euler.net Problem 52
#
# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and
# 6x, contain the same digits.
#
# Answer:


def test2(n1):
    if (n1<100):  # Quick pre-tests
        return False

    n2 = n1 * 2
    #print "n1 = {0}".format(n1)
    #print "n2 = {0}".format(n2)

    s1 = "{0}".format(n1)
    s2 = "{0}".format(n2)

    l1 = len(s1)
    l2 = len(s2)
    #print "l1 = {0}".format(l1)
    #print "l2 = {0}".format(l2)

    if (l1 == l2):
        pass
    else:
        return False

    c1 = 0
    c2 = 0
    for i in range(l1):
        c1 += (ord(s1[i])**2)
        c2 += (ord(s2[i])**2)
    #print "c1 = {0}".format(c1)
    #print "c2 = {0}".format(c2)

    if (c1 == c2):
        pass
    else:
        return False

    return True


def test6(n1):
    if (n1<100):  # Quick pre-tests
        return False

    n2 = n1 * 2
    n3 = n1 * 3
    n4 = n1 * 4
    n5 = n1 * 5
    n6 = n1 * 6
    #print "n1 = {0}".format(n1)
    #print "n2 = {0}".format(n2)
    #print "n3 = {0}".format(n3)
    #print "n4 = {0}".format(n4)
    #print "n5 = {0}".format(n5)
    #print "n6 = {0}".format(n6)

    s1 = "{0}".format(n1)
    s2 = "{0}".format(n2)
    s3 = "{0}".format(n3)
    s4 = "{0}".format(n4)
    s5 = "{0}".format(n5)
    s6 = "{0}".format(n6)

    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    l4 = len(s4)
    l5 = len(s5)
    l6 = len(s6)
    #print "l1 = {0}".format(l1)
    #print "l2 = {0}".format(l2)
    #print "l3 = {0}".format(l3)
    #print "l4 = {0}".format(l4)
    #print "l5 = {0}".format(l5)
    #print "l6 = {0}".format(l6)

    # Check that all are the same number of characters
    if (l1 == l2 == l3 == l4 == l5 == l6):
        pass
    else:
        return False

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    for i in range(l1):
        c1 += (ord(s1[i])**2)
        c2 += (ord(s2[i])**2)
        c3 += (ord(s3[i])**2)
        c4 += (ord(s4[i])**2)
        c5 += (ord(s5[i])**2)
        c6 += (ord(s6[i])**2)
    #print "c1 = {0}".format(c1)
    #print "c2 = {0}".format(c2)
    #print "c3 = {0}".format(c3)
    #print "c4 = {0}".format(c4)
    #print "c5 = {0}".format(c5)
    #print "c6 = {0}".format(c6)

    # Check that all use the same of characters
    if (c1 == c2 == c3 == c4 == c5 == c6):
        pass
    else:
        return False

    return True


if (test2(12345) == False):  # Should be false
    pass
else:
    print "Self test failed!"

if (test2(125874) == True):  # Should be true
    pass
else:
    print "Self test failed!"

if (test6(125874) == False):  # Should be false
    pass
else:
    print "Self test failed!"


print "Search 2 digit candidates"
for i in range(10, 17):
    if test6(i):
        print "Found {0}".format(i)

print "Search 3 digit candidates"
for i in range(100, 167):
    if test6(i):
        print "Found {0}".format(i)

print "Search 4 digit candidates"
for i in range(1000, 1667):
    if test6(i):
        print "Found {0}".format(i)

print "Search 5 digit candidates"
for i in range(10000, 16667):
    if test6(i):
        print "Found {0}".format(i)

print "Search 6 digit candidates"
for i in range(100000, 166667):
    if test6(i):
        print "Found {0}".format(i)
