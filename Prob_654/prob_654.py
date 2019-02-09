#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 654
#
# Neighbourly Constraints
#
# Let T(n,m) be the number of m-tuples of positive integers such that
# the sum of any two neighbouring elements of the tuple is <=n.
#
# For example, T(3,4)=8, via the following eight 4-tuples:
#    (1,1,1,1)
#    (1,1,1,2)
#    (1,1,2,1)
#    (1,2,1,1)
#    (1,2,1,2)
#    (2,1,1,1)
#    (2,1,1,2)
#    (2,1,2,1)
#
# You are also given that T(5,5)=246, T(10,10^2)≡862820094(mod 1000000007)
# and T(10^2,10)≡782136797(mod 1000000007).
#
# Find T(5000,10^12) mod 1000000007.

import sys
import time
start_time = time.clock()
import functools

DEBUG = True
DEBUG = False

if DEBUG:
    print(sys.version)

PRIME = 1000000007


###############################################################################

@functools.lru_cache(maxsize=2**22)
def Comb(S, P, B, E, Depth=1, Debug=DEBUG):
    '''Calculate number of m-tuples of length P+1
    S = max sum of a pair
    P = number of pairs
    B = beginning value (0 means any valid value)
    E = ending value (0 means any valid value)'''

    global Calls
    Calls += 1

    print("  "*Depth, end='')
    print("Comb(P={}, {:2} - {:2})".format(P, B, E))
    if Debug:
        print("Comb(S={},P={},B={},E={})".format(S, P, B, E))

    assert (B <= E), ("Comb(S={},P={},B={},E={})".format(S, P, B, E))

    if   (P == 1) and (B == 0) and (E == 0):
        Result = S*(S-1)//2

    elif (P == 1) and (B == 0):
        Result = max(0, (S-E))

    # Optimized the (P == 1) and (E == 0) case away by ensuring B <= E

    elif (P == 1):
        if ((B + E) <= S):
            Result = 1
        else:
            Result = 0

    elif (P == 2) and (B != 0) and (E != 0):
        Result = S - max(B, E)

    else:
        # Implement divide and conquer recursion
        # Divide and conquer using powers of 2, to allow caching to work better
        Result = 0

        Split = 1
        while Split*2 < P:
            Split *= 2
        #Split = P//2
        for Mid in range(1,S):
            if (B > Mid):
                Left  = Comb(S, Split, Mid, B, Depth+1)
            else:
                Left  = Comb(S, Split, B, Mid, Depth+1)
            if (Mid > E):
                Right = Comb(S, P - Split, E, Mid, Depth+1)
            else:
                Right = Comb(S, P - Split, Mid, E, Depth+1)
            Result = (Result + Left * Right) % PRIME
            if Debug:
                print("    Recursing to L = Comb(S={},P={},B={},E={}) = {}".format(S, P//2, B, Mid, Left))
                print("    Recursing to R = Comb(S={},P={},B={},E={}) = {}".format(S, P - P//2, Mid, E, Right))
                print("    Result += {} * {}".format(Left, Right))

        if Debug:
            print("Comb(S={},P={},B={},E={}) = {}".format(S, P, B, E, Result))
    return Result % PRIME

###############################################################################

def T(n, m):
    return Comb(S=n, P=m-1, B=0, E=0)

###############################################################################


TestData = [
    # ((  n,      m)    T(n, m)),
    # ((  3,      4),         8),  # problem description
    # ((  3,      5),        13),  # hand calculated
    # ((  4,      4),        31),  # hand calculated
    # ((  5,      5),       246),  # problem description
    # ((  5,     10),     48620),
    # ((  5,     20), 904652096),
    # ((  5,     50), 470279892),
    # ((  5,    100), 507204810),
    # (( 10,     10),  83833256),  # problem description
    # (( 10,     25), 247610452),
    # (( 10,     50), 474746258),
    # (( 10,    100), 862820094),  # problem description
    # (( 10,    200), 504071520),
    # (( 10,    500),  51121641),
    # (( 10,   1000), 380913635),
    # (( 20,    257),  44422060),
      (( 20,    513), 593197885),
    # (( 20,   1000), 785677136),
    # (( 30,   1000), 500353563),
    # (( 40,   1000), 244000114),
    # (( 50,   1000),   2128094),
    # (( 60,   1000), 411903171),
    # (( 80,   1000), 171954316),
    # ((100,   1000), 501206836),
    # ((200,   1000), 382292968),
    # ((400,   1000), 721621254),
    # (( 10,   2000), 321695548),
    # (( 10,   4000), 919409306),
    # (( 10,   8000), 581708032),
    # (( 10,  10**4), 442497068),
    # ((100,  10**4), 274534218),
    # ((200,  10**4), 446641259),
    # (( 10,  10**6), 110065821),
    # ((100,  10**6), 573315194),
    # (( 10,  10**8), 296483121),
    # (( 10, 10**10), 577517464),
    # (( 10, 10**12), 660447611),
    # (( 20, 10**12), 712726820),
    # (( 30, 10**12), 787281392),
    # (( 40, 10**12),  14261752),
    # (( 50, 10**12), 737148354),
    # (( 60, 10**12), 403897723),
    # (( 80, 10**12), 947086078),
    # ((100, 10**12), 841900381),
    # (( 20,     10), 826079706),
    # (( 30,     10), 213392789),
    # (( 40,     10), 441011854),
    # (( 50,     10), 576909352),
    # (( 60,     10), 883964964),
    # (( 70,     10), 546153888),
    # (( 80,     10), 215968804),
    # (( 90,     10), 955789694),
    # ((100,     10), 782136797),  # problem description
    # ((200,     10), 644523115),
    # ((250,     10), 934021685),
    # ((500,     10), 255819865),
]

for ((n, m), expect) in TestData:
    b_time = time.clock()
    Calls = 0
    Comb.cache_clear()
    result = T(n, m)
    #print(Comb.cache_info())
    e_time = time.clock()
    if (result != expect) and (expect != 0):
        print("ERROR: T({}, {}) = {}, expecting {}".format(n, m, result, expect), end='')
    else:
        print("T({}, {}) = {}".format(n, m, result), end='')
    print(", calculated in {:.2f} seconds with {:,} calls".format(e_time-b_time, Calls))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))

#
# Initial working version, with @functools.lru_cache(), cleared between testcases
#
# T(3, 4) = 8, calculated in 0.00 seconds with 10 calls
# T(3, 5) = 13, calculated in 0.00 seconds with 8 calls
# T(4, 4) = 31, calculated in 0.00 seconds with 16 calls
# T(5, 5) = 246, calculated in 0.00 seconds with 19 calls
# T(5, 10) = 48620, calculated in 0.00 seconds with 67 calls
# T(5, 20) = 904652096, calculated in 0.00 seconds with 85 calls
# T(5, 50) = 470279892, calculated in 0.00 seconds with 115 calls
# T(5, 100) = 507204810, calculated in 0.00 seconds with 133 calls
# T(10, 10) = 83833256, calculated in 0.00 seconds with 1,019 calls
# T(10, 25) = 247610452, calculated in 0.04 seconds with 10,988 calls
# T(10, 50) = 474746258, calculated in 0.74 seconds with 238,029 calls
# T(10, 100) = 862820094, calculated in 10.46 seconds with 3,395,042 calls
# T(20, 10) = 826079706, calculated in 0.15 seconds with 119,487 calls
# T(30, 10) = 213392789, calculated in 0.79 seconds with 727,027 calls
# T(40, 10) = 441011854, calculated in 2.55 seconds with 2,520,764 calls
# T(50, 10) = 576909352, calculated in 6.26 seconds with 6,355,901 calls
# T(60, 10) = 883964964, calculated in 12.86 seconds with 13,150,786 calls
# T(70, 10) = 546153888, calculated in 33.50 seconds with 46,491,235 calls
# T(80, 10) = 215968804, calculated in 58.47 seconds with 79,978,495 calls
# T(90, 10) = 955789694, calculated in 93.21 seconds with 128,835,155 calls
#
# Bigger lru_cache maxsize=2**16
#
# T(3, 4) = 8, calculated in 0.00 seconds with 10 calls
# T(3, 5) = 13, calculated in 0.00 seconds with 8 calls
# T(4, 4) = 31, calculated in 0.00 seconds with 16 calls
# T(5, 5) = 246, calculated in 0.00 seconds with 19 calls
# T(5, 10) = 48620, calculated in 0.00 seconds with 67 calls
# T(5, 20) = 904652096, calculated in 0.00 seconds with 85 calls
# T(5, 50) = 470279892, calculated in 0.00 seconds with 115 calls
# T(5, 100) = 507204810, calculated in 0.00 seconds with 133 calls
# T(10, 10) = 83833256, calculated in 0.00 seconds with 262 calls
# T(10, 25) = 247610452, calculated in 0.00 seconds with 262 calls
# T(10, 50) = 474746258, calculated in 0.00 seconds with 460 calls
# T(10, 100) = 862820094, calculated in 0.00 seconds with 523 calls
# T(10, 200) = 504071520, calculated in 0.00 seconds with 586 calls
# T(20, 10) = 826079706, calculated in 0.01 seconds with 1,027 calls
# T(30, 10) = 213392789, calculated in 0.03 seconds with 2,292 calls
# T(40, 10) = 441011854, calculated in 0.06 seconds with 4,057 calls
# T(50, 10) = 576909352, calculated in 0.11 seconds with 6,322 calls
# T(60, 10) = 883964964, calculated in 0.18 seconds with 9,087 calls
# T(70, 10) = 546153888, calculated in 0.29 seconds with 12,352 calls
# T(80, 10) = 215968804, calculated in 0.42 seconds with 16,117 calls
# T(90, 10) = 955789694, calculated in 0.61 seconds with 20,382 calls
# T(100, 10) = 782136797, calculated in 0.81 seconds with 25,147 calls
# T(200, 10) = 644523115, calculated in 8.42 seconds with 112,876 calls
# Time taken = 10.94 seconds
#
# Bigger lru_cache maxsize=2**22
#
# T(3, 4) = 8, calculated in 0.00 seconds with 10 calls
# T(3, 5) = 13, calculated in 0.00 seconds with 8 calls
# T(4, 4) = 31, calculated in 0.00 seconds with 16 calls
# T(5, 5) = 246, calculated in 0.00 seconds with 19 calls
# T(5, 10) = 48620, calculated in 0.00 seconds with 67 calls
# T(5, 20) = 904652096, calculated in 0.00 seconds with 85 calls
# T(5, 50) = 470279892, calculated in 0.00 seconds with 115 calls
# T(5, 100) = 507204810, calculated in 0.00 seconds with 133 calls
# T(10, 10) = 83833256, calculated in 0.00 seconds with 262 calls
# T(10, 25) = 247610452, calculated in 0.00 seconds with 262 calls
# T(10, 50) = 474746258, calculated in 0.00 seconds with 460 calls
# T(10, 100) = 862820094, calculated in 0.00 seconds with 523 calls
# T(10, 200) = 504071520, calculated in 0.00 seconds with 586 calls
# T(20, 10) = 826079706, calculated in 0.01 seconds with 1,027 calls
# T(30, 10) = 213392789, calculated in 0.03 seconds with 2,292 calls
# T(40, 10) = 441011854, calculated in 0.06 seconds with 4,057 calls
# T(50, 10) = 576909352, calculated in 0.11 seconds with 6,322 calls
# T(60, 10) = 883964964, calculated in 0.19 seconds with 9,087 calls
# T(70, 10) = 546153888, calculated in 0.30 seconds with 12,352 calls
# T(80, 10) = 215968804, calculated in 0.42 seconds with 16,117 calls
# T(90, 10) = 955789694, calculated in 0.61 seconds with 20,382 calls
# T(100, 10) = 782136797, calculated in 0.82 seconds with 25,147 calls
# T(200, 10) = 644523115, calculated in 7.39 seconds with 100,297 calls
# Time taken = 9.94 seconds
#
# Optimized the (P==2) and (B!=0) and (E != 0) common case to calculate
# locally and not recurse
#
# T(3, 4) = 8, calculated in 0.00 seconds with 10 calls
# T(3, 5) = 13, calculated in 0.00 seconds with 8 calls
# T(4, 4) = 31, calculated in 0.00 seconds with 16 calls
# T(5, 5) = 246, calculated in 0.00 seconds with 19 calls
# T(5, 10) = 48620, calculated in 0.00 seconds with 57 calls
# T(5, 20) = 904652096, calculated in 0.00 seconds with 75 calls
# T(5, 50) = 470279892, calculated in 0.00 seconds with 105 calls
# T(5, 100) = 507204810, calculated in 0.00 seconds with 123 calls
# T(10, 10) = 83833256, calculated in 0.00 seconds with 217 calls
# T(10, 25) = 247610452, calculated in 0.00 seconds with 217 calls
# T(10, 50) = 474746258, calculated in 0.00 seconds with 415 calls
# T(10, 100) = 862820094, calculated in 0.00 seconds with 478 calls
# T(10, 200) = 504071520, calculated in 0.00 seconds with 541 calls
# T(20, 10) = 826079706, calculated in 0.00 seconds with 837 calls
# T(30, 10) = 213392789, calculated in 0.01 seconds with 1,857 calls
# T(40, 10) = 441011854, calculated in 0.02 seconds with 3,277 calls
# T(50, 10) = 576909352, calculated in 0.04 seconds with 5,097 calls
# T(60, 10) = 883964964, calculated in 0.07 seconds with 7,317 calls
# T(70, 10) = 546153888, calculated in 0.11 seconds with 9,937 calls
# T(80, 10) = 215968804, calculated in 0.15 seconds with 12,957 calls
# T(90, 10) = 955789694, calculated in 0.23 seconds with 16,377 calls
# T(100, 10) = 782136797, calculated in 0.29 seconds with 20,197 calls
# T(200, 10) = 644523115, calculated in 2.41 seconds with 80,397 calls
# Time taken = 3.36 seconds
#
# Optimized to favor P = powers of 2 when recursing
#
# T(3, 4) = 8, calculated in 0.00 seconds with 10 calls
# T(3, 5) = 13, calculated in 0.00 seconds with 8 calls
# T(4, 4) = 31, calculated in 0.00 seconds with 16 calls
# T(5, 5) = 246, calculated in 0.00 seconds with 19 calls
# T(5, 10) = 48620, calculated in 0.00 seconds with 51 calls
# T(5, 20) = 904652096, calculated in 0.00 seconds with 93 calls
# T(5, 50) = 470279892, calculated in 0.00 seconds with 89 calls
# T(5, 100) = 507204810, calculated in 0.00 seconds with 123 calls
# T(10, 10) = 83833256, calculated in 0.00 seconds with 181 calls
# T(10, 25) = 247610452, calculated in 0.00 seconds with 397 calls
# T(10, 50) = 474746258, calculated in 0.00 seconds with 334 calls
# T(10, 100) = 862820094, calculated in 0.00 seconds with 478 calls
# T(10, 200) = 504071520, calculated in 0.00 seconds with 622 calls
# T(20, 10) = 826079706, calculated in 0.00 seconds with 666 calls
# T(30, 10) = 213392789, calculated in 0.01 seconds with 1,451 calls
# T(40, 10) = 441011854, calculated in 0.02 seconds with 2,536 calls
# T(50, 10) = 576909352, calculated in 0.04 seconds with 3,921 calls
# T(60, 10) = 883964964, calculated in 0.07 seconds with 5,606 calls
# T(70, 10) = 546153888, calculated in 0.11 seconds with 7,591 calls
# T(80, 10) = 215968804, calculated in 0.16 seconds with 9,876 calls
# T(90, 10) = 955789694, calculated in 0.22 seconds with 12,461 calls
# T(100, 10) = 782136797, calculated in 0.29 seconds with 15,346 calls
# T(200, 10) = 644523115, calculated in 2.39 seconds with 60,696 calls
# Time taken = 3.34 seconds
#


############################################################
#
# T(3,5)=13, via the following...
#    (1,1,1,1,1)
#    (1,1,1,1,2)
#    (1,1,1,2,1)
#    (1,1,2,1,1)
#    (1,2,1,1,1)
#    (2,1,1,1,1)
#    (1,1,2,1,2)
#    (1,2,1,1,2)
#    (2,1,1,1,2)
#    (1,2,1,2,1)
#    (2,1,1,2,1)
#    (2,1,2,1,1)
#    (2,1,2,1,2)
#
# T(4,4)=31, via the following...
#
#    (1,1)
#    (2,1)
#    (3,1)        3 solutions
#       *         *
#      (1,1,1)    6 solutions
#      (1,1,2)    =
#      (1,1,3)    18 solutions
#      (1,2,1)
#      (1,2,2)
#      (1,3,1)
#
#    (1,2)
#    (2,2)        2 solutions
#       *         *
#      (2,1,1)    5 solutions
#      (2,1,2)    =
#      (2,1,3)    10 solutions
#      (2,2,1)
#      (2,2,2)
#
#    (1,3)        1 solution
#       *         *
#      (3,1,1)    3 solutions
#      (3,1,2)    =
#      (3,1,3)    3 solutions
#
#  31 solutions total
#    (1,1,1,1)
#    (1,1,1,2)
#    (1,1,1,3)
#    (1,1,2,1)
#    (1,1,2,2)
#    (1,1,3,1)
#    (1,2,1,1)
#    (1,2,1,2)
#    (1,2,1,3)
#    (1,2,2,1)
#    (1,2,2,2)
#    (1,3,1,1)
#    (1,3,1,2)
#    (1,3,1,3)
#    (2,1,1,1)
#    (2,1,1,2)
#    (2,1,1,3)
#    (2,1,2,1)
#    (2,1,2,2)
#    (2,1,3,1)
#    (2,2,1,1)
#    (2,2,1,2)
#    (2,2,1,3)
#    (2,2,2,1)
#    (2,2,2,2)
#    (3,1,1,1)
#    (3,1,1,2)
#    (3,1,1,3)
#    (3,1,2,1)
#    (3,1,2,2)
#    (3,1,3,1)
