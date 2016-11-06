#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 575
#
# Wandering Robots
#
# It was quite an ordinary day when a mysterious alien vessel appeared
# as if from nowhere. After waiting several hours and receiving no
# response it is decided to send a team to investigate, of which you
# are included. Upon entering the vessel you are met by a friendly
# holographic figure, Katharina, who explains the purpose of the
# vessel, Eulertopia.
#
# She claims that Eulertopia is almost older than time itself. Its
# mission was to take advantage of a combination of incredible
# computational power and vast periods of time to discover the answer
# to life, the universe, and everything. Hence the resident cleaning
# robot, Leonhard, along with his housekeeping responsibilities, was
# built with a powerful computational matrix to ponder the meaning of
# life as he wanders through a massive 1000 by 1000 square grid of
# rooms. She goes on to explain that the rooms are numbered
# sequentially from left to right, row by row. So, for example, if
# Leonhard was wandering around a 5 by 5 grid then the rooms would be
# numbered in the following way.
#
#    +----+----+----+----+----+
#    |  1 |  2 |  3 |  4 |  5 |
#    +----+----+----+----+----+
#    |  6 |  7 |  8 |  9 | 10 |
#    +----+----+----+----+----+
#    | 11 | 12 | 13 | 14 | 15 |
#    +----+----+----+----+----+
#    | 16 | 17 | 18 | 19 | 20 |
#    +----+----+----+----+----+
#    | 21 | 22 | 23 | 24 | 25 |
#    +----+----+----+----+----+
#
# Many millenia ago Leonhard reported to Katharina to have found the
# answer and he is willing to share it with any life form who proves
# to be worthy of such knowledge.
#
# Katharina further explains that the designers of Leonhard were given
# instructions to program him with equal probability of remaining in
# the same room or travelling to an adjacent room. However, it was not
# clear to them if this meant (i) an equal probability being split
# equally between remaining in the room and the number of available
# routes, or, (ii) an equal probability (50%) of remaining in the same
# room and then the other 50% was to be split equally between the
# number of available routes.
#
#    +------+------+------+    +------+------+------+
#    |      |      |      |    |      |      |      |
#    | 1/4  |      |      |    | 1/6  |      |      |
#    |  ^   |      |      |    |  ^   |      |      |
#    +--|---+------+------+    +--|---+------+------+
#    |  |   |      |      |    |  |   |      |      |
#    | 1/4 --> 1/4 |      |    | 1/2 --> 1/6 |      |
#    |  |   |      |      |    |  |   |      |      |
#    +--|---+------+------+    +--|---+------+------+
#    |  v   |      |      |    |  v   |      |      |
#    | 1/4  |      |      |    | 1/6  |      |      |
#    |      |      |      |    |      |      |      |
#    +------+------+------+    +------+------+------+
#   (i) Probability of        (ii) Fixed 50% probability
#       remaining related          of remaining
#       to number of exits
#
# The records indicate that they decided to flip a coin. Heads would
# mean that the probability of remaining was dynamically related to
# the number of exits whereas tails would mean that they program
# Leonhard with a fixed 50% probability of remaining in a particular
# room. Unfortunately there is no record of the outcome of the coin,
# so without further information we would need to assume that there is
# equal probability of either of the choices being implemented.
#
# Katharina suggests it should not be too challenging to determine
# that the probability of finding him in a square numbered room in a 5
# by 5 grid after unfathomable periods of time would be approximately
# 0.177976190476 [12 d.p.].
#
# In order to prove yourself worthy of visiting the great oracle you
# must calculate the probability of finding him in a square numbered
# room in the 1000 by 1000 lair in which he has been wandering.
#
#(Give your answer rounded to 12 decimal places)
#
# Solved ??/??/16
# ?? problems solved
# Position #??? on level ?

#import numpy as np


import sys
#print(sys.version)
import time
start_time = time.clock()
Debug = False
#Debug = True


########################################
SIZE = 5
print("Running with SIZE = {}".format(SIZE))
INIT_VALUE = 1.0 / (SIZE * SIZE)
TableA = [[INIT_VALUE for x in range(SIZE)] for y in range(SIZE)]
TableB = [[INIT_VALUE for x in range(SIZE)] for y in range(SIZE)]


########################################
def PrintTable(Table):
    for y in range(SIZE):
        for x in range(SIZE):
            print("{:-16.13f}".format(Table[x][y]), end='')
            if x < SIZE-1:
                print(", ", end='')
            else:
                print()

if False:
    PrintTable(TableA)


########################################
def SumTable(Table):
    Result = 0.0
    for y in range(len(Table)):
        for x in range(len(Table[y])):
            Result += Table[x][y]
    return Result

