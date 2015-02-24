#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 493
#
# Under The Rainbow
#
# 70 colored balls are placed in an urn, 10 for each of the seven
# rainbow colors.
#
# What is the expected number of distinct colors in 20 randomly picked
# balls?
#
# Give your answer with nine digits after the decimal point
# (a.bcdefghij).
#
# Solved ??/??/14
# ??? problems solved
# Position #??? on level ?

import time
start_time = time.clock()

def count(l):
    ans = 0
    for i in l:
        if i != 0:
            ans += 1
    return ans

solutions = list()

solution = dict()
picked = [0] * 7
solution[str(picked)] = (picked, 1.0)
solutions.append(solution)

for ball in range(20):
    this_level = solutions[ball]
    next_level = dict()
    for key in this_level:
        solution, prob = this_level[key]
        #print("ball={}, solution={}, prob={}".format(ball, solution, prob))

        for color in range(7):
            if solution[color] >= 10:
                continue
            new_prob = prob * (10-solution[color]) / (70-ball)
            new_solution = solution[:]
            new_solution[color] += 1
            new_solution.sort()

            if str(new_solution) in next_level:
                new_prob += next_level[str(new_solution)][1]
            next_level[str(new_solution)] = (new_solution, new_prob)
    solutions.append(next_level)

    print("Solution for level {}".format(ball))
    expected = 0.0
    for key in next_level:
        solution, prob = next_level[key]
        #print("    solution={} count={} prob={}".format(solution, count(solution), prob))
        expected += count(solution) * prob
    print("    Expected number of distinct colors is {:11.9f}".format(expected))

print("Answer is {:11.9f}".format(expected))
print("time taken {:.1f} seconds".format(time.clock() - start_time))
