#!/usr/bin/python
#
# Project Euler.net Problem 122
#
# The most naive way of computing n^(15) requires fourteen
# multiplications:
#
#     n x n x ... x n = n^(15)
#
# But using a "binary" method you can compute it in six
# multiplications:
#
#     n x n = n^(2)
#     n^(2) x n^(2) = n^(4)
#     n^(4) x n^(4) = n^(8)
#     n^(8) x n^(4) = n^(12)
#     n^(12) x n^(2) = n^(14)
#     n^(14) x n = n^(15)
#
# However it is yet possible to compute it in only five
# multiplications:
#
#     n x n = n^(2)
#     n^(2) x n = n^(3)
#     n^(3) x n^(3) = n^(6)
#     n^(6) x n^(6) = n^(12)
#     n^(12) x n^(3) = n^(15)
#
# We shall define m(k) to be the minimum number of multiplications to
# compute n^(k); for example m(15) = 5.
#
# For 1 <= k <= 200, find sum(m(k)).
#
# Solved 10/03/13
# 187 problems solved
# Position #204 on level 7

import sys
import time
start_time = time.clock()

########################################

SIZE = 200
MAX_DEPTH = 11
best_path = [(-1, [])] * (SIZE + 1)
best_path[0] = (0, [])
best_path[1] = (0, [1])

def find_best_way(d, max_d, path):
    #print "find_best_way({}, {}, {})".format(d, max_d, path)
    for m in path:
        res = m + path[-1]
        if (res <= SIZE):
            best = best_path[res]
            if ((best[0] == -1) or (best[0] > d+1)):
                best_path[res] = (d+1, path + [res])
                print "Found new path for x^{} = {} steps, {}".format(res, d+1, path+[res])
            if (d < max_d-1):
                find_best_way(d+1, max_d, path+[res])

find_best_way(0, MAX_DEPTH, [1])

print "========================================"
for n, path in enumerate(best_path[1:]):
    print "Best solution for x^{} is {} steps = {}".format(n+1, path[0], path[1])
    assert (path[0] != -1), "didn't find a solution for x^{}, user a higher value of MAX_DEPTH, currently set to {}".format(n,MAX_DEPTH)

answer = 0
for path in best_path[1:SIZE+1]:
    answer += path[0]
print "Answer =", answer
print "Time taken = {0} seconds".format(time.clock() - start_time)
