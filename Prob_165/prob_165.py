#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 165
#
# Intersections
#
# A segment is uniquely defined by its two endpoints.
# By considering two line segments in plane geometry there are three
# possibilities:
# the segments have zero points, one point, or infinitely many points
# in common.
#
# Moreover when two segments have exactly one point in common it might
# be the case that that common point is an endpoint of either one of
# the segments or of both. If a common point of two segments is not an
# endpoint of either of the segments it is an interior point of both
# segments.
# We will call a common point T of two segments L1 and L2 a true
# intersection point of L1 and L2 if T is the only common point of L1
# and L2 and T is an interior point of both segments.
#
# Consider the three segments L1, L2, and L3:
#
#    L1: (27, 44) to (12, 32)
#    L2: (46, 53) to (17, 62)
#    L3: (46, 70) to (22, 40)
#
# It can be verified that line segments L2 and L3 have a true
# intersection point. We note that as the one of the end points of L3:
# (22,40) lies on L1 this is not considered to be a true point of
# intersection. L1 and L2 have no common point. So among the three
# line segments, we find one true intersection point.
#
# Now let us do the same for 5000 line segments. To this end, we
# generate 20000 numbers using the so-called "Blum Blum Shub"
# pseudo-random number generator.
#
#    s(0) = 290797
#
#    s(n+1) = s(n) x s(n) (modulo 50515093)
#
#    t(n) = s(n) (modulo 500)
#
# To create each line segment, we use four consecutive numbers
# t(n). That is, the first line segment is given by:
#
#    (t1, t2) to (t3, t4)
#
# The first four numbers computed according to the above generator
# should be: 27, 144, 12 and 232. The first segment would thus be
# (27,144) to (12,232).
#
# How many distinct true intersection points are found among the 5000
# line segments?
#
# Solved ??/??/11
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()
prev_time = start_time

MAX = 50
lines = []
intersect_e = [[False]*MAX for _ in range(MAX)]  # This is how you create a 2D array in python!
intersect_x = [[0.0]*MAX for _ in range(MAX)]  # This is how you create a 2D array in python!
intersect_y = [[0.0]*MAX for _ in range(MAX)]  # This is how you create a 2D array in python!


########################################
def generate_lines(n):
    sn = 290797
    for i in xrange(n):
        sn = (sn**2) % 50515093
        x0 = (sn % 500)
        sn = (sn**2) % 50515093
        y0 = (sn % 500)

        sn = (sn**2) % 50515093
        x1 = (sn % 500)
        sn = (sn**2) % 50515093
        y1 = (sn % 500)

        xp = max(x0,x1)
        xm = min(x0,x1)
        yp = max(y0,y1)
        ym = min(y0,y1)

        line = (x0,y0, x1,y1, xm,ym, xp,yp)
        lines.append(line)

########################################
def fake_generate_lines(n):
    for (x0,y0, x1,y1) in [(453,51, 485,83), (460,58, 402,0), (86,460, 464,53)]:
        line = (x0,y0, x1,y1, min(x0,x1),min(y0,y1), max(x0,x1),max(y0,y1))
        lines.append(line)


########################################
def f(x,y, x0,y0, x1,y1):
    # y-y0 = (x-x0) * (y1-y0)/(x1-x0)
    if ((x1-x0) != 0):
        f = (y1-y0)*(x-x0) - (x1-x0)*(y-y0)
    else:
        f = (x-x0)
    return f
    # returns 0 if (x,y) is on the line formed by (x0,y0)-(x1,y1)
    # returns negative value if it is above that line
    # returns positive value if it is below that line


