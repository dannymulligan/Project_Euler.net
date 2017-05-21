#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 587
#
# Concave triangle
#
# A square is drawn around a circle as shown in the diagram below on
# the left.
#
# We shall call the blue shaded region the L-section.
#
# A line is drawn from the bottom left of the square to the top right
# as shown in the diagram on the right.
#
# We shall call the orange shaded region a concave triangle.
#
# <2 missing diagrams>
#
# It should be clear that the concave triangle occupies exactly half
# of the L-section.
#
# Two circles are placed next to each other horizontally, a rectangle
# is drawn around both circles, and a line is drawn from the bottom
# left to the top right as shown in the diagram below.
#
# <2 missing diagrams>
#
# This time the concave triangle occupies approximately 36.46% of the
# L-section.
#
# If n circles are placed next to each other horizontally, a rectangle
# is drawn around the n circles, and a line is drawn from the bottom
# left to the top right, then it can be shown that the least value of
# n for which the concave triangle occupies less than 10% of the
# L-section is n = 15.
#
# What is the least value of n for which the concave triangle occupies
# less than 0.1% of the L-section?

import math
import sys
#print(sys.version)
import time
start_time = time.clock()

########################################

lsection_area = (4. - math.pi) / 4.
target = 0.001

# (x0, y0) is the center of the circle = (1, 1)

# (x1, y1) is the intersection point between the line and circle
def circle_line_intersect(n):
    x1 = ((1. + 1./n) - (2./n)**0.5) / (1. + 1./(n**2))
    y1 = x1/n
    return x1, y1

# (x2, 0) is the intersection point between the line from the center
# of the circle and the x axis
def line_axis_intersect(x1, y1):
    x2 = 1. - (x1-1.)/(y1-1.)
    return x2

# theta is the angle inside the circle between the (1, 1) and (1, 0)
# line and the (1, 1) and (x1, y1) line.
def angle_center_circle(x1, y1):
    theta = math.atan((1.-x1)/(1.-y1))
    return theta

def area_concave_triangle(x1, y1, x2, theta):
    area = 0.5*(1.-x2)*1.  # triangle (x0, y0), (1, 0), (x2, 0)
    area += 0.5*y1*x1      # triangle (0, 0), (x1, y1), (x2, 0)
    area -= theta/2.
    return area

for n in range(1, 5000):
    x1, y1 = circle_line_intersect(float(n))
    x2 = line_axis_intersect(x1, y1)
    theta = angle_center_circle(x1, y1)
    area = area_concave_triangle(x1, y1, x2, theta)
    fraction = area/lsection_area
    print("n={}, x1={}, y1={}, x2={}, theta={}, area={}, fraction={}".format(n, x1, y1, x2, theta, area, fraction))
    if fraction < target:
        print("Solution found with n = {}".format(n))
        break
    
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
