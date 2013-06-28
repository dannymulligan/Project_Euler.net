#!/usr/bin/python
#
# Project Euler.net Problem 096
#
# Su Doku (Japanese meaning number place) is the name given to a popular
# puzzle concept. Its origin is unclear, but credit must be attributed
# to Leonhard Euler who invented a similar, and much more difficult,
# puzzle idea called Latin Squares. The objective of Su Doku puzzles,
# however, is to replace the blanks (or zeros) in a 9 by 9 grid in such
# that each row, column, and 3 by 3 box contains each of the digits 1 to
# 9. Below is an example of a typical starting puzzle grid and its
# solution grid.
#
#     +-------+-------+-------+    +-------+-------+-------+
#     | 0 0 3 | 0 2 0 | 6 0 0 |    | 4 8 3 | 9 2 1 | 6 5 7 |
#     | 9 0 0 | 3 0 5 | 0 0 1 |    | 9 6 7 | 3 4 5 | 8 2 1 |
#     | 0 0 1 | 8 0 6 | 4 0 0 |    | 2 5 1 | 8 7 6 | 4 9 3 |
#     +-------+-------+-------+    +-------+-------+-------+
#     | 0 0 8 | 1 0 2 | 9 0 0 |    | 5 4 8 | 1 3 2 | 9 7 6 |
#     | 7 0 0 | 0 0 0 | 0 0 8 |    | 7 2 9 | 5 6 4 | 1 3 8 |
#     | 0 0 6 | 7 0 8 | 2 0 0 |    | 1 3 6 | 7 9 8 | 2 4 5 |
#     +-------+-------+-------+    +-------+-------+-------+
#     | 0 0 2 | 6 0 9 | 5 0 0 |    | 3 7 2 | 6 8 9 | 5 1 4 |
#     | 8 0 0 | 2 0 3 | 0 0 9 |    | 8 1 4 | 2 5 3 | 7 6 9 |
#     | 0 0 5 | 0 1 0 | 3 0 0 |    | 6 9 5 | 4 1 7 | 3 8 2 |
#     +-------+-------+-------+    +-------+-------+-------+
#
# A well constructed Su Doku puzzle has a unique solution and can be
# solved by logic, although it may be necessary to employ "guess and
# test" methods in order to eliminate options (there is much contested
# opinion over this). The complexity of the search determines the
# difficulty of the puzzle; the example above is considered easy because
# it can be solved by straight forward direct deduction.
#
# The 6K text file, sudoku.txt (right click and 'Save Link/Target
# As...'), contains fifty different Su Doku puzzles ranging in
# difficulty, but all with unique solutions (the first puzzle in the
# file is the example above).
#
# By solving all fifty puzzles find the sum of the 3-digit numbers found
# in the top left corner of each solution grid; for example, 483 is the
# 3-digit number found in the top left corner of the solution grid
# above.


import sys
import math
import itertools


################################
def new_res ():
    res = [[ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],

           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],

           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ],
           [ 0, 0, 0,  0, 0, 0,  0, 0, 0 ]]
    return res


################################
def new_poss ():
    poss = [[ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],
            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],
            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],

            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],
            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],
            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],

            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],
            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ],
            [ set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)),  set(range(1,10)), set(range(1,10)), set(range(1,10)) ]]
    return poss


################################
def print_res(res):
    g = [['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],
         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],
         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],

         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],
         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],
         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],

         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],
         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.'],
         ['.', '.', '.',  '.', '.', '.',  '.', '.', '.']]

    for x in range(9):
        for y in range(9):
            if (res[x][y] == 0):  g[x][y] = '.'
            else:                 g[x][y] = '{0}'.format(res[x][y])

    print "+-------+-------+-------+"
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][0], g[1][0], g[2][0],  g[3][0], g[4][0], g[5][0],  g[6][0], g[7][0], g[8][0])
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][1], g[1][1], g[2][1],  g[3][1], g[4][1], g[5][1],  g[6][1], g[7][1], g[8][1])
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][2], g[1][2], g[2][2],  g[3][2], g[4][2], g[5][2],  g[6][2], g[7][2], g[8][2])
    print "+-------+-------+-------+"
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][3], g[1][3], g[2][3],  g[3][3], g[4][3], g[5][3],  g[6][3], g[7][3], g[8][3])
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][4], g[1][4], g[2][4],  g[3][4], g[4][4], g[5][4],  g[6][4], g[7][4], g[8][4])
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][5], g[1][5], g[2][5],  g[3][5], g[4][5], g[5][5],  g[6][5], g[7][5], g[8][5])
    print "+-------+-------+-------+"
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][6], g[1][6], g[2][6],  g[3][6], g[4][6], g[5][6],  g[6][6], g[7][6], g[8][6])
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][7], g[1][7], g[2][7],  g[3][7], g[4][7], g[5][7],  g[6][7], g[7][7], g[8][7])
    print "| {0} {1} {2} | {3} {4} {5} | {6} {7} {8} |".format(g[0][8], g[1][8], g[2][8],  g[3][8], g[4][8], g[5][8],  g[6][8], g[7][8], g[8][8])
    print "+-------+-------+-------+"


