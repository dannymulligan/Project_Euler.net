#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 178
#
# Step Numbers
#
# Consider the number 45656.
#
# It can be seen that each pair of consecutive digits of 45656 has a
# difference of one.
#
# A number for which every pair of consecutive digits has a difference
# of one is called a step number.
#
# A pandigital number contains every decimal digit from 0 to 9 at
# least once.
#
# How many pandigital step numbers less than 10^40 are there? 

import sys
#print(sys.version)
import time
start_time = time.clock()

DEPTH = 40

#
# We can divide the problem into the following cases...
#
# The case where the first 0 comes before the last 9
#     Some number of digits chosen from 1-9
#     0 - the first zero in the number
#     Some number of digits chosen from 0-9
#     9 - the last nine in the number
#     Some number of digits chosen from 0-8
#
# The case where the last 9 comes before the first 0
#     Some number of digits chosen from 1-9
#     9 - the last nine in the number
#     Some number of digits chosen from 1-8
#     0 - the first zero in the number
#     Some number of digits chosen from 0-8
#
# In more detail...
#
# We are going to define the following sequences...
#
#     Sequence #1a: start with 1-9, use 1-9, end with 0
#     Sequence #1b: start with 0, use 1-9, end with 9
#     Sequence #1c: start with 9, use 0-8, end with 0-8
#
#     Sequence #2a: start with 1-9, use 1-9, end with 9
#     Sequence #2b: start with 8, use 1-8, end with 1
#     Sequence #2c: start with 0, use 0-8, end with 0-8
#
# Further refining...
#
# The case where the first 0 comes before the last 9
#     Sequence #1a: start with 1-9, use 1-9, end with 0 
#         (0 - the first zero in the number)
#     Sequence #1b: start with 0, use 0-9, end with 9
#         (9 - the last nine in the number)
#     Sequence #1c: start with 9, use 0-8, end with 0-8
#
# The case where the last 9 comes before the first 0
#     Sequence #2a: start with 1-9, use 1-9, end with 9
#         (9 - the last nine in the number)
#     Sequence #2b: start with 9, use 1-8, end with 0
#         (0 - the first zero in the number)
#     Sequence #2c: start with 0, use 0-8, end with 0-8
#

################################################################################
def print_table(table, sequence):
    print(" Sequence", end='')
    for i in range(10):
        print("  <<{}>>".format(i), end='')
    print("")

    print(" --------", end='')
    for i in range(10):
        print("  -----", end='')
    print("")

    for n in range(len(table)):
        line = table[n]
        print("{:2}:".format(n), end='')
        print("{:5,}, ".format(sequence[n]), end='')
        for i in range(10):
            print("{:5,}, ".format(line[i]), end='')
        print()


################################################################################
# Sequence #1a: start with 1-9, use 1-9, end with 0
sequence = [0, 0]
table = list()
#            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
table.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
for i in range(DEPTH):
    prev = table[-1]
    next = [0 for _ in range(10)]
    for i in range(10):
        if (i == 0):
            continue
        
        if (i == 0):
            next[i] = prev[i+1]
        elif (i == 9):
            next[i] = prev[i-1]
        else:
            next[i] = prev[i-1] + prev[i+1]
    table.append(next)
    sequence.append(prev[1])

#print()
#print("Sequence #1a: start with 1-9, use 1-9, end with 0")
#print_table(table, sequence)
sequence_1a = sequence


################################################################################
# Sequence #1b: start with 0, use 0-9, end with 9
sequence = [0, 0]
table = list()
#            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
table.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in range(DEPTH):
    prev = table[-1]
    next = [0 for _ in range(10)]
    for i in range(10):
        if (i == 0):
            next[i] = prev[i+1]
        elif (i == 9):
            next[i] = prev[i-1]
        else:
            next[i] = prev[i-1] + prev[i+1]
    table.append(next)
    sequence.append(prev[8])

#print()
#print("Sequence #1b: start with 0, use 0-9, end with 9")
#print_table(table, sequence)
sequence_1b = sequence
        

