#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 301
#
# Nim
#
# Nim is a game played with heaps of stones, where two players take it
# in turn to remove any number of stones from any heap until no stones
# remain.
#
# We'll consider the three-heap normal-play version of Nim, which works as follows:
#
# - At the start of the game there are three heaps of stones.
# - On his turn the player removes any positive number of stones from any single heap.
# - The first player unable to move (because no stones remain) loses.
#
# If (n1,n2,n3) indicates a Nim position consisting of heaps of size
# n1, n2 and n3 then there is a simple function X(n1,n2,n3) — that you
# may look up or attempt to deduce for yourself — that returns:
#
#    zero if, with perfect strategy, the player about to move will
#    eventually lose; or
#
#    non-zero if, with perfect strategy, the player about to move will
#    eventually win.
#
# For example X(1,2,3) = 0 because, no matter what the current player
# does, his opponent can respond with a move that leaves two heaps of
# equal size, at which point every move by the current player can be
# mirrored by his opponent until no stones remain; so the current
# player loses. To illustrate:
#
# - current player moves to (1,2,1)
# - opponent moves to (1,0,1)
# - current player moves to (0,0,1)
# - opponent moves to (0,0,0), and so wins.
#
# For how many positive integers n <= 2^30 does X(n,2n,3n) = 0 ?
#

import sys
import time
start_time = time.clock()

# The strategy for determining if a position is winning is to binary
# XOR the sizes of the piles.  If the result is zero, then the next
# player to move will lose given perfect play, so our function should
# return 0.  Given N, 2*N and 3*N, we XOR them together, and the
# result will be zero, provided that there are no consecutive binary
# 1's in N.
#
# So our problem becomes one of finding how many different binary
# strings below 2^30 do not have consecutive 1's.


########################################
def fit_x_into_y(x, y):
    # How many ways can I fit X 1's into a string Y digits long
    # without two 1's being adjacent to each other?
    if (x == 1):
        #print("fit_x_into_y({x}, {y}) = {a}".format(x=x, y=y, a=y))
        return y
    elif (x * 2) == y:
        #print("fit_x_into_y({x}, {y}) = {a}".format(x=x, y=y, a=2))
        return x + 1
    elif (x * 2) == (y + 1):
        #print("fit_x_into_y({x}, {y}) = {a}".format(x=x, y=y, a=1))
        return 1
    elif (x * 2) > (y + 1):
        return 0
    else:
        answer = 0
        for i in range(1, y-x+1):
            #print("recurse fit_x_into_y({x}, {y})".format(x=x-1, y=y-i-1))
            answer += fit_x_into_y(x-1, y-i-1)
        return answer

#assert fit_x_into_y(1, 6) == 6
#assert fit_x_into_y(2, 6) == 10
#assert fit_x_into_y(3, 6) == 4
#assert fit_x_into_y(4, 6) == 0
#assert fit_x_into_y(5, 6) == 0


########################################

LIMIT = 30

answer = 0
for i in range(1, LIMIT/2+2):
    x = fit_x_into_y(i, LIMIT)
    print("fit_x_into_y({x}, {y}) = {r}".format(x=i, y=LIMIT, r=x))
    answer += x

# Need to add 1 to the answer, to account for the n = 2^30 case
answer += 1
print("Answer is {}".format(answer))

#answer2 = 0
#for i in range(1,2**LIMIT):
#    x = i^i*2^i*3
#    if x == 0:
#        #print("{:2}: {:09b} {:09b} {:09b} = {:09b} win".format(i, i, i*2, i*3, x))
#        answer2 += 1
#    else:
#        pass
#        #print("{:2}: {:09b} {:09b} {:09b} = {:09b}".format(i, i, i*2, i*3, x))
#print("Answer2 is {}".format(answer2))
#
#if (answer != answer2):
#    print("Error")

print("Time taken = {0} seconds".format(time.clock() - start_time))
