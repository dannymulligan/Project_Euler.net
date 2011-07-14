#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 185
#
# Number Mind
#
# The game Number Mind is a variant of the well known game Master
# Mind.
#
# Instead of coloured pegs, you have to guess a secret sequence of
# digits. After each guess you're only told in how many places you've
# guessed the correct digit. So, if the sequence was 1234 and you
# guessed 2036, you'd be told that you have one correct digit;
# however, you would NOT be told that you also have another digit in
# the wrong place.
#
# For instance, given the following guesses for a 5-digit secret
# sequence,
#
#     90342  2 correct
#     70794  0 correct
#     39458  2 correct
#     34109  1 correct
#     51545  2 correct
#     12531  1 correct
#
# The correct sequence 39542 is unique.
#
# Based on the following guesses,
#
#     5616185650518293  2 correct
#     3847439647293047  1 correct
#     5855462940810587  3 correct
#     9742855507068353  3 correct
#     4296849643607543  3 correct
#     3174248439465858  1 correct
#     4513559094146117  2 correct
#     7890971548908067  3 correct
#     8157356344118483  1 correct
#     2615250744386899  2 correct
#     8690095851526254  3 correct
#     6375711915077050  1 correct
#     6913859173121360  1 correct
#     6442889055042768  2 correct
#     2321386104303845  0 correct
#     2326509471271448  2 correct
#     5251583379644322  2 correct
#     1748270476758276  3 correct
#     4895722652190306  1 correct
#     3041631117224635  3 correct
#     1841236454324589  3 correct
#     2659862637316867  2 correct
#
# Find the unique 16-digit secret sequence.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time
import random

start_time = time.clock()

def cnt_match(nn, mm, cc):
    c = 0
    if (nn[ 0] == mm[ 0]):  c += 1
    if (nn[ 1] == mm[ 1]):  c += 1
    if (nn[ 2] == mm[ 2]):  c += 1
    if (nn[ 3] == mm[ 3]):  c += 1
    if (nn[ 4] == mm[ 4]):  c += 1
    if (nn[ 5] == mm[ 5]):  c += 1
    if (nn[ 6] == mm[ 6]):  c += 1
    if (nn[ 7] == mm[ 7]):  c += 1
    if (nn[ 8] == mm[ 8]):  c += 1
    if (nn[ 9] == mm[ 9]):  c += 1
    if (nn[10] == mm[10]):  c += 1
    if (nn[11] == mm[11]):  c += 1
    if (nn[12] == mm[12]):  c += 1
    if (nn[13] == mm[13]):  c += 1
    if (nn[14] == mm[14]):  c += 1
    if (nn[15] == mm[15]):  c += 1
    if (c == cc):  return True
    return False



(m0, c0) = ([ 5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7 ], 3)  # 5855462940810587  3 correct
(m1, c1) = ([ 1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6 ], 3)  # 1748270476758276  3 correct
(m2, c2) = ([ 9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3 ], 3)  # 9742855507068353  3 correct
(m3, c3) = ([ 4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3 ], 3)  # 4296849643607543  3 correct
(m4, c4) = ([ 7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7 ], 3)  # 7890971548908067  3 correct
(m5, c5) = ([ 8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4 ], 3)  # 8690095851526254  3 correct
(m6, c6) = ([ 3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5 ], 3)  # 3041631117224635  3 correct
(m7, c7) = ([ 1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9 ], 3)  # 1841236454324589  3 correct
(m8, c8) = ([ 5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3 ], 2)  # 5616185650518293  2 correct
(m9, c9) = ([ 4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7 ], 2)  # 4513559094146117  2 correct
(mA, cA) = ([ 2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9 ], 2)  # 2615250744386899  2 correct
(mB, cB) = ([ 6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8 ], 2)  # 6442889055042768  2 correct
(mC, cC) = ([ 2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8 ], 2)  # 2326509471271448  2 correct
(mD, cD) = ([ 5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2 ], 2)  # 5251583379644322  2 correct
(mE, cE) = ([ 2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7 ], 2)  # 2659862637316867  2 correct
(mF, cF) = ([ 3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7 ], 1)  # 3847439647293047  1 correct
(mG, cG) = ([ 3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8 ], 1)  # 3174248439465858  1 correct
(mH, cH) = ([ 8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3 ], 1)  # 8157356344118483  1 correct
(mI, cI) = ([ 6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0 ], 1)  # 6375711915077050  1 correct
(mJ, cJ) = ([ 6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0 ], 1)  # 6913859173121360  1 correct
(mL, cL) = ([ 4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6 ], 1)  # 4895722652190306  1 correct
(mK, cK) = ([ 2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5 ], 0)  # 2321386104303845  0 correct


