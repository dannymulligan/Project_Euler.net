#!/usr/bin/python
#
# Project Euler.net Problem 113
#
# Working from left-to-right if no digit is exceeded by the digit to
# its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is
# called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor
# decreasing a "bouncy" number; for example, 155349.
#
# As n increases, the proportion of bouncy numbers below n increases
# such that there are only 12951 numbers below one-million that are
# not bouncy and only 277032 non-bouncy numbers below 10^10.
#
# How many numbers below a googol (10^100) are not bouncy?
#
# Answer:
# Solved 07/04/11
# ??? problems solved
# Position #??? on level 3

import sys

r = 0
f = 0
b = 0
for i in range(1,1000000):
    ii = i
    n0 = ii % 10
    ii = (ii - n0)/10
    n1 = ii % 10
    ii = (ii - n1)/10
    n2 = ii % 10
    ii = (ii - n2)/10
    n3 = ii % 10
    ii = (ii - n3)/10
    n4 = ii % 10
    ii = (ii - n4)/10
    n5 = ii % 10

    rising = False
    falling = False

    if ((n5 <= n4) & (n4 <= n3) & (n3 <= n2) & (n2 <= n1) & (n1 <= n0)):
        rising = True

    if (
           (        (n5 >= n4 >= n3 >= n2 >= n1 >= n0))
         | ((n5 == 0)  &  (n4 >= n3 >= n2 >= n1 >= n0))
         | ((n5 == n4 == 0)  &  (n3 >= n2 >= n1 >= n0))
         | ((n5 == n4 == n3 == 0)  &  (n2 >= n1 >= n0))
         | ((n5 == n4 == n3 == n2 == 0)  &  (n1 >= n0))
         | ((n5 == n4 == n3 == n2 == n1 == 0)         )
       ):
        falling = True

    if (rising & falling):  b += 1
    elif (rising):          r += 1
    elif (falling):         f += 1

    if ((i == 999) | (i == 9999) | (i == 99999) | (i == 999999)):
        print "1..{0:6}: ".format(i), "Rising = {0:4},".format(r+b), "Falling = {0:4},".format(f+b), "Both = {0:4},".format(b), "Not bouncy = {0:4}".format(f+r+b)

#           Falling  Rising
#   0-  9 =  10       10
#  10- 99 =  54       45
# 100-199 =   3       45
# 200-299 =   6       36
# 300-399 =  10       28
# 400-499 =  15       21
# 500-599 =  21       15
# 600-699 =  28       10
# 700-799 =  36        6
# 800-899 =  45        3
# 900-999 =  55        1
#
# Total     283      220

# Need to subtract 1 because algorithm counts 000...000 as a valid
# decreasing number.  Each valid increasing number is a valid
# decreasing number written backwards, so count of increasing numbers
# = count of decreasing numbers.  So our answer = 2*(result-1)
sys.exit()
