#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 115
# 
# NOTE: This is a more difficult version of problem 114.
# 
# A row measuring n units in length has red blocks with a minimum
# length of m units placed on it, such that any two red blocks (which
# are allowed to be different lengths) are separated by at least one
# black square.
# 
# Let the fill-count function, F(m, n), represent the number of ways
# that a row can be filled.
# 
# For example, F(3, 29) = 673135 and F(3, 30) = 1089155.
# 
# That is, for m = 3, it can be seen that n = 30 is the smallest value
# for which the fill-count function first exceeds one million.
# 
# In the same way, for m = 10, it can be verified that F(10, 56) =
# 880711 and F(10, 57) = 1148904, so n = 57 is the least value for
# which the fill-count function first exceeds one million.
# 
# For m = 50, find the least value of n for which the fill-count
# function first exceeds one million.
#
# Answer: 168
# Solved 09/12/10
# 126 problems solved
# Position #532 on level 3

import sys

# Count the possiblities of arranging dof items into grps groups
# Example: poss_cnt(3,2) should count the following 6 possibilities
#     0 0 2  0 1 1  0 2 0
#     1 0 1  1 1 0
#     2 0 0
# Example: poss_cnt(3,3) should count the following 10 possibilities
#     0 0 3  0 1 2  0 2 1  0 3 0
#     1 0 2  1 1 1  1 2 0
#     2 0 1  2 1 0
#     3 0 0
def poss_cnt(grps, dof):

    if ((dof == 0) | (grps == 1)):
        #print "    poss_cnt({0},{1}) = {2}".format(grps, dof, 1)
        return 1

    cnt = 0
    for i in range(dof+1):
        cnt += poss_cnt(grps-1, dof-i)
    #print "    poss_cnt({0},{1}) = {2}".format(grps, dof, cnt)
    return cnt


# fill_cnt(min, len)
# How many ways can a row of length len be filled with red pieces of minimum length
# min seperated by at least one black square
def fill_cnt(min, len):
    cnt = 0
    for red_grp in range(1+(len+1)/(min+1)):
        #print "{0} groups of reds".format(red_grp)
        if (red_grp == 0):
            cnt += 1
            #print "    {0} possibilities".format(1)
        else:
            min_red_len = red_grp*min
            max_red_len = len-red_grp+1
            for red_len in range(min_red_len, max_red_len+1):
                red_cnt = poss_cnt(red_grp, red_len-red_grp*min)
                blk_cnt = poss_cnt(red_grp+1, len-red_len-red_grp+1) # 3, 2
                cnt += red_cnt*blk_cnt
                #print "    {0} red length, {1} possibilities = {2} red possibilities * {3} black possibilities".format(red_len, red_cnt*blk_cnt, red_cnt, blk_cnt)
    return cnt

# # F(3, 3) = 2
# ans = fill_cnt(3, 3)
# print "fill_cnt(3, 3) =", ans,
# if (ans == 2):  print "Correct"
# else:           print "Error!, should be 2"
# 
# # F(3, 4) = 4
# ans = fill_cnt(3, 4)
# print "fill_cnt(3, 4) =", ans,
# if (ans == 4):  print "Correct"
# else:           print "Error!, should be 4"
# 
# # F(3, 7) = 17
# ans = fill_cnt(3, 7)
# print "fill_cnt(3, 7) =", ans,
# if (ans == 17):  print "Correct"
# else:            print "Error!, should be 17"
# 
# # F(3, 8) = 27
# ans = fill_cnt(3, 8)
# print "fill_cnt(3, 8) =", ans,
# if (ans == 27):  print "Correct"
# else:            print "Error!, should be 27"
# 
# # F(3, 9) = 44
# ans = fill_cnt(3, 9)
# print "fill_cnt(3, 9) =", ans,
# if (ans == 44):  print "Correct"
# else:            print "Error!, should be 44"
# 
# # F(3, 29) = 673135
# ans = fill_cnt(3, 29)
# print "fill_cnt(3, 29) =", ans,
# if (ans == 673135):  print "Correct"
# else:                print "Error!, should be 673135"
# 
# # F(3, 30) = 1089155
# ans = fill_cnt(3, 30)
# print "fill_cnt(3, 30) =", ans,
# if (ans == 1089155):  print "Correct"
# else:                 print "Error! should be 1089155"
# 
# # F(10, 56) = 880711
# ans = fill_cnt(10, 56)
# print "fill_cnt(10, 56) =", ans,
# if (ans == 880711):  print "Correct"
# else:                print "Error!, should be 880711"
# 
# # F(10, 57) = 1148904
# ans = fill_cnt(10, 57)
# print "fill_cnt(10, 57) =", ans,
# if (ans == 1148904):  print "Correct"
# else:                 print "Error!, 1148904"

min = 50
len = 3
cnt = 0
while (cnt < 1000000):
    cnt = fill_cnt(min, len)
    print "fill_cnt({0}, {1}) = {2}".format(min, len, cnt)
    len += 1
print "Answer =", len-1
