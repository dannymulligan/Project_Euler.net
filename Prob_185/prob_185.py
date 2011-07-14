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

start_time = time.clock()

def cnt_match(nn, mm, cc):
    c = 0
    if (nn[0] == mm[0]):  c += 1
    if (nn[1] == mm[1]):  c += 1
    if (nn[2] == mm[2]):  c += 1
    if (nn[3] == mm[3]):  c += 1
    if (nn[4] == mm[4]):  c += 1
    if (c == cc):  return True
    return False

(m0, c0) = ([ 9, 0, 3, 4, 2 ], 2)  # 2 correct
(m1, c1) = ([ 5, 1, 5, 4, 5 ], 2)  # 2 correct
(m2, c2) = ([ 3, 9, 4, 5, 8 ], 2)  # 2 correct
(m3, c3) = ([ 3, 4, 1, 0, 9 ], 1)  # 1 correct
(m4, c4) = ([ 1, 2, 5, 3, 1 ], 1)  # 1 correct
(m5, c5) = ([ 7, 0, 7, 9, 4 ], 0)  # 0 correct

f = [0]*6

prev_time = time.clock()
for x in range(10000, 99999):

    n = x
    n0 = n % 10
    n = (n - n0)/10
    n1 = n % 10
    n = (n - n1)/10
    n2 = n % 10
    n = (n - n2)/10
    n3 = n % 10
    n = (n - n3)/10
    n4 = n
    nn = [n4, n3, n2, n1, n0]

    if ((x % 10000) == 0):
        now_time = time.clock()
        print "Checking {0}, time taken = {1}, total time = {2}".format(x, now_time-prev_time, now_time-start_time)
        prev_time = now_time

    if not(cnt_match(nn, m0, c0)):
        f[0] += 1
        continue
    if not(cnt_match(nn, m1, c1)):
        f[1] += 1
        continue
    if not(cnt_match(nn, m2, c2)):
        f[2] += 1
        continue
    if not(cnt_match(nn, m3, c3)):
        f[3] += 1
        continue
    if not(cnt_match(nn, m4, c4)):
        f[4] += 1
        continue
    if not(cnt_match(nn, m5, c5)):
        f[5] += 1
        continue

    answer = x
    #break

print "Answer =", answer
now_time = time.clock()
print "Total time taken =", now_time - start_time
print f
sys.exit()
