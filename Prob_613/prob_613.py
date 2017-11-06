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

########################################


def calc_prob(step):
    #print("step size {}".format(step))
    
    x = np.arange(step, 30.+step, step)
    #print("x =\n", x)

    y = 40.0/x
    #print("y =\n", y)

    theta = np.arctan(y)
    #print("theta (radians) =\n", theta)
    #print("theta (degrees) =\n", theta * 180. / np.pi)

    angle = np.pi - theta
    #print("angle (radians) =\n{}".format(angle))
    #print("angle (degrees) =\n{}".format(angle*180./np.pi))

    average = np.average(angle)
    #print("average = {}".format(average))

    probability = average / (2.*np.pi)
    #print("probability = {:.11f}".format(probability))
    
    return probability
        
def function(x):
    y = 40.0/x
    theta = np.arctan(y)
    angle = np.pi - theta
    value = angle / (2.*np.pi)
    return value


for step in [1.0, 1.e-1, 1.e-2, 1.e-3, 1.e-4, 1.e-5]:
    print("with step size {}, answer is {:.12f}".format(step, calc_prob(step)))

(result, accuracy) = integrate.quad(function, 0, 30.0)

print("result = {}".format(result/30.))
print("accuracy = {}".format(accuracy/30.))

print("Result to 10 digits = {:.10f}".format(result/30.))
      
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