################################
def print_poss(res,poss):
    g = [['', '', '',  '', '', '',  '', '', ''],
         ['', '', '',  '', '', '',  '', '', ''],
         ['', '', '',  '', '', '',  '', '', ''],

         ['', '', '',  '', '', '',  '', '', ''],
         ['', '', '',  '', '', '',  '', '', ''],
         ['', '', '',  '', '', '',  '', '', ''],

         ['', '', '',  '', '', '',  '', '', ''],
         ['', '', '',  '', '', '',  '', '', ''],
         ['', '', '',  '', '', '',  '', '', '']]

    for x in range(9):
        for y in range(9):
            if (res[x][y] == 0):  sss = '.'
            else:                 sss = ' '

            if (1 in poss[x][y]):  s1 = '1'
            else:                  s1 = sss
            if (2 in poss[x][y]):  s2 = '2'
            else:                  s2 = sss
            if (3 in poss[x][y]):  s3 = '3'
            else:                  s3 = sss
            if (4 in poss[x][y]):  s4 = '4'
            else:                  s4 = sss
            if (5 in poss[x][y]):  s5 = '5'
            else:                  s5 = sss
            if (6 in poss[x][y]):  s6 = '6'
            else:                  s6 = sss
            if (7 in poss[x][y]):  s7 = '7'
            else:                  s7 = sss
            if (8 in poss[x][y]):  s8 = '8'
            else:                  s8 = sss
            if (9 in poss[x][y]):  s9 = '9'
            else:                  s9 = sss
            g[x][y] = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9

    print "+---------------+---------------+---------------+"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][0][0:3], g[1][0][0:3], g[2][0][0:3],  g[3][0][0:3], g[4][0][0:3], g[5][0][0:3],  g[6][0][0:3], g[7][0][0:3], g[8][0][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][0][3:6], g[1][0][3:6], g[2][0][3:6],  g[3][0][3:6], g[4][0][3:6], g[5][0][3:6],  g[6][0][3:6], g[7][0][3:6], g[8][0][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][0][6:9], g[1][0][6:9], g[2][0][6:9],  g[3][0][6:9], g[4][0][6:9], g[5][0][6:9],  g[6][0][6:9], g[7][0][6:9], g[8][0][6:9])
    print "|               |               |               |"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][1][0:3], g[1][1][0:3], g[2][1][0:3],  g[3][1][0:3], g[4][1][0:3], g[5][1][0:3],  g[6][1][0:3], g[7][1][0:3], g[8][1][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][1][3:6], g[1][1][3:6], g[2][1][3:6],  g[3][1][3:6], g[4][1][3:6], g[5][1][3:6],  g[6][1][3:6], g[7][1][3:6], g[8][1][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][1][6:9], g[1][1][6:9], g[2][1][6:9],  g[3][1][6:9], g[4][1][6:9], g[5][1][6:9],  g[6][1][6:9], g[7][1][6:9], g[8][1][6:9])
    print "|               |               |               |"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][2][0:3], g[1][2][0:3], g[2][2][0:3],  g[3][2][0:3], g[4][2][0:3], g[5][2][0:3],  g[6][2][0:3], g[7][2][0:3], g[8][2][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][2][3:6], g[1][2][3:6], g[2][2][3:6],  g[3][2][3:6], g[4][2][3:6], g[5][2][3:6],  g[6][2][3:6], g[7][2][3:6], g[8][2][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][2][6:9], g[1][2][6:9], g[2][2][6:9],  g[3][2][6:9], g[4][2][6:9], g[5][2][6:9],  g[6][2][6:9], g[7][2][6:9], g[8][2][6:9])
    print "+---------------+---------------+---------------+"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][3][0:3], g[1][3][0:3], g[2][3][0:3],  g[3][3][0:3], g[4][3][0:3], g[5][3][0:3],  g[6][3][0:3], g[7][3][0:3], g[8][3][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][3][3:6], g[1][3][3:6], g[2][3][3:6],  g[3][3][3:6], g[4][3][3:6], g[5][3][3:6],  g[6][3][3:6], g[7][3][3:6], g[8][3][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][3][6:9], g[1][3][6:9], g[2][3][6:9],  g[3][3][6:9], g[4][3][6:9], g[5][3][6:9],  g[6][3][6:9], g[7][3][6:9], g[8][3][6:9])
    print "|               |               |               |"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][4][0:3], g[1][4][0:3], g[2][4][0:3],  g[3][4][0:3], g[4][4][0:3], g[5][4][0:3],  g[6][4][0:3], g[7][4][0:3], g[8][4][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][4][3:6], g[1][4][3:6], g[2][4][3:6],  g[3][4][3:6], g[4][4][3:6], g[5][4][3:6],  g[6][4][3:6], g[7][4][3:6], g[8][4][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][4][6:9], g[1][4][6:9], g[2][4][6:9],  g[3][4][6:9], g[4][4][6:9], g[5][4][6:9],  g[6][4][6:9], g[7][4][6:9], g[8][4][6:9])
    print "|               |               |               |"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][5][0:3], g[1][5][0:3], g[2][5][0:3],  g[3][5][0:3], g[4][5][0:3], g[5][5][0:3],  g[6][5][0:3], g[7][5][0:3], g[8][5][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][5][3:6], g[1][5][3:6], g[2][5][3:6],  g[3][5][3:6], g[4][5][3:6], g[5][5][3:6],  g[6][5][3:6], g[7][5][3:6], g[8][5][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][5][6:9], g[1][5][6:9], g[2][5][6:9],  g[3][5][6:9], g[4][5][6:9], g[5][5][6:9],  g[6][5][6:9], g[7][5][6:9], g[8][5][6:9])
    print "+---------------+---------------+---------------+"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][6][0:3], g[1][6][0:3], g[2][6][0:3],  g[3][6][0:3], g[4][6][0:3], g[5][6][0:3],  g[6][6][0:3], g[7][6][0:3], g[8][6][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][6][3:6], g[1][6][3:6], g[2][6][3:6],  g[3][6][3:6], g[4][6][3:6], g[5][6][3:6],  g[6][6][3:6], g[7][6][3:6], g[8][6][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][6][6:9], g[1][6][6:9], g[2][6][6:9],  g[3][6][6:9], g[4][6][6:9], g[5][6][6:9],  g[6][6][6:9], g[7][6][6:9], g[8][6][6:9])
    print "|               |               |               |"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][7][0:3], g[1][7][0:3], g[2][7][0:3],  g[3][7][0:3], g[4][7][0:3], g[5][7][0:3],  g[6][7][0:3], g[7][7][0:3], g[8][7][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][7][3:6], g[1][7][3:6], g[2][7][3:6],  g[3][7][3:6], g[4][7][3:6], g[5][7][3:6],  g[6][7][3:6], g[7][7][3:6], g[8][7][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][7][6:9], g[1][7][6:9], g[2][7][6:9],  g[3][7][6:9], g[4][7][6:9], g[5][7][6:9],  g[6][7][6:9], g[7][7][6:9], g[8][7][6:9])
    print "|               |               |               |"
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][8][0:3], g[1][8][0:3], g[2][8][0:3],  g[3][8][0:3], g[4][8][0:3], g[5][8][0:3],  g[6][8][0:3], g[7][8][0:3], g[8][8][0:3])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][8][3:6], g[1][8][3:6], g[2][8][3:6],  g[3][8][3:6], g[4][8][3:6], g[5][8][3:6],  g[6][8][3:6], g[7][8][3:6], g[8][8][3:6])
    print "| {0}  {1}  {2} | {3}  {4}  {5} | {6}  {7}  {8} |".format(g[0][8][6:9], g[1][8][6:9], g[2][8][6:9],  g[3][8][6:9], g[4][8][6:9], g[5][8][6:9],  g[6][8][6:9], g[7][8][6:9], g[8][8][6:9])
    print "+---------------+---------------+---------------+"

    print "score = {0:4.3f}".format(score_poss(poss))


