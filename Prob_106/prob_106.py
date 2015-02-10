#!/usr/bin/python
#
# Project Euler.net Problem 106
#
# Let S(A) represent the sum of elements in set A of size n. We shall
# call it a special sum set if for any two non-empty disjoint subsets,
# B and C, the following properties are true:
#
#    1. S(B) != S(C); that is, sums of subsets cannot be equal.
#    2. If B contains more elements than C then S(B) > S(C).
#
# For this problem we shall assume that a given set contains n
# strictly increasing elements and it already satisfies the second
# rule.
#
# Surprisingly, out of the 25 possible subset pairs that can be
# obtained from a set for which n = 4, only 1 of these pairs need to
# be tested for equality (first rule). Similarly, when n = 7, only 70
# out of the 966 subset pairs need to be tested.
#
# For n = 12, how many of the 261625 subset pairs that can be obtained
# need to be tested for equality?
#
# NOTE: This problem is related to problems 103 and 105.
#
# Solved:
# ? problems solved
# Position #??? on level ?

import itertools
import time

def count_subset_pairs(n):
    print("----------------")
    print("count_subset_pairs(n={})".format(n))
    start_time = time.clock()
    answer = 0
    nums = [n for n in range(1, n+1)]

    for i in range(2, n/2 + 1):
        for g_1_2 in itertools.combinations(nums, i*2):
            #print("g_1_2 = {}".format(g_1_2))
            for g_1 in itertools.combinations(g_1_2, i):
                g_1 = list(g_1)
                g_2 = list()
                for j in g_1_2:
                    if not j in g_1:
                        g_2.append(j)
                #print("    g_1 = {}, g_2 = {}".format(g_1, g_2))
                g_1_larger = False
                g_2_larger = False
                for j in range(i):
                    if g_1[j] > g_2[j]:  g_1_larger = True
                    if g_1[j] < g_2[j]:  g_2_larger = True
                if (g_1_larger & g_2_larger):
                    answer += 1
    print("count_subset_pairs(n={}) = {}".format(n, answer/2))
    print("time taken {:.1f} seconds".format(time.clock() - start_time))
    return answer/2

print("Answer is {}".format(count_subset_pairs(12)))
