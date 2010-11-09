#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 205
#
# Dice Game
#
# Peter has nine four-sided (pyramidal) dice, each with faces numbered
# 1, 2, 3, 4.
# Colin has six six-sided (cubic) dice, each with faces numbered 1, 2,
# 3, 4, 5, 6.
#
# Peter and Colin roll their dice and compare totals: the highest
# total wins. The result is a draw if the totals are equal.
#
# What is the probability that Pyramidal Pete beats Cubic Colin? Give
# your answer rounded to seven decimal places in the form 0.abcdefg
#
# Answer: 0.5731441
# Solved 11/07/10
# 129 problems solved
# Position #460 on level 3

import sys

P_die = 4
C_die = 6
P_combinations = [0] * 37
C_combinations = [0] * 37

for p0 in range(1,P_die+1):
    for p1 in range(1,P_die+1):
        for p2 in range(1,P_die+1):
            for p3 in range(1,P_die+1):
                for p4 in range(1,P_die+1):
                    for p5 in range(1,P_die+1):
                        for p6 in range(1,P_die+1):
                            for p7 in range(1,P_die+1):
                                for p8 in range(1,P_die+1):
                                    sum = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
                                    P_combinations[sum] += 1
P_sum = 0
for i in P_combinations:
    P_sum += i

for c0 in range(1,C_die+1):
    for c1 in range(1,C_die+1):
        for c2 in range(1,C_die+1):
            for c3 in range(1,C_die+1):
                for c4 in range(1,C_die+1):
                    for c5 in range(1,C_die+1):
                        sum = c0 + c1 + c2 + c3 + c4 + c5
                        C_combinations[sum] += 1
C_sum = 0
for i in C_combinations:
    C_sum += i

# Calculate the probability that P wins with each possible score
P_wins = [0.0] * 37
worse_C_scores = 0
for i in range(1,37):
    worse_C_scores += C_combinations[i-1]
    P_wins[i] = 1.0 * worse_C_scores / C_sum

print "P_wins =", P_wins

# Calculate the probability that P gets each possible score
P_prob = [0.0] * 37
for i in range(0,37):
    P_prob[i] = 1.0 * P_combinations[i] / P_sum

print "P_prob =", P_prob

# Calculate the answer to the question
Answer = 0.0
for i in range(0,37):
    Answer += P_prob[i] * P_wins[i]

print "Answer =", Answer
print "Answer = {0:.7f} (rounded to 7 decimal places)".format(Answer)

sys.exit()



