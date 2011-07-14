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


# My own test case
#
#     11111111  1 correct
#     12222222  2 correct
#     12333333  3 correct
#     12344444  4 correct
#     12345555  5 correct
#     12345666  6 correct
#     12345677  7 correct
#     12345678  8 correct
#
#     Solution = 12345678
import sys
import time

start_time = time.clock()
now_time = start_time
prev_time = start_time


# Test case #0: solution = 39542
clues = []
clues.append([ 9, 0, 3, 4, 2 ])  # 90342  2 correct
clues.append([ 7, 0, 7, 9, 4 ])  # 70794  0 correct
clues.append([ 3, 9, 4, 5, 8 ])  # 39458  2 correct
clues.append([ 3, 4, 1, 0, 9 ])  # 34109  1 correct
clues.append([ 5, 1, 5, 4, 5 ])  # 51545  2 correct
clues.append([ 1, 2, 5, 3, 1 ])  # 12531  1 correct
target = []
target.append(2)  # 90342  2 correct
target.append(0)  # 70794  0 correct
target.append(2)  # 39458  2 correct
target.append(1)  # 34109  1 correct
target.append(2)  # 51545  2 correct
target.append(1)  # 12531  1 correct


# Test case #1: solution = 12345678
clues = []
clues.append([ 1, 1, 1, 1, 1, 1, 1, 1 ])  #  11111111  1 correct
clues.append([ 1, 2, 2, 2, 2, 2, 2, 2 ])  #  12222222  2 correct
clues.append([ 1, 2, 3, 3, 3, 3, 3, 3 ])  #  12333333  3 correct
clues.append([ 1, 2, 3, 4, 4, 4, 4, 4 ])  #  12344444  4 correct
clues.append([ 1, 2, 3, 4, 5, 5, 5, 5 ])  #  12345555  5 correct
clues.append([ 1, 2, 3, 4, 5, 6, 6, 6 ])  #  12345666  6 correct
clues.append([ 1, 2, 3, 4, 5, 6, 7, 7 ])  #  12345677  7 correct
clues.append([ 1, 2, 3, 4, 5, 6, 7, 8 ])  #  12345678  8 correct
target = []
target.append(1)  #  11111111  1 correct
target.append(2)  #  12222222  2 correct
target.append(3)  #  12333333  3 correct
target.append(4)  #  12344444  4 correct
target.append(5)  #  12345555  5 correct
target.append(6)  #  12345666  6 correct
target.append(7)  #  12345677  7 correct
target.append(8)  #  12345678  8 correct


# Test case #2: solution = 12345678
clues = []
clues.append([ 1, 1, 1, 1, 1, 1, 1, 1 ])  #  11111111  1 correct
clues.append([ 2, 2, 2, 2, 2, 2, 2, 2 ])  #  22222222  1 correct
clues.append([ 3, 3, 3, 3, 3, 3, 3, 3 ])  #  33333333  1 correct
clues.append([ 4, 4, 4, 4, 4, 4, 4, 4 ])  #  44444444  1 correct
clues.append([ 5, 5, 5, 5, 5, 5, 5, 5 ])  #  55555555  1 correct
clues.append([ 6, 6, 6, 6, 5, 6, 6, 6 ])  #  66665666  2 correct
clues.append([ 7, 7, 7, 7, 5, 6, 7, 7 ])  #  77775677  3 correct
clues.append([ 8, 8, 8, 8, 5, 6, 7, 8 ])  #  88885678  4 correct
target = []
target.append(1)  #  
target.append(1)  #  
target.append(1)  #  
target.append(1)  #  
target.append(1)  #  
target.append(2)  #  
target.append(3)  #  
target.append(4)  #  