################################
def score_poss(poss):
    score = 0.0
    for x in range(9):
        for y in range(9):
            score += math.log(len(poss[x][y]))
    return score


################################
def fix_xyn(res,poss, x, y, n):
    #print "    fix_xyn(res,poss, {0}, {1}, {2})".format(x, y, n)
    res[x][y] = n

    for ix in range(9):
       poss[ix][y].discard(n)
    for iy in range(9):
       poss[x][iy].discard(n)
    ix = 3 * (x / 3)
    iy = 3 * (y / 3)
    poss[ix+0][iy+0].discard(n);  poss[ix+1][iy+0].discard(n);  poss[ix+2][iy+0].discard(n)
    poss[ix+0][iy+1].discard(n);  poss[ix+1][iy+1].discard(n);  poss[ix+2][iy+1].discard(n)
    poss[ix+0][iy+2].discard(n);  poss[ix+1][iy+2].discard(n);  poss[ix+2][iy+2].discard(n)

    poss[x][y].clear()
    poss[x][y].add(n)


################################
def read_puzzle(res,poss, src_file):
    for y in range(9):
        l = src_file.next()
        for x in range(9):
            v = int(l[x])
            if (v != 0):
                fix_xyn(res,poss, x, y, v)


################################
def solve_done(res,poss):
    for x in range(9):
        for y in range(9):
            if (res[x][y] == 0):
                return False
    return True


################################
def solve_singleton(res,poss):
    # find cells with only one possibility
    progress = False
    for x in range(9):
        for y in range(9):
            if (res[x][y] == 0) & (len(poss[x][y]) == 1):
                fix_xyn(res,poss, x, y, poss[x][y].pop())
                progress = True
    return progress


################################
def to_list(cell):
    res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1,10):
        if (i in cell):
            res[i] = 1
    res[0] = sum(res[1:])
    return res


################################
def find_unique(res,poss, cells):
# cells = [(x0,y0), (x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5), (x6,y6), (x7,y7), (x8,y8)]
    #print "find_unique(res,poss, {0})".format(cells),
    progress = False

    for n in range(1,10):
        (cnt, loc) = (0, 0)
        for cell in range(9):
            (x, y) = cells[cell]
            if (n in poss[x][y]):  (cnt, loc) = (cnt + 1, cell)
        if (cnt == 1):
            (x, y) = cells[loc]
            if (res[x][y] == 0):
                fix_xyn(res,poss, x, y, n)
                progress = True

    #print "score = {0:4.3f}".format(score_poss(poss))
    return progress


################################
def solve_unique(res,poss):
    # find numbers that only appear once in an area
    progress = False

    # horizontal
    for i in range(9):
        progress = progress | find_unique(res,poss, [(0,i), (1,i), (2,i), (3,i), (4,i), (5,i), (6,i), (7,i), (8,i)])

    # vertical
    for i in range(9):
        progress = progress | find_unique(res,poss, [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)])

    # boxes
    for x in range(0,7,3):
        for y in range(0,7,3):
           progress = progress | find_unique(res,poss, [(x+0,y+0), (x+0,y+1), (x+0,y+2), (x+1,y+0), (x+1,y+1), (x+1,y+2), (x+2,y+0), (x+2,y+1), (x+2,y+2)])

    return progress


################################
def find_overlap(res,poss, ccells, lcells, rcells):
# ccells = [(x0,y0), (x1,y1), (x2,y2)]
# lcells = [(x0,y0), (x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5)]
# rcells = [(x0,y0), (x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5)]
    #print "find_overlap(res,poss, {0}, {1}, {2})".format(ccells, lcells, rcells),
    progress = False

    cset = set()
    for (cx, cy) in ccells:
        cset = cset | poss[cx][cy]

    lset = set()
    for (lx, ly) in lcells:
        lset = lset | poss[lx][ly]

    rset = set()
    for (rx, ry) in rcells:
        rset = rset | poss[rx][ry]

    #print_poss(res,poss)
    #print "cset = ", cset
    #print "lset = ", lset
    #print "rset = ", rset

    for n in range(1,10):
        if ((n in lset) and (n in cset) and not(n in rset)):
            for (lx, ly) in lcells:
                poss[lx][ly].discard(n)
            progress = True

        if (not (n in lset) and (n in cset) and (n in rset)):
            for (rx, ry) in rcells:
                poss[rx][ry].discard(n)
            progress = True

    #print "score = {0:4.3f}".format(score_poss(poss))
    return progress