########################################
def intersect(x0,y0, x1,y1, x2,y2, x3,y3, xam,yam, xap,yap, xbm,ybm, xbp,ybp):
    if ((xap < xbm) | (xam > xbp)):
        #print "    No X overlap"
        return False
    if ((yap < ybm) | (yam > ybp)):
        #print "    No Y overlap"
        return False

    #print "f({0},{1}) = {2}".format(x0,y0, f(x0,y0, x2,y2, x3,y3))
    #print "f({0},{1}) = {2}".format(x1,y1, f(x1,y1, x2,y2, x3,y3))
    #print "f({0},{1}) = {2}".format(x2,y2, f(x2,y2, x0,y0, x1,y1))
    #print "f({0},{1}) = {2}".format(x3,y3, f(x3,y3, x0,y0, x1,y1))

    a = f(x0,y0, x2,y2, x3,y3)
    b = f(x1,y1, x2,y2, x3,y3)
    if ((a*b) >= 0):
        #print "    line 1 doesn't overlap line 2", a, b
        return False

    c = f(x2,y2, x0,y0, x1,y1)
    d = f(x3,y3, x0,y0, x1,y1)
    if ((c*d) >= 0):
        #print "    line 2 doesn't overlap line 1", c, d
        return False

    #print "    Found an intersection", a, b, c, d
    return True


########################################
def intersect_point(x0,y0, x1,y1, x2,y2, x3,y3):
    # Lines are known to intersect, figure out the intersection point

    (fx0,fy0) = (float(x0), float(y0))
    (fx1,fy1) = (float(x1), float(y1))
    (fx2,fy2) = (float(x2), float(y2))
    (fx3,fy3) = (float(x3), float(y3))

    if ((x0-x1)*(x2-x3) != 0):  # No vertical lines
        # (y-y0) = (x-x0)*(y1-y0)/(x1-x0)
        # => y = y0 + (x-x0)*(y1-y0)/(x1-x0)
        # and
        # => y = y2 + (x-x2)*(y3-y2)/(x3-x2)
        #
        # We calculate the X intersection point from
        #     y0 + (x-x0)*(y1-y0)/(x1-x0) = y = y2 + (x-x2)*(y3-y2)/(x3-x2)
        #     y0 + x*(y1-y0)/(x1-x0) - x0*(y1-y0)/(x1-x0) = y2 + x*(y3-y2)/(x3-x2) - x2*(y3-y2)/(x3-x2)
        #     x*(y1-y0)/(x1-x0) - x*(y3-y2)/(x3-x2) = y2-y0 + x0*(y1-y0)/(x1-x0) - x2*(y3-y2)/(x3-x2)
        #     x*((y1-y0)/(x1-x0) - (y3-y2)/(x3-x2)) = y2-y0 + x0*(y1-y0)/(x1-x0) - x2*(y3-y2)/(x3-x2)
        #     x = (y2-y0 + x0*(y1-y0)/(x1-x0) - x2*(y3-y2)/(x3-x2)) / ((y1-y0)/(x1-x0) - (y3-y2)/(x3-x2))
        fx = (fy2-fy0 + fx0*(fy1-fy0)/(fx1-fx0) - fx2*(fy3-fy2)/(fx3-fx2)) / ((fy1-fy0)/(fx1-fx0) - (fy3-fy2)/(fx3-fx2))

        # Then given that we know x, we can calculate y
        # (y-y0) = (x-x0)*(y1-y0)/(x1-x0)
        # y = y0 + (x-x0)*(y1-y0)/(x1-x0)
        fy = fy0 + (fx-fx0)*(fy1-fy0)/(fx1-fx0)
    elif ((x0-x1) != 0):  # Line (x0,y0)-(x1,y1) is not vertical
        #print "Line (x2,y2)-(x3,y3) is vertical, (x0,y0)-(x1,y1) is not"
        fx = fx2

        # Then given that we know x, we can calculate y
        # (y-y0) = (x-x0)*(y1-y0)/(x1-x0)
        # y = y0 + (x-x0)*(y1-y0)/(x1-x0)
        fy =  fy0 + (fx-fx0)*(fy1-fy0)/(fx1-fx0)
    elif ((x2-x3) != 0):  # Line (x2,y2)-(x3,y3) is not vertical
        #print "Line (x0,y0)-(x1,y1) is vertical, (x2,y2)-(x3,y3) is not"
        fx = fx0

        # Then given that we know x, we can calculate y
        # (y-y2) = (x-x2)*(y3-y2)/(x3-x2)
        # y = y2 + (x-x2)*(y3-y2)/(x3-x2)
        fy =  fy2 + (fx-fx2)*(fy3-fy2)/(fx3-fx2)
    else:  # Both lines are vertical, should never happen
        print "ERROR: Two vertical line segments, should never happen"
        sys.exit(1)
        fx = 0.0
        fy = 0.0
    return (fx,fy)


