#!/usr/bin/python
#!/usr/bin/python -m pdb
# coding=utf-8
#
# Project Euler.net Problem 147
#
# Rectangles in cross-hatched grids
#
# In a 3x2 cross-hatched grid, a total of 37 different rectangles
# could be situated within that grid as indicated in the sketch.
#
# There are 5 grids smaller than 3x2, vertical and horizontal
# dimensions being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each
# of them is cross-hatched, the following number of different
# rectangles could be situated within those smaller grids:
# 
#     1x1: 1
#     2x1: 4
#     3x1: 8
#     1x2: 4
#     2x2: 18
# 
# Adding those to the 37 of the 3x2 grid, a total of 72 different
# rectangles could be situated within 3x2 and smaller grids.
#
# How many different rectangles could be situated within 47x43 and
# smaller grids?
#
# Solved 07/26/11
# 152 problems solved
# Position #721 on level 4

import sys
import time

start_time = time.clock()

def scnt(x,y):  # Square count
    xpos = x*(x+1)/2
    ypos = y*(y+1)/2
    result = xpos*ypos
    #print "scnt({0},{1})={2}".format(x,y,result)
    return result


##def dcnt(x,y):  # Diagonal count
##    tot = 0
##    solo = 0
##    a = max(x,y)
##    b = min(x,y)
##    for i in range(2,b*2-1,2):
##        print "len =", i
##        tot += 2*(i*(i+1)/2)
##        solo += 2*i
##    maxl = 2*b-1
##    tot += (a-b)*(maxl*(maxl+1)/2)
##    sol += (a-b)*maxl
##    result = tot*2 - solo
##    return result
##    # Bug: only counts 1x1 & 1xN rectangles
##    # doesn't count anything 2xN or higher

def dcnt(x,y):  # Diagonal count
    #print "dcnt({0},{1})".format(x,y)

    # Create a table list the length of diagonal runs
    grid = []
    a = max(x,y)
    b = min(x,y)
    start = 1
    for i in range(2,b*2-1,2):
        start = start - 1
        grid.append((start,start+i))
    maxl = 2*b-1
    for i in range(0,a-b):
        grid.append((start,start+maxl))
        start = start + 1
    for i in range(b*2-2,1,-2):
        grid.append((start,start+i))
        start = start + 1
    #print "grid =", grid, ", len(grid) =", len(grid)

    # Cover ever possible box L x W that can fit
    ans = 0
    for w in range(1,maxl+1):
        for r in range(len(grid)-w+1):
            (loc_min,loc_max) = grid[r]
            for s in range(1,w):
                (tmp_min,tmp_max) = grid[r+s]
                if (tmp_min > loc_min): loc_min = tmp_min
                if (tmp_max < loc_max): loc_max = tmp_max

            # (loc_min,loc_max) = length available for LxW box
            for l in range(w,maxl+1):
                loc_cnt = 0
                if (l <= (loc_max - loc_min)):
                    loc_cnt = (loc_max - loc_min - l + 1)
                    if (l == w):
                        ans += loc_cnt
                    else:
                        ans += 2*loc_cnt
                #print "grid {3}: {0}x{1} count = {2}, loc = ({4},{5})".format(w, l, loc_cnt, r, loc_min,loc_max)
    return ans


def bcnt(x,y):  # Both square & diagonal count
    return scnt(x,y) + dcnt(x,y)


#def cscnt(x,y):  # Cumulative square count
#    ans = 0
#    for i in range(1,x+1):
#        for j in range(1,y+1):
#            ans += scnt(i,j)
#    return ans
def cscnt(x,y):  # Cumulative square count
    ans = 0
    m = min(x,y)
    n = max(x,y)

    for i in range(1,m+1):  # Process the diagonal
        ans += scnt(i,i)

    for i in range(2,m+1):  # Fill in the square
        for j in range(1,i):
            ans += 2*(scnt(i,j))

    for i in range(m+1,n+1):  # Fill in the rectangle
        for j in range(1,m+1):
            ans += scnt(i,j)
    return ans

