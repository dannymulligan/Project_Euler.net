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
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

#           < 100:      20 reversible numbers  ( 0m 0.061s)
#         < 1,000:     120 reversible numbers  ( 0m 0.068s)
#        < 10,000:     720 reversible numbers  ( 0m 0.136s)
#       < 100,000:     720 reversible numbers  ( 0m 0.899s)
#     < 1,000,000:  18,720 reversible numbers  ( 0m 8.730s)
#    < 10,000,000:  68,720 reversible numbers  ( 1m30.279s)
#   < 100,000,000: 608,720 reversible numbers  (22m49.344s)
# < 1,000,000,000:       ? reversible numbers

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


Answer = 0
for n in range(10,1000):
    if ((n % 10) == 0):  continue
    t = n + reverse(n)
    if chodd(t):
        Answer += 1
        #print "{0} + {1} = {2}".format(n, reverse(n), n+reverse(n))

print "Answer =", Answer
