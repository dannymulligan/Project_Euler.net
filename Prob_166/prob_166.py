#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 166
#
# Criss Cross
#
# A 4x4 grid is filled with digits d, 0 <= d <= 9.
#
# It can be seen that in the grid
# 
#     6 3 3 0
#     5 0 4 3
#     0 7 1 4
#     1 2 4 5
# 
# the sum of each row and each column has the value 12. Moreover the
# sum of each diagonal is also 12.
# 
# In how many ways can you fill a 4x4 grid with the digits d, 0 <= d
# <= 9 so that each row, each column, and both diagonals have the same
# sum?
#
# Answer: 7130034
# Solved 08/07/10
# 116 problems solved
# Position #825 on level 3 (previously #868 on level 3)

# Variables we're using
#
#     a00 a01 a02 a03
#     a10 a11 a12 a13
#     a20 a21 a22 a23
#     a30 a31 a32 a33
#
# Target =  0 Found      1 solutions
# Target =  1 Found      8 solutions
# Target =  2 Found     48 solutions
# Target =  3 Found    200 solutions
# Target =  4 Found    675 solutions
# Target =  5 Found   1904 solutions
# Target =  6 Found   4736 solutions
# Target =  7 Found  10608 solutions
# Target =  8 Found  21925 solutions
# Target =  9 Found  42328 solutions
# Target = 10 Found  76976 solutions
# Target = 11 Found 131320 solutions
# Target = 12 Found 209127 solutions
# Target = 13 Found 309968 solutions
# Target = 14 Found 427440 solutions
# Target = 15 Found 549184 solutions
# Target = 16 Found 658457 solutions
# Target = 17 Found 736744 solutions
# Target = 18 Found 766736 solutions
# Target = 19 Found 736744 solutions
# 
# Target = 28 Found  21925 solutions
# Target = 29 Found  10608 solutions
# Target = 30 Found   4736 solutions
# Target = 31 Found   1904 solutions
# Target = 32 Found    675 solutions
# Target = 33 Found    200 solutions
# Target = 34 Found     48 solutions
# Target = 35 Found      8 solutions
# Target = 36 Found      1 solutions


answer = 0

for target in range(0,19):
    tans = 0
    print "Target =", target,

    for a00 in range(10):
        if ((a00 +   0 +   0 +   0) > target):  break
        if ((a00 +   9 +   9 +   9) < target):  continue

        for a01 in range(10):
            if ((a00 + a01 +   0 +   0) > target):  break
            if ((a00 + a01 +   9 +   9) < target):  continue

            for a02 in range(10):
                if ((a00 + a01 + a02 +   0) > target):  break
                if ((a00 + a01 + a02 +   9) < target):  continue

                a03 = target - a00 - a01 - a02

                for a10 in range(10):
                    if ((a10 +   0 +   0 +   0) > target):  break
                    if ((a10 +   9 +   9 +   9) < target):  continue
                    if ((a00 + a10 +   0 +   0) > target):  break
                    if ((a00 + a10 +   9 +   9) < target):  continue

                    for a11 in range(10):
                        if ((a10 + a11 +   0 +   0) > target):  break
                        if ((a10 + a11 +   9 +   9) < target):  continue
                        if ((a01 + a11 +   0 +   0) > target):  break
                        if ((a01 + a11 +   9 +   9) < target):  continue

                        if ((a00 + a11 +   0 +   0) > target):  break
                        if ((a00 + a11 +   9 +   9) < target):  continue

                        for a12 in range(10):
                            if ((a10 + a11 + a12 +   0) > target):  break
                            if ((a10 + a11 + a12 +   9) < target):  continue
                            if ((a02 + a12 +   0 +   0) > target):  break
                            if ((a02 + a12 +   9 +   9) < target):  continue

                            if ((  0 +   0 + a12 + a03) > target):  break
                            if ((  9 +   9 + a12 + a03) < target):  continue

                            a13 = target - a10 - a11 - a12

                            for a20 in range(10):
                                if ((a20 +   0 +   0 +   0) > target):  break
                                if ((a20 +   9 +   9 +   9) < target):  continue
                                if ((a00 + a10 + a20 +   0) > target):  break
                                if ((a00 + a10 + a20 +   9) < target):  continue

                                a30 = target - a00 - a10 - a20

                                for a21 in range(10):
                                    if ((a20 + a21 +   0 +   0) > target):  break
                                    if ((a20 + a21 +   9 +   9) < target):  continue
                                    if ((a01 + a11 + a21 +   0) > target):  break
                                    if ((a01 + a11 + a21 +   9) < target):  continue

                                    if ((a30 + a21 + a12 + a03) != target):  continue

                                    for a22 in range(10):
                                        if ((a20 + a21 + a22 +   0) > target):  break
                                        if ((a20 + a21 + a22 +   9) < target):  continue
                                        if ((a02 + a12 + a22 +   0) > target):  break
                                        if ((a02 + a12 + a22 +   9) < target):  continue

                                        if ((a00 + a11 + a22 +   0) > target):  break
                                        if ((a00 + a11 + a22 +   9) < target):  continue

                                        a23 = target - a20 - a21 - a22
                                        a33 = target - a00 - a11 - a22
                                        if ((a03 + a13 + a23 + a33) != target):  continue

                                        a31 = target - a01 - a11 - a21
                                        a32 = target - a02 - a12 - a22
                                        if ((a30 + a31 + a32 + a33) != target):  continue

                                        tans += 1

                                        #print a00, a01, a02, a03
                                        #print a10, a11, a12, a13
                                        #print a20, a21, a22, a23
                                        #print a30, a31, a32, a33
                                        #print
    print "Found", tans, "solutions"
    answer += tans
    if (target != 18): 
        answer += tans

print "The answer is", answer
