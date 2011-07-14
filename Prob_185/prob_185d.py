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


#clues = []
#clues.append([ 9, 0, 3, 4, 2 ])  # 90342  2 correct
#clues.append([ 7, 0, 7, 9, 4 ])  # 70794  0 correct
#clues.append([ 3, 9, 4, 5, 8 ])  # 39458  2 correct
#clues.append([ 3, 4, 1, 0, 9 ])  # 34109  1 correct
#clues.append([ 5, 1, 5, 4, 5 ])  # 51545  2 correct
#clues.append([ 1, 2, 5, 3, 1 ])  # 12531  1 correct
#match = []
#match.append([ 2, 0, 0, 0, 0, 0])  # 90342  2 correct
#match.append([ 0, 0, 0, 0, 0, 0])  # 70794  0 correct
#match.append([ 2, 0, 0, 0, 0, 0])  # 39458  2 correct
#match.append([ 1, 0, 0, 0, 0, 0])  # 34109  1 correct
#match.append([ 2, 0, 0, 0, 0, 0])  # 51545  2 correct
#match.append([ 1, 0, 0, 0, 0, 0])  # 12531  1 correct

clues = []
clues.append([ 5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3 ])  # 5616185650518293  2 correct
clues.append([ 3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7 ])  # 3847439647293047  1 correct
clues.append([ 5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7 ])  # 5855462940810587  3 correct
clues.append([ 9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3 ])  # 9742855507068353  3 correct
clues.append([ 4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3 ])  # 4296849643607543  3 correct
clues.append([ 3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8 ])  # 3174248439465858  1 correct
clues.append([ 4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7 ])  # 4513559094146117  2 correct
clues.append([ 7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7 ])  # 7890971548908067  3 correct
clues.append([ 8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3 ])  # 8157356344118483  1 correct
clues.append([ 2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9 ])  # 2615250744386899  2 correct
clues.append([ 8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4 ])  # 8690095851526254  3 correct
clues.append([ 6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0 ])  # 6375711915077050  1 correct
clues.append([ 6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0 ])  # 6913859173121360  1 correct
clues.append([ 6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8 ])  # 6442889055042768  2 correct
clues.append([ 2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5 ])  # 2321386104303845  0 correct
clues.append([ 2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8 ])  # 2326509471271448  2 correct
clues.append([ 5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2 ])  # 5251583379644322  2 correct
clues.append([ 1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6 ])  # 1748270476758276  3 correct
clues.append([ 4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6 ])  # 4895722652190306  1 correct
clues.append([ 3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5 ])  # 3041631117224635  3 correct
clues.append([ 1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9 ])  # 1841236454324589  3 correct
clues.append([ 2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7 ])  # 2659862637316867  2 correct
match = []
match.append([ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 5616185650518293  2 correct
match.append([ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 3847439647293047  1 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 5855462940810587  3 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 9742855507068353  3 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 4296849643607543  3 correct
match.append([ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 3174248439465858  1 correct
match.append([ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 4513559094146117  2 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 7890971548908067  3 correct
match.append([ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 8157356344118483  1 correct
match.append([ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 2615250744386899  2 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 8690095851526254  3 correct
match.append([ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 6375711915077050  1 correct
match.append([ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 6913859173121360  1 correct
match.append([ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 6442889055042768  2 correct
match.append([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 2321386104303845  0 correct
match.append([ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 2326509471271448  2 correct
match.append([ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 5251583379644322  2 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 1748270476758276  3 correct
match.append([ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 4895722652190306  1 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 3041631117224635  3 correct
match.append([ 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 1841236454324589  3 correct
match.append([ 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ])  # 2659862637316867  2 correct

print "clues =", clues
print "match =", match

def search(depth, hypothesis):
    if (depth <= 8):
        print "search({0}, {1})".format(depth, hypothesis)

    #print "Clues"
    #for c in clues:
    #    print c

    for i in range(10):
        hypothesis.append(i)

        #print "    Trying", hypothesis
        valid = True
        found = True
        for x in range(len(clues)):
            #print "x = {0}, depth = {1}, i = {2}".format(x, depth, i)
            #print "clues[x][depth] = {0}, i = {1}".format(clues[x][depth], i)
            if (clues[x][depth] == i):
                match[x][depth+1] = match[x][depth] - 1
                if (match[x][depth+1] < 0):
                    valid = False
                    found = False
            else:
                match[x][depth+1] = match[x][depth]

            if (match[x][depth+1] != 0):
                found = False

        #print "Match ="
        #for m in match:
        #    print m
        #print "Valid =", valid, "Found =", found

        if ((len(hypothesis) == len(clues[0])) & (found == True)):
            print "answer =", hypothesis
            now_time = time.clock()
            print "Total time taken =", now_time - start_time
            sys.exit()

        if ((len(hypothesis) < len(clues[0])) & (valid == True)):
            search(depth+1, hypothesis)

        del hypothesis[-1]
    return

def root_search(now, depth, hypothesis):
    print "searching with search({0}, {1})".format(depth, hypothesis),
#    for i in range(len(hypothesis)):
#        for c in clues:
#            if (c[i] == hypothesis[i]):

    search(depth, hypothesis)
    print " Time taken = {0}".format(time.clock() - now)


search(0, [])
sys.exit()

t = time.clock()
root_search(t, 1, [1])
t = time.clock()
root_search(t, 0, [])
t = time.clock()
root_search(t, 1, [2])
t = time.clock()
root_search(t, 1, [3])
t = time.clock()
root_search(t, 1, [4])
t = time.clock()
root_search(t, 1, [5])
t = time.clock()
root_search(t, 1, [6])
sys.exit()


t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 0])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 1])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 2])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 3])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 4])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 5])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 6])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 7])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 8])
t = time.clock()
root_search(t, 9, [1, 0, 0, 0, 0, 0, 0, 0, 9])

t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 1])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 2])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 3])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 4])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 5])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 6])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 7])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 8])
t = time.clock()
root_search(t, 8, [1, 0, 0, 0, 0, 0, 0, 9])