################################
def solve_overlap(res,poss):
    # spread knowledge through set overlaps
    progress = False

    # horizontal line <-> box
    for x in range(3):
        for y in range(9):
            (cx, cy) = (x*3, y)

            if (x == 0):
                (l0x, l0y) = (3,y)
                (l1x, l1y) = (6,y)
            elif (x == 1):
                (l0x, l0y) = (0,y)
                (l1x, l1y) = (6,y)
            else:
                (l0x, l0y) = (0,y)
                (l1x, l1y) = (3,y)

            if ((y % 3) == 0):
                (b0x, b0y) = (x*3,y+1)
                (b1x, b1y) = (x*3,y+2)
            elif ((y % 3) == 1):
                (b0x, b0y) = (x*3,y-1)
                (b1x, b1y) = (x*3,y+1)
            else:
                (b0x, b0y) = (x*3,y-2)
                (b1x, b1y) = (x*3,y-1)

            progress = progress | find_overlap(res,poss, [(cx+0,cy), (cx+1,cy), (cx+2,cy)],
                                                         [(l0x+0,l0y), (l0x+1,l0y), (l0x+2,l0y),  (l1x+0,l1y), (l1x+1,l1y), (l1x+2,l1y)],
                                                         [(b0x+0,b0y), (b0x+1,b0y), (b0x+2,b0y),  (b1x+0,b1y), (b1x+1,b1y), (b1x+2,b1y)])


    # vertical line <-> box
    for y in range(3):
        for x in range(9):
            (cx, cy) = (x, y*3)

            if (y == 0):
                (l0x, l0y) = (x,3)
                (l1x, l1y) = (x,6)
            elif (y == 1):
                (l0x, l0y) = (x,0)
                (l1x, l1y) = (x,6)
            else:
                (l0x, l0y) = (x,0)
                (l1x, l1y) = (x,3)

            if ((x % 3) == 0):
                (b0x, b0y) = (x+1,y*3)
                (b1x, b1y) = (x+2,y*3)
            elif ((x % 3) == 1):
                (b0x, b0y) = (x-1,y*3)
                (b1x, b1y) = (x+1,y*3)
            else:
                (b0x, b0y) = (x-2,y*3)
                (b1x, b1y) = (x-1,y*3)

            progress = progress | find_overlap(res,poss, [(cx,cy+0), (cx,cy+1), (cx,cy+2)],
                                                         [(l0x,l0y+0), (l0x,l0y+1), (l0x,l0y+2),  (l1x,l1y+0), (l1x,l1y+1), (l1x,l1y+2)],
                                                         [(b0x,b0y+0), (b0x,b0y+1), (b0x,b0y+2),  (b1x,b1y+0), (b1x,b1y+1), (b1x,b1y+2)])

    return progress


################################
def find_doubles(res,poss, cells):
# cells = [(x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2)]
    #print "find_doubles(res,poss, {0})".format(cells),
    progress = False

    for a in range(8):
        for b in range(a+1,9):
            (xa,ya) = cells[a]
            (xb,yb) = cells[b]

            if ((res[xa][ya] != 0) or (res[xb][yb] != 0)):
                continue

            combo = poss[xa][ya] | poss[xb][yb]

            if (len(combo) == 2):
                for c in range(9):
                    if ((c == a) or (c == b)):
                        continue
                    (xc,yc) = cells[c]
                    for d in combo:
                        if (d in poss[xc][yc]):
                            progress = True
                            poss[xc][yc].discard(d)

    #print "score = {0:4.3f}".format(score_poss(poss))
    return progress


################################
def solve_doubles(res,poss):
    # eliminate possibilities by finding doubles
    progress = False

    # horizontal
    for i in range(9):
        progress = progress | find_doubles(res,poss, [(0,i), (1,i), (2,i), (3,i), (4,i), (5,i), (6,i), (7,i), (8,i)])

    # vertical
    for i in range(9):
        progress = progress | find_doubles(res,poss, [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)])

    # boxes
    for x in range(0,7,3):
        for y in range(0,7,3):
           progress = progress | find_doubles(res,poss, [(x+0,y+0), (x+0,y+1), (x+0,y+2), (x+1,y+0), (x+1,y+1), (x+1,y+2), (x+2,y+0), (x+2,y+1), (x+2,y+2)])

    return progress


################################
def find_trebles(res,poss, cells):
# cells = [(x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2)]
    #print "find_trebles(res,poss, {0})".format(cells),
    progress = False

    for a in range(7):
        for b in range(a+1,8):
            for c in range(b+1,9):
                (xa,ya) = cells[a]
                (xb,yb) = cells[b]
                (xc,yc) = cells[c]

                if ((res[xa][ya] != 0) or (res[xb][yb] != 0) or (res[xc][yc] != 0)):
                    continue

                combo = poss[xa][ya] | poss[xb][yb] | poss[xc][yc]

                if (len(combo) == 3):
                    for d in range(9):
                        if ((d == a) or (d == b) or (d == c)):  continue
                        (xd,yd) = cells[d]
                        for e in combo:
                            if (e in poss[xd][yd]):
                                progress = True
                                poss[xd][yd].discard(e)

    #print "score = {0:4.3f}".format(score_poss(poss))
    return progress


################################
def solve_trebles(res,poss):
    # eliminate possibilities by finding trebles
    progress = False

    # horizontal
    for i in range(9):
        progress = progress | find_trebles(res,poss, [(0,i), (1,i), (2,i), (3,i), (4,i), (5,i), (6,i), (7,i), (8,i)])

    # vertical
    for i in range(9):
        progress = progress | find_trebles(res,poss, [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)])

    # boxes
    for x in range(0,7,3):
        for y in range(0,7,3):
           progress = progress | find_trebles(res,poss, [(x+0,y+0), (x+0,y+1), (x+0,y+2), (x+1,y+0), (x+1,y+1), (x+1,y+2), (x+2,y+0), (x+2,y+1), (x+2,y+2)])

    return progress


################################
def find_quads(res,poss, cells):
# cells = [(x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2)]
    #print "find_quads(res,poss, {0})".format(cells),
    progress = False

    for a in range(6):
        for b in range(a+1,7):
            for c in range(b+1,8):
                for d in range(c+1,9):
                    (xa,ya) = cells[a]
                    (xb,yb) = cells[b]
                    (xc,yc) = cells[c]
                    (xd,yd) = cells[d]

                    if ((res[xa][ya] != 0) or (res[xb][yb] != 0) or (res[xc][yc] != 0) or (res[xd][yd] != 0)):
                        continue

                    combo = poss[xa][ya] | poss[xb][yb] | poss[xc][yc] | poss[xd][yd]

                    if (len(combo) == 4):
                        for e in range(9):
                            if ((e == a) or (e == b) or (e == c) or (e == d)):  continue
                            (xe,ye) = cells[e]
                            for f in combo:
                                if (f in poss[xe][ye]):
                                    progress = True
                                    poss[xe][ye].discard(f)

    #print "score = {0:4.3f}".format(score_poss(poss))
    return progress