################################################################################
# Sequence #1c: start with 9, use 0-8, end with 0-8
sequence = [0, 1]
table = list()
#            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
table.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
for i in range(DEPTH):
    prev = table[-1]
    next = [0 for _ in range(10)]
    for i in range(10):
        if (i == 9):
            continue
        
        if (i == 0):
            next[i] = prev[i+1]
        elif (i == 9):
            next[i] = prev[i-1]
        else:
            next[i] = prev[i-1] + prev[i+1]
    table.append(next)
    sequence.append(sum(next))

#print()
#print("Sequence #1c: start with 9, use 0-8, end with 0-8")
#print_table(table, sequence)
sequence_1c = sequence


################################################################################
# Sequence #2a: start with 1-9, use 1-9, end with 9
sequence = [0, 1]
table = list()
#            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
table.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
for i in range(DEPTH):
    prev = table[-1]
    next = [0 for _ in range(10)]
    for i in range(10):
        if (i == 0):
            continue
        
        if (i == 0):
            next[i] = prev[i+1]
        elif (i == 9):
            next[i] = prev[i-1]
        else:
            next[i] = prev[i-1] + prev[i+1]
    table.append(next)
    sequence.append(prev[8])

#print()
#print("Sequence #2a: start with 1-9, use 1-9, end with 9")
#print_table(table, sequence)
sequence_2a = sequence


################################################################################
# Sequence #2b: start with 9, use 1-8, end with 0
sequence = [0, 0]
table = list()
#            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
table.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
for i in range(DEPTH):
    prev = table[-1]
    next = [0 for _ in range(10)]
    for i in range(10):
        if (i == 0) or (i == 9):
            continue

        if (i == 0):
            next[i] = prev[i+1]
        elif (i == 9):
            next[i] = prev[i-1]
        else:
            next[i] = prev[i-1] + prev[i+1]
    table.append(next)
    sequence.append(prev[1])

#print()
#print("Sequence #2b: start with 9, use 1-8, end with 0")
#print_table(table, sequence)
sequence_2b = sequence


################################################################################
# Sequence #2c: start with 0, use 0-8, end with 0-8
sequence = [0, 1]
table = list()
#            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
table.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in range(DEPTH):
    prev = table[-1]
    next = [0 for _ in range(10)]
    for i in range(10):
        if (i == 9):
            continue

        if (i == 0):
            next[i] = prev[i+1]
        elif (i == 9):
            next[i] = prev[i-1]
        else:
            next[i] = prev[i-1] + prev[i+1]
    table.append(next)
    sequence.append(sum(next))

#print()
#print("Sequence #2c: start with 0, use 0-8, end with 0-8")
#print_table(table, sequence)
sequence_2c = sequence


################################################################################
def pandigital(length, debug=False):
    answer = 0
    for a in range(1, length+1):
        for b in range(a+1, length+1):
            # The case where the first 0 comes before the last 9
            #
            # a = location of first 0
            # b = location of last 9
            term = sequence_1a[a] * sequence_1b[b-a+1] * sequence_1c[length-b+1]
            answer += term
            if (term != 0) and debug:
                print("first 0 = {},  last 9 = {}".format(a, b), end='')
                print(", sequence_1a[{}] = {}".format(a, sequence_1a[a]), end='')
                print(", sequence_1b[{}] = {}".format(b-a+1, sequence_1b[b-a+1]), end='')
                print(", sequence_1d[{}] = {}".format(length-b+1, sequence_1c[length-b+1]), end='')
                print(", answer = {}".format(term))
                
            # The case where the last 9 comes before the first 0
            #
            # a = location of last 9
            # b = location of first 0
            term = sequence_2a[a] * sequence_2b[b-a+1] * sequence_2c[length-b+1]
            answer += term
            if (term != 0) and debug:
                print(" last 9 = {}, first 0 = {}".format(a, b), end='')
                print(", sequence_2a[{}] = {}".format(a, sequence_2a[a]), end='')
                print(", sequence_2b[{}] = {}".format(b-a+1, sequence_2b[b-a+1]), end='')
                print(", sequence_2d[{}] = {}".format(length-b+1, sequence_2c[length-b+1]), end='')
                print(", answer = {}".format(term))
                
    return answer


################################################################################
answer = 0
for length in range(10, DEPTH+1):
    p = pandigital(length)
    print("{:,} pandigital numbers of length {}".format(p, length))
    answer += p


################################################################################

print("Answer = {:,}".format(answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))

