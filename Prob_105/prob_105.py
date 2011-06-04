#!/usr/bin/python
#
# Project Euler.net Problem 105
# 
# Let S(A) represent the sum of elements in set A of size n. We shall
# call it a special sum set if for any two non-empty disjoint subsets,
# B and C, the following properties are true:
# 
#    1. S(B) != S(C); that is, sums of subsets cannot be equal.
#    2. If B contains more elements than C then S(B) > S(C).
# 
# For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum
# set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164,
# 119, 79, 159, 161, 139, 158} satisfies both rules for all possible
# subset pair combinations and S(A) = 1286.
# 
# Using sets.txt (right click and "Save Link/Target As..."), a 4K text
# file with one-hundred sets containing seven to twelve elements (the
# two examples given above are the first two sets in the file),
# identify all the special sum sets, A_(1), A_(2), ..., A_(k), and
# find the value of S(A_(1)) + S(A_(2)) + ... + S(A_(k)).
# 
# NOTE: This problem is related to problems 103 and 106.
#
# Answer: 73702
# Solved: 06/04/11
# 140 problems solved
# Position #216 on level 3

import itertools

tfile = open("./sets.txt", "r")
answer = 0

lcount = 0
for line in tfile:
    lcount += 1
    #setA = (map(int, x) for x in line.split(','))
    #setA = (float(x) for x in line.split(','))
    sAs = line.split(',')
    sA = []
    found = True
    for s in sAs:
       sA.append(int(s))
    
    print "Set {0}: {1}, sum={2}".format(lcount, sA, sum(sA))
    lA = len(sA)
    for x in itertools.product('ABC', repeat=lA):
        (lB,lC) = (0,0)
        (tB,tC) = (0,0)
        (sB,sC) = ([],[])
        for i in range(lA):
            if x[i] == 'B':
               lB += 1
               tB += sA[i]
               sB.append(sA[i])
            if x[i] == 'C':
               lC += 1
               tC += sA[i]
               sC.append(sA[i])
        if (lB == 0) | (lC == 0):  continue

        if (((lB == lC) & (tB == tC))
          | ((lB >  lC) & (tB <= tC))
          | ((lB <  lC) & (tB >= tC))):
            found = False
            print "    Fail", sB, sC
            break
        
        
    if (found == True):
        answer += sum(sA)

print "Answer =", answer
