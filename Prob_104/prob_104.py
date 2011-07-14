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
# Solved:
# ? problems solved
# Position #??? on level ?


# Takes 6.586 seconds to test to F(10000)

pandigital = list('123456789')
pandigital.sort()

F = [0, 1, 1]

print "F({0}) = {1}".format(1, F[1])
print "F({0}) = {1}".format(2, F[2])

for i in range(3,10000):
    fib = F[i-1] + F[i-2]
    F.append(fib)

    Fstring = str(fib)
    start = list(Fstring[:9])
    end   = list(Fstring[-9:])
    start.sort()
    end.sort()
    print "F({0}) = {1}".format(i, F[i])
    if (start == pandigital == end):
        print "F({0}) = start & end pandigital ({1} digits long)".format(i, len(Fstring))
        print "Answer =", i+1
        exit()
    elif (start == pandigital):
        print "    F({0}) = start pandigital ({1} digits long)".format(i, len(Fstring))
    elif (end == pandigital):
        print "    F({0}) = end pandigital ({1} digits long)".format(i, len(Fstring))

    if ((i % 1000) == 0):
        print "Testing F({0}) = {1} digits long".format(i, len(Fstring))