def AbsSumTable(Table):
    Result = 0.0
    for y in range(len(Table)):
        for x in range(len(Table[y])):
            Result += abs(Table[x][y])
    return Result



########################################
def UpdateTable(Table, Type):
    Delta = [[0.0 for x in range(SIZE)] for y in range(SIZE)]
    if Type == 'A':
        Dcorner, Dedge, Dcore = (1.0/3.0, 1.0/4.0, 1.0/5.0)
    else:
        Dcorner, Dedge, Dcore = (1.0/4.0, 1.0/6.0, 1.0/8.0)

    # Corners
    if Debug:
        print("Corners")

    for (x, y, dx, dy) in [
        (     0,      0,  1,  1),
        (SIZE-1,      0, -1,  1),
        (     0, SIZE-1,  1, -1),
        (SIZE-1, SIZE-1, -1, -1),
    ]:
        Delta[x][y]    -= Table[x][y] * 2.0 * Dcorner
        Delta[x+dx][y] += Table[x][y] * Dcorner
        Delta[x][y+dy] += Table[x][y] * Dcorner

        if Debug:
            print("({},{}) = {:.3f}".format(x, y, Table[x][y]))
            print("({},{}) -> {:.3f} ".format(x, y, -Table[x][y] * 2.0 * Dcorner))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcorner, x+dx, y))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcorner, x, y+dy))
            print("----")

    # Edges
    if Debug:
        print("Edges")

    for (x, y, dx1, dy1, dx2, dy2) in \
        [ (     x,      0, 1, 0,  0,  1) for x in range(1, SIZE-1) ] + \
        [ (     x, SIZE-1, 1, 0,  0, -1) for x in range(1, SIZE-1) ] + \
        [ (     0,      y, 0, 1,  1,  0) for y in range(1, SIZE-1) ] + \
        [ (SIZE-1,      y, 0, 1, -1,  0) for y in range(1, SIZE-1) ]:

        Delta[x][y]         -= Table[x][y] * 3.0 * Dedge
        Delta[x-dx1][y-dy1] += Table[x][y] * Dedge
        Delta[x+dx1][y+dy1] += Table[x][y] * Dedge
        Delta[x+dx2][y+dy2] += Table[x][y] * Dedge

        if Debug:
            print("({},{}) = {:.3f}".format(x, y, Table[x][y]))
            print("({},{}) -> {:.3f} ".format(x, y, -Table[x][y] * 3.0 * Dedge))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dedge, x-dx1, y-dy1))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dedge, x+dx1, y+dy1))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dedge, x+dx2, y+dy2))
            print("----")

    # Core
    if Debug:
        print("Core")

    for y in range(1, SIZE-1):
        for x in range(1, SIZE-1):

            Delta[x][y]   -= Table[x][y] * 4.0 * Dcore
            Delta[x-1][y] += Table[x][y] * Dcore
            Delta[x+1][y] += Table[x][y] * Dcore
            Delta[x][y-1] += Table[x][y] * Dcore
            Delta[x][y+1] += Table[x][y] * Dcore

            if Debug:
                print("({},{}) = {:.3f}".format(x, y, Table[x][y]))
                print("({},{}) -> {:.3f} ".format(x, y, -Table[x][y] * 4.0 * Dcore))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore, x-1,   y))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore, x+1,   y))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore,   x, y-1))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore,   x, y+1))
                print("----")

    return Delta