t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 1])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 2])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 3])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 4])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 5])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 6])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 7])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 8])
t = time.clock()
root_search(t, 7, [1, 0, 0, 0, 0, 0, 9])

t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 1])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 2])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 3])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 4])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 5])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 6])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 7])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 8])
t = time.clock()
root_search(t, 6, [1, 0, 0, 0, 0, 9])

t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 1])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 2])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 3])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 4])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 5])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 6])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 7])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 8])
t = time.clock()
root_search(t, 5, [1, 0, 0, 0, 9])

t = time.clock()
root_search(t, 4, [1, 0, 0, 1])
t = time.clock()
root_search(t, 4, [1, 0, 0, 2])
t = time.clock()
root_search(t, 4, [1, 0, 0, 3])
t = time.clock()
root_search(t, 4, [1, 0, 0, 4])
t = time.clock()
root_search(t, 4, [1, 0, 0, 5])
t = time.clock()
root_search(t, 4, [1, 0, 0, 6])
t = time.clock()
root_search(t, 4, [1, 0, 0, 7])
t = time.clock()
root_search(t, 4, [1, 0, 0, 8])
t = time.clock()
root_search(t, 4, [1, 0, 0, 9])

t = time.clock()
root_search(t, 3, [1, 0, 1])
t = time.clock()
root_search(t, 3, [1, 0, 2])
t = time.clock()
root_search(t, 3, [1, 0, 3])
t = time.clock()
root_search(t, 3, [1, 0, 4])
t = time.clock()
root_search(t, 3, [1, 0, 5])
t = time.clock()
root_search(t, 3, [1, 0, 6])
t = time.clock()
root_search(t, 3, [1, 0, 7])
t = time.clock()
root_search(t, 3, [1, 0, 8])
t = time.clock()
root_search(t, 3, [1, 0, 9])

t = time.clock()
root_search(t, 2, [1, 1])
t = time.clock()
root_search(t, 2, [1, 2])
t = time.clock()
root_search(t, 2, [1, 3])
t = time.clock()
root_search(t, 2, [1, 4])
t = time.clock()
root_search(t, 2, [1, 5])
t = time.clock()
root_search(t, 2, [1, 6])
t = time.clock()
root_search(t, 2, [1, 7])
t = time.clock()
root_search(t, 2, [1, 8])
t = time.clock()
root_search(t, 2, [1, 9])

t = time.clock()
root_search(t, 2, [2, 0])
t = time.clock()
root_search(t, 2, [2, 1])
t = time.clock()
root_search(t, 2, [2, 2])
t = time.clock()
root_search(t, 2, [2, 3])
t = time.clock()
root_search(t, 2, [2, 4])
t = time.clock()
root_search(t, 2, [2, 5])
t = time.clock()
root_search(t, 2, [2, 6])
t = time.clock()
root_search(t, 2, [2, 7])
t = time.clock()
root_search(t, 2, [2, 8])
t = time.clock()
root_search(t, 2, [2, 9])

