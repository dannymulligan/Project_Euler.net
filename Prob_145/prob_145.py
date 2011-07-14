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
# Solved 11/09/10
# 130 problems solved
# Position #423 on level 3

# Brute force technique:
#           < 100:      20 reversible numbers  (  0m 0.061s)
#         < 1,000:     120 reversible numbers  (  0m 0.068s)
#        < 10,000:     720 reversible numbers  (  0m 0.136s)
#       < 100,000:     720 reversible numbers  (  0m 0.899s)
#     < 1,000,000:  18,720 reversible numbers  (  0m 8.730s)
#    < 10,000,000:  68,720 reversible numbers  (  1m30.279s)
#   < 100,000,000: 608,720 reversible numbers  ( 22m49.344s)
# < 1,000,000,000: 608,720 reversible numbers  (196m38.503s)

#
# Why are there no 9 digit reversible numbers?
#
#   9876 5 4321
#   ABCD E FGHI  - 9 digit number
#   IHGF E DCBA  - reversed
#
# The only way that result position 5 is odd is if F+D > 10 and we
#     carry 1 from position 4.
# This means that we carry 1 from position 6, so C + G = even.
# This means that position 3 is even unless we carry 1 from position
#     2.
# This means that B + H > 10.
# This means that position 8 is > 10, and position 9 A + I must be
#     even.
# But if A+I is even, then position 1 can never add to an odd number

# How many 8 digit reversible numbers are there?
#
#   8765 4321
#   ABCD EFGH  - 8 digit number
#   HGFE DCBA  - reversed
#
# With no carries...
#     A + H = odd and < 10
#        A    H
#        1    2, 4, 6, 8
#        2    1, 3, 5, 7
#        3    2, 4, 6
#        4    1, 3, 5
#        5    2, 4
#        6    1, 3
#        7    2
#        8    1
#     = 20 possibilities
#     B + G = odd and < 10
#        B    G
#        0    1, 3, 5, 7, 9
#        1    0, 2, 4, 6, 8
#        2    1, 3, 5, 7
#        3    0, 2, 4, 6
#        4    1, 3, 5
#        5    0, 2, 4
#        6    1, 3
#        7    0, 2
#        8    1
#        9    0
#     = 30 possibilities
#    C + F and D + E are the same as B + G
#    so there are 20 * 30 * 30 * 30 = 540,000 possibilities with no carries
#
# With carries...
#
#   8765 4321
#   ABCD EFGH  - 8 digit number
#   HGFE DCBA  - reversed
#
# A+H must be odd, or else position 1 would be even
# B+G < 10 or position 7 would carry and position 8 would be even
# If A+H is >= 10, then G+B = even
#     
# If A+H is < 10, then G+B = odd

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
for n in xrange(10, 10000000):  # Only have to test to <10,000,000
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

Answer += 540000
print "n = {0}, Answer = {1}, time = {2}".format((n+1), Answer, (time.clock() - start))
