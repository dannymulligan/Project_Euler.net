#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 392
#
# Enmeshed unit circle
#
# A rectilinear grid is an orthogonal grid where the spacing between
# the gridlines does not have to be equidistant.
#
# An example of such grid is logarithmic graph paper.
#
# Consider rectilinear grids in the Cartesian coordinate system with
# the following properties:
#
#    - The gridlines are parallel to the axes of the Cartesian coordinate
#      system.
#    - There are N+2 vertical and N+2 horizontal gridlines. Hence
#      there are (N+1) x (N+1) rectangular cells.
#    - The equations of the two outer vertical gridlines are x = -1 and
#      x = 1.
#    - The equations of the two outer horizontal gridlines are y = -1
#      and y = 1.
#    - The grid cells are colored red if they overlap with the unit
#      circle, black otherwise.
#
# For this problem we would like you to find the postions of the
# remaining N inner horizontal and N inner vertical gridlines so that
# the area occupied by the red cells is minimized.
#
# E.g. here is a picture of the solution for N = 10:
#
# p392_gridlines.png
#
# The area occupied by the red cells for N = 10 rounded to 10 digits
# behind the decimal point is 3.3469640797.
#
# Find the positions for N = 400.
# Give as your answer the area occupied by the red cells rounded to 10
# digits behind the decimal point.

import math
import sys
import time
start_time = time.clock()

########################################
N = 400
print("N = {}".format(N))
assert ((N % 2) == 0), "This solution assumes that N is even"
AREA_THRESHOLD = 1e-14
X_THRESHOLD = 5e-16

N45 = ((N % 4) != 0)  # Is there a point at (1/sqrt(2), 1/sqrt(2))?
#if N45:
#    print("N45")


########################################
def CalculateArea(points):
    Area = 0.0
    for (x0, y0), (x1, y1) in zip(points[1:], points[:-1]):
        dArea = x1 * (y0 - y1)
        Area += dArea
        #print("({:.04f}, {:.04f}), ({:.04f}, {:.04f}), area = {}".format(x0, y0, x1, y1, dArea))
    return 4.0 * Area


########################################
def InitialPoints(N):
    # Creat an initial placement by placing points at equal angles
    Points = list()
    for nn in range(2 + N//2):
        angle = nn * math.pi / 2.0 / (N//2 + 1)
        x = math.cos(angle)
        y = math.sin(angle)
        Points.append((x, y))
        #angle360 = nn * 90.0 / (N//2 + 1)
        #print("n={}, angle={}, (x, y) = ({}, {})".format(nn, angle360, x, y))
    return Points


########################################
# Optimize the position of a middle point
def OptimizePoint(x0, y0, x, y, x1, y1):
    oldArea = (x0 - x) * (y1 - y)

    # Find the value of x and y where
    # (x-x0)*x = (y-y1)*y
    xl = x0
    yl = (1.0 - xl**2.0)**0.5
    vl = (xl - x0)*xl - (yl - y1)*yl
    
    xr = x1
    yr = (1.0 - xr**2.0)**0.5
    vr = (xr - x0)*xr - (yr - y1)*yr
    
    xm = (xl + xr)/2.0
    ym = (1.0 - xm**2.0)**0.5
    vm = (xm - x0)*xm - (ym - y1)*ym

    #print("L", xl, yl, vl)
    #print("M", xm, ym, vm)
    #print("R", xr, yr, vr)

    while abs(xr - xl) > X_THRESHOLD:
        if vm <= 0.0:
            xr = xm
            yr = ym
            vr = vm
        else:
            xl = xm
            yl = ym
            vl = vm
            
        xm = (xl + xr)/2.0
        ym = (1.0 - xm**2.0)**0.5
        vm = (xm - x0)*xm - (ym - y1)*ym
        
        #print("L", xl, yl, vl)
        #print("M", xm, ym, vm)
        #print("R", xr, yr, vr)

    x = xm
    y = ym
    newArea = (x0 - x) * (y1 - y)
    dArea = newArea - oldArea
    return (x, y, dArea)

    
########################################
# Create the initial points
Points = InitialPoints(N)
for i, Point in enumerate(Points):
    print(i, Point)


########################################
# Optimize the location of the points
Top = N//2
Bot = 1
print("Top =", Top)
print("Bot =", Bot)
dArea = 1.0
while (dArea > AREA_THRESHOLD):
    dArea = 0.0
    for j in range(2, Top+1):
        (lx, ly) = Points[j-1]
        (ox, oy) = Points[j]
        (rx, ry) = Points[j+1]
        (nx, ny, da) = OptimizePoint(lx, ly, ox, oy, rx, ry)
        Points[j] = (nx, ny)
        dArea += da
        #print("optimize point {}, area saved {}".format(j, da))
    #print("----")
    for j in range(Top-1, 0, -1):
        (lx, ly) = Points[j-1]
        (ox, oy) = Points[j]
        (rx, ry) = Points[j+1]
        (nx, ny, da) = OptimizePoint(lx, ly, ox, oy, rx, ry)
        Points[j] = (nx, ny)
        dArea += da
        #print("optimize point {}, area saved {}".format(j, da))
    #print("====")
    
    Area = CalculateArea(Points)
    print("Area is calculated to be {:.12f}, da = {:.4e}, answer = {:.10f}".format(Area, da, Area))


########################################
# Calculate the result
Area = CalculateArea(Points)
print("Area is calculated to be {:.10f}".format(Area))
print("Time taken = {:.3f} seconds".format(time.clock() - start_time))