t = time.clock()
root_search(t, 2, [3, 0])
t = time.clock()
root_search(t, 2, [3, 1])
t = time.clock()
root_search(t, 2, [3, 2])
t = time.clock()
root_search(t, 2, [3, 3])
t = time.clock()
root_search(t, 2, [3, 4])
t = time.clock()
root_search(t, 2, [3, 5])
t = time.clock()
root_search(t, 2, [3, 6])
t = time.clock()
root_search(t, 2, [3, 7])
t = time.clock()
root_search(t, 2, [3, 8])
t = time.clock()
root_search(t, 2, [3, 9])

t = time.clock()
root_search(t, 2, [4, 0])
t = time.clock()
root_search(t, 2, [4, 1])
t = time.clock()
root_search(t, 2, [4, 2])
t = time.clock()
root_search(t, 2, [4, 3])
t = time.clock()
root_search(t, 2, [4, 4])
t = time.clock()
root_search(t, 2, [4, 5])
t = time.clock()
root_search(t, 2, [4, 6])
t = time.clock()
root_search(t, 2, [4, 7])
t = time.clock()
root_search(t, 2, [4, 8])
t = time.clock()
root_search(t, 2, [4, 9])

t = time.clock()
root_search(t, 2, [5, 0])
t = time.clock()
root_search(t, 2, [5, 1])
t = time.clock()
root_search(t, 2, [5, 2])
t = time.clock()
root_search(t, 2, [5, 3])
t = time.clock()
root_search(t, 2, [5, 4])
t = time.clock()
root_search(t, 2, [5, 5])
t = time.clock()
root_search(t, 2, [5, 6])
t = time.clock()
root_search(t, 2, [5, 7])
t = time.clock()
root_search(t, 2, [5, 8])
t = time.clock()
root_search(t, 2, [5, 9])

t = time.clock()
root_search(t, 2, [6, 0])
t = time.clock()
root_search(t, 2, [6, 1])
t = time.clock()
root_search(t, 2, [6, 2])
t = time.clock()
root_search(t, 2, [6, 3])
t = time.clock()
root_search(t, 2, [6, 4])
t = time.clock()
root_search(t, 2, [6, 5])
t = time.clock()
root_search(t, 2, [6, 6])
t = time.clock()
root_search(t, 2, [6, 7])
t = time.clock()
root_search(t, 2, [6, 8])
t = time.clock()
root_search(t, 2, [6, 9])

t = time.clock()
root_search(t, 2, [7, 0])
t = time.clock()
root_search(t, 2, [7, 1])
t = time.clock()
root_search(t, 2, [7, 2])
t = time.clock()
root_search(t, 2, [7, 3])
t = time.clock()
root_search(t, 2, [7, 4])
t = time.clock()
root_search(t, 2, [7, 5])
t = time.clock()
root_search(t, 2, [7, 6])
t = time.clock()
root_search(t, 2, [7, 7])
t = time.clock()
root_search(t, 2, [7, 8])
t = time.clock()
root_search(t, 2, [7, 9])

t = time.clock()
root_search(t, 2, [8, 0])
t = time.clock()
root_search(t, 2, [8, 1])
t = time.clock()
root_search(t, 2, [8, 2])
t = time.clock()
root_search(t, 2, [8, 3])
t = time.clock()
root_search(t, 2, [8, 4])
t = time.clock()
root_search(t, 2, [8, 5])
t = time.clock()
root_search(t, 2, [8, 6])
t = time.clock()
root_search(t, 2, [8, 7])
t = time.clock()
root_search(t, 2, [8, 8])
t = time.clock()
root_search(t, 2, [8, 9])

t = time.clock()
root_search(t, 2, [9, 0])
t = time.clock()
root_search(t, 2, [9, 1])
t = time.clock()
root_search(t, 2, [9, 2])
t = time.clock()
root_search(t, 2, [9, 3])
t = time.clock()
root_search(t, 2, [9, 4])
t = time.clock()
root_search(t, 2, [9, 5])
t = time.clock()
root_search(t, 2, [9, 6])
t = time.clock()
root_search(t, 2, [9, 7])
t = time.clock()
root_search(t, 2, [9, 8])
t = time.clock()
root_search(t, 2, [9, 9])

print "No solution found"
now_time = time.clock()
print "Total time taken =", now_time - start_time
