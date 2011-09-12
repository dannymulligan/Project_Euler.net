#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 348
#
# Sum of a square and a cube
#
# Many numbers can be expressed as the sum of a square and a
# cube. Some of them in more than one way.
#
# Consider the palindromic numbers that can be expressed as the sum of
# a square and a cube, both greater than 1, in exactly 4 different
# ways.
#
# For example, 5229225 is a palindromic number and it can be expressed
# in exactly 4 different ways:
# 
#     2285^2 + 20^3
#     2223^2 + 66^3
#     1810^2 + 125^3
#     1197^2 + 156^3
#
# Find the sum of the five smallest such palindromic numbers.
#
# Solved 09/12/11
# 169 problems solved
# Position #378 on level 4

import sys
import time
start_time = time.clock()

########################################
def palindrome(max_palindrome):
    if (max_palindrome >= 1e12):
        print "palindrome limit exceeded"
        sys.exit(1)

    # 2 digit palindromes
    for i in xrange(1,10):
        n = int(str(i) + str(i)[::-1])
        if (n < max_palindrome):  yield n
        else:                     return

    # 3 digit palindromes
    for i in xrange(1,10):
        for j in xrange(10):
            n = int(str(i) + str(j) + str(i)[::-1])
            if (n < max_palindrome):  yield n
            else:                     return

    # 4 digit palindromes
    for i in xrange(10,100):
        n = int(str(i) + str(i)[::-1])
        if (n < max_palindrome):  yield n
        else:                     return

    # 5 digit palindromes
    for i in xrange(10,100):
        for j in xrange(10):
            n = int(str(i) + str(j) + str(i)[::-1])
            if (n < max_palindrome):  yield n
            else:                     return

    # 6 digit palindromes
    for i in xrange(100,1000):
        n = int(str(i) + str(i)[::-1])
        if (n < max_palindrome):  yield n
        else:                     return

    # 7 digit palindromes
    for i in xrange(100,1000):
        for j in xrange(10):
            n = int(str(i) + str(j) + str(i)[::-1])
            if (n < max_palindrome):  yield n
            else:                     return

    # 8 digit palindromes
    for i in xrange(1000,10000):
        n = int(str(i) + str(i)[::-1])
        if (n < max_palindrome):  yield n
        else:                     return

    # 9 digit palindromes
    for i in xrange(1000,10000):
        for j in xrange(10):
            n = int(str(i) + str(j) + str(i)[::-1])
            if (n < max_palindrome):  yield n
            else:                     return

    # 10 digit palindromes
    for i in xrange(10000,100000):
        n = int(str(i) + str(i)[::-1])
        if (n < max_palindrome):  yield n
        else:                     return

    # 11 digit palindromes
    for i in xrange(10000,100000):
        for j in xrange(10):
            n = int(str(i) + str(j) + str(i)[::-1])
            if (n < max_palindrome):  yield n
            else:                     return


########################################
def int_sqrt(n):
    # return s if s^2 = n
    # return 0 if s is not an integer square root of n
    ans = int(n**.5)
    if   ((ans**2) == n): return ans
    else:                 return 0
#print "ins_sqrt({0}) = {1}".format(16,int_sqrt(16))
#print "ins_sqrt({0}) = {1}".format(25,int_sqrt(25))
#print "ins_sqrt({0}) = {1}".format(26,int_sqrt(26))
#print "ins_sqrt({0}) = {1}".format(512,int_sqrt(512))
#print "ins_sqrt({0}) = {1}".format(1024,int_sqrt(1024))


########################################
answer = 0
ans_cnt = 0
p_cnt = 0
for p in palindrome(1e9):
    p_cnt += 1
    if ((p_cnt % 1e4) == 0):
        print "Testing p({0}) = {1}".format(p_cnt,p)

    c = 2
    cnt = 0
    while (c**3 < p):
        r = p - c**3
        s = int_sqrt(r)
        if (s != 0):
            #print "{0} = {1}^2 + {2}^3".format(p,s,c)
            cnt += 1
        c += 1
    if (cnt == 4):
        answer += p
        ans_cnt += 1
        print "Found 4 solutions for {0}, answer so far is {1}".format(p, answer)
        if (ans_cnt == 5):
            print "Answer = {0}".format(answer)
            break

print "Examined {0} palindromes, ending with {1}".format(p_cnt,p)
print "Time taken = {0} seconds".format(time.clock() - start_time)

