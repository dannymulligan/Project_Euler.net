#!/usr/bin/python
#
# Project Euler.net Problem 91
#
# The points P (x1, y1) and Q (x2, y2) are plotted at integer
# co-ordinates and are joined to the origin, O(0,0), to form OPQ.
#
# There are exactly fourteen triangles containing a right angle that
# can be formed when each co-ordinate lies between 0 and 2 inclusive;
# that is,
#
#     0 <= x1, y1, x2, y2 <= 2.
#
# Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can
# be formed?
#


# For a coordinate system up to N, we have...
#     N^2 triangles with the right angle located on the origin
#     N^2 triangles with the right angle located on the X axis
#     N^2 triangles with the right angle located on the Y axis
# Then we calculate triangles with the right angle located elsewhere

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

def rtri_count(n):
    answer = 0
    # N^2 triangles with the right angle located on the origin
    # N^2 triangles with the right angle located on the X axis
    # N^2 triangles with the right angle located on the Y axis
    answer += 3*(n**2)

    # Count trianges with right angle located not on origin, X or Y axis
    for x in range(1,n+1):
        for y in range(1,n+1):
            if (gcd(x,y) == 1):
                # Evaluate triangles defined by vector (x, y)
                # One point will be (0, 0)
                # One point will be (x1, y1), located on the vector (x, y), this will be the right angle
                # One point will be (x2, y2), located on a vector (y, x) from the right angle
                (x1, y1) = (x, y)  # (x1, y1) is the right angle node
                ##print "Count triangles on the ({0},{1}) vector".format(x,y)
                while ((x1 <= n) & (y1 <= n)):
                    ##print "    Right angle at <{0},{1}>".format(x1,y1)

                    # Count triangles above the (x, y) vector
                    (x2, y2) = (x1-y, y1+x)
                    while ((0 <= x2 <= n) & (0 <= y2 <= n)):
                        answer += 1
                        ##print "        Triangle+ (0,0) <{0},{1}> ({2},{3})".format(x1,y1,x2,y2)
                        (x2, y2) = (x2-y, y2+x)

                    # Count triangles below the (x, y) vector
                    (x2, y2) = (x1+y, y1-x)
                    while ((0 <= x2 <= n) & (0 <= y2 <= n)):
                        answer += 1
                        ##print "        Triangle- (0,0) <{0},{1}> ({2},{3})".format(x1,y1,x2,y2)
                        (x2, y2) = (x2+y, y2-x)

                    # Move to next origin on this vector
                    (x1, y1) = (x1+x, y1+y)
                
    return answer

print "In a grid of 2x2, {0} right angle triangles can be formed".format(rtri_count(2))   # Answer should be 14
print "In a grid of 3x3, {0} right angle triangles can be formed".format(rtri_count(3))   # Answer should be 33
print "In a grid of 4x4, {0} right angle triangles can be formed".format(rtri_count(4))   # Answer should be 62
print "In a grid of 50x50, {0} right angle triangles can be formed".format(rtri_count(50))
