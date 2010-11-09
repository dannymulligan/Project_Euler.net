#!/usr/bin/python
#
# Project Euler.net Problem 90
#
# Each of the six faces on a cube has a different digit (0 to 9)
# written on it; the same is done to a second cube. By placing the two
# cubes side-by-side in different positions we can form a variety of
# 2-digit numbers.
# 
# For example, the square number 64 could be formed:
#
#            +---+   +---+
#           /   /|  /   /|
#          +---+ + +---+ +
#          | 6 |/  | 4 |/ 
#          +---+   +---+  
#
# In fact, by carefully choosing the digits on both cubes it is
# possible to display all of the square numbers below one-hundred: 01,
# 04, 09, 16, 25, 36, 49, 64, and 81.
# 
# For example, one way this can be achieved is by placing {0, 5, 6, 7,
# 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
# 
# However, for this problem we shall allow the 6 or 9 to be turned
# upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1,
# 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed;
# otherwise it would be impossible to obtain 09.
# 
# In determining a distinct arrangement we are interested in the
# digits on each cube, not the order.
# 
#     {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#     {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
# 
# But because we are allowing 6 and 9 to be reversed, the two distinct
# sets in the last example both represent the extended set {1, 2, 3,
# 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
# 
# How many distinct arrangements of the two cubes allow for all of the
# square numbers to be displayed?
#
# Answer:
# Solved 9/11/09
# 100 problems solved
# Postion #1332 on level 3
#
# The projecteuler.net site says...
# Congratulations, the answer you gave to problem 90 is correct.
#
# Excellent work, dannymulligan! By solving your 100th problem you
# have earned a place among the top 2.53% of members and have advanced
# to level 3.

# The numbers we have to hit are
#     0 <-> 1
#     0 <-> 4
#     0 <-> 6/9
#     1 <-> 6/9
#     2 <-> 5
#     3 <-> 6/9
#     4 <-> 6/9
#     6/9 <-> 4
#     8 <-> 1
# This leads to 2^14 possible base solutions = 16384 possible solutions
# Eliminate cases with >6 digits per die = 6784 possible solutions
# Eliminate duplicate cases = 308 possible solutions



Bsol = []

for (a1,b1) in [(0,1), (1,0)]:
    for (a2,b2) in [(0,4), (4,0)]:
        for (a3,b3) in [(0,6), (0,9), (6,0), (9,0)]:
            for (a4,b4) in [(1,6), (1,9), (6,1), (9,1)]:
                for (a5,b5) in [(2,5), (5,2)]:
                    for (a6,b6) in [(3,6), (3,9), (6,3), (9,3)]:
                        for (a7,b7) in [(4,6), (4,9), (6,4), (9,4)]:
                            for (a8,b8) in [(6,4), (9,4), (4,6), (4,9)]:
                                for (a9,b9) in [(8,1), (1,8)]:
                                    Da = [a1]
                                    if (a2 not in Da):  Da.append(a2)
                                    if (a3 not in Da):  Da.append(a3)
                                    if (a4 not in Da):  Da.append(a4)
                                    if (a5 not in Da):  Da.append(a5)
                                    if (a6 not in Da):  Da.append(a6)
                                    if (a7 not in Da):  Da.append(a7)
                                    if (a8 not in Da):  Da.append(a8)
                                    if (a9 not in Da):  Da.append(a9)
                                    Da.sort()

                                    Db = [b1]
                                    if (b2 not in Db):  Db.append(b2)
                                    if (b3 not in Db):  Db.append(b3)
                                    if (b4 not in Db):  Db.append(b4)
                                    if (b5 not in Db):  Db.append(b5)
                                    if (b6 not in Db):  Db.append(b6)
                                    if (b7 not in Db):  Db.append(b7)
                                    if (b8 not in Db):  Db.append(b8)
                                    if (b9 not in Db):  Db.append(b9)
                                    Db.sort()

                                    if ((len(Da) <= 6) & (len(Db) <= 6)):
                                        if (([Da, Db] not in Bsol) & ([Db, Da] not in Bsol)):
                                            Bsol.append([Da, Db])
                                            #print "Base", len(Da), len(Db), Da, Db

print "Base solutions total = ", len(Bsol)

Esol = []
for sol in Bsol:
    Da = sol[0]
    Db = sol[1]

    if (len(Da) == 6):
        Da_exp = [Da]
    elif (len(Da) == 5):
        Da_exp = []
        for x in range(10):
            if (x not in Da):
                temp = list(Da)
                temp.append(x)
                temp.sort()
                Da_exp.append(temp)
    elif (len(Da) == 4):
        Da_exp = []
        for x in range(10):
            for y in range(10):
                if ((x != y) & (x not in Da) & (y not in Da)):
                    temp = list(Da)
                    temp.append(x)
                    temp.append(y)
                    temp.sort()
                    Da_exp.append(temp)

    if (len(Db) == 6):
        Db_exp = [Db]
    elif (len(Db) == 5):
        Db_exp = []
        for x in range(10):
            if (x not in Db):
                temp = list(Db)
                temp.append(x)
                temp.sort()
                Db_exp.append(temp)
    elif (len(Db) == 4):
        Db_exp = []
        for x in range(10):
            for y in range(10):
                if ((x != y) & (x not in Db) & (y not in Db)):
                    temp = list(Db)
                    temp.append(x)
                    temp.append(y)
                    temp.sort()
                    Db_exp.append(temp)

    #print "Base", len(Da), len(Db), Da, Db
    #print "Exp", len(Da_exp), len(Db_exp), Da_exp, Db_exp
    for Daa in Da_exp:
        for Dbb in Db_exp:
            if (([Daa, Dbb] not in Esol) & ([Dbb, Daa] not in Esol)):
                #print "    ", Daa, Dbb
                Esol.append([Daa,Dbb])

print "Extended solutions = ", len(Esol)

print "Answer = ", len(Esol)
