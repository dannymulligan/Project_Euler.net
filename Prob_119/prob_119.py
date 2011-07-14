#!/usr/bin/python
#
# Project Euler.net Problem 119
# 
# The number 512 is interesting because it is equal to the sum of its
# digits raised to some power: 5 + 1 + 2 = 8, and 8^(3) = 512. Another
# example of a number with this property is 614656 = 28^(4).
# 
# We shall define a_(n) to be the nth term of this sequence and insist
# that a number must contain at least two digits to have a sum.
# 
# You are given that a_(2) = 512 and a_(10) = 614656.
# 
# Find a_(30).
#
# Solved 11/?/09
# 10? solved
# Position #???? on level 3

count = 0
for n in range(10,100000000):
    digits = map(lambda x: int(x), list(str(n)))
    b = reduce(lambda x, y: x+y, digits)

    # search for n = b^x
    if (((n % b) == 0) & (b != 1)):
        nc = n
        x = 0
        while ((nc != 1) & ((nc % b) == 0)):
            x += 1
            nc /= b
        if (nc == 1):
            count += 1
            print "a({0}) = {1} = {2}^{3}".format(count,n,b,x)