#def cdcnt(x,y):  # Cumulative diagonal count
#    ans = 0
#    for i in range(1,x+1):
#        for j in range(1,y+1):
#            ans += dcnt(i,j)
#    return ans
def cdcnt(x,y):  # Cumulative diagonal count
    ans = 0
    m = min(x,y)
    n = max(x,y)

    for i in range(1,m+1):  # Process the diagonal
        ans += dcnt(i,i)

    for i in range(2,m+1):  # Fill in the square
        for j in range(1,i):
            ans += 2*(dcnt(i,j))

    for i in range(m+1,n+1):  # Fill in the rectangle
        for j in range(1,m+1):
            ans += dcnt(i,j)
    return ans

#def cbcnt(x,y):  # Cumulative both count
#    ans = 0
#    for i in range(1,x+1):
#        for j in range(1,y+1):
#            ans += bcnt(i,j)
#    return ans
def cbcnt(x,y):  # Cumulative both count
    ans = 0
    m = min(x,y)
    n = max(x,y)

    for i in range(1,m+1):  # Process the diagonal
        ans += bcnt(i,i)

    for i in range(2,m+1):  # Fill in the square
        for j in range(1,i):
            ans += 2*(bcnt(i,j))

    for i in range(m+1,n+1):  # Fill in the rectangle
        for j in range(1,m+1):
            ans += bcnt(i,j)
    return ans

#answer = dcnt(3,2)
#expected = 19
#if (answer != expected):
#    print "Error: dcnt(3,2) = {0} but expecting {1}".format(answer,expected)
#    sys.exit()
#else:
#    print "OK: dcnt(3,2) = {0} as expected".format(answer)

#answer = cscnt(3,2)
#expected = 40
#if (answer != expected):
#    print "Error: cscnt(3,2) = {0} but expecting {1}".format(answer,expected)
#    sys.exit()
#else:
#    print "OK: cscnt(3,2) = {0} as expected".format(answer)

#answer = cscnt(47,43)
#expected = 261436560
#if (answer != expected):
#    print "Error: cscnt(47,43) = {0} but expecting {1}".format(answer,expected)
#    sys.exit()
#else:
#    print "OK: cscnt(47,43) = {0} as expected".format(answer)

#answer = cscnt(470,430)
#expected = 232374107894400
#if (answer != expected):
#    print "Error: cscnt(470,430) = {0} but expecting {1}".format(answer,expected)
#    sys.exit()
#else:
#    print "OK: cscnt(470,430) = {0} as expected".format(answer)

#answer = cscnt(1970,2430)
#expected = 3055709492512934400
#if (answer != expected):
#    print "Error: cscnt(1970,2430) = {0} but expecting {1}".format(answer,expected)
#    sys.exit()
#else:
#    print "OK: cscnt(1970,2430) = {0} as expected".format(answer)


answer = cbcnt(3,2)
expected = 72
if (answer != expected):
    print "Error: cbcnt(3,2) = {0} but expecting {1}".format(answer,expected)
    sys.exit()
else:
    print "OK: cbcnt(3,2) = {0} as expected".format(answer)

answer = cbcnt(47,43)
print "Answer =", answer

end_time = time.clock()
print "Time taken = {0} seconds".format(end_time-start_time)


sys.exit()

# grid 0: 1x1 count = 2, loc_maxl = 2
# grid 1: 1x1 count = 3, loc_maxl = 3
# grid 2: 1x1 count = 2, loc_maxl = 2
# 
# grid 0: 1x2 count = 1, loc_maxl = 2
# grid 1: 1x2 count = 2, loc_maxl = 3
# grid 2: 1x2 count = 1, loc_maxl = 2
# 
# grid 0: 1x3 count = 1, loc_maxl = 2  # wrong
# grid 1: 1x3 count = 1, loc_maxl = 3
# grid 2: 1x3 count = 1, loc_maxl = 2  # wrong
# 
# grid 0: 2x2 count = 1, loc_maxl = 2
# grid 1: 2x2 count = 1, loc_maxl = 2
# 
# grid 0: 2x3 count = 1, loc_maxl = 2  # wrong
# grid 1: 2x3 count = 1, loc_maxl = 2  # wrong
# 
# grid 0: 3x3 count = 1, loc_maxl = 0
