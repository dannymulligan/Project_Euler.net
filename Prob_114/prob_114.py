#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 114
# 
# A row measuring seven units in length has red blocks with a minimum
# length of three units placed on it, such that any two red blocks
# (which are allowed to be different lengths) are separated by at
# least one black square. There are exactly seventeen ways of doing
# this.
#                                                 
#     [B][B][B][B][B][B][B]  [R--R--R][B][B][B][B]  [B][R--R--R][B][B][B]  
#
#     [B][B][R--R--R][B][B]  [B][B][B][R--R--R][B]  [B][B][B][B][R--R--R]
#                                 
#     [R--R--R][B][R--R--R]  [R--R--R--R][B][B][B]  [B][R--R--R--R][B][B]
#         
#     [B][B][R--R--R--R][B]  [B][B][B][R--R--R--R]  [R--R--R--R--R][B][B]
#                                 
#     [B][R--R--R--R--R][B]  [B][B][R--R--R--R--R]  [R--R--R--R--R--R][B]
#                                 
#     [B][R--R--R--R--R--R]  [R--R--R--R--R--R--R]
# 
# How many ways can a row measuring fifty units in length be filled?
# 
# NOTE: Although the example above does not lend itself to the
# possibility, in general it is permitted to mix block sizes. For
# example, on a row measuring eight units in length you could use red
# (3), black (1), and red (4).
#
# Solved 09/12/10
# 127 problems solved
# Position #504 on level 3

import sys

# Solution calculated using code developed for problem 115

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
        print "{0} groups of reds".format(red_grp)
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

# # F(3, 7) = 17
# ans = fill_cnt(3, 7)
# print "fill_cnt(3, 7) =", ans,
# if (ans == 17):  print "Correct"
# else:            print "Error!, should be 17"

ans = fill_cnt(3,50)
print "Answer =", ans
sys.exit()