#clues = []
#clues.append([ 5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3 ])  # 5616185650518293  2 correct
#clues.append([ 3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7 ])  # 3847439647293047  1 correct
#clues.append([ 5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7 ])  # 5855462940810587  3 correct
#clues.append([ 9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3 ])  # 9742855507068353  3 correct
#clues.append([ 4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3 ])  # 4296849643607543  3 correct
#clues.append([ 3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8 ])  # 3174248439465858  1 correct
#clues.append([ 4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7 ])  # 4513559094146117  2 correct
#clues.append([ 7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7 ])  # 7890971548908067  3 correct
#clues.append([ 8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3 ])  # 8157356344118483  1 correct
#clues.append([ 2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9 ])  # 2615250744386899  2 correct
#clues.append([ 8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4 ])  # 8690095851526254  3 correct
#clues.append([ 6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0 ])  # 6375711915077050  1 correct
#clues.append([ 6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0 ])  # 6913859173121360  1 correct
#clues.append([ 6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8 ])  # 6442889055042768  2 correct
#clues.append([ 2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5 ])  # 2321386104303845  0 correct
#clues.append([ 2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8 ])  # 2326509471271448  2 correct
#clues.append([ 5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2 ])  # 5251583379644322  2 correct
#clues.append([ 1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6 ])  # 1748270476758276  3 correct
#clues.append([ 4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6 ])  # 4895722652190306  1 correct
#clues.append([ 3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5 ])  # 3041631117224635  3 correct
#clues.append([ 1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9 ])  # 1841236454324589  3 correct
#clues.append([ 2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7 ])  # 2659862637316867  2 correct
#target = []
#target.append(2)  # 5616185650518293  2 correct
#target.append(1)  # 3847439647293047  1 correct
#target.append(3)  # 5855462940810587  3 correct
#target.append(3)  # 9742855507068353  3 correct
#target.append(3)  # 4296849643607543  3 correct
#target.append(1)  # 3174248439465858  1 correct
#target.append(2)  # 4513559094146117  2 correct
#target.append(3)  # 7890971548908067  3 correct
#target.append(1)  # 8157356344118483  1 correct
#target.append(2)  # 2615250744386899  2 correct
#target.append(3)  # 8690095851526254  3 correct
#target.append(1)  # 6375711915077050  1 correct
#target.append(1)  # 6913859173121360  1 correct
#target.append(2)  # 6442889055042768  2 correct
#target.append(0)  # 2321386104303845  0 correct
#target.append(2)  # 2326509471271448  2 correct
#target.append(2)  # 5251583379644322  2 correct
#target.append(3)  # 1748270476758276  3 correct
#target.append(1)  # 4895722652190306  1 correct
#target.append(3)  # 3041631117224635  3 correct
#target.append(3)  # 1841236454324589  3 correct
#target.append(2)  # 2659862637316867  2 correct

#print "clues =", clues
#print "target =", target
cnt_clues = len(clues)
cnt_digits = len(clues[0])

#match = [[0]*cnt_digits for _ in range(cnt_clues)]  # This is how you create a 2D array 
## reference with match[clue][digit]

def search(depth, hypothesis):
    if (depth < 3):
    #if (True):
        print "search({0}, {1})".format(depth, hypothesis)

    for i in range(10):
        hypothesis.append(i)
        hypo_valid = True

        # Count digits in the clues that match the hypothesis
        m_y = [0]*cnt_clues  # count of digits that match in each clue
        for c in range(cnt_clues):
            for i in range(depth+1):
                if (hypothesis[i] == clues[c][i]):
                    m_y[c] += 1

        # Check for clues with too many matches 
        for c in range(cnt_clues):
            if (m_y[c] > target[c]):
                hypo_valid = False
                #print "  fail - too many matches on clue", c
                break

# With this 'not enough matches' code, test case #2 above takes 7.7 seconds, without 116.6 = 15x speedup
        # Count digits in the clues that cannot possibly match
        m_n = [0]*cnt_clues  # count of digits that can't possible match in each clue
        for c in range(cnt_clues):
            for i in range(depth+1,cnt_digits):
                cant_match = False
                for cc in range(cnt_clues):
                    if (cc == c): continue
                    if ((clues[c][i] == clues[cc][i])
                      & ((target[cc] - m_y[cc]) == 0)):
                        cant_match = True
                if (cant_match):
                    m_n[c] += 1

        # Check for clues with not enough matches
        for c in range(cnt_clues):
            already_matched = m_y[c]
            could_match = cnt_digits - (depth+1) - m_n[c]
            if ((already_matched + could_match) < target[c]):
                hypo_valid = False
                break

        # Check if we've found the solution
        if (m_y == target):
            print "Solution =", hypothesis
            now_time = time.clock()
            print "Total time taken =", now_time - start_time
            sys.exit()

        # Recurse if possible
        if (hypo_valid & ((depth+1) < cnt_digits)):
                search(depth+1, hypothesis)

        # Unwind this hypothesis
        del hypothesis[-1]

search(0, [])
#search(4, [3, 9, 5, 4])
#search(7, [9, 9, 9, 9, 9, 9, 8])

print "No solution found"
now_time = time.clock()
print "Total time taken =", now_time - start_time
sys.exit()
