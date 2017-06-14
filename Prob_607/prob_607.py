#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 607
#
# Marsh Crossing
#
# Frodo and Sam need to travel 100 leagues due East from point A to
# point B. On normal terrain, they can cover 10 leagues per day, and
# so the journey would take 10 days. However, their path is crossed by
# a long marsh which runs exactly South-West to North-East, and
# walking through the marsh will slow them down. The marsh is 50
# leagues wide at all points, and the mid-point of AB is located in
# the middle of the marsh. A map of the region is shown in the diagram
# below:
#
# p607_marsh.png
# 
# The marsh consists of 5 distinct regions, each 10 leagues across, as
# shown by the shading in the map. The strip closest to point A is
# relatively light marsh, and can be crossed at a speed of 9 leagues
# per day. However, each strip becomes progressively harder to
# navigate, the speeds going down to 8, 7, 6 and finally 5 leagues per
# day for the final region of marsh, before it ends and the terrain
# becomes easier again, with the speed going back to 10 leagues per
# day.
#
# If Frodo and Sam were to head directly East for point B, they would
# travel exactly 100 leagues, and the journey would take approximately
# 13.4738 days. However, this time can be shortened if they deviate
# from the direct path.
#
# Find the shortest possible time required to travel from point A to
# B, and give your answer in days, rounded to 10 decimal places.


import sys
#print(sys.version)
import math

import time
start_time = time.clock()

########################################

SIMPLE_TIME = 13.4738

def time_taken_simple (theta):
    time = 0.0
    wet_distance = 10.0/math.cos(theta)
    dry_distance = 100.0 - 5.0*wet_distance
    time = dry_distance/10.0
    time += wet_distance/9.0
    time += wet_distance/8.0
    time += wet_distance/7.0
    time += wet_distance/6.0
    time += wet_distance/5.0
    #print("time_taken({}) = {}".format(theta, time))
    return time

max_theta = 0.999*math.pi/2.0
min_theta = 0.001*math.pi/2.0
while (max_theta - min_theta)/math.pi > 1.0e-8:
    theta = (max_theta + min_theta) / 2.0
    days = time_taken_simple(theta)
    if days > SIMPLE_TIME:
        max_theta = theta
    else:
        min_theta = theta

wet_distance = 10.0/math.cos(theta)
dry_distance = 100.0 - 5.0*wet_distance

print("theta = {} radians".format(theta))
print("theta = {} degrees".format(180.0*theta/math.pi))
print("days = {}".format(days))
print("wet_distance = {}".format(wet_distance))
print("dry_distance = {}".format(dry_distance))

############################################################
# theta is exactly 45 degrees
theta = math.pi/4.0
wet_distance = 10.0/math.cos(theta)
dry_distance = 100.0 - 5.0*wet_distance

############################################################
c = [-x*wet_distance/2.0 for x in range(-5, +7, 2)]
c = [0.0] + c + [0.0]
x = [x*wet_distance/2.0 for x in range(-5, +7, 2)]
x = [-50.0] + x + [50.0]
m = [0.0] + [1.0]*6 + [0.0]
y = [_m*_x + _c for _m, _x, _c in zip(m, x, c)]
s = [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 10.0]
print("y = {}".format(y))
print("m = {}".format(m))
print("x = {}".format(x))
print("c = {}".format(c))
print("s = {}".format(s))

############################################################
def time_taken():
    days = 0.0
    for n in range(7):
        x0, y0 = x[n], y[n]
        x1, y1 = x[n+1], y[n+1]
        distance = ((x1-x0)**2 + (y1-y0)**2)**0.5
        days += distance/s[n]
        #print("({},{}) to ({},{}): distance = {}, time = {}, total time = {}".format(x0, y0, x1, y1, distance, distance/s[n], days))
    return days

############################################################
def differentiate(x, m, c, x0, y0, s):
    y = m*x + c
    d = ((x - x0)**2.0 + (y - y0)**2.0)**0.5
    answer1 = 1.0 / (2 * d * s)
    answer2 = 2*x - 2*x0 + 2*m*m*x + 2*m*(c-y0)
    return answer1 * answer2
        
############################################################
def gradient():
    grad = [0.0]*8
    for i in range(1,7):
        grad[i] = differentiate(x[i], m[i], c[i], x[i-1], y[i-1], s[i-1])
        grad[i] += differentiate(x[i], m[i], c[i], x[i+1], y[i+1], s[i])
    return grad

############################################################
def update(gradient, rate):
    global x
    global y
    for i in range(len(gradient)):
        x[i] -= rate * gradient[i]
    y = [_m*_x + _c for _m, _x, _c in zip(m, x, c)]

############################################################

prev_days = time_taken()
for i in range(10000):
    grad = gradient()
    if (i % 1000) == 0:
        print("{:6,}:".format(i))
        print("   x = {}".format(x))
        print("grad = {}".format(grad))
    update(grad, 5.0)

    if (i % 1000) == 0:
        days = time_taken()
        days_change = days - prev_days
        prev_days = days
        print("   x = {}".format(x))
        print("days = {:15.12f}, change = {:15.12f}".format(days, days_change))
        print()

#    days = time_taken()
#    if (prev_days - days) > 1.0e-10:
#        progress = True

print("Answer = {:.10f}".format(days))
print("x = {}".format(x))
print("y = {}".format(y))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
