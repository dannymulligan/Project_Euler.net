#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 458
#
# Permutations of Project
#
# Consider the alphabet A made out of the letters of the word
# "project": A={c,e,j,o,p,r,t}.
#
# Let T(n) be the number of strings of length n consisting of letters
# from A that do not have a substring that is one of the 5040
# permutations of "project".
#
# T(7)=77-7!=818503.
#
# Find T(10^12). Give the last 9 digits of your answer.


import sys
import time
start_time = time.clock()

########################################

# In the following
#    x means any of the letters of PROJECT
#    y means any of the letters of PROJECT except the last one
#
# T(7) = 7^7 - 7!
# T(8) = 7! * (7^8/7^7)        # PROJECTx  where x is any of 7 possibilities
       + 7 * 6*6!              # rPROJECT  where r is not the last letter in PROJECT
# T(9) = 7! * (7^9/7^7)        # PROJECTxx  where x is any of 7 possibilities
       + 7 * 6*6! * (7^9/7^7)  # xPROJECT  where r is not the last letter in PROJECT
       + 7 * 6*6! * (7^9/7^7)  # xPROJECT  where x is not the last letter in PROJECT
# T(n) = 7^n = n*7!

MOD = 10**10


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
