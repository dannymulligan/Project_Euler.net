#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 145
#
# How many reversible numbers are there below one-billion?
#
# Some positive integers n have the property that the sum [ n +
# reverse(n) ] consists entirely of odd (decimal) digits. For
# instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such
# numbers reversible; so 36, 63, 409, and 904 are reversible. Leading
# zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (10^9)?
#
# Answer: 
# Solved 11/09/10
# 130 problems solved
# Position #423 on level 3

#           < 100:      20 reversible numbers  (  0m 0.061s)
#         < 1,000:     120 reversible numbers  (  0m 0.068s)
#        < 10,000:     720 reversible numbers  (  0m 0.136s)
#       < 100,000:     720 reversible numbers  (  0m 0.899s)
#     < 1,000,000:  18,720 reversible numbers  (  0m 8.730s)
#    < 10,000,000:  68,720 reversible numbers  (  1m30.279s)
#   < 100,000,000: 608,720 reversible numbers  ( 22m49.344s)
# < 1,000,000,000: 608,720 reversible numbers  (196m38.503s)

import time

def reverse(n):
    sn = str(n)
    ln = []
    for ch in sn:
        ln.append(ch)
    ln.reverse()
    rsn = ''
    for ch in ln:
       rsn += ch
    return int(rsn)

def chodd(n):
    sn = str(n)
    for ch in sn:
        if ((int(ch) % 2) == 0):  # even(ch)
            return False
    return True


start = time.clock()

Answer = 0
for n in xrange(10, 1000000000):
    if ((n % 10) == 0):  continue
    t = n + reverse(n)
    if chodd(t):
        Answer += 1
        #print "{0} + {1} = {2}".format(n, reverse(n), n+reverse(n))
    if ( ((n <     100) & ((n %      10) ==      9)) |
         ((n <    1000) & ((n %     100) ==     99)) |
         ((n <   10000) & ((n %    1000) ==    999)) |
         ((n <  100000) & ((n %   10000) ==   9999)) |
         ((n < 1000000) & ((n %  100000) ==  99999)) |
         ((n > 1000000) & ((n % 1000000) == 999999)) ):
        print "n = {0}, Answer = {1}, time = {2}".format(n, Answer, (time.clock() - start))

print "n = {0}, Answer = {1}, time = {2}".format((n+1), Answer, (time.clock() - start))
