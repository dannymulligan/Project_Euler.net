#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 371
#
# License plates
#
# Oregon licence plates consist of three letters followed by a three
# digit number (each digit can be from [0..9]).
#
# While driving to work Seth plays the following game: Whenever the
# numbers of two licence plates seen on his trip add to 1000 that's a
# win.
#
# E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500 too. (as
# long as he sees them in the same trip).
#
# Find the expected number of plates he needs to see for a win.
#
# Give your answer rounded to 8 decimal places behind the decimal
# point.
#
# Note: We assume that each licence plate seen is equally likely to
# have any three digit number on it.


import sys
#print(sys.version)
import time
start_time = time.clock()
import string

SIZE = 1000
TOLERANCE = 1e-9
DEBUG = False

SIZE = 10
TOLERANCE = 1e-8
DEBUG = True


###############################################################################

def NoMatchX(N, debug=False):
    # Calculate the probability of seeing N plates without a match
    # Assuming that none of the plates are "000" or "500"
    Probability = 1.0
    DebugList = []
    for i in range(N):
        DebugList.append("{}/{}".format(SIZE-2-i, SIZE))
        Probability *= (SIZE-2-i)/SIZE
    DebugString = " * ".join(DebugList)
    return Probability, DebugString

###############################################################################

def ProbX(N, debug=False):
    # Calculate the probability of seeing N-1 plates without a match,
    # then 1 plate that is a match
    # Assuming that none of the plates are "000" or "500"
    if (N < 2):
        return 0.0, "0"
    p, s = NoMatchX(N-1)
    Probability = p * (N-1)/SIZE
    DebugString = s + " * {}/{}".format(N-1, SIZE)
    return Probability, DebugString

###############################################################################

def ProbX5(N, debug=False):
    # Calculate the probability of seeing N-1 plates without a match,
    # then 1 plate that is a match
    # Assuming that 1 of the first N-1 plates is "500"
    # Assuming that the last plate is not "500"
    if (N < 3):
        return 0.0, "0"
    p, s = NoMatchX(N-2)
    Probability = p * (N-1)/SIZE * (N-2)/SIZE
    DebugString = s + " * {}/{} * {}/{}".format(N-1, SIZE, N-2, SIZE)
    return Probability, DebugString

###############################################################################

def ProbX55(N, debug=False):
    # Calculate the probability of seeing N-1 plates without a match,
    # then 1 plate that is a match
    # Assuming that 1 of the first N-1 plates is "500"
    # Assuming that the last plate is "500"
    p, s = NoMatchX(N-2)
    Probability = p * (N-1)/SIZE * 1/SIZE
    if (N < 2):
        return 0.0, "0"
    elif (N == 2):
        DebugString = "{}/{} * 1/{}".format(N-1, SIZE, SIZE)
    else:
        DebugString = s + " * {}/{} * 1/{}".format(N-1, SIZE, SIZE)
    return Probability, DebugString

###############################################################################

def Prob(N, debug=False):
    # Calculate the probability of seeing N-1 plates without a match,
    # then 1 plate that is a match
    # Assuming that plates can be anything but "000"
    pX, sX = ProbX(N)
    pX5, sX5 = ProbX5(N)
    pX55, sX55 = ProbX55(N)

    if debug:
        print("ProbX({}) = {} = {:f}".format(N, sX, pX))
        print("ProbX5({}) = {} = {:f}".format(N, sX5, pX5))
        print("ProbX55({}) = {} = {:f}".format(N, sX55, pX55))

    return pX + pX5 + pX55

###############################################################################

