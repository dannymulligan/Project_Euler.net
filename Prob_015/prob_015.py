#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 015
#
# Lattice paths
#
# Starting in the top left corner of a 2×2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#

import sys
import time
start_time = time.clock()

########################################

SIZE = 6

# Create an empty array of node values
nodes = list()
for x in range(SIZE+1):
    sublist = list()
    for y in range(SIZE+1):
        sublist.append(0)
    nodes.append(sublist)

# Next we step through the array and calculate the number of paths to that node
# We have to remember to initialize nodes[0][0] to 1
for x in range(SIZE+1):
    for y in range(SIZE+1):
        if (x-1) < 0:
            value_above = 0
        else:
            value_above = nodes[x-1][y]

        if (y-1) < 0:
            value_left = 0
        else:
            value_left = nodes[x][y-1]

        if (x == 0) & (y == 0):
            nodes[x][y] = 1
        else:
            nodes[x][y] = value_above + value_left

# And our answer is in the lower right node, which is nodes[SIZE][SIZE]
print("For a {}x{} grid...".format(SIZE, SIZE))
print("Answer is {}".format(nodes[SIZE][SIZE]))

print("Time taken = {0} seconds".format(time.clock() - start_time))