################################
def solve_quads(res,poss):
    # eliminate possibilities by finding quads
    progress = False

    # horizontal
    for i in range(9):
        progress = progress | find_quads(res,poss, [(0,i), (1,i), (2,i), (3,i), (4,i), (5,i), (6,i), (7,i), (8,i)])

    # vertical
    for i in range(9):
        progress = progress | find_quads(res,poss, [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)])

    # boxes
    for x in range(0,7,3):
        for y in range(0,7,3):
           progress = progress | find_quads(res,poss, [(x+0,y+0), (x+0,y+1), (x+0,y+2), (x+1,y+0), (x+1,y+1), (x+1,y+2), (x+2,y+0), (x+2,y+1), (x+2,y+2)])

    return progress


################################
def find_group2(res,poss, cells):
# cells = [(x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2)]
    #print "find_group2(res,poss, {0})".format(cells),
    progress = False

    combo = set()
    for a in range(9):
        (x,y) = cells[a]
        if (res[x][y] == 0):
            combo = combo | poss[x][y]

    if (len(combo) > 2):
        for c2 in itertools.combinations(combo,2):
            cfound = []
            for a in range(9):
                (x,y) = cells[a]
                if (len(set(c2) & poss[x][y]) > 0):
                    cfound.append((x,y))

            if (len(cfound) == 2):
                (xa,ya) = cfound[0]
                (xb,yb) = cfound[1]
                if (len(poss[xa][ya]) > 2):
                    poss[xa][ya] = set(c2)
                    progress = True
                if (len(poss[xb][yb]) > 2):
                    poss[xb][yb] = set(c2)
                    progress = True

    #print "score = {0:4.3f}".format(score_poss(poss))
    return progress


################################
def solve_group2(res,poss):
    # eliminate possibilities by finding groups of 2
    progress = False

    # horizontal
    for i in range(9):
        progress = progress | find_group2(res,poss, [(0,i), (1,i), (2,i), (3,i), (4,i), (5,i), (6,i), (7,i), (8,i)])

    # vertical
    for i in range(9):
        progress = progress | find_group2(res,poss, [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)])

    # boxes
    for x in range(0,7,3):
        for y in range(0,7,3):
           progress = progress | find_group2(res,poss, [(x+0,y+0), (x+0,y+1), (x+0,y+2), (x+1,y+0), (x+1,y+1), (x+1,y+2), (x+2,y+0), (x+2,y+1), (x+2,y+2)])

    return progress


################################
def find_group3(res,poss, cells):
# cells = [(x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2), (x0,y0), (x1,y1), (x2,y2)]
    #print "find_group2(res,poss, {0})".format(cells),
    progress = False

    combo = set()
    for a in range(9):
        (x,y) = cells[a]
        if (res[x][y] == 0):
            combo = combo | poss[x][y]

    if (len(combo) > 3):
        for c3 in itertools.combinations(combo,3):
            cfound = []
            for a in range(9):
                (x,y) = cells[a]
                if (len(set(c3) & poss[x][y]) > 0):
                    cfound.append((x,y))

            if (len(cfound) == 3):
                (xa,ya) = cfound[0]
                (xb,yb) = cfound[1]
                (xc,yc) = cfound[2]
                if (len(poss[xa][ya]) > 3):
                    poss[xa][ya] = set(c3)
                    progress = True
                if (len(poss[xb][yb]) > 3):
                    poss[xb][yb] = set(c3)
                    progress = True
                if (len(poss[xc][yc]) > 3):
                    poss[xc][yc] = set(c3)
                    progress = True

    #print "score = {0:4.3f}".format(score_poss(poss))
    return progress


################################
def solve_group3(res,poss):
    # eliminate possibilities by finding groups of 3
    progress = False

    # horizontal
    for i in range(9):
        progress = progress | find_group3(res,poss, [(0,i), (1,i), (2,i), (3,i), (4,i), (5,i), (6,i), (7,i), (8,i)])

    # vertical
    for i in range(9):
        progress = progress | find_group3(res,poss, [(i,0), (i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8)])

    # boxes
    for x in range(0,7,3):
        for y in range(0,7,3):
           progress = progress | find_group3(res,poss, [(x+0,y+0), (x+0,y+1), (x+0,y+2), (x+1,y+0), (x+1,y+1), (x+1,y+2), (x+2,y+0), (x+2,y+1), (x+2,y+2)])

    return progress


