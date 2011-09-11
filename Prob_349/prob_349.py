#!/usr/local/bin/python
# coding=utf-8
#
# Project Euler.net Problem 349
#
# Langton's ant
#
# An ant moves on a regular grid of squares that are coloured either
# black or white.
#
# The ant is always oriented in one of the cardinal directions (left,
# right, up or down) and moves from square to adjacent square
# according to the following rules:
#
#   - if it is on a black square, it flips the color of the square to
#     white, rotates 90 degrees counterclockwise and moves forward one
#     square.
#
#   - if it is on a white square, it flips the color of the square to
#     black, rotates 90 degrees clockwise and moves forward one
#     square.
#
# Starting with a grid that is entirely white, how many squares are
# black after 10^18 moves of the ant?
#
# Solved 09/10/11
# 167 problems solved
# Position #407 on level 4

import sys
import time
start_time = time.clock()

#import matplotlib.pyplot as plt
#import numpy as np
#
## Generate some data...
#x, y = np.meshgrid(np.linspace(-2,2,200), np.linspace(-2,2,200))
#x, y = x - x.mean(), y - y.mean()
#z = x * np.exp(-x**2 - y**2)
#
## Plot the grid
#plt.imshow(z)
#plt.gray()
#plt.show()
#sys.exit()

########################################
SIZE = 500
bboard = [[False]*SIZE for _ in range(SIZE)]  # This is how you create a 2D array in python!
                                              # True = Black, False = White
count = 0  # number of Black squares

# From: http://en.wikipedia.org/wiki/Langton%27s_ant
#
# after an initial period of apparently chaotic behavior, that lasts
# for about 10,000 steps (in the simplest case), the ant starts
# building a recurrent "highway" pattern of 104 steps that repeat
# indefinitely
#
# So we will run the test for 10^18 - n*104 where n is large enough to
# reduce the total number of steps we evaluate to somewhere in the
# region of 10,000 to 12,000
#
# Every 104 steps adds 12 blacks to the total

steps =  10**18 - 104*(9615384615384500)
print "Running with steps = {0}".format(steps)
count += 12*(9615384615384500)

prevc = 0
(x, y, d) = (SIZE/2,SIZE/2,'w')
for s in xrange(steps):
    if (bboard[x][y]):  # Black square
        bboard[x][y] = False  # Flip to White
        count -= 1
        # turn counter-clockwise and advance one step
        if   (d == 'n'):  (x,y,d) = (x-1,y,'w')
        elif (d == 'e'):  (x,y,d) = (x,y+1,'n')
        elif (d == 's'):  (x,y,d) = (x+1,y,'e')
        elif (d == 'w'):  (x,y,d) = (x,y-1,'s')
    else:  # White square
        bboard[x][y] = True  # Flip to Black
        count += 1
        # turn clockwise and advance one step
        if   (d == 'n'):  (x,y,d) = (x+1,y,'e')
        elif (d == 'e'):  (x,y,d) = (x,y-1,'s')
        elif (d == 's'):  (x,y,d) = (x-1,y,'w')
        elif (d == 'w'):  (x,y,d) = (x,y+1,'n')

    if ((s % 104) == 0):
        print "{0}: ({1},{2},{3}), {4} black (delta = {5})".format(s,x,y,d,count, count-prevc)
        prevc = count

#    if ((x<0) or (y<0) or (x>=SIZE) or (y>=SIZE)):
#        print "{0}: ({1},{2},{3}), {4} black".format(s,x,y,d,count)
#        print "Error"
#        print "Time taken = {0} seconds".format(time.clock() - start_time)
#        sys.exit(1)
        
print "Answer =", count
print "Time taken = {0} seconds".format(time.clock() - start_time)