f = [0]*20

prev_time = time.clock()
answer = 0
cnt = 0

#for x in range(1000000):
x = 1000000000000000
while (x <= 9999999999999999):

    #n = random.randrange(1000000000000000, 9999999999999999)
    n = x

    #print "Checking {0}".format(x)

    n0 = n % 10
    if (n0 == 5):
        x += 1
        continue
    n = (n - n0)/10
    n1 = n % 10
    if (n1 == 4):
        x += 10
        continue
    n = (n - n1)/10
    n2 = n % 10
    if (n2 == 8):
        x += 100
        continue
    n = (n - n2)/10
    n3 = n % 10
    if (n3 == 3):
        x += 1000
        continue
    n = (n - n3)/10

    n4 = n % 10
    if (n4 == 0):
        x += 10000
        continue
    n = (n - n4)/10
    n5 = n % 10
    if (n5 == 3):
        x += 100000
        continue
    n = (n - n5)/10
    n6 = n % 10
    if (n6 == 4):
        x += 1000000
        continue
    n = (n - n6)/10
    n7 = n % 10
    if (n7 == 0):
        x += 10000000
        continue
    n = (n - n7)/10

    n8 = n % 10
    if (n8 == 1):
        x += 100000000
        continue
    n = (n - n8)/10
    n9 = n % 10
    if (n9 == 6):
        x += 1000000000
        continue
    n = (n - n9)/10
    nA = n % 10
    if (nA == 8):
        x += 10000000000
        continue
    n = (n - nA)/10
    nB = n % 10
    if (nB == 3):
        x += 100000000000
        continue
    n = (n - nB)/10

    nC = n % 10
    if (nC == 1):
        x += 1000000000000
        continue
    n = (n - nC)/10
    nD = n % 10
    if (nD == 2):
        x += 10000000000000
        continue
    n = (n - nD)/10
    nE = n % 10
    if (nE == 3):
        x += 100000000000000
        continue
    n = (n - nE)/10
    nF = n % 10
    if (nF == 2):
        x += 1000000000000000
        continue

    nn = [nF, nE, nD, nC, nB, nA, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0]

    cnt += 1
    if ((cnt % 1000000) == 0):
    #if (True):
        now_time = time.clock()
        print "Checking {0}, time taken = {1}, total time = {2}".format(x, now_time-prev_time, now_time-start_time)
        prev_time = now_time

    x += 1

    if not(cnt_match(nn, m0, c0)):
        f[ 0] += 1
        continue
    if not(cnt_match(nn, m1, c1)):
        f[ 1] += 1
        continue
    if not(cnt_match(nn, m2, c2)):
        f[ 2] += 1
        continue
    if not(cnt_match(nn, m3, c3)):
        f[ 3] += 1
        continue
    if not(cnt_match(nn, m4, c4)):
        f[ 4] += 1
        continue
    if not(cnt_match(nn, m5, c5)):
        f[ 5] += 1
        continue
    if not(cnt_match(nn, m6, c6)):
        f[ 6] += 1
        continue
    if not(cnt_match(nn, m7, c7)):
        f[ 7] += 1
        continue
    if not(cnt_match(nn, m8, c8)):
        f[ 8] += 1
        continue
    if not(cnt_match(nn, m9, c9)):
        f[ 9] += 1
        continue
    if not(cnt_match(nn, mA, cA)):
        f[10] += 1
        continue
    if not(cnt_match(nn, mB, cB)):
        f[11] += 1
        continue
    if not(cnt_match(nn, mC, cC)):
        f[12] += 1
        continue
    if not(cnt_match(nn, mD, cD)):
        f[13] += 1
        continue
    if not(cnt_match(nn, mE, cE)):
        f[14] += 1
        continue
    if not(cnt_match(nn, mF, cF)):
        f[15] += 1
        continue

    answer = x
    break

print f
print "Answer =", answer
now_time = time.clock()
print "Total time taken =", now_time - start_time
sys.exit()
