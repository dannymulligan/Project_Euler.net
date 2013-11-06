#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 126
#
# Exploring the number of cubes required to cover every visible face
# on a cuboid
#
# The minimum number of cubes to cover every visible face on a cuboid
# measuring 3 x 2 x 1 is twenty-two.
#
# <Picture>
#
# If we then add a second layer to this solid it would require
# forty-six cubes to cover every visible face, the third layer would
# require seventy-eight cubes, and the fourth layer would require
# one-hundred and eighteen cubes to cover every visible face.
#
# However, the first layer on a cuboid measuring 5 x 1 x 1 also
# requires twenty-two cubes; similarly the first layer on cuboids
# measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six
# cubes.
#
# We shall define C(n) to represent the number of cuboids that contain
# n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5,
# and C(118) = 8.
#
# It turns out that 154 is the least value of n for which C(n) = 10.
#
# Find the least value of n for which C(n) = 1000.
#
# Solved 10/15/13
# 188 problems solved
# Position #187 on level 7


# 1x1x1-1: (t, x, y, z) = (6, 4, 4, 4)
# 1x1x1-2: (t, x, y, z) = (18, 8, 8, 8)
# 1x1x1-3: (t, x, y, z) = (38, 12, 12, 12)
#
# For 1x1x1-1, t = 4 + 2*(1) = 6
# For 1x1x1-2, t = 8 + 2*(4 + 1) = 18
# For 1x1x1-3, t = 12 + 2*(8 + 4 + 1) = 38
# For 1x1x1-4, t = 16 + 2*(12 + 8 + 4 + 1) = 66
#
#  . . . . 4 . . . .
#  . . . 4 3 4 . . .
#  . . 4 3 2 3 4 . .
#  . 4 3 2 1 2 3 4 .
#  4 3 2 1 X 1 2 3 4
#  . 4 3 2 1 2 3 4 .
#  . . 4 3 2 3 4 . .
#  . . . 4 3 4 . . .
#  . . . . 4 . . . .
#
#  . . . . . . . . .
#  . . . . 4 . . . .
#  . . . 4 3 4 . . .
#  . . 4 3 2 3 4 . .
#  . 4 3 2 1 2 3 4 .
#  . . 4 3 2 3 4 . .
#  . . . 4 3 4 . . .
#  . . . . 4 . . . .
#  . . . . . . . . .
#
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . 4 . . . .
#  . . . 4 3 4 . . .
#  . . 4 3 2 3 4 . .
#  . . . 4 3 4 . . .
#  . . . . 4 . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . 4 . . . .
#  . . . 4 3 4 . . .
#  . . . . 4 . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . 4 . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#  . . . . . . . . .
#
# In general...
# 1x1x1-n: (t, x, y, z) = (4n^2+2, 4n, 4n, 4n)

import sys
import time
start_time = time.clock()

SIZE = 69  # Finds 18522 in 3.97 seconds
#SIZE = 70  # Finds 18522
#SIZE = 80  # Finds 18522
#SIZE = 100  # Finds 18522
#SIZE = 125  # Finds 18522
#SIZE = 150  # Finds 18522

RES_SIZE = 4*SIZE**2+2+1  # Number of cubes in 1x1x1-SIZE
results = [0]*RES_SIZE

for d in range(1, SIZE):
    t = 4*d**2 + 2
    print("Calculating layers of depth {d}, they start with {t} cubes".format(d=d, t=t))
    for x in range(1, SIZE**2):
        cx = 4*d
        if (t + (x-1)*cx) > RES_SIZE:
            break
        for y in range(1, x+1):
            cy = 4*d + 2*(x-1)
            if (t + (x-1)*cx + (y-1)*cy) > RES_SIZE:
                break
            for z in range(1, y+1):
                cz = 4*d + 2*(x-1) + 2*(y-1)
                a = t + (x-1)*cx + (y-1)*cy + (z-1)*cz
                #res = "{x}x{y}x{z}-{d} (a={a}, t={t}, cx={cx}, cy={cy}, cz={cz})".format(x=x, y=y, z=z, d=d, a=a, t=t, cx=cx, cy=cy, cz=cz)
                #print(res)
                if a < RES_SIZE:
                    results[a] += 1
                else:
                    break

for a in range(RES_SIZE):
    if results[a] == 1000:
        print("answer = {a}".format(a=a))
        print "Time taken = {0} seconds".format(time.clock() - start_time)
        sys.exit()

print("Answer not found")
print "Time taken = {0} seconds".format(time.clock() - start_time)
