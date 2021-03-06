#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 128
#
# Which tiles in the hexagonal arrangement have prime differences with
# neighbours?
#
# A hexagonal tile with number 1 is surrounded by a ring of six
# hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2
# to 7 in an anti-clockwise direction.
#
# New rings are added in the same fashion, with the next rings being
# numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below
# shows the first three rings.
#
# By finding the difference between tile n and each its six neighbours
# we shall define PD(n) to be the number of those differences which
# are prime.
#
# For example, working clockwise around tile 8 the differences are 12,
# 29, 11, 6, 1, and 13. So PD(8) = 3.
#
# In the same way, the differences around tile 17 are 1, 17, 16, 1,
# 11, and 10, hence PD(17) = 2.
#
# It can be shown that the maximum value of PD(n) is 3.
#
# If all of the tiles for which PD(n) = 3 are listed in ascending
# order to form a sequence, the 10th tile would be 271.
#
# Find the 2000th tile in this sequence.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()

MAX = 3

####
def test_it(st):
    cnt = 0
    ch = [0]*26
    ch[st[0]] += 1
    for i in xrange(len(st)-1):
        if (st[i+1] > st[i]):
            cnt += 1
            if (ch[st[i+1]] == 1):
                return "Error"
            else:
                ch[st[i+1]] += 1
    if (cnt == 1):
        return "OK"
    else:
        return "Error"


########################################
def pn(lth,lex,avail,st):
    #print "pn({0},{1},{2},{3})".format(lth,lex,avail,st)
    # lth = length of string left to do
    # lex = one char lexographically after char to its left is avail
    # avail = characters alread used
    # st  = current character string (as a list of integers)
    cur = st[-1]
    if (lth == 1):
        if lex:
            ans = 0
            for i in xrange(cur+1,26):
                if (avail[i] == 1):  continue
                st.append(i)
                #print "   ", st, test_it(st)
                del st[-1]
                ans += 1
            #print "    tot =", 25-cur
            return ans
        else:
            ans = 0
            for i in xrange(0,cur+1):
                if (avail[i] == 1):  continue
                st.append(i)
                #print "   ", st, test_it(st)
                del st[-1]
                ans += 1
            #print "    tot =", cur
            return ans
    ans = 0
    if (lex):
        for i in xrange(cur):
            if (avail[i] == 1):  continue
            st.append(i)
            avail[i] = 1
            ans += pn(lth-1,True,avail,st)
            avail[i] = 0
            del st[-1]
        for i in xrange(cur+1,26):
            if (avail[i] == 1):  continue
            st.append(i)
            avail[i] = 1
            ans += pn(lth-1,False,avail,st)
            avail[i] = 0
            del st[-1]
    else:
        for i in xrange(cur):
            if (avail[i] == 1):  continue
            st.append(i)
            avail[i] = 1
            ans += pn(lth-1,False,avail,st)
            avail[i] = 0
            del st[-1]
    #print "pn({0},{1},{2},{3}) = {4}".format(lth,lex,avail,st,ans)
    return ans


########################################
def p(n):
    ans = 0
    avail = [0]*26
    for i in xrange(0,26):
        st = [i]
        avail[i] = 1
        ans += pn(n-1,True,avail,st)
        avail[i] = 0
    return ans


########################################
results = []
best_result = 0
best_n = 0
for n in xrange(4,4+1):
    a = p(n)
    print "p({0}) = {1}".format(n,a)
    if (a > best_result):
        best_result = a
        best_n = n

print "Answer =", best_result
print "Time taken = {0} seconds".format(time.clock() - start_time)
