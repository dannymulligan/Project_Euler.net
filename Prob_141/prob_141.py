#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 141
#
# Investigating progressive numbers, n, which are also square.
#
# A positive integer, n, is divided by d and the quotient and
# remainder are q and r respectively. In addition d, q, and r are
# consecutive positive integer terms in a geometric sequence, but not
# necessarily in that order.
#
# For example, 58 divided by 6 has quotient 9 and remainder 4. It can
# also be seen that 4, 6, 9 are consecutive terms in a geometric
# sequence (common ratio 3/2).
#
# We will call such numbers, n, progressive.
#
# Some progressive numbers, such as 9 and 10404 = 1022, happen to also
# be perfect squares.  The sum of all progressive perfect squares
# below one hundred thousand is 124657.
#
# Find the sum of all progressive perfect squares below one trillion
# (10^12).
#
# Solved 04/09/14
# 190 problems solved

import time

start_time = time.clock()

def gcd(a,b):
    if (b > a):
        a,b = b,a
    while b:
        a, b = b, a%b
    return a

# from: https://stackoverflow.com/questions/15390807/integer-square-root-in-python
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# And here's our new is_square function
def is_square(n):
    x = isqrt(n)
    if (x**2 == n):
        return True
    return False

def generate_candidates(n_limit):
    r = 1
    while ((r**2 + r) < n_limit):
        for (n, d, q, r, a, b) in generate_candidates_given_r(r, n_limit):
            yield (n, d, q, r, a, b)
        r += 1

def generate_candidates_given_r(r, n_limit):
    b = 1
    while True:  # Loop through values of b
        a = b+1
        while ((r % (b**2)) == 0):  # Loop through values of a
            if (gcd(a,b) == 1):
                q = r*a/b
                d = r*a*a/b/b
                n = d*q + r
                if (n < n_limit):
                    yield (n, d, q, r, a, b)
                else:
                    break
            a += 1

        b += 1
        if (b**2 > r):
            break

def solve_problem(n_limit, debug=False):
    answer = 0
    for (n, d, q, r, a, b) in generate_candidates(n_limit):
        if is_square(n):
            answer += n
            if debug:
                print("{n:5} = {d}*{q} + {r}    (ratio = {a}/{b})".format(n=n, d=d, q=q, r=r, a=a, b=b))
    return answer

print("Answer = {}".format(solve_problem(1000000000000)))  # n < 10^12
print("Time taken =", time.clock() - start_time, "seconds")
