#!/usr/bin/python
#
# Project Euler.net Problem 93
#
# By using each of the digits from the set, {1, 2, 3, 4}, exactly
# once, and making use of the four arithmetic operations (+, -, *, /)
# and brackets/parentheses, it is possible to form different positive
# integer targets.
# 
# For example,
# 
#     8 = (4 * (1 + 3)) / 2
#     14 = 4 * (3 + 1 / 2)
#     19 = 4 * (2 + 3) - 1
#     36 = 3 * 4 * (2 + 1)
# 
# Note that concatenations of the digits, like 12 + 34, are not allowed.
# 
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one
# different target numbers of which 36 is the maximum, and each of the
# numbers 1 to 28 can be obtained before encountering the first
# non-expressible number.
# 
# Find the set of four distinct digits, a < b < c < d, for which the
# longest set of consecutive positive integers, 1 to n, can be
# obtained, giving your answer as a string: abcd.
#
# Answer:

# String is of the form
#
#    A  op0  B  op1  C  op2  D
#
# where op? = '+', '-', '*', or '/'
# and brackets can be positioned as follows
#
#    A  op0  B  op1  C  op2  D    Case
#  (---)   (---)   (---)   (---)   0
#  (---)   (---)   (-----------)   1
#  (---)   (-----------)   (---)   2
#  (-----------)   (---)   (---)   3
#
#  (-----------)   (-----------)   4
#
#  (-------------------)   (---)   5
#  ((==========)-------)   (---)   6
#  (-------(==========))   (---)   7
#  (---)   (-------------------)   8
#  (---)   ((==========)-------)   9
#  (---)   (-------(==========))   10
#
# ...or...
#
#    A  op0  B  op1  C  op2  D    Case
#                                  0
#                  (-----------)   1
#          (-----------)           2
#  (-----------)                   3
#
#  (-----------)   (-----------)   4
#
#  (-------------------)           5
#  ((==========)-------)           6
#  (-------(==========))           7
#          (-------------------)   8
#          ((==========)-------)   9
#          (-------(==========))   10

# Searched all combinations of numbers 1..42
# best solutions found so far are...
# [1, 2, 3, 4]    New max 28
# [1, 2, 4, 5]    New max 32
# [1, 2, 5, 6]    New max 43
# [1, 2, 5, 8]    New max 43
# [2, 5, 6, 8]    New max 46
# [4, 5, 6, 8]    New max 52
# [5, 6, 8, 9]    New max 57
# [3, 4, 10, 11]  New max 57
# [2, 4, 7, 15]   New max 61
# [3, 6, 8, 19]   New max 61
# [2, 5, 13, 20]  New max 61
# [2, 4, 9, 23]   New max 61
# [3, 5, 7, 23]   New max 61
# [3, 11, 21, 23] New max 61
# [5, 8, 17, 23]  New max 61
# [1, 2, 5, 24]   New max 62
# [5, 10, 17, 24] New max 62
# [1, 2, 5, 25]   New max 63
# [6, 7, 15, 25]  New max 64
# [7, 10, 22, 25] New max 73
# [24, 28, 35, 38] New max 74
# [25, 27, 30, 39] New max 75
# [28, 32, 38, 41] New max 76


def groups_of_4(nums):
    cnt = len(nums)
    for a in range(1,cnt+1):
        for b in range(a+1,cnt+1):
            for c in range(b+1,cnt+1):
                for d in range(c+1,cnt+1):
                    yield [a,b,c,d]

max_conseq = 0
max_candidates = []

for candidates in groups_of_4(range(1,10)):
    results = []
    for a in candidates:
        A = str(a)

        for b in candidates:
            B = str(b)
            if (B == A):  continue

            for c in candidates:
                C = str(c)
                if (C == A):  continue
                if (C == B):  continue

                for d in candidates:
                    D = str(d)
                    if (D == A):  continue
                    if (D == B):  continue
                    if (D == C):  continue

                    for op0 in ['+', '-', '*', '/']:
                        for op1 in ['+', '-', '*', '/']:
                            for op2 in ['+', '-', '*', '/']:

                                for case in range(11):
                                    if   (case ==  0):  eqn = A + op0 + B + op1 + C + op2 + D
                                    elif (case ==  1):  eqn = A + op0 + B + op1 + '(' + C + op2 + D + ')'
                                    elif (case ==  2):  eqn = A + op0 + '(' + B + op1 + C + ')' + op2 + D
                                    elif (case ==  3):  eqn = '(' + A + op0 + B + ')' + op1 + C + op2 + D
                                    elif (case ==  4):  eqn = '(' + A + op0 + B + ')' + op1 + '(' + C + op2 + D + ')'
                                    elif (case ==  5):  eqn = '(' + A + op0 + B + op1 + C + ')' + op2 + D
                                    elif (case ==  6):  eqn = '((' + A + op0 + B + ')' + op1 + C + ')' + op2 + D
                                    elif (case ==  7):  eqn = '(' + A + op0 + '(' + B + op1 + C + '))' + op2 + D
                                    elif (case ==  8):  eqn = A + op0 + '(' + B + op1 + C + op2 + D + ')'
                                    elif (case ==  9):  eqn = A + op0 + '((' + B + op1 + C + ')' + op2 + D + ')'
                                    elif (case == 10):  eqn = A + op0 + '(' + B + op1 + '(' + C + op2 + D + '))'

                                    try:
                                        res = eval(eqn)
                                        #print res, '=', eqn
                                    except ZeroDivisionError:
                                        continue
                                    if ((res >= 1) & (res not in results)):
                                        results.append(res)

    results.sort()
    conseq = 1
    while (conseq in results):
        conseq += 1
    conseq -= 1
    if (conseq >= max_conseq):
        max_conseq = conseq
        max_candidates = candidates
        print candidates, "New max", conseq, len(results), results
    else:
        print candidates, conseq

print "Answer", max_candidates, max_conseq
