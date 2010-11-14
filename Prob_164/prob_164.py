#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 164
#
# Numbers for which no three consecutive digits have a sum greater
# than a given value.
#
# How many 20 digit numbers n (without any leading zero) exist such
# that no three consecutive digits of n have a sum greater than 9?
#
# Answer: 378158756814587
# Solved 11/13/10
# 131 problems solved
# Position #398 on level 3

import time
import sys

start_time = time.clock()

cache_03 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                cnt += 1
                cache_03[a*100+b*10+c] = 1
                #print a, b, c, cache_03
                #print "_03[{0}][{1}][{2}] = {3}".format(b,c,0,1),
                #print "{0}{1}{2}".format(a,b,c)
print "{0} digit numbers - found {1} solutions".format(3, cnt)

cache_04 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_03[b*100+c*10+0] + cache_03[b*100+c*10+1] + cache_03[b*100+c*10+2] + cache_03[b*100+c*10+3] + cache_03[b*100+c*10+4] \
                    + cache_03[b*100+c*10+5] + cache_03[b*100+c*10+6] + cache_03[b*100+c*10+7] + cache_03[b*100+c*10+8] + cache_03[b*100+c*10+9]
                cnt += ans
                cache_04[a*100+b*10+c] = ans
                #print "{0}{1}{2}x has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(4, cnt)

cache_05 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_04[b*100+c*10+0] + cache_04[b*100+c*10+1] + cache_04[b*100+c*10+2] + cache_04[b*100+c*10+3] + cache_04[b*100+c*10+4] \
                    + cache_04[b*100+c*10+5] + cache_04[b*100+c*10+6] + cache_04[b*100+c*10+7] + cache_04[b*100+c*10+8] + cache_04[b*100+c*10+9]
                cnt += ans
                cache_05[a*100+b*10+c] = ans
                #print "{0}{1}{2}xx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(5, cnt)

