#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 197
#
# Investigating the behaviour of a recursively defined sequence
#
# Given is the function
#      f(x) = |_2^(30.403243784-x^2)_| × 10-9
# (|_ _| is the floor-function), the sequence u(n) is defined by
#     u(0) -1 and
#     u(n+1) = f(u(n)).
#
# Find u(n) + u(n+1) for n = 1012.
# Give your answer with 9 digits after the decimal point.
#
# Solved 07/10/10
# 149 problems solved
# Position #22 on level 3

# Trivia (but not relevant to this problem)
# 30,403,243,784 = 8 * 149 * 163 * 167 * 937

N = 30403243784

# Store values multiplied by 1,000,000,000 to allow us to store 9
# digits of precision in an integer
u = [-1000000000]  # u[0] = -1
print "u[{0}] = {1}".format(0,u[0])

for n in xrange(1,4000):
    #print "u[n-1] =", u[n-1]
    p = u[n-1]**2 / 1000000000
    #print "p =", p
    p = N - p
    #print "p =", p
    ff = 2**(p * 0.000000001)
    #print "ff =", ff
    f = int(ff)
    #print "f =", f
    u.append(f)

    print "u[{0}] = {1:11}".format(n,u[n])

# Begins repeating after 522 iterations...
#
# u[522] =  1029461841
# u[523] =   681175876
# u[524] =  1029461841
# u[525] =   681175876
#
# Therefore, the answer for any n > 522 will be 1.029461841 + 0.681175876 = 1.710637717
