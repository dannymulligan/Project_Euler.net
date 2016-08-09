#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 185
#
# Number Mind
#
# The game Number Mind is a variant of the well known game Master
# Mind.
#
# Instead of coloured pegs, you have to guess a secret sequence of
# digits. After each guess you're only told in how many places you've
# guessed the correct digit. So, if the sequence was 1234 and you
# guessed 2036, you'd be told that you have one correct digit;
# however, you would NOT be told that you also have another digit in
# the wrong place.
#
# For instance, given the following guesses for a 5-digit secret
# sequence,
#
#     90342  2 correct
#     70794  0 correct
#     39458  2 correct
#     34109  1 correct
#     51545  2 correct
#     12531  1 correct
#
# The correct sequence 39542 is unique.
#
# Based on the following guesses,
#
#     5616185650518293  2 correct
#     3847439647293047  1 correct
#     5855462940810587  3 correct
#     9742855507068353  3 correct
#     4296849643607543  3 correct
#     3174248439465858  1 correct
#     4513559094146117  2 correct
#     7890971548908067  3 correct
#     8157356344118483  1 correct
#     2615250744386899  2 correct
#     8690095851526254  3 correct
#     6375711915077050  1 correct
#     6913859173121360  1 correct
#     6442889055042768  2 correct
#     2321386104303845  0 correct
#     2326509471271448  2 correct
#     5251583379644322  2 correct
#     1748270476758276  3 correct
#     4895722652190306  1 correct
#     3041631117224635  3 correct
#     1841236454324589  3 correct
#     2659862637316867  2 correct
#
# Find the unique 16-digit secret sequence.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?


import sys
import time

start_time = time.clock()
now_time = start_time
prev_time = start_time


def search(clues, soln_so_far):
    #print("{} DEBUG: search({})".format(soln_so_far, clues))
    clue_depth = len(clues[0][0])

    for i in range(0,10):
        # Try all digits 0..9 for the first digit in the clues
        #print("{} Trying leading digit = {}".format(soln_so_far, i))

        if (clue_depth == 1):
            # Clues are of length 1, find a solution without recursion
            good_match = True
            for clue in clues:
                #print("{}Processing clue {}".format(soln_so_far, clue))
                if (clue[0][0] == i) and (clue[1] != 1):
                    good_match = False
                if (clue[0][0] != i) and (clue[1] != 0):
                    good_match = False

                if not good_match:
                    break

            if good_match:
                #print("FOUND match {}, clues={}".format(soln_so_far + [i], clues))
                yield [i]

        else:
            # Remaining clues are of length > 1
            good_match = True
            new_clues = []

            for clue in clues:
                #print("{} Processing clue {}".format(soln_so_far, clue))
                #print("{}     clue[0] = {}".format(soln_so_far, clue[0]))
                #print("{}     clue[1] = {}".format(soln_so_far, clue[1]))
                if (clue[0][0] == i):
                    if clue[1] > 0:
                        new_clue = (clue[0][1:], clue[1]-1)
                    else:
                        good_match = False
                        break
                else:
                    if clue[1] < clue_depth:
                        new_clue = (clue[0][1:], clue[1])
                    else:
                        good_match = False
                        break

                #print("{} Adding new_clue {}".format(soln_so_far, new_clue))
                new_clues.append(new_clue)

            if good_match:
                for solution in search(new_clues, soln_so_far + [i]):
                    yield [i] + solution


# Test case #0: solution = 39542
if False:
    clues = []                            # 39542  5 correct
    clues.append(([ 9, 0, 3, 4, 2 ], 2))  # 90342  2 correct
    clues.append(([ 7, 0, 7, 9, 4 ], 0))  # 70794  0 correct
    clues.append(([ 3, 9, 4, 5, 8 ], 2))  # 39458  2 correct
    clues.append(([ 3, 4, 1, 0, 9 ], 1))  # 34109  1 correct
    clues.append(([ 5, 1, 5, 4, 5 ], 2))  # 51545  2 correct
    clues.append(([ 1, 2, 5, 3, 1 ], 1))  # 12531  1 correct

if False:
    clues = []                   # 42  2 correct
    clues.append(([ 4, 2 ], 2))  # 42  2 correct
    clues.append(([ 9, 4 ], 0))  # 94  0 correct
    clues.append(([ 5, 8 ], 0))  # 58  0 correct
    clues.append(([ 0, 9 ], 0))  # 09  0 correct
    clues.append(([ 4, 5 ], 1))  # 45  1 correct
    clues.append(([ 3, 1 ], 0))  # 31  0 correct


# Test case #1: solution = 12345678
if False:
    clues = []                                     #  12345678  8 correct
    clues.append(([ 1, 1, 1, 1, 1, 1, 1, 1 ], 1))  #  11111111  1 correct
    clues.append(([ 1, 2, 2, 2, 2, 2, 2, 2 ], 2))  #  12222222  2 correct
    clues.append(([ 1, 2, 3, 3, 3, 3, 3, 3 ], 3))  #  12333333  3 correct
    clues.append(([ 1, 2, 3, 4, 4, 4, 4, 4 ], 4))  #  12344444  4 correct
    clues.append(([ 1, 2, 3, 4, 5, 5, 5, 5 ], 5))  #  12345555  5 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 6, 6 ], 6))  #  12345666  6 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 7, 7 ], 7))  #  12345677  7 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 7, 8 ], 8))  #  12345678  8 correct


