#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 140
#
# Investigating the value of infinite polynomial series for which the
# coefficients are a linear second order recurrence relation.
#
# Consider the infinite polynomial series AG(x) = xG(1) + x^2G(2) +
# x^3G(3) + ..., where G(k) is the kth term of the second order
# recurrence relation G(k) = G(k-1) + G(k-2), G(1) = 1 and G(2) = 4;
# that is, 1, 4, 5, 9, 14, 23, ... .
#
# For this problem we shall be concerned with values of x for which
# AG(x) is a positive integer.
#
# The corresponding values of x for the first five natural numbers are
# shown below.
# 
#     x                AG(x)
#     (sqrt(5)-1)/4     1
#     2/5               2
#     (sqrt(22)-2)/6    3
#     (sqrt(137)-5)/14  4
#     1/2               5
# 
# We shall call AG(x) a golden nugget if x is rational, because they
# become increasingly rarer; for example, the 20th golden nugget is
# 211345365.
#
# Find the sum of the first thirty golden nuggets.
#
# Solved 08/11/11
# 162 problems solved
# Position #476 on level 4


#           AG(x) = xG(1) + x^2G(2) + x^3G(3) + ... + x^nG(n  ) + ...
#      -   xAG(x) =         x^2G(1) + x^3G(2) + ... + x^nG(n-1) + ...
#      - x^2AG(x) =                   x^3G(1) + ... + x^nG(n-2) + ...
# --------------------------------------------------------------
# AG(x)*(1-x-x^2) = xG(1) + x^2(G(2)-G(1)) + 0 + ... + 0 + ...
# AG(x)*(1-x-x^2) = x + 3x^2
#
#            x + 3x^2
# AG(x) = -------------
#         (1 - x - x^2)
#
# for known AG(x) = N
#     N - N.X - N.X^2 = X + 3.X^2
# or
#     (N+3).X^2 + (N+1).X - N = 0
# which is of the form
#     a.X^2 + b.X + c = 0
# so
#         -b +/- sqrt(b^2 - 4ac)
#     X = ----------------------
#                 2a
# so
#         -(N+1) +/- sqrt(N^2 + 2N + 1 + 4N.(N+3))
#     X = ----------------------------------------
#                      2(N+3)
#
#         +/- sqrt(5N^2 + 14N + 1) - (N+1)
#     X = -------------------------------
#                      2N+6
#
# We're only using the +sqrt solution here (-sqrt works too)
#
#         sqrt(5N^2 + 14N + 1) - (N+1)
#     X = ----------------------------
#                     2N+6
# 
# For N = 1:
#         sqrt(5N^2 + 14N + 1) - (N+1)   sqrt(20) - 2   sqrt(5) - 1
#     X = ---------------------------- = ------------ = -----------
#                     2N+6                    8              4
#       = sqrt(2) - 1
#
# For N = 2:
#         sqrt(5N^2 + 14N + 1) - (N+1)   sqrt(49) - 3   7 - 3    2
#     X = ---------------------------- = ------------ = ----- = ---
#                     2N+6                    10         10      5
#
# For N = 3:
#         sqrt(5N^2 + 14N + 1) - (N+1)   sqrt(88) - 4   sqrt(22) - 2
#     X = ---------------------------- = ------------ = ------------
#                     2N+6                    12              6
#
# So the solution will be rational if sqrt(5N^2 + 14N + 1) is rational
# which will happen if (5N^2 + 14N + 1) is a square
#
# If we assume that 5N^2 + 14N + 1 = M^2, then
#     5N^2 + 14N + (1-M^2) = 0



import time

start_time = time.clock()

def even(n):
    return not(n%2)

def f(n):
    return 5*n**2 + 14*n + 1

def main():
    answer = 0
    soln_cnt = 0
    n = 1
    m = 1
    prev_m = 1
    while soln_cnt < 30:
        #print "    M={0}, M^2={1}, N={2}, f(N)={3}".format(M, M**2, N, f(N))

        while f(n) < m**2:
            n += 1
            #print "    N={0}, f({0})={1}".format(N,f(N))

        if f(n) == m**2:
            soln_cnt += 1
            answer += n
            print "Golden nugget {0}: Af(x) = {1} has a rational x, (M,N) = ({2},{3})".format(soln_cnt, n, m,n),

            print "M={0}, prev_M={1}, ratio={2}".format(m,prev_m,1.0*m/prev_m),
            prev_m = m

            if soln_cnt < 2:
                m += 1
            elif soln_cnt < 12:
                if even(soln_cnt):
                    m = m * 353 / 100
                    n = n * 353 / 100
                else:
                    m = m * 193 / 100
                    n = n * 193 / 100
            elif soln_cnt < 20:
                if even(soln_cnt):
                    m = m * 353532 / 100000
                    n = n * 353532 / 100000
                else:
                    m = m * 193874 / 100000
                    n = n * 193874 / 100000
            else:
                if even(soln_cnt):
                    m = m * 35353221 / 10000000
                    n = n * 35353221 / 10000000
                else:
                    m = m * 19387489 / 10000000
                    n = n * 19387489 / 10000000

            print "new (M,N)=({0},{1})".format(m,n)

            #elif (soln_cnt < 5):
            #    M = M * 685 / 100
            #    N = N * 685 / 100
            #else:
            #    M = M * 68541 / 10000
            #    N = N * 68541 / 10000
            #print "    starting off search for next golden nugget with M={0}, N={1}".format(M,N)
            # Examining the first 10 results shows that M grows by 6.8-6.85410197x from solution to solution
        else:
            m += 1

    print "Answer = ", answer
    print "Time taken =", time.clock() - start_time, "seconds"

#cProfile.run('main()')
main()
