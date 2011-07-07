#!/usr/bin/python
#
# Project Euler.net Problem 110
#
# n the following equation x, y, and n are positive integers.
#
#     1     1     1
#    --- + --- = ---
#     x     y     n
#
# It can be verified that when n = 1260 there are 113 distinct
# solutions and this is the least value of n for which the total
# number of distinct solutions exceeds one hundred.
#
# What is the least value of n for which the number of distinct
# solutions exceeds four million?
#
# NOTE: This problem is a much more difficult version of problem 108
# and as it is well beyond the limitations of a brute force approach
# it requires a clever implementation.
#
# Answer: 9350130049860600
# Solved: 7/7/11
# 146 problems solved
# Position #83 on level 3

# See solution for problem 107

# ####################
# 5 answers found with n = 6
#
# n = 6 = 2^1 * 3^1
# n^2 = 2^2 + 3^2
#
# possible values of a = (1 + 3 * 3) / 2 = 5
# n^2 = 36 = 2*18, 3*12, 6*6,
#
# ####################
# 8 answers found with n = 12
#
# n = 12 = 2^2 * 3
# n^2 = 2^4 * 3^2
#
# a = 2^0 * 3^0 = 1
# a = 2^1 * 3^0 = 2
# a = 2^2 * 3^0 = 4
# a = 2^3 * 3^0 = 8
# a = 2^0 * 3^1 = 3
# a = 2^1 * 3^1 = 6
# a = 2^0 * 3^2 = 9
# a = 2^2 * 3^1 = 12
# a = 2^1 * 3^2 = 18
# a = 2^3 * 3^1 = 24
# a = 2^2 * 3^2 = 36
# a = 2^3 * 3^2 = 72
#
# n^2 = 144 = 1*144, 2*72, 3*48, 4*36, 6*24, 8*18, 9*16, 12*12
#
# possible values of a =
#
# ####################
# 41 answers found with n = 210
#
# n = 210 = 2 * 3 * 5 * 7
# n^2 = 2^2 * 3^3 * 5^2 * 7^2
#
# a * b = n^2
#
# possible values of a = (1 + 3 * 3 * 3 * 3) / 2 = 41
#
# ####################
# 63 answers found with n = 900
# n = 900 = 2^2 * 3^2 * 5^2
#
# n^2 = 2^4 * 3^4 * 5^4
#
# posible values of a = (1 + 5 * 5 * 5) / 2 = 63
#
# 1 answers found with n = 1
# 2 answers found with n = 2
# 3 answers found with n = 4
# 5 answers found with n = 6
# 8 answers found with n = 12
# 14 answers found with n = 30
# 13 answers found with n = 36
# 23 answers found with n = 60
# 38 answers found with n = 180
# 68 answers found with n = 420
# 63 answers found with n = 900
# 113 answers found with n = 1260
# 122 answers found with n = 2310
# 203 answers found with n = 4620
# 188 answers found with n = 6300
# 338 answers found with n = 13860
# 365 answers found with n = 30030
# 313 answers found with n = 44100
# 608 answers found with n = 60060
# 563 answers found with n = 69300
# 1013 answers found with n = 180180

primes = [41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]

def calc_poss(num):
    ans = 1
    for i in num:
        ans *= (2*i+1)
    ans += 1
    ans /= 2
    return ans

def calc_n(num):
    ans = 1
    for i in range(len(num)):
        ans *= primes[i]**num[i]
    return ans


ans_e = False
ans_n = 0
ans_p = 0

#nn = []
#nn.append([0, 3, 3, 3, 3, 3, 3, 3, 3])
#nn.append([1, 3, 3, 3, 3, 3, 3, 3, 3])
#nn.append([1, 2, 4, 3, 3, 3, 3, 3, 3])
#nn.append([1, 2, 3, 3, 3, 3, 3, 3, 4])
#nn.append([1, 1, 3, 3, 3, 3, 3, 4, 4])
#nn.append([1, 1, 2, 3, 3, 3, 3, 4, 4])
#nn.append([1, 1, 1, 3, 3, 3, 4, 4, 5])
#
#for x in nn:
#    n = calc_n(x)
#    p = calc_poss(x)
#    print x, p, n
#    if (p > 4000000):
#        if (ans_e):
#            if (n < ans_n):
#                ans_n = n
#                ans_p = p
#        else:
#            ans_e = True
#            ans_n = n
#            ans_p = p
#
#if (ans_e):
#    print "Answer =", ans_n
#    print "This answer has", ans_p, "solutions"
#else:
#    print "Answer not found"
#
for p0 in range(2):
    for p1 in range(2):
        for p2 in range(2):
            for p3 in range(2):
                for p4 in range(2):
                    for p5 in range(2):
                        for p6 in range(2):
                            for p7 in range(3):
                                for p8 in range(3):
                                    for p9 in range(3):
                                        for pa in range(4):
                                            for pb in range(4):
                                                for pc in range(4):
                                                        x = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, pa, pb, pc]
                                                        n = calc_n(x)
                                                        p = calc_poss(x)
                                                        #print x, p, n
                                                        if (p > 4000000):
                                                            if (ans_e):
                                                                if (n < ans_n):
                                                                    ans_n = n
                                                                    ans_p = p
                                                                    print x, p, n
                                                            else:
                                                                ans_e = True
                                                                ans_n = n
                                                                ans_p = p

if (ans_e):
    print "Answer =", ans_n
    print "This answer has", ans_p, "solutions"
else:
    print "Answer not found"

# [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 6] 4146188 139885119141768000
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 7] 4018613  20216497405104000
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3] 4018613   9350130049860600
