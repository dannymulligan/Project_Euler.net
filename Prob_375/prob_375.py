#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 375
#
# Minimum of subsequences
#
# Let S(n) be an integer sequence produced with the following
# pseudo-random number generator:
#
#    S(0)    =  290797
#    S(n+1)  =  S(n)^2 mod 50515093
#
# Let A(i, j) be the minimum of the numbers Si, Si+1, ... , Sj for i
# <= j.
#
# Let M(N) = sum(A(i, j)) for 1 <= i <= j <= N.
#
# We can verify that M(10) = 432256955 and M(10000) = 3264567774119.
#
# Find M(2000000000).
#
# Solved 03/17/17

import sys
#print(sys.version)
import time
start_time = time.clock()


########################################
N = 2000000000
Debug = False


########################################
def S():
    S =  290797
    while True:
        S = S**2 % 50515093
        yield S


########################################
def RowSum(Row):
    Sum = 0
    for (s, cnt) in Row:
        Sum += s*cnt
    return Sum


########################################
MinS = 290797
MinN = 0
Answer = 0
Row = list()  # Tuples like this (S, Repeat count)
Answers = list()
FirstLoop = True
n = 1
for s in S():
    if FirstLoop:
        FirstLoop = False
        Row.append((s, 1))
        Answers.append(RowSum(Row))
        Answer += RowSum(Row)
    else:
        if s > Row[-1][0]:
            # Add the current S(n) to the end of the list
            Row.append((s, 1))
            Answer += RowSum(Row)
            Answers.append(Answer)
        else:
            cnt = 1
            while (len(Row) > 0) and (s < Row[-1][0]):
                # Roll up items from the end of the list until we get one smaller than the current S(n)
                cnt += Row[-1][1]
                del Row[-1]
                del Answers[-1]

            # Add the rolled up item to the end of the list
            Row.append((s, cnt))
            Answer += RowSum(Row)
            Answers.append(Answer)

            # Check if we have detected a loop
            if (len(Row) > 1) and (Row[-2][0] == Row[-1][0]):
                # We've detected a loop
                DeltaN = Row[-1][1]
                DeltaAnswer = Answers[-1] - Answers[-2]
                
                if Debug:
                    print("Detected a loop at n = {:,}".format(n))
                    print("Row = {}".format(Row))
                    print("Answers = {}".format(Answers))
                    print("DeltaN = {:,}, DeltaAnswer = {:,}".format(DeltaN, DeltaAnswer))

                i = 1
                while (n+DeltaN < N):
                    Answer += DeltaAnswer + i * DeltaN * DeltaN * s
                    n += DeltaN
                    i += 1
                    if Debug:
                        print("n = {:,}, Answer = {:,}".format(n, Answer))
                    
                del Row[-1]
                del Answers[-1]
                del Row[-1]
                del Answers[-1]
                Row.append((s, n))
                Answers.append(Answer)

    if s < MinS:
        MinS = s
        MinN = n

    if Debug:
        print("S({:3}) = {:12,}, Row sum = {:12,}, Answer sum = {:12,}, Row = {}, ".format(n, s, RowSum(Row), Answer, Row))

    if (n % 1000000) == 0:
        print("M({:,}) = {:,}, len(Row) = {:,}".format(n, Answer, len(Row)))
        
    if n == N:
        break
    else:
        n += 1


########################################
if Debug:
    print("Min at S({:,}) = {:,}".format(MinN, MinS))
    print("len(Row) = {:,}".format(len(Row)))
    print("Row = {}".format(Row))
    print("len(Answers) = {:,}".format(len(Answers)))
    print("Answers = {}".format(Answers))

if   N == 100000:
    print("Answer: M(100,000) = 55,258,601,351,663 (Expected)")
elif N == 200000:
    print("Answer: M(200,000) = 112,875,845,964,775 (Expected)")
elif N == 1000000:
    print("Answer: M(1,000,000) = 617,770,209,962,939 (Expected)")
elif N == 2000000:
    print("Answer: M(2,000,000) = 1,294,245,562,777,329 (Expected)")
elif N == 10000000:
    print("Answer: M(10,000,000) = 7,049,973,190,459,058 (Expected)")
elif N == 20000000:
    print("Answer: M(20,000,000) = 14,721,617,435,604,943 (Expected)")
elif N == 200000000:
    print("Answer: M(200,000,000) = 203,286,305,732,490,134 (Expected)")

print("Answer: M({:,}) = {:,}".format(n, Answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))

