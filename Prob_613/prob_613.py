#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 613
#
# Pythagorean Ant
#
# Dave is doing his homework on the balcony and, preparing a
# presentation about Pythagorean triangles, has just cut out a
# triangle with side lengths 30cm, 40cm and 50cm from some cardboard,
# when a gust of wind blows the triangle down into the garden.
#
# Another gust blows a small ant straight onto this triangle. The poor
# ant is completely disoriented and starts to crawl straight ahead in
# random direction in order to get back into the grass.
#
# Assuming that all possible positions of the ant within the triangle
# and all possible directions of moving on are equiprobable, what is
# the probability that the ant leaves the triangle along its longest
# side?
#
# Give your answer rounded to 10 digits after the decimal point.

import numpy as np
import scipy.integrate as integrate

import sys
#print(sys.version)
import time
start_time = time.clock()

X = 30.0
Y = 40.0
# Z = 50.0 mm

###############################################################################

def local_probability(x, y):
    #print("local_probability(x={}, y={})".format(x, y))
    # Calculate angle between (X, 0), (x, y), & (0, Y)
    # return this angle divided by a full circle.
    # Calculate using the law of cosines
    #     c^2 = a^2 + b^2 - 2ab Cos (C)
    # or
    #     Cos(C) = (a^2 + b^2 - c^2) / 2ab

    a = np.sqrt((x - X)**2 + y**2)  # a = distance between (x, y) and (X, 0)
    b = np.sqrt(x**2 + (Y-y)**2)    # b = distance between (x, y) and (0, Y)
    c = np.sqrt(X**2 + Y**2)        # c = distance between (X, 0) and (0, Y)

    CosC = (a**2 + b**2 - c**2) / (2*a*b)
    angle = np.arccos(CosC)
    value = angle / (2.*np.pi)
    return value


###############################################################################

f = lambda y, x: local_probability(x, y)
(volume, accuracy) = integrate.dblquad(f, 0., X, (lambda x: 0.0), (lambda x: Y-x*Y/X), epsabs=1.49e-10, epsrel=1.49e-10)
area = X * Y * 0.5
result = volume / area

print("volume = {}".format(volume))
print("area = {}".format(area))
print("result = {}".format(result))
print("accuracy = {}".format(accuracy/area))

print("Result ranges from {:.10f} to {:.10f}".format(result-accuracy/area, result+accuracy/area))
print("Answer = {:.10f} (which is the result rounded to 10 digits)".format(result))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