################################
def solve_xwing(res,poss):
    # eliminate possibilities between pairs of possibilities
    progress = False

    # if N only exists in rows y0 & y1 in the 4 places shown
    #   then N can't exist anywhere else on columns x0 or x1
    #  (x0,y0) -- (x1,y0)
    #     |          |
    #  (x0,y1) -- (x1,y1)
    #
    # then repeat with columns and rows swapped

    for n in range(1,10):
        #print "xwing: searching with n={0}".format(n)
        # find n in 2 possible places on 2 rows, and use to eliminate n on 2 columns
        for y0 in range(8):
            y0cnt = 0
            for x in range(9):
                if (res[x][y0] != 0):  continue
                if (n in poss[x][y0]):  y0cnt += 1
            if (y0cnt != 2):  continue
            # we've found y0

            for y1 in range(y0+1,9):
                y1cnt = 0
                for x in range(9):
                    if (res[x][y1] != 0):  continue
                    if (n in poss[x][y1]):  y1cnt += 1
                if (y1cnt != 2):  continue
                # we've found y0 & y1
                #print "Found y0={0}, y1={1}, y0cnt={2}, y1cnt={3}".format(y0, y1, y0cnt, y1cnt)

                for x0 in range(8):
                    if (res[x0][y0] != 0):  continue
                    if (n in poss[x0][y0]):  break
                # we've found (x0,y0)

                for x1 in range(x0+1,9):
                    if (res[x1][y0] != 0):  continue
                    if (n in poss[x1][y0]):  break
                # we've found (x1,y0)

                if (res[x0][y1] != 0):  continue
                if (res[x1][y1] != 0):  continue
                if not(n in poss[x0][y1]):  continue
                if not(n in poss[x1][y1]):  continue
                # we've verified that (x0,y0) and (x1,y0) are the only cells in row y0 containing n
                # we've verified that (x0,y1) and (x1,y1) are the only cells in row y1 containing n

                #print "Found (x0,y0)={0}={1} (x1,y0)={2}={3}".format((x0,y0), poss[x0][y0], (x1,y0), poss[x1][y0])
                #print "  ... (x0,y1)={0}={1} (x1,y1)={2}={3}".format((x0,y1), poss[x0][y1], (x1,y1), poss[x1][y1])

                for y in range(9):
                    if ((y == y0) or (y == y1)):  continue
                    if (n in poss[x0][y]):
                        #print "    poss[{0}][{1}].discard({2})".format(x0,y,n)
                        progress = True
                        poss[x0][y].discard(n)
                    if (n in poss[x1][y]):
                        #print "    poss[{0}][{1}].discard({2})".format(x1,y,n)
                        progress = True
                        poss[x1][y].discard(n)

    for n in range(1,10):
        #print "xwing: searching with n={0}".format(n)
        # find n in 2 possible places on 2 rows, and use to eliminate n on 2 columns
        for x0 in range(8):
            x0cnt = 0
            for y in range(9):
                if (res[x0][y] != 0):  continue
                if (n in poss[x0][y]):  x0cnt += 1
            if (x0cnt != 2):  continue
            # we've found x0

            for x1 in range(x0+1,9):
                x1cnt = 0
                for y in range(9):
                    if (res[x1][y] != 0):  continue
                    if (n in poss[x1][y]):  x1cnt += 1
                if (x1cnt != 2):  continue
                # we've found x0 & x1
                #print "Found x0={0}, x1={1}, x0cnt={2}, x1cnt={3}".format(x0, x1, x0cnt, x1cnt)

                for y0 in range(8):
                    if (res[x0][y0] != 0):  continue
                    if (n in poss[x0][y0]):  break
                # we've found (x0,y0)

                for y1 in range(y0+1,9):
                    if (res[x0][y1] != 0):  continue
                    if (n in poss[x0][y1]):  break
                # we've found (x0,y1)

                if (res[x1][y0] != 0):  continue
                if (res[x1][y1] != 0):  continue
                if not(n in poss[x1][y0]):  continue
                if not(n in poss[x1][y1]):  continue
                # we've verified that (x0,y0) and (x0,y1) are the only cells in column x0 containing n
                # we've verified that (x1,y0) and (x1,y1) are the only cells in column x1 containing n

                #print "Found (x0,y0)={0}={1} (x0,y1)={2}={3}".format((x0,y0), poss[x0][y0], (x0,y1), poss[x0][y1])
                #print "  ... (x1,y0)={0}={1} (x1,y1)={2}={3}".format((x1,y0), poss[x1][y0], (x1,y1), poss[x1][y1])

                for x in range(9):
                    if ((x == x0) or (x == x1)):  continue
                    if (n in poss[x][y0]):
                        #print "    poss[{0}][{1}].discard({2})".format(x,y0,n)
                        progress = True
                        poss[x][y0].discard(n)
                    if (n in poss[x][y1]):
                        #print "    poss[{0}][{1}].discard({2})".format(x,y1,n)
                        progress = True
                        poss[x][y1].discard(n)

    return progress


