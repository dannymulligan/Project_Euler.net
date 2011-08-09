#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 137
#
# Determining the value of infinite polynomial series for which the
# coefficients are Fibonacci numbers.
#
# Consider the infinite polynomial series AF(x) = xF(1) + x^2F(2) +
# x^3F(3) + ..., where F(k) is the kth term in the Fibonacci sequence:
# 1, 1, 2, 3, 5, 8, ... ; that is, F(k) = F(k-1) + F(k−2), F(1) = 1
# and F(2) = 1.
#
# For this problem we shall be interested in values of x for which
# AF(x) is a positive integer.
#
# Surprisingly AF(1/2) = (1/2)*1 + (1/2)^2*1 + (1/2)^3*2 + (1/2)^4*3 +
# (1/2)^5*5 + ...
#         = 1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
#         = 2
#
# The corresponding values of x for the first five natural numbers are
# shown below.
#
#       x              AF(x)
#     sqrt(2)-1         1
#     1/2               2
#     (sqrt(13)-2)/3    3
#     (sqrt(89)-5)/8    4
#     (sqrt(34)-3)/5    5
#
# We shall call AF(x) a golden nugget if x is rational, because they
# become increasingly rarer; for example, the 10th golden nugget is
# 74049690.
#
# Find the 15th golden nugget.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

#           Af(x) = xF(1) + x^2F(2) + x^3F(3) + ... + x^nF(n  ) + ...
#      -   xAf(x) =         x^2F(1) + x^3F(2) + ... + x^nF(n-1) + ...
#      - x^2Af(x) =                   x^3F(1) + ... + x^nF(n-2) + ...
# --------------------------------------------------------------
# Af(x)*(1-x-x^2) = xF(1) + x^2(F(2)-F(1)) + 0 + ... + 0 + ...
# Af(x)*(1-x-x^2) = x
#
#               x
# Af(x) = -------------
#         (1 - x - x^2)
#
# for known Af(x) = N
#     N - N.X - N.X^2 = X
# or
#     N.X^2 + (N+1).X - N = 0
# which is of the form
#     a.X^2 + b.X + c = 0
# so
#         -b +/- sqrt(b^2 - 4ac)
#     X = ----------------------
#                 2a
# so
#         -(N+1) +/- sqrt(N^2 + 2N + 1 + 4N^2)
#     X = ------------------------------------
#                      2N
#
#         +/- sqrt(5N^2 + 2N + 1) - (N+1)
#     X = -------------------------------
#                      2N
#
# We're only using the +sqrt solution here (-sqrt works too)
#
#         sqrt(5N^2 + 2N + 1) - (N+1)
#     X = ---------------------------
#                     2N
# 
# For N = 1:
#         sqrt(5N^2 + 2N + 1) - (N+1)   sqrt(8) - 2   2sqrt(2) - 2
#     X = --------------------------- = ----------- = ------------
#                     2N                     2              2
#
#       = sqrt(2) - 1
#
# For N = 2:
#         sqrt(5N^2 + 2N + 1) - (N+1)   sqrt(25) - 3   5 - 3    1
#     X = --------------------------- = ------------ = ----- = ---
#                     2N                     4           4      2
#
# For N = 3:
#         sqrt(5N^2 + 2N + 1) - (N+1)   sqrt(52) - 4   sqrt(13) - 2
#     X = --------------------------- = ------------ = ------------
#                     2N                     6               3
#
# So the solution will be rational if sqrt(5N^2 + 2N + 1) is rational
# which will happen if (5N^2 + 2N + 1) is a square
#
# If we assume that 5N^2 + 2N + 1 = M^2, then
#     5N^2 + 2N + (1-M^2) = 0


import time
import sys
import cProfile

start_time = time.clock()

def f(N):
    return (5*N**2 + 2*N + 1)

def main():
    soln_cnt = 0
    N = 1
    M = 1
    while (soln_cnt < 15):
        #print "    M={0}, M^2={1}, N={2}, f(N)={3}".format(M, M**2, N, f(N))

        while (f(N) < M**2):
            N += 1
            #print "    N={0}, f({0})={1}".format(N,f(N))

        if (f(N) == M**2):
            soln_cnt += 1
            print "Golden nugget {0}: Af(x) = {1} has a rational x".format(soln_cnt, N)
            #print "    M={0}, M^2={1}, N={2}, f(N)={3}".format(M, M**2, N, f(N))
            if (soln_cnt < 2):
                M = M * 679 / 100
                N = N * 679 / 100
            elif (soln_cnt < 5):
                M = M * 685 / 100
                N = N * 685 / 100
            else:
                M = M * 68541 / 10000
                N = N * 68541 / 10000
            #print "    starting off search for next golden nugget with M={0}, N={1}".format(M,N)
            # Examinging the first 10 results shows that M grows by 6.8-6.85410197x from solution to solution
        else:
            M += 1

    print "Answer = ", N
    print "Time taken =", time.clock() - start_time, "seconds"

#cProfile.run('main()')
main()
