#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 317
#
# Firecracker
#
# A firecracker explodes at a height of 100 m above level ground. It
# breaks into a large number of very small fragments, which move in
# every direction; all of them have the same initial velocity of 20
# m/s.
#
# We assume that the fragments move without air resistance, in a
# uniform gravitational field with g=9.81 m/s^2.
#
# Find the volume (in m^3) of the region through which the fragments
# move before reaching the ground. Give your answer rounded to four
# decimal places.

import numpy as np
np.set_printoptions(edgeitems=4)
np.core.arrayprint._line_width = 180

import sys
import time
start_time = time.clock()

########################################

D_RESOLUTION = 0.0025   # meters
A_RESOLUTION = 0.00005  # radians
MAX_X = 105.0  # meters
G  =   9.81  # meters/second^2
X0 =   0.0   # meters
Y0 = 100.0   # meters
V0 =  20.0   # meters/second
DEBUG = False

########################################

ymax = np.zeros(int(MAX_X/D_RESOLUTION))
x = np.zeros(int(MAX_X/D_RESOLUTION))
x = np.arange(0.0, MAX_X, D_RESOLUTION)
a = np.zeros(int(MAX_X/D_RESOLUTION))


########################################
# Special case for a = 0.0, so Vx = 0.0
Vy0 = V0
t = Vy0 / G
ymax[0] = -G*t*t/2 + Vy0*t + Y0


########################################
# All the other cases with non-zero Vx
i = 0
for a in np.arange(A_RESOLUTION, A_RESOLUTION+np.pi/2.0, A_RESOLUTION):
    Vx0 = V0 * np.sin(a)
    Vy0 = V0 * np.cos(a)
    t = x / Vx0
    y = -G*t*t/2 + Vy0*t + Y0
    ymax = np.maximum(ymax, y)

    if DEBUG:
        print("Theta = {} radians = {} degrees,  Vx0 = {} m/s,  Vy0 = {} m/w".format(a, a*180./np.pi, Vx0, Vy0))
        print(" x    = {}".format(x))
        print(" t    = {}".format(t))
        print(" y    = {}".format(y))
        print(" ymax = {}".format(ymax))


########################################
# Convert the height values into a volume number
def cylinder_volume (x, y):
    return np.pi * x**2 * y

volume = 0.0  # meter^3
for i in range(ymax.shape[0]-1):
    inner_x, outer_x = x[i], x[i+1]
    inner_y, outer_y = ymax[i], ymax[i+1]
    avg_y = (inner_y + outer_y) / 2
    inner_v = cylinder_volume(inner_x, avg_y)
    outer_v = cylinder_volume(outer_x, avg_y)
    volume += outer_v - inner_v

print("Volume = {:.8f} = {:.4f} meters^3".format(volume, volume))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
