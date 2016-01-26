#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 504
#
# Square on the Inside
#
# Let ABCD be a quadrilateral whose vertices are lattice points lying
# on the coordinate axes as follows:
#
# A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and
# a, b, c, d, m are integers.
#
# It can be shown that for m = 4 there are exactly 256 valid ways to
# construct ABCD. Of these 256 quadrilaterals, 42 of them strictly
# contain a square number of lattice points.
#
# How many quadrilaterals ABCD strictly contain a square number of
# lattice points for m = 100?

import sys
import time
start_time = time.clock()

############################################################
SIZE = 100


############################################################
# Generator to calculate squares
def squares(limit):
    i = 1
    while (i**2 <= limit):
        yield i**2
        i += 1

list_of_squares = []
for x in squares(4*SIZE**2):
    list_of_squares.append(x)

def is_square(x):
    return x in list_of_squares

#assert is_square(  4) == True
#assert is_square(  5) == False
#assert is_square( 15) == False
#assert is_square( 16) == True
#assert is_square( 99) == False
#assert is_square(100) == True


############################################################
# Function to calculate how many points are strictly inside
# a triangle between (0,0), (0,y), & (x,0)
def points_inside_triangle(x1, y1):
    #print("points_inside_triangle({x1}, {y1})".format(x1=x1, y1=y1))
    answer = 0
    y = y1
    for x in range(1, x1):
        while (y * x1) >= (y1 * (x1 - x)) and y > 0:
            y -= 1
        answer += y
    return answer

#assert points_inside_triangle(1,1) == 0
#assert points_inside_triangle(2,2) == 0
#assert points_inside_triangle(2,4) == 1
#assert points_inside_triangle(4,6) == 7
#assert points_inside_triangle(6,4) == 7


############################################################
# Create a lookup table to accelerate calculations
# quad = one quadrant at a time
# quadrant[a][b] = point count (not including points on the axes)
quad = [[points_inside_triangle(x, y) for y in range(SIZE+1)] for x in range(SIZE+1)]

#for y in range(SIZE+1):
#    for x in range(SIZE+1):
#        print("quad[{x}][{y}] = {i}".format(x=x, y=y, i=quad[x][y])),
#    print


############################################################
# Create another lookup table to accelerate calculations
# one half at a time = two adjacent quadrants
# half[a][c] = point count (not including points on the Y axis)
half = [[[] for c in range(SIZE+1)] for a in range(SIZE+1)]

for a in range(SIZE+1):
    for c in range(SIZE+1):
        poss = []
        for b in range(1,SIZE+1):
            count = quad[a][b] + quad[b][c] + b - 1
            poss.append((count, b))
        half[a][c] = poss

#for a in range(1, SIZE+1):
#    for c in range(1, a+1):
#        print("a={a} c={c}".format(a=a, c=c))
#
#        poss = half[a][c]
#        for p in poss:
#            (x, b) = p
#            print("    count for {a}-{b}-{c} = {x}".format(a=a, b=b, c=c, x=x))


############################################################
# Now we search for solutions
print("Searching for solutions up to SIZE={}".format(SIZE))
answer = 0
for a in range(1, SIZE+1):
    for b in range(1, SIZE+1):
        for c in range(1, SIZE+1):
            for d in range(1, SIZE+1):
                count = quad[a][b] + quad[b][c] + quad[c][d] + quad[d][a] + a + b + c + d - 3
                if is_square(count):
                    #print("solution: count={x} a={a} b={b} c={c} d={d}".format(a=a, b=b, c=c, d=d, x=count))
                    answer += 1
                    if (answer % 10000) == 0:
                        print("{} solutions found".format(answer))

print("Answer = {}".format(answer))


# Now create a reverse table to allow us to find (x,y) combinations
# with a defined number of inside points
#rev_inside = {x: [] for x in range(1, SIZE*SIZE+1)}
#print("rev_inside = {}".format(rev_inside))
#
#for y in range(SIZE+1):
#    for x in range(y+1):
#        i = inside[x][y]
#        if i < 1:
#            continue
#
#        l = rev_inside[i]
#        l.append((x, y))
#        rev_inside[i] = l
#
#for l in rev_inside.keys():
#    print(l, rev_inside[l])
#
#print("rev_inside = {}".format(rev_inside))

print("Time taken = {0} seconds".format(time.clock() - start_time))