cache_06 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_05[b*100+c*10+0] + cache_05[b*100+c*10+1] + cache_05[b*100+c*10+2] + cache_05[b*100+c*10+3] + cache_05[b*100+c*10+4] \
                    + cache_05[b*100+c*10+5] + cache_05[b*100+c*10+6] + cache_05[b*100+c*10+7] + cache_05[b*100+c*10+8] + cache_05[b*100+c*10+9]
                cnt += ans
                cache_06[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(6, cnt)

cache_07 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_06[b*100+c*10+0] + cache_06[b*100+c*10+1] + cache_06[b*100+c*10+2] + cache_06[b*100+c*10+3] + cache_06[b*100+c*10+4] \
                    + cache_06[b*100+c*10+5] + cache_06[b*100+c*10+6] + cache_06[b*100+c*10+7] + cache_06[b*100+c*10+8] + cache_06[b*100+c*10+9]
                cnt += ans
                cache_07[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(7, cnt)

cache_08 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_07[b*100+c*10+0] + cache_07[b*100+c*10+1] + cache_07[b*100+c*10+2] + cache_07[b*100+c*10+3] + cache_07[b*100+c*10+4] \
                    + cache_07[b*100+c*10+5] + cache_07[b*100+c*10+6] + cache_07[b*100+c*10+7] + cache_07[b*100+c*10+8] + cache_07[b*100+c*10+9]
                cnt += ans
                cache_08[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(8, cnt)

cache_09 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_08[b*100+c*10+0] + cache_08[b*100+c*10+1] + cache_08[b*100+c*10+2] + cache_08[b*100+c*10+3] + cache_08[b*100+c*10+4] \
                    + cache_08[b*100+c*10+5] + cache_08[b*100+c*10+6] + cache_08[b*100+c*10+7] + cache_08[b*100+c*10+8] + cache_08[b*100+c*10+9]
                cnt += ans
                cache_09[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(9, cnt)

cache_10 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_09[b*100+c*10+0] + cache_09[b*100+c*10+1] + cache_09[b*100+c*10+2] + cache_09[b*100+c*10+3] + cache_09[b*100+c*10+4] \
                    + cache_09[b*100+c*10+5] + cache_09[b*100+c*10+6] + cache_09[b*100+c*10+7] + cache_09[b*100+c*10+8] + cache_09[b*100+c*10+9]
                cnt += ans
                cache_10[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(10, cnt)

cache_11 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_10[b*100+c*10+0] + cache_10[b*100+c*10+1] + cache_10[b*100+c*10+2] + cache_10[b*100+c*10+3] + cache_10[b*100+c*10+4] \
                    + cache_10[b*100+c*10+5] + cache_10[b*100+c*10+6] + cache_10[b*100+c*10+7] + cache_10[b*100+c*10+8] + cache_10[b*100+c*10+9]
                cnt += ans
                cache_11[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(11, cnt)

cache_12 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_11[b*100+c*10+0] + cache_11[b*100+c*10+1] + cache_11[b*100+c*10+2] + cache_11[b*100+c*10+3] + cache_11[b*100+c*10+4] \
                    + cache_11[b*100+c*10+5] + cache_11[b*100+c*10+6] + cache_11[b*100+c*10+7] + cache_11[b*100+c*10+8] + cache_11[b*100+c*10+9]
                cnt += ans
                cache_12[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(12, cnt)

cache_13 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_12[b*100+c*10+0] + cache_12[b*100+c*10+1] + cache_12[b*100+c*10+2] + cache_12[b*100+c*10+3] + cache_12[b*100+c*10+4] \
                    + cache_12[b*100+c*10+5] + cache_12[b*100+c*10+6] + cache_12[b*100+c*10+7] + cache_12[b*100+c*10+8] + cache_12[b*100+c*10+9]
                cnt += ans
                cache_13[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(13, cnt)

cache_14 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_13[b*100+c*10+0] + cache_13[b*100+c*10+1] + cache_13[b*100+c*10+2] + cache_13[b*100+c*10+3] + cache_13[b*100+c*10+4] \
                    + cache_13[b*100+c*10+5] + cache_13[b*100+c*10+6] + cache_13[b*100+c*10+7] + cache_13[b*100+c*10+8] + cache_13[b*100+c*10+9]
                cnt += ans
                cache_14[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(14, cnt)

cache_15 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_14[b*100+c*10+0] + cache_14[b*100+c*10+1] + cache_14[b*100+c*10+2] + cache_14[b*100+c*10+3] + cache_14[b*100+c*10+4] \
                    + cache_14[b*100+c*10+5] + cache_14[b*100+c*10+6] + cache_14[b*100+c*10+7] + cache_14[b*100+c*10+8] + cache_14[b*100+c*10+9]
                cnt += ans
                cache_15[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(15, cnt)

cache_16 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_15[b*100+c*10+0] + cache_15[b*100+c*10+1] + cache_15[b*100+c*10+2] + cache_15[b*100+c*10+3] + cache_15[b*100+c*10+4] \
                    + cache_15[b*100+c*10+5] + cache_15[b*100+c*10+6] + cache_15[b*100+c*10+7] + cache_15[b*100+c*10+8] + cache_15[b*100+c*10+9]
                cnt += ans
                cache_16[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(16, cnt)

cache_17 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_16[b*100+c*10+0] + cache_16[b*100+c*10+1] + cache_16[b*100+c*10+2] + cache_16[b*100+c*10+3] + cache_16[b*100+c*10+4] \
                    + cache_16[b*100+c*10+5] + cache_16[b*100+c*10+6] + cache_16[b*100+c*10+7] + cache_16[b*100+c*10+8] + cache_16[b*100+c*10+9]
                cnt += ans
                cache_17[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(17, cnt)

cache_18 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_17[b*100+c*10+0] + cache_17[b*100+c*10+1] + cache_17[b*100+c*10+2] + cache_17[b*100+c*10+3] + cache_17[b*100+c*10+4] \
                    + cache_17[b*100+c*10+5] + cache_17[b*100+c*10+6] + cache_17[b*100+c*10+7] + cache_17[b*100+c*10+8] + cache_17[b*100+c*10+9]
                cnt += ans
                cache_18[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(18, cnt)

cache_19 = [0]*1000
cnt = 0
ans = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_18[b*100+c*10+0] + cache_18[b*100+c*10+1] + cache_18[b*100+c*10+2] + cache_18[b*100+c*10+3] + cache_18[b*100+c*10+4] \
                    + cache_18[b*100+c*10+5] + cache_18[b*100+c*10+6] + cache_18[b*100+c*10+7] + cache_18[b*100+c*10+8] + cache_18[b*100+c*10+9]
                cnt += ans
                cache_19[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(19, cnt)

cache_20 = [0]*1000
cnt = 0
ans = 0
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            if ((a+b+c) <= 9):
                ans = cache_19[b*100+c*10+0] + cache_19[b*100+c*10+1] + cache_19[b*100+c*10+2] + cache_19[b*100+c*10+3] + cache_19[b*100+c*10+4] \
                    + cache_19[b*100+c*10+5] + cache_19[b*100+c*10+6] + cache_19[b*100+c*10+7] + cache_19[b*100+c*10+8] + cache_19[b*100+c*10+9]
                cnt += ans
                cache_20[a*100+b*10+c] = ans
                #print "{0}{1}{2}xxxxxxxxxxxxxxxxx has {3} solutions".format(a,b,c, ans)
print "{0} digit numbers - found {1} solutions".format(20, cnt)


print "Answer =", cnt
print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()
