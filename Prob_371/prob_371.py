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
import time
start_time = time.clock()
import string

SIZE = 1000.0
TOLERANCE = 1e-20
DEBUG = False

if DEBUG:
    print(sys.version)
    print("debug =", DEBUG)
    print()


###############################################################################

# Initialize variables for 0th plate
probabilities = [0.0]
#       (N, X, H)
prev = {(0, 0, 0): 1.0}
done = False

while not done:
    next = {}
    done = True
    probabilities.append(0.0)
    for (n, x, h) in prev:
        prob = prev[(n, x, h)]

        if DEBUG:
            print()
            print("    prob(N={},X={},H={}) == {}".format(n, x, h, prob))

        if (prob < TOLERANCE):
            continue
        else:
            done = False

        if not (n+1, x  , 0) in next:  next[(n+1, x  , 0)] = 0.0
        if not (n+1, x+1, 0) in next:  next[(n+1, x+1, 0)] = 0.0
        if not (n+1, x  , 1) in next:  next[(n+1, x  , 1)] = 0.0
        if not (n+1, x+1, 1) in next:  next[(n+1, x+1, 1)] = 0.0

        if (h == 0):
            next[(n+1, x  , 0)] += prob * (1.0+x)/SIZE           # Z or prev X
            next[(n+1, x+1, 0)] += prob * (SIZE-2.0-2.0*x)/SIZE  # new X
            next[(n+1, x  , 1)] += prob * 1.0/SIZE               # first H
            probabilities[n+1]  += prob * x/SIZE                 # compliment of prev X
        else:
            next[(n+1, x  , 1)] += prob * (1.0+x)/SIZE           # Z or prev X
            next[(n+1, x+1, 1)] += prob * (SIZE-2.0-2.0*x)/SIZE  # new X
            probabilities[n+1]  += prob * (1.0+x)/SIZE           # second H or compliment of prev X

        if DEBUG:
            if (h == 0):
                print("prob(N={},X={},H={}) += prob(N={},X={},H={}) * {}/{}  # Z or prev X".format(n+1, x  , 0, n, x, h,            1.0+x, SIZE))
                print("prob(N={},X={},H={}) += prob(N={},X={},H={}) * {}/{}  # new X"      .format(n+1, x+1, 0, n, x, h, (SIZE-2.0-2.0*x), SIZE))
                print("prob(N={},X={},H={}) += prob(N={},X={},H={}) * {}/{}  # first H"    .format(n+1, x  , 1, n, x, h,              1.0, SIZE))
                print("probabilities[{}] += prob(N={},X={},H={}) * {}/{} == {}  # compliment of prev X".format(n+1, n, x, h, x, SIZE, prob*x/SIZE))
            else:
                print("prob(N={},X={},H={}) += prob(N={},X={},H={}) * {}/{}  # Z or prev X".format(n+1, x  , 1, n, x, h,            1.0+x, SIZE))
                print("prob(N={},X={},H={}) += prob(N={},X={},H={}) * {}/{}  # new X"      .format(n+1, x+1, 1, n, x, h, (SIZE-2.0-2.0*x), SIZE))
                print("probabilities[{}] += prob(N={},X={},H={}) * {}/{} == {}  # second H or compliment of prev X".format(n+1, n, x, h, (1.0+x), SIZE, prob*(1.0+x)/SIZE))

    prev = next
    if DEBUG:
        print()
        print("probabilities[{}] == {}".format(n+1, probabilities[n+1]))
        print("----------------------------------------")

total = 0.0
answer = 0.0
for i in range(len(probabilities)):
    if probabilities[i] == 0:
        continue
    answer += i * probabilities[i]
    total += probabilities[i]
    print("Probability of match after {} plates = {:.10f}, answer += {:.10f}, answer = {:.10f}".format(i, probabilities[i], i*probabilities[i], answer))
print("Answer = {}".format(answer))
print("Answer = {:.8f} (rounded to 8 decimal places)".format(answer))
print("Total probability = {}".format(total))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
