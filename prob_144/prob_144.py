#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 144
#
# Investigating multiple reflections of a laser beam.
#
# In laser physics, a "white cell" is a mirror system that acts as a
# delay line for the laser beam. The beam enters the cell, bounces
# around on the mirrors, and eventually works its way back out.
#
# The specific white cell we will be considering is an ellipse with
# the equation 4x^2 + y^2 = 100
#
# The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is
# missing, allowing the light to enter and exit through the hole.
#
# The light beam in this problem starts at the point (0.0,10.1) just
# outside the white cell, and the beam first impacts the mirror at
# (1.4,-9.6).
#
# Each time the laser beam hits the surface of the ellipse, it follows
# the usual law of reflection "angle of incidence equals angle of
# reflection." That is, both the incident and reflected beams make the
# same angle with the normal line at the point of incidence.
#
# In the figure on the left, the red line shows the first two points
# of contact between the laser beam and the wall of the white cell;
# the blue line shows the line tangent to the ellipse at the point of
# incidence of the first bounce.
#
# The slope m of the tangent line at any point (x,y) of the given
# ellipse is: m = −4x/y
#
# The normal line is perpendicular to this tangent line at the point
# of incidence.
#
# The animation on the right shows the first 10 reflections of the
# beam.
#
# How many times does the beam hit the internal surface of the white
# cell before exiting?
#
# Solved 08/09/11
# 160 problems solved
# Position #517 on level 4


# y = m*x + c
# c = y - m*x
# y - y1 = m*(x - x1)

import time
import sys
#import cProfile

start_time = time.clock()

def done(x,y):
    return ((x>=-0.01) & (x<=0.01) & (y>9.0))

(x1,y1) = (0.0, 10.1)  # source
(x2,y2) = (1.4, -9.6)  # first reflection point

cnt = 0
while not(done(x2,y2)):
    cnt += 1
    print "Reflection #{0} at ({1},{2})".format(cnt,x2,y2)

    m = (y2-y1)/(x2-x1)  # Slope of incoming beam
    c = y1 - m*x1        # Y incercept of incoming beam
    mt = -4.0*x2/y2      # Slope of the tangent at the reflection point
    mn = -1.0/mt         # Slope of the normal at the reflection point

    # Imagine two lines,
    # One is parallel to the tangent at the reflection point, and goes through (x1,y1)
    #     y-y1 = mt*(x-x1)  => y = y1 + mt*(x-x1)
    # and one is the normal to the reflection point, and goes through (x2,y2)
    #     y-y2 = mn*(x-x2) => y = y2 + mn*(x-x2)
    # they intersect at (x3,y3)
    #     y1 + mt*(x3-x1) = y3 = y2 + mn*(x3-x2)
    #     y1 + mt*x3 - m*x1 = y2 + mn*x3 - mn*x2
    #     (mt-mn)*x3 = y2 - y1 + mt*x1 - mn*x2
    x3 = (y2 - y1 + mt*x1 - mn*x2)/(mt-mn)
    y3 = y1 + mt*(x3-x1)

    # The point (x4,y4) is on 2x as far from (x1,y1) as (x3,y3)
    x4,y4 = x1 + (x3-x1)*2, y1 + (y3-y1)*2

    # The points (x2,y2) and (x4,y4) are on the reflected beam
    #     y-y2 = (y4-y2)/(x4-x2) * (x-x2) => y = y2 + (y4-y2)/(x4-x2) * (x-x2)
    #     y = (y4-y2)/(x4-x2)*x + y2 - x2*(y4-y2)/(x4-x2)
    #     y = mr*x + cr
    mr = (y4-y2)/(x4-x2)
    cr = y2 - x2*(y4-y2)/(x4-x2)

    # We need to figure out where this line intersects with the ellipse
    #     4x^2 + y^2 = 100
    # The intersection point are given by
    #     4x^2 + (mr*x + cr)^2 = 100
    #     4x^2 + mr^2*x^2 + 2*mr*cr*x + cr^2 -100 = 0
    # This equation is of the form
    #     a*x^2 + b*x + c = 0
    a = 4 + mr**2
    b = 2*mr*cr
    c = cr**2 - 100
    xa = (-1*b + (b**2 - 4*a*c)**.5)/(2*a)
    xb = (-1*b - (b**2 - 4*a*c)**.5)/(2*a)
    if (abs(xa - x2) > abs(xb - x2)):
        # xa is the next reflection point
        x5 = xa
    else:
        # xb is the next reflection point
        x5 = xb
    y5 = mr*x5 + cr

    (x1,y1) = (x2,y2)
    (x2,y2) = (x5,y5)

print "Answer =", cnt
print "Time taken =", time.clock() - start_time, "seconds"

#cProfile.run('main()')
