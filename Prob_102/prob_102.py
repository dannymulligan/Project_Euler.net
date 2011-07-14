#!/usr/bin/python
#
# Project Euler.net Problem 102
# 
# Three distinct points are plotted at random on a Cartesian plane,
# for which -1000 <= x, y <= 1000, such that a triangle is formed.
# 
# Consider the following two triangles:
# 
#     A(-340,495), B(-153,-910), C(835,-947)
# 
#     X(-175,41), Y(-421,-714), Z(574,-645)
# 
# It can be verified that triangle ABC contains the origin, whereas
# triangle XYZ does not.
# 
# Using triangles.txt (right click and 'Save Link/Target As...'), a
# 27K text file containing the co-ordinates of one thousand "random"
# triangles, find the number of triangles for which the interior
# contains the origin.
# 
# NOTE: The first two examples in the file represent the triangles in
# the example given above.
#
# Solved: 11/22/09
# 106 problems solved
# Position #976 on level 3

tfile = open("./triangles.txt", "r")
#tfile = open("./test.txt", "r")

i = 0
answer = 0
for line in tfile:
    i += 1

    (x0,y0, x1,y1, x2,y2) = (float(x) for x in line.split(','))
    #print "{0}: ({1},{2}), ({3},{4}), ({5},{6})".format(i, x0,y0, x1,y1, x2,y2)

    if ((x0 == x1) | (x1 == x2) | (x2 == x0)):
        # About to have problem with division by zero, swap x & y's to avoid
        (x0,y0, x1,y1, x2,y2) = (y0,x0, y1,x1, y2,x2)

    m0 = (y1-y0)/(x1-x0)
    m1 = (y2-y1)/(x2-x1)
    m2 = (y0-y2)/(x0-x2)
    c0 = y0 - m0*x0
    c1 = y1 - m1*x1
    c2 = y2 - m2*x2
    #print "    eqn 0-1: y = {0} x + {1}".format(m0,c0)
    #print "    eqn 1-2: y = {0} x + {1}".format(m1,c1)
    #print "    eqn 2-0: y = {0} x + {1}".format(m2,c2)

    s0 = (x2*m0 + c0) - y2
    s1 = (x0*m1 + c1) - y0
    s2 = (x1*m2 + c2) - y1
    #print "    s0: {0} {1}".format(s0,c0)
    #print "    s1: {0} {1}".format(s1,c1)
    #print "    s2: {0} {1}".format(s2,c2)

    if (s0*c0>0) & (s1*c1>0) & (s2*c2>0):
        answer += 1
        #print "    Origin inside, {0} found so far".format(answer)

print "Answer =", answer
