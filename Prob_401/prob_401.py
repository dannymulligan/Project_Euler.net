#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 401
#
# Sum of squares of divisors
#
# The divisors of 6 are 1,2,3 and 6.
# The sum of the squares of these numbers is 1+4+9+36=50.
#
# Let sigma2(n) represent the sum of the squares of the divisors of
# n. Thus sigma2(6)=50.
#
# Let SIGMA2 represent the summatory function of sigma2, that is
# SIGMA2(n)=∑sigma2(i) for i=1 to n.
# The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.
#
# Find SIGMA2(10^15) modulo 10^9.
#

import sys
import time
start_time = time.clock()

########################################


print("Time taken = {0} seconds".format(time.clock() - start_time))



#  1 = 1               factors = 1                         sigma2 = 1
#  2 = 2               factors = 1, 2                      sigma2 = 1 + 4
#  3 = 3               factors = 1, 3                      sigma2 = 1 + 9
#  4 = 2 x 2           factors = 1, 2, 4                   sigma2 = 1
#  5 = 5               factors = 1, 5                      sigma2 =
#  6 = 2 x 3           factors = 1, 2, 3, 6                sigma2 =
#  7 = 7               factors = 1, 7                      sigma2 =
#  8 = 2 x 2 x 2       factors = 1, 2, 4, 8                sigma2 =
#  9 = 3 x 3           factors = 1, 3, 9                   sigma2 =
# 10 = 2 x 5           factors = 1, 2, 5, 10               sigma2 =
# 11 = 11              factors = 1, 11                     sigma2 =
# 12 = 2 x 2 x 3       factors = 1, 2, 3, 4, 6, 12         sigma2 =
# 13 = 13              factors = 1, 13                     sigma2 =
# 14 = 2 x 7           factors = 1, 2, 7, 14               sigma2 =
# 15 = 3 x 5           factors = 1, 3, 5, 15               sigma2 =
# 16 = 2 x 2 x 2 x 2   factors = 1, 2, 4, 8, 16            sigma2 =
# 17 = 17              factors = 1, 17                     sigma2 =
# 18 = 2 x 3 x 3       factors = 1, 2, 6, 9, 18            sigma2 =
# 19 = 19              factors = 1, 19                     sigma2 =
# 20 = 2 x 2 x 5       factors = 1, 2, 4, 5, 10, 20        sigma2 =
# 21 = 3 x 7           factors = 1, 3, 7, 21               sigma2 =
# 22 = 2 x 11          factors = 1, 2, 11, 22              sigma2 =
# 23 = 23              factors = 1, 23                     sigma2 =
# 24 = 2 x 2 x 2 x 3   factors = 1, 2, 3, 4, 6, 8, 12, 24  sigma2 =



#  1 = 1               factors = 1                         sigma2 = 1
#  2 = 2               factors = 1, 2                      sigma2 = 1 + 4
#  3 = 3               factors = 1,
#  4 = 2 x 2           factors = 1, 2
#  5 = 5               factors = 1,
#  6 = 2 x 3           factors = 1, 2
#  7 = 7               factors = 1,
#  8 = 2 x 2 x 2       factors = 1, 2
#  9 = 3 x 3           factors = 1,
# 10 = 2 x 5           factors = 1, 2
# 11 = 11              factors = 1,
# 12 = 2 x 2 x 3       factors = 1, 2
# 13 = 13              factors = 1,
# 14 = 2 x 7           factors = 1, 2
# 15 = 3 x 5           factors = 1,
# 16 = 2 x 2 x 2 x 2   factors = 1, 2
# 17 = 17              factors = 1,
# 18 = 2 x 3 x 3       factors = 1, 2
# 19 = 19              factors = 1,
# 20 = 2 x 2 x 5       factors = 1, 2
# 21 = 3 x 7           factors = 1,
# 22 = 2 x 11          factors = 1, 2
# 23 = 23              factors = 1,
# 24 = 2 x 2 x 2 x 3   factors = 1, 2