################################
def solve_swordfish(res,poss):
    # eliminate possibilities between triples of possibilities
    progress = False

    # if N only exists in rows y0, y1, & y2 in the 9 places shown
    #   then N can't exist anywhere else on columns x0, x1, or x2
    #  (x0,y0) -- (x1,y0) -- (x2,y0)
    #     |          |          |
    #  (x0,y1) -- (x1,y1) -- (x2,y1)
    #     |          |          |
    #  (x0,y2) -- (x1,y2) -- (x2,y2)
    #
    # then repeat with columns and rows swapped

    for n in range(1,10):
        print "swordfish: searching with n={0}".format(n)
        # find n in 3 possible places on 3 rows, and use to eliminate n on 3 columns
        for y0 in range(7):
            y0cnt = 0
            for x in range(9):
                if (res[x][y0] != 0):  continue
                if (n in poss[x][y0]):  y0cnt += 1
            if (y0cnt != 3):  continue
            # we've found y0

            for y1 in range(y0+1,8):
                y1cnt = 0
                for x in range(9):
                    if (res[x][y1] != 0):  continue
                    if (n in poss[x][y1]):  y1cnt += 1
                if (y1cnt != 3):  continue
                # we've found y0 & y1

                for y2 in range(y1+1,9):
                    y2cnt = 0
                    for x in range(9):
                        if (res[x][y2] != 0):  continue
                        if (n in poss[x][y2]):  y1cnt += 1
                    if (y2cnt != 3):  continue
                    # we've found y0, y1, & y2
                    print "Found y0={0}, y1={1}, y2={2}, y0cnt={3}, y1cnt={4}, y2cnt={5}".format(y0, y1, y2, y0cnt, y1cnt, y2cnt)

                    for x0 in range(7):
                        if (res[x0][y0] != 0):  continue
                        if (n in poss[x0][y0]):  break
                    # we've found (x0,y0)

                    for x1 in range(x0+1,8):
                        if (res[x1][y0] != 0):  continue
                        if (n in poss[x1][y0]):  break
                    # we've found (x1,y0)

                    for x2 in range(x1+1,9):
                        if (res[x2][y0] != 0):  continue
                        if (n in poss[x2][y0]):  break
                    # we've found (x2,y0)

                    if (res[x0][y1] != 0):  continue
                    if (res[x1][y1] != 0):  continue
                    if (res[x2][y1] != 0):  continue
                    if (res[x0][y2] != 0):  continue
                    if (res[x1][y2] != 0):  continue
                    if (res[x2][y2] != 0):  continue
                    if not(n in poss[x0][y1]):  continue
                    if not(n in poss[x1][y1]):  continue
                    if not(n in poss[x2][y1]):  continue
                    if not(n in poss[x0][y2]):  continue
                    if not(n in poss[x1][y2]):  continue
                    if not(n in poss[x2][y2]):  continue
                    # we've verified that (x0,y0), (x1,y0) & (x2,y0) are the only cells in row y0 containing n
                    # we've verified that (x0,y1), (x1,y1) & (x2,y1) are the only cells in row y1 containing n
                    # we've verified that (x0,y2), (x1,y2) & (x2,y2) are the only cells in row y2 containing n

                    print "Found (x0,y0)={0}={1} (x1,y0)={2}={3} (x2,y0)={4}={5}".format((x0,y0), poss[x0][y0], (x1,y0), poss[x1][y0], (x2,y0), poss[x2][y0])
                    print "  ... (x0,y1)={0}={1} (x1,y1)={2}={3} (x2,y1)={4}={5}".format((x0,y1), poss[x0][y1], (x1,y1), poss[x1][y1], (x2,y1), poss[x2][y1])
                    print "  ... (x0,y2)={0}={1} (x1,y2)={2}={3} (x2,y2)={4}={5}".format((x0,y2), poss[x0][y2], (x1,y2), poss[x1][y2], (x2,y2), poss[x2][y2])

                    for y in range(9):
                        if ((y == y0) or (y == y1) or (y == y2)):  continue
                        if (n in poss[x0][y]):
                            print "    poss[{0}][{1}].discard({2})".format(x0,y,n)
                            progress = True
                            poss[x0][y].discard(n)
                        if (n in poss[x1][y]):
                            print "    poss[{0}][{1}].discard({2})".format(x1,y,n)
                            progress = True
                            poss[x1][y].discard(n)
                        if (n in poss[x2][y]):
                            print "    poss[{0}][{1}].discard({2})".format(x2,y,n)
                            progress = True
                            poss[x2][y].discard(n)

    for n in range(1,10):
        print "swordfish: searching with n={0}".format(n)
        # find n in 3 possible places on 3 rows, and use to eliminate n on 3 columns
        for x0 in range(7):
            x0cnt = 0
            for y in range(9):
                if (res[x0][y] != 0):  continue
                if (n in poss[x0][y]):  x0cnt += 1
            if (x0cnt != 3):  continue
            # we've found x0
            print "Found x0={0}, x0cnt={1}".format(x0, x0cnt)

            for x1 in range(x0+1,8):
                x1cnt = 0
                for y in range(9):
                    if (res[x1][y] != 0):  continue
                    if (n in poss[x1][y]):  x1cnt += 1
                if (x1cnt != 3):  continue
                # we've found x0 & x1
                print "Found x0={0}, x1={1}, x0cnt={2}, x1cnt={3}".format(x0, x1, x0cnt, x1cnt)

                for x2 in range(x1+1,9):
                    x2cnt = 0
                    for y in range(9):
                        if (res[x2][y] != 0):  continue
                        if (n in poss[x2][y]):  x1cnt += 1
                    if (x2cnt != 3):  continue
                    # we've found x0, x1, & x2
                    print "Found x0={0}, x1={1}, x2={2}, x0cnt={3}, x1cnt={4}, x2cnt={5}".format(x0, x1, x2, x0cnt, x1cnt, x2cnt)

                    for y0 in range(7):
                        if (res[x0][y0] != 0):  continue
                        if (n in poss[x0][y0]):  break
                    # we've found (x0,y0)

                    for y1 in range(y0+1,8):
                        if (res[x0][y1] != 0):  continue
                        if (n in poss[x0][y1]):  break
                    # we've found (x0,y1)

                    for y2 in range(y1+1,9):
                        if (res[x0][y2] != 0):  continue
                        if (n in poss[x0][y2]):  break
                    # we've found (x0,y2)

                    if (res[x1][y0] != 0):  continue
                    if (res[x1][y1] != 0):  continue
                    if (res[x1][y2] != 0):  continue
                    if (res[x2][y0] != 0):  continue
                    if (res[x2][y1] != 0):  continue
                    if (res[x2][y2] != 0):  continue
                    if not(n in poss[x1][y0]):  continue
                    if not(n in poss[x1][y1]):  continue
                    if not(n in poss[x1][y2]):  continue
                    if not(n in poss[x2][y0]):  continue
                    if not(n in poss[x2][y1]):  continue
                    if not(n in poss[x2][y2]):  continue
                    # we've verified that (x0,y0), (x0,y1) & (x0,y2) are the only cells in column x0 containing n
                    # we've verified that (x1,y0), (x1,y1) & (x1,y2) are the only cells in column x1 containing n
                    # we've verified that (x2,y0), (x2,y1) & (x2,y2) are the only cells in column x2 containing n

                    print "Found (x0,y0)={0}={1} (x0,y1)={2}={3} (x0,y2)={4}={5}".format((x0,y0), poss[x0][y0], (x0,y1), poss[x0][y1], (x0,y2), poss[x0][y2])
                    print "  ... (x1,y0)={0}={1} (x1,y1)={2}={3} (x1,y2)={4}={5}".format((x1,y0), poss[x1][y0], (x1,y1), poss[x1][y1], (x1,y2), poss[x1][y2])
                    print "  ... (x2,y0)={0}={1} (x2,y1)={2}={3} (x2,y2)={4}={5}".format((x2,y0), poss[x2][y0], (x2,y1), poss[x2][y1], (x2,y2), poss[x2][y2])

                    for x in range(9):
                        if ((x == x0) or (x == x1) or (x == x2)):  continue
                        if (n in poss[x][y0]):
                            print "    poss[{0}][{1}].discard({2})".format(x,y0,n)
                            progress = True
                            poss[x][y0].discard(n)
                        if (n in poss[x][y1]):
                            print "    poss[{0}][{1}].discard({2})".format(x,y1,n)
                            progress = True
                            poss[x][y1].discard(n)
                        if (n in poss[x][y2]):
                            print "    poss[{0}][{1}].discard({2})".format(x,y2,n)
                            progress = True
                            poss[x][y2].discard(n)

    return progress