########################################
def duplicate_point(i,j,k,l):
    (x ,y ) = (intersect_x[j][i], intersect_y[j][i])
    (xp,yp) = (intersect_x[l][k], intersect_y[l][k])
    if ((abs(x-xp) > 0.0001) | (abs(y-yp) > 0.0001)):
        return False
    d = ((x-xp)**2 + (y-yp)**2)
    if (d < 0.0000001):
        print "The intersection of #{0}-{1} at".format(i,j), (x,y),
        print "is distance {0}".format(d**0.5), "from",
        print "the intersection of #{0}-{1} at".format(k,l), (xp,yp)
        return True
    else:
        return False


########################################
print "Running with MAX = {0}".format(MAX)
ans = 0
generate_lines(MAX)
#fake_generate_lines(MAX)

#for i in xrange(len(lines)):
#    (x0,y0, x1,y1, xam,yam, xap,yap) = lines[i]
#    print "Line segment #{0}: ({1},{2}) - ({3},{4})".format(i, x0,y0, x1,y1)
#sys.exit()

for i in xrange(1,len(lines)):
    if ((i % 100) == 0):
        print "Working on line segment #{0} at time {1}, delta time {2}".format(i, time.clock()-start_time, time.clock()-prev_time)
        prev_time = time.clock()
    for j in xrange(0,i):
        (x0,y0, x1,y1, xam,yam, xap,yap) = lines[i]
        (x2,y2, x3,y3, xbm,ybm, xbp,ybp) = lines[j]

        #print "{0}-{1}: ({2},{3})-({4},{5}) to ({6},{7})-({8},{9})".format(i,j,x0,y0,x1,y1,x2,y2,x3,y3)
        if intersect(x0,y0, x1,y1, x2,y2, x3,y3, xam,yam, xap,yap, xbm,ybm, xbp,ybp):
            (x,y) = intersect_point(x0,y0, x1,y1, x2,y2, x3,y3)
            intersect_e[i][j] = True
            intersect_x[i][j] = x
            intersect_y[i][j] = y

            intersect_e[j][i] = True
            intersect_x[j][i] = x
            intersect_y[j][i] = y
            ans += 1
            #dup = False
            #for k in xrange(len(points)):
            #    (xp,yp,ip,jp) = points[k]
            #    if ((abs(x-xp) > 0.00001) | (abs(y-yp) > 0.00001)):
            #        continue
            #    d = ((x-xp)**2 + (y-yp)**2)
            #    if (d < 0.00000001):
            #        dup = True
            #        break
            #if (dup):
            #    print "intersection point", (x,y), " {0}-{1} is distance {2}".format(i,j,d**0.5), "from point #{0} {1}-{2}".format(k,ip,jp), (xp,yp)
            #else:
            #    #print "intersection point #{0}".format(ans), (xp,yp)
            #    points.append((x,y,i,j))
            #    print "points =", points
            #    points.sort()
            #    print "points =", points
            #    ans += 1

print "Raw answer =", ans, "at time = {0} seconds".format(time.clock() - start_time)
prev_time = time.clock()

for i in xrange(MAX):
    if ((i % 100) == 0):
        print "Working on line segment #{0} at time {1}, delta time {2}".format(i, time.clock()-start_time, time.clock()-prev_time)
        prev_time = time.clock()
    for j in xrange(0,i):
        if (intersect_e[j][i] == False):  continue

        for k in xrange(0,i):
            #if ((i == 411) & (j == 122)):
            #    print "intersect_e[{0}][{1}] = {2}".format(k,j,intersect_e[k][j])
            #    print "intersect_e[{0}][{1}] = {2}".format(j,k,intersect_e[j][k])
            #    print "duplicate_point({0},{1},{2},{3}) = {4}".format(i,j,k,j,duplicate_point(i,j,k,j))
            if (intersect_e[k][j] == False):  continue
            if duplicate_point(i,j,k,j):
                ans -= 1

        for l in xrange(0,j):
            if (intersect_e[i][l] == False):  continue
            if duplicate_point(i,j,i,l):
                ans -= 1

print "Final answer =", ans
print "Time taken = {0} seconds".format(time.clock() - start_time)
