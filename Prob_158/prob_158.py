#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 158
#
# Exploring strings for which only one character comes
# lexicographically after its neighbour to the left.
#
# Taking three different letters from the 26 letters of the alphabet,
# character strings of length three can be formed.
#
# Examples are 'abc', 'hat' and 'zyx'.
#
# When we study these three examples we see that for 'abc' two
# characters come lexicographically after its neighbour to the left.
#
# For 'hat' there is exactly one character that comes
# lexicographically after its neighbour to the left. For 'zyx' there
# are zero characters that come lexicographically after its neighbour
# to the left.
#
# In all there are 10400 strings of length 3 for which exactly one
# character comes lexicographically after its neighbour to the left.
#
# We now consider strings of n <= 26 different characters from the
# alphabet.
#
# For every n, p(n) is the number of strings of length n for which
# exactly one character comes lexicographically after its neighbour to
# the left.
#
# What is the maximum value of p(n)?
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time
start_time = time.clock()
import cProfile

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
def main():
    results = []
    best_result = 0
    best_n = 0
    for n in xrange(2,8+1):
        a = p(n)
        print "p({0}) = {1}".format(n,a)
        if (a > best_result):
            best_result = a
            best_n = n

    print "Answer =", best_result
    print "Time taken = {0} seconds".format(time.clock() - start_time)

cProfile.run('main()')