################################
def solve_symmetry(res,poss):
    # eliminate possibilities by breaking symmetries
    progress = False

    # if 3 of these locations have the same pair of possibilities,
    #   then we can eliminate both possibilities from the 4th location
    #  (x0,y0) -- (x1,y0)
    #     |          |
    #  (x0,y1) -- (x1,y1)

    for x0 in range(8):
        for y0 in range(8):
            if (res[x0][y0] != 0):  continue
            if (len(poss[x0][y0]) != 2):  continue

            for x1 in range(x0+1,9):
                if (res[x1][y0] != 0):  continue
                if (len(poss[x0][y0] | poss[x1][y0]) != 2):  continue
                # (x0,y0), & (x1,y0) have the same pair of possibilities

                for y1 in range(9):
                    if (y1 == y0):  continue

                    if (len(poss[x0][y0] | poss[x1][y1]) == 2):
                        # (x0,y0), (x1,y0), & (x1,y1) have the same pair of possibilities
                        # remove those possibilites from (x0,y1)
                        for d in poss[x0][y0]:
                            if not(d in poss[x0][y1]):  continue
                            progress = True
                            poss[x0][y1].discard(d)

                    if (len(poss[x0][y0] | poss[x0][y1]) == 2):
                        # (x0,y0), (x1,y0), & (x0,y1) have the same pair of possibilities
                        # remove those possibilites from (x1,y1)
                        for d in poss[x0][y0]:
                            if not(d in poss[x1][y1]):  continue
                            progress = True
                            poss[x1][y1].discard(d)

    return progress


################################
def solve_puzzle(res,poss):
    global score_from_starting_score
    global score_from_solve_singleton
    global score_from_solve_unique   
    global score_from_solve_overlap  
    global score_from_solve_doubles  
    global score_from_solve_trebles  
    global score_from_solve_quads
    global score_from_solve_group2   
    global score_from_solve_group3   
    global score_from_solve_xwing    
    global score_from_solve_swordfish
    global score_from_solve_symmetry 


    score = score_poss(poss)
    score_from_starting_score += score
    old_score = score
    iteration = 0
    print "score = {0:4.3f}".format(score)
    while not(solve_done(res,poss)):
        iteration += 1
        #print "==== Iteration {0} ====".format(iteration)
        #print_res(res)
        #print_poss(res,poss)

        if (iteration > 25):
            print "Iteration limit reached!"
            sys.exit()

        if solve_singleton(res,poss):
            score = score_poss(poss)
            print "solve_singleton reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_singleton += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_singleton"

        if solve_unique(res,poss):
            score = score_poss(poss)
            print "solve_unique reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_unique    += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_unique"

        if solve_overlap(res,poss):
            score = score_poss(poss)
            print "solve_overlap reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_overlap   += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_overlap"

        if solve_doubles(res,poss):
            score = score_poss(poss)
            print "solve_doubles reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_doubles   += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_doubles"

        if solve_trebles(res,poss):
            score = score_poss(poss)
            print "solve_trebles reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_trebles   += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_trebles"

        if solve_quads(res,poss):
            score = score_poss(poss)
            print "solve_quads reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_quads     += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_quads"

        if solve_group2(res,poss):
            score = score_poss(poss)
            print "solve_group2 reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_group2    += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_group2"

        if solve_group3(res,poss):
            score = score_poss(poss)
            print "solve_group3 reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_group3    += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_group3"
        
        if solve_xwing(res,poss):
            score = score_poss(poss)
            print "solve_xwing reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_xwing     += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_xwing"
        
        if solve_swordfish(res,poss):
            score = score_poss(poss)
            print "solve_swordfish reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_swordfish += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_swordfish"
        
        if solve_symmetry(res,poss):
            score = score_poss(poss)
            print "solve_symmetry reduced score by {0:4.3f} to {1:4.3f}".format(old_score-score, score)
            score_from_solve_symmetry  += (old_score - score)
            old_score = score
            continue
        else:
            print "no progress from solve_symmetry"

        print "==== Out of ideas on iteration {0} ====".format(iteration)
        return False
    return True


################################
##r1, p1 = new_res(), new_poss()
##r2, p2 = new_res(), new_poss()
##
##print_res(r1)
##print_poss(r1,p1)
##
##fix_xyn(r2, p2, 1, 2, 7)
##fix_xyn(r2, p2, 2, 8, 7)
##print_res(r2)
##print_poss(r2,p2)
##
##import sys
##sys.exit()

s_file = open("./sudoku.txt", "r")


score_from_starting_score = 0.0
score_from_solve_singleton = 0.0
score_from_solve_unique    = 0.0
score_from_solve_overlap   = 0.0
score_from_solve_doubles   = 0.0
score_from_solve_trebles   = 0.0
score_from_solve_quads     = 0.0
score_from_solve_group2    = 0.0
score_from_solve_group3    = 0.0
score_from_solve_xwing     = 0.0
score_from_solve_swordfish = 0.0
score_from_solve_symmetry  = 0.0

answer = 0
puzzles_tried = 0
puzzles_solved = 0
for line in s_file:
    description = line
    print "================================"
    print description[:-1]

    gr, gp = new_res(), new_poss()
    read_puzzle(gr, gp, s_file)
    print_res(gr)

    solved = solve_puzzle(gr, gp)
    puzzles_tried += 1
    if (solved):
        puzzles_solved += 1
        print "Solution for", description[:-1]
        print_res(gr)
        answer += gr[0][0]*100 + gr[1][0]*10 + gr[2][0]
    else:
        print "Failed to find solution for", description
        print_poss(gr,gp)

    print "{0} puzzles solved out of {1} tried".format(puzzles_solved, puzzles_tried)

print "Answer =", answer

print "Average starting score =", score_from_starting_score / puzzles_tried
print "Average contribution from solve_singleton =", score_from_solve_singleton / puzzles_tried
print "Average contribution from solve_unique    =", score_from_solve_unique    / puzzles_tried
print "Average contribution from solve_overlap   =", score_from_solve_overlap   / puzzles_tried
print "Average contribution from solve_doubles   =", score_from_solve_doubles   / puzzles_tried
print "Average contribution from solve_trebles   =", score_from_solve_trebles   / puzzles_tried
print "Average contribution from solve_quads     =", score_from_solve_quads     / puzzles_tried
print "Average contribution from solve_group2    =", score_from_solve_group2    / puzzles_tried
print "Average contribution from solve_group3    =", score_from_solve_group3    / puzzles_tried
print "Average contribution from solve_xwing     =", score_from_solve_xwing     / puzzles_tried
print "Average contribution from solve_swordfish =", score_from_solve_swordfish / puzzles_tried
print "Average contribution from solve_symmetry  =", score_from_solve_symmetry  / puzzles_tried

# Other ideas to implement
#  speculative