def Partitions(Z, N, debug=False):
    # Calculate the number of unique partitions of Z zeros
    # into N locations
    if (Z == 0):
        return 1
    elif (Z == 1):
        return N
    elif (Z == 2):
        return (N+1)*N//2
    elif (N == 1):
        return 1
    elif (N == 2):
        return Z+1
    else:
        ans = 0
        for x in range(Z+1):
            ans += Partitions(x, N//2) * Partitions(Z-x, N-N//2)
        return ans

if False:
    testcases = [(1,  3,         3),  (3,  4,        20),
                 (3, 74,     70300),  (5, 53,   4187106),
                 (5, 88,  49177128),  (6, 13,     18564),
                 (6, 30,   1623160),  (6, 36,   4496388),
                 (6, 47,  20358520),  (6, 56,  55525372),
                 (6, 68, 170230452),  (6, 73, 256851595),
                 (6, 82, 504981379),  (6, 88, 762245484)]
    for (Z, N, ans) in testcases:
        test_start_time = time.clock()
        test_ans = Partitions(Z=Z, N=N)
        test_finish_time = time.clock()

        if test_ans != ans:
            print("ERROR ", end='')
        print("Partitions(Z={}, N={}) == {} in {:.2f} seconds".format(Z, N, test_ans, test_finish_time - test_start_time))
    sys.exit()

###############################################################################

Probabilities = [0] * 50
expected = 0.0

N = 2
while True:
    prob = Prob(N, DEBUG)
    delta = N * prob
    expected += delta
    print("Prob({}) = {:.12f}, exp += {:.12f}, exp = {:.12f}".format(N, prob, delta, expected))
    if (N < 20):
        Probabilities[N] += prob
    if DEBUG:
        print()

    if (N > 5) and (delta < TOLERANCE):
        break

    Z = 1
    while True:
        part = Partitions(Z, N)
        zprob = prob * part / (SIZE**Z)
        zdelta = (N+Z) * zprob
        expected += zdelta
        print("Prob0(T={}, Z={}, N={}) = {:.12f}, exp += {:.12f}, exp = {:.12f}, Partitions(Z={}, N={}) = {:,}".format(N+Z, Z, N, zprob, zdelta, expected, Z, N, part))
        if ((N+Z) < 50):
            Probabilities[(N+Z)] += zprob

        if (Z > 1) and (zdelta < TOLERANCE):
            break

        Z += 1

    N += 1


print("Answer = {}".format(expected))
print("Answer = {:.8f} (to 8 decimal places)".format(expected))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))

total = 0.0
answer = 0.0
for i in range(50):
    if Probabilities[i] == 0:
        continue
    answer += i * Probabilities[i]
    total += Probabilities[i]
    print("Probability of match after {} plates = {:.8f}, answer += {:.8f}, answer = {:.8f}".format(i, Probabilities[i], i*Probabilities[i], answer))
print("Alternate calculation answer = {}".format(answer))
print("Alternata answer = {:.8f} (to 8 decimal places)".format(answer))
print("Difference = {}".format(expected-answer))
print("Total probability = {}".format(total))


# Key:
#    0 = "000" = zero
#    5 = "500" = half
#    X = any other number other than a compliment of previously picked X
#    M = compliment of a previously picked X
# (a compliment of a number and the number add up to 1000)
#
# Possible wins of length 3
#
#    XXM = 998/1000 * 997/1000 * 2/1000
#
#    5XM =   1/1000 * 998/1000 * 1/1000
#    X5M = 998/1000 *   1/1000 * 1/1000
#
#    5X5 =   1/1000 * 998/1000 * 1/1000
#    X55 = 998/1000 *   1/1000 * 1/1000
#
# Possible wins of length 4
#
#    XXXM = 998/1000 * 997/1000 * 996/1000 * 3/1000
#
#    5XXM =   1/1000 * 998/1000 * 997/1000 * 2/1000
#    X5XM = 998/1000 *   1/1000 * 997/1000 * 2/1000
#    XX5M = 998/1000 * 997/1000 *   1/1000 * 2/1000
#
#    5XX5 =   1/1000 * 998/1000 * 997/1000 * 1/1000
#    X5X5 = 998/1000 *   1/1000 * 997/1000 * 1/1000
#    XX55 = 998/1000 * 997/1000 *   1/1000 * 1/1000
#
# NoMatchX(N) = 998/1000 * 997/1000 * ... * (999-N)/1000
# ProbX(N) = NoMatchX(N-1) * (N-1)/1000
# ProbX5(N) = NoMatchX(N-2) * (N-2)/1000 * (N-1)/1000
# ProbX55(N) = NoMatchX(N-2) * (N-2)/1000 * 1/1000
# Prob(N) = ProbX(N) + ProbX5(N) + ProbX55(N)
#
# Plus all of the above could have 0's inserted into them to make
# longer wins
#
# With 0's inserted, the length N goes up, the probability goes down,
# but there are a multiple of cases according to the number of partitions
# of X 0's, inserted into N locations.
#
# Partition(Z, N) =
