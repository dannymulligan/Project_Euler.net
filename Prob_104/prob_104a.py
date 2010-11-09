#!/usr/bin/python
#
# Project Euler.net Problem 104
# 
# The Fibonacci sequence is defined by the recurrence relation:
# 
#     F_(n) = F_(n-1) + F_(n-2), where F_(1) = 1 and F_(2) = 1.
# 
# It turns out that F_(541), which contains 113 digits, is the first
# Fibonacci number for which the last nine digits are 1-9 pandigital
# (contain all the digits 1 to 9, but not necessarily in order). And
# F_(2749), which contains 575 digits, is the first Fibonacci number
# for which the first nine digits are 1-9 pandigital.
# 
# Given that F_(k) is the first Fibonacci number for which the first
# nine digits AND the last nine digits are 1-9 pandigital, find k.
#
# Answer:
# Solved:
# ? problems solved
# Position #??? on level ?


# Takes 6.586 seconds to test to F(10000) when using arbitrary precision math
# Takes 0.054 seconds to test to F(10000) when using standard math (i.e. truncating to bottom 10 digits at each step)
#  => arbitrary precision match is very slow

# Takes 572 minutes to get to F(175000), need a faster technique


def is_pandigital(n): return len(n)==9 and not '123456789'.strip(n)

pandigital = list('123456789')
pandigital.sort()

f0 = 1
f1 = 1
for i in range(3,400000):
#    f0, f1 = f1, (f1 + f0) % 1000000000
    f0, f1 = f1, (f1 + f0)

    Fstring = str(f1)
    start = list(Fstring[:9])
    end   = list(Fstring[-9:])
    start.sort()
    end.sort()
    #print "F({0}) = {1}".format(i, F[i])
    #if (start == pandigital == end):
    #    print "F({0}) = start & end pandigital ({1} digits long)".format(i, len(Fstring))
    #    print "Answer =", i+1
    #    exit()
    if (start == pandigital):
        print "    F({0}) = start pandigital ({1} digits long)".format(i, len(Fstring))
    elif (end == pandigital):
        print "    F({0}) = end pandigital ({1} digits long)".format(i, len(Fstring))

    if ((i % 1000) == 0):
        print "Testing F({0}) = {1} digits long".format(i, len(Fstring))
