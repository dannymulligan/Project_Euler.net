#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 411
#
# Uphill paths
#
# Let n be a positive integer. Suppose there are stations at the
# coordinates (x, y) = (2^i mod n, 3^i mod n) for 0 <= i <= 2n. We
# will consider stations with the same coordinates as the same
# station.
#
# We wish to form a path from (0, 0) to (n, n) such that the x and y
# coordinates never decrease.
#
# Let S(n) be the maximum number of stations such a path can pass
# through.
#
# For example, if n = 22, there are 11 distinct stations, and a valid
# path can pass through at most 5 stations. Therefore, S(22) = 5. The
# case is illustrated below, with an example of an optimal path:
#
# It can also be verified that S(123) = 14 and S(10000) = 48.
#
# Find sum S(k^5) for 1 <= k <= 30.


import sys
#print(sys.version)
import time
start_time = time.clock()

###############################################################################
def gen_coords(n):
    x, y = 1, 1
    yield (x, y)
    for i in range(2*n):
        x = (x*2) % n
        y = (y*3) % n
        yield (x, y)

if True:
    def coords(n):
        #print("coords({})".format(n))
        if (n == 1):
            clist = [(1, 1), (0, 0)]
        elif (n == 2):
            clist = [(1, 1), (0, 1)]
        elif (n == 3):
            clist =  [(1, 1), (2, 0), (1, 0)]
        else:
            clist = []
            (stopx, stopy) = (2, 3)
            for i, (x, y) in enumerate(gen_coords(n)):
                if (i > 1) and (x, y) == (1, 1):
                    return clist
                if (i > 1) and (x, y) == (stopx, stopy):
                    return clist
                if (stopx != 0) and (x == 0):
                    (stopx, stopy) = (x, y)
                if (stopy != 0) and (y == 0):
                    (stopx, stopy) = (x, y)
                clist.append((x, y))
                #print("{:2}: ({:2},{:2})".format(i, x, y))
        return clist
else:
    def coords(n):
        cset = set((x, y) for (x, y) in gen_coords(n))
        return cset


###############################################################################
def process_coords(c):
    print(sorted(c, reverse=True))
    return True


###############################################################################

#for k in range(1, 33):
#    points = coords(k)
#    print("coords({}) generates {:,} points= {}".format(
#        k, len(points), points))

k = 7776
points = coords(k)
print("coords({}) generates {:,} points= {}".format(
    k, len(points), points[653:655]))
print((3904,2673) in points[:652])
print((32,243) in points[:653])
print((64,729) in points[:653])
sys.exit()

for k in range(1, 12):
    prev_time = time.clock()
    #points = coords(k)
    points = coords(k**5)
    print("With k = {:2}, coords({}) generated {:,} points in {:.2f} seconds".format(
        k, k**5, len(points), time.clock() - prev_time))
    #result = process_coords(points)


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
