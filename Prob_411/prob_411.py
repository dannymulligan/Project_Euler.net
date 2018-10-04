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

def coords(n):
    cset = set((x+y, x, y) for (x, y) in gen_coords(n))
    clist = sorted(list(cset), reverse=True)
    return [(x, y) for (xy, x, y) in clist]


###############################################################################
def S(n):
    #print("S({})".format(n))
    points = coords(n)
    #print("points = {}".format(points))
    frontier = []
    for (x, y) in points:
        # Calculate the number of stations on the path of the current point
        max_s = 0
        for (fx, fy, fs) in frontier:
            if (fx >= x) and (fy >= y):
                max_s = max(max_s, fs)

        ## Delete points in the frontier supersceded by the current point
        #frontier = [p for p in frontier if (p[0] <= x) or (p[1] <= y)]

        # Add new point to the frontier
        frontier.append((x, y, max_s+1))
        #print("point = {}, frontier = {}".format((x,y), frontier))

    # Find the final answer
    max_s = 0
    for (x, y, s) in frontier:
        max_s = max(max_s, s)

    #print("S({}) = {}".format(n, max_s))
    return max_s


###############################################################################

#for n in [22, 123, 10000]:
#    print("S({}) = {}".format(n, S(n)))
#sys.exit()

answer = 0
for k in range(1, 31):
    prev_time = time.clock()
    s = S(k**5)
    answer += s
    print("S({}) = S({:,}) = {:,}, calculated in {:.2f} seconds".format(
        k, k**5, s, time.clock() - prev_time))
    #result = process_coords(points)

print("Answer = {:,}".format(answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