########################################
def UpdateMatrix(Type):
    Delta = [[0.0 for x in range(SIZE)] for y in range(SIZE)]
    if Type == 'A':
        Dcorner, Dedge, Dcore = (1.0/3.0, 1.0/4.0, 1.0/5.0)
    else:
        Dcorner, Dedge, Dcore = (1.0/4.0, 1.0/6.0, 1.0/8.0)

    # Corners
    if Debug:
        print("Corners")

    for (x, y, dx, dy) in [
        (     0,      0,  1,  1),
        (SIZE-1,      0, -1,  1),
        (     0, SIZE-1,  1, -1),
        (SIZE-1, SIZE-1, -1, -1),
    ]:
        Delta[x][y]    -= Table[x][y] * 2.0 * Dcorner
        Delta[x+dx][y] += Table[x][y] * Dcorner
        Delta[x][y+dy] += Table[x][y] * Dcorner

        if Debug:
            print("({},{}) = {:.3f}".format(x, y, Table[x][y]))
            print("({},{}) -> {:.3f} ".format(x, y, -Table[x][y] * 2.0 * Dcorner))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcorner, x+dx, y))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcorner, x, y+dy))
            print("----")

    # Edges
    if Debug:
        print("Edges")

    for (x, y, dx1, dy1, dx2, dy2) in \
        [ (     x,      0, 1, 0,  0,  1) for x in range(1, SIZE-1) ] + \
        [ (     x, SIZE-1, 1, 0,  0, -1) for x in range(1, SIZE-1) ] + \
        [ (     0,      y, 0, 1,  1,  0) for y in range(1, SIZE-1) ] + \
        [ (SIZE-1,      y, 0, 1, -1,  0) for y in range(1, SIZE-1) ]:

        Delta[x][y]         -= Table[x][y] * 3.0 * Dedge
        Delta[x-dx1][y-dy1] += Table[x][y] * Dedge
        Delta[x+dx1][y+dy1] += Table[x][y] * Dedge
        Delta[x+dx2][y+dy2] += Table[x][y] * Dedge

        if Debug:
            print("({},{}) = {:.3f}".format(x, y, Table[x][y]))
            print("({},{}) -> {:.3f} ".format(x, y, -Table[x][y] * 3.0 * Dedge))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dedge, x-dx1, y-dy1))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dedge, x+dx1, y+dy1))
            print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dedge, x+dx2, y+dy2))
            print("----")

    # Core
    if Debug:
        print("Core")

    for y in range(1, SIZE-1):
        for x in range(1, SIZE-1):

            Delta[x][y]   -= Table[x][y] * 4.0 * Dcore
            Delta[x-1][y] += Table[x][y] * Dcore
            Delta[x+1][y] += Table[x][y] * Dcore
            Delta[x][y-1] += Table[x][y] * Dcore
            Delta[x][y+1] += Table[x][y] * Dcore

            if Debug:
                print("({},{}) = {:.3f}".format(x, y, Table[x][y]))
                print("({},{}) -> {:.3f} ".format(x, y, -Table[x][y] * 4.0 * Dcore))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore, x-1,   y))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore, x+1,   y))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore,   x, y-1))
                print("({},{}) -> {:.3f} -> ({},{})".format(x, y, Table[x][y] * Dcore,   x, y+1))
                print("----")

    return Delta


########################################
def ApplyUpdate(Table, Update, Scale):
    Result = [[0.0 for x in range(SIZE)] for y in range(SIZE)]
    for y in range(SIZE):
        for x in range(SIZE):
            Result[x][y] = Table[x][y] + Scale*Update[x][y]

    return Result


########################################

AbsSumA = 1.0
IterationA = 1
while (AbsSumA > 1.0e-13):
    #print("====================")
    #print("TableA =")
    #PrintTable(TableA)

    UpdateA = UpdateTable(TableA, 'A')
    AbsSumA = AbsSumTable(UpdateA)
    TableA = ApplyUpdate(TableA, UpdateA, 1.0)

    #print("UpdateA =")
    #PrintTable(UpdateA)
    #print("Sum = {}".format(SumTable(UpdateA)))

    if (IterationA % 500) == 0:
        print("{}: AbsSumA = {:.13f}".format(IterationA, AbsSumA))
    IterationA += 1

#print("TableA =")
#PrintTable(TableA)
#print("UpdateA =")
#PrintTable(UpdateA)

AnswerA = TableA[0][0] + TableA[3][0] + TableA[3][1] + TableA[0][3] + TableA[4][4]
print("Calculated Answer A = {} after {:,} iterations".format(AnswerA, IterationA))


AbsSumB = 1.0
IterationB = 1
while (AbsSumB > 1.0e-13):
    #print("====================")
    #print("TableB =")
    #PrintTable(TableB)

    UpdateB = UpdateTable(TableB, 'B')
    AbsSumB = AbsSumTable(UpdateB)
    TableB = ApplyUpdate(TableB, UpdateB, 1.0)

    #print("UpdateA =")
    #PrintTable(UpdateA)
    #print("Sum = {}".format(SumTable(UpdateA)))

    if (IterationB % 500) == 0:
        print("{}: AbsSumB = {:.13f}".format(IterationB, AbsSumB))
    IterationB += 1

#print("TableB =")
#PrintTable(TableB)
#print("UpdateB =")
#PrintTable(UpdateB)

AnswerB = TableB[0][0] + TableB[3][0] + TableB[3][1] + TableB[0][3] + TableB[4][4]
print("Calculated Answer B = {} after {:,} iterations".format(AnswerB, IterationB))

print("Final solution = {:.12f}".format(0.5*(AnswerA + AnswerB)))
AnswerString = "{:.12f}".format(0.5*(AnswerA + AnswerB))
if (AnswerString == "0.177976190476"):
    print("Answer matches example")

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
