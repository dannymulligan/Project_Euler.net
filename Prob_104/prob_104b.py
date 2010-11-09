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
# Answer: 329468
# Solved: 11/11/09
# 105 problems solved
# Position #1016 on level 3


# Takes 6.586 seconds to test to F(10000) when using arbitrary precision math
# Takes 0.054 seconds to test to F(10000) when using standard math (i.e. truncating to bottom 10 digits at each step)
#  => arbitrary precision match is very slow

# Takes 572 minutes to get to F(175000), need a faster technique


def is_pandigital(n): return len(n)==9 and not '123456789'.strip(n)

pandigital = list('123456789')
pandigital.sort()

# Find n where F(n) is end pandigital
end_candidates = []

f0 = 1
f1 = 1
prev_n = 0
for n in range(3,340000):
    f0, f1 = f1, (f1 + f0) % 1000000000

    Fstring = str(f1)
    end = list(Fstring[-9:])
    end.sort()
    if (end == pandigital):
        print "    F({0}) = end pandigital, delta n = {1}".format(n, (n-prev_n))
        end_candidates.append(n)
        prev_n = n

print "{0} candidates to test".format(len(end_candidates))

# Search the list of end pandigital n's to find the first one that is start pandigital


# If we have
#    F(n-1) =   x
#    F(n)   =         y
# then
#    F(n+1) =  1x +  1y
#    F(n+2) =  1x +  2y
#    F(n+3) =  2x +  3y
#    F(n+4) =  3x +  5y
#    F(n+5) =  5x +  8y
#    F(n+6) =  8x + 13y
#    F(n+7) = 13x + 21y
#    F(n+8) = 21x + 34y
#    F(n+9) = 34x + 55y
#    etc...
# or
#    F(n+i) = F(i)x + F(i+1)y
# or
#    F(n+i)   =   F(i)F(n-1) + F(i+1)F(n)
#    F(n+i-1) = F(i-1)F(n-1) +   F(i)F(n)

# Calculate a table of the first 5,001 F(n)'s
F = [0, 1, 1]
for n in range(3,5002):
    fib = F[n-1] + F[n-2]
    F.append(fib)

# Process each item in end_candidates
n, Fn, Fn_m_1 = 2, F[2], F[1]
for next in end_candidates:
    print "Testing F({0})".format(next)
    delta_n = next - n
    while (delta_n > 0):
        if (delta_n > 5000):
            n, Fn, Fn_m_1 = (n+5000), (F[5000]*Fn_m_1 + F[5001]*Fn), (F[4999]*Fn_m_1 + F[5000]*Fn)
        else:
            n, Fn, Fn_m_1 = (n+delta_n), (F[delta_n]*Fn_m_1 + F[delta_n+1]*Fn), (F[delta_n-1]*Fn_m_1 + F[delta_n]*Fn)
        delta_n = next - n

        #print "    F({0}) = {1}".format(n,Fn)

    Fstring = str(Fn)
    start = list(Fstring[:9])
    start.sort()
    if (start == pandigital):
        print "    F({0}) = {1} digit number = start & end pandigital = {2}".format(n, len(Fstring), Fn)