# Test case #2: solution = 12345678, many other solutions
if False:
    clues = []                                     #  12345678  8 correct
    clues.append(([ 1, 1, 1, 1, 1, 1, 1, 1 ], 1))  #  11111111  1 correct
    clues.append(([ 2, 2, 2, 2, 2, 2, 2, 2 ], 1))  #  22222222  1 correct
    clues.append(([ 3, 3, 3, 3, 3, 3, 3, 3 ], 1))  #  33333333  1 correct
    clues.append(([ 4, 4, 4, 4, 4, 4, 4, 4 ], 1))  #  44444444  1 correct
    clues.append(([ 5, 5, 5, 5, 5, 5, 5, 5 ], 1))  #  55555555  1 correct
    clues.append(([ 6, 6, 6, 6, 5, 6, 6, 6 ], 2))  #  66665666  2 correct
    clues.append(([ 7, 7, 7, 7, 5, 6, 7, 7 ], 3))  #  77775677  3 correct
    clues.append(([ 8, 8, 8, 8, 5, 6, 7, 8 ], 4))  #  88885678  4 correct


# Test case #3: solution = 1234567890
if False:
    clues = []                                            #  1234567890  10 correct
    clues.append(([ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],  1))  #  1111111111   1 correct
    clues.append(([ 1, 2, 2, 2, 2, 2, 2, 2, 2, 2 ],  2))  #  1222222222   2 correct
    clues.append(([ 1, 2, 3, 3, 3, 3, 3, 3, 3, 3 ],  3))  #  1233333333   3 correct
    clues.append(([ 1, 2, 3, 4, 4, 4, 4, 4, 4, 4 ],  4))  #  1234444444   4 correct
    clues.append(([ 1, 2, 3, 4, 5, 5, 5, 5, 5, 5 ],  5))  #  1234555555   5 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 6, 6, 6, 6 ],  6))  #  1234566666   6 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 7, 7, 7, 7 ],  7))  #  1234567777   7 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 7, 8, 8, 8 ],  8))  #  1234567888   8 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 9 ],  9))  #  1234567899   9 correct
    clues.append(([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ], 10))  #  1234567890  10 correct


# The real problem:
if True:
    clues = []
    clues.append(([ 5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3 ], 2))  # 5616185650518293  2 correct
    clues.append(([ 3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7 ], 1))  # 3847439647293047  1 correct
    clues.append(([ 5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7 ], 3))  # 5855462940810587  3 correct
    clues.append(([ 9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3 ], 3))  # 9742855507068353  3 correct
    clues.append(([ 4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3 ], 3))  # 4296849643607543  3 correct
    clues.append(([ 3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8 ], 1))  # 3174248439465858  1 correct
    clues.append(([ 4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7 ], 2))  # 4513559094146117  2 correct
    clues.append(([ 7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7 ], 3))  # 7890971548908067  3 correct
    clues.append(([ 8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3 ], 1))  # 8157356344118483  1 correct
    clues.append(([ 2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9 ], 2))  # 2615250744386899  2 correct
    clues.append(([ 8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4 ], 3))  # 8690095851526254  3 correct
    clues.append(([ 6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0 ], 1))  # 6375711915077050  1 correct
    clues.append(([ 6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0 ], 1))  # 6913859173121360  1 correct
    clues.append(([ 6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8 ], 2))  # 6442889055042768  2 correct
    clues.append(([ 2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5 ], 0))  # 2321386104303845  0 correct
    clues.append(([ 2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8 ], 2))  # 2326509471271448  2 correct
    clues.append(([ 5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2 ], 2))  # 5251583379644322  2 correct
    clues.append(([ 1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6 ], 3))  # 1748270476758276  3 correct
    clues.append(([ 4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6 ], 1))  # 4895722652190306  1 correct
    clues.append(([ 3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5 ], 3))  # 3041631117224635  3 correct
    clues.append(([ 1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9 ], 3))  # 1841236454324589  3 correct
    clues.append(([ 2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7 ], 2))  # 2659862637316867  2 correct


solution_count = 0
for i in search(clues, []):
    solution_count += 1
    print("Soution = {}".format(i))

if solution_count == 0:
    print "No solution found"
else:
    print("{} soutions found".format(solution_count))


#print "clues =", clues
#print "len(clues) =", len(clues)
#print "clues[0] =", clues[0]
#print "len(clues[0]) =", len(clues[0])
#print "clues[0][0] =", clues[0][0]
#print "clues[0][1] =", clues[0][1]


now_time = time.clock()
print "Total time taken =", now_time - start_time
sys.exit()
