#!/usr/bin/python
#
# Project Euler.net Problem 80
#
# It is well known that if the square root of a natural number is not
# an integer, then it is irrational. The decimal expansion of such
# square roots is infinite without any repeating pattern at all.
#
# The square root of two is 1.41421356237309504880..., and the digital
# sum of the first one hundred decimal digits is 475.
#
# For the first one hundred natural numbers, find the total of the
# digital sums of the first one hundred decimal digits for all the
# irrational square roots.
# 
# Answer:

import decimal

decimal.getcontext().prec = 110
# Precision of 100 gives 100 digits, including digita both before and after decimal point
# We generate 110 digits but use only 100, so rounding is unlikely to affect the 100th digit
# The algorithm produces the wrong result if we use 100 or 101 digits only.

big_sum = 0
for i in range(100):
    x = decimal.Decimal(i)
    y = x.sqrt()
    s = "{0}".format(y)
    l_sum = int(s[0])
    if (len(s) > 2):
        for j in range(2,101):
            l_sum += int(s[j])
        big_sum += l_sum
    print "big_sum = {0}, l_sum = {1}, i = {2}, len(s) = {3}, s = {4}".format(big_sum, l_sum, i, len(s), s)

print "Result is {0}".format(big_sum)
