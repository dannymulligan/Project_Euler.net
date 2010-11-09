#!/usr/bin/python
#
# Project Euler.net Problem 68
#
# Consider the following "magic" 3-gon ring, filled with the numbers 1
# to 6, and each line adding to nine.
#
#     3-gon ring diagram
#
#               ( )
#                 \ 
#                 ( )
#               /     \   
#             ( )-----( )----( )
#           /
#         ( )

#
# Working clockwise, and starting from the group of three with the
# numerically lowest external node (4,3,2 in this example), each
# solution can be described uniquely. For example, the above solution
# can be described by the set: 4,3,2; 6,2,1; 5,1,3.
#
# It is possible to complete the ring with four different totals: 9,
# 10, 11, and 12. There are eight solutions in total.
#
#     Total      Solution Set
#       9     4,2,3; 5,3,1; 6,1,2
#       9     4,3,2; 6,2,1; 5,1,3
#      10     2,3,5; 4,5,1; 6,1,3
#      10     2,5,3; 6,3,1; 4,1,5
#      11     1,4,6; 3,6,2; 5,2,4
#      11     1,6,4; 5,4,2; 3,2,6
#      12     1,5,6; 2,6,4; 3,4,5
#      12     1,6,5; 3,5,4; 2,4,6
#
# By concatenating each group it is possible to form 9-digit strings;
# the maximum string for a 3-gon ring is 432621513.
#
# Using the numbers 1 to 10, and depending on arrangements, it is
# possible to form 16- and 17-digit strings. What is the maximum
# 16-digit string for a "magic" 5-gon ring?
#
#         5-gon ring diagram
#
#               ( )
#                 \ 
#                 ( )       ( )
#              /      \    /
#           ( )         ( )
#         /  \           /
#      ( )    \         /
#             ( )-----( )---( )
#               \
#                ( )
#
#
#
# Answer: 6531031914842725
# Solved 10/22/09
# 85 problems solved
# Position #225 on level 2




# Key for 3-gon:
#               (A)
#                 \ 
#                 (D)
#               /     \   
#             (F)-----(E)----(B)
#           /
#         (C)
#
# A, B, C, D, E, F: can be 1..6

print "Solving 3-gon"
answer = 0
for A in range(1,7):
    #print "A ", [A]

    for B in range(1,7):
        if (B in [A]):  continue
        #print "B ", [A, B]

        for C in range(1,7):
            if (C in [A, B]):  continue
            #print "C ", [A, B, C]

            for D in range(1,7):
                if (D in [A, B, C]):  continue
                #print "D ", [A, B, C, D]

                for E in range(1,7):
                    if (E in [A, B, C, D]):  continue
                    #print "E ", [A, B, C, D, E]

                    for F in range(1,7):
                        if (F in [A, B, C, D, E]):  continue
                        #print "F ", [A, B, C, D, E, F]

                        ADE = (A + D + E)
                        BEF = (B + E + F)
                        CFD = (C + F + D)
                        if (ADE == BEF == CFD):
                            #print [A, B, C, D, E, F]
                            if   (A == min(A, B, C)):
                                sADE = str(A) + str(D) + str(E)
                                sBEF = str(B) + str(E) + str(F)
                                sCFD = str(C) + str(F) + str(D)
                            elif (B == min(A, B, C)):
                                sCFD = str(A) + str(D) + str(E)
                                sADE = str(B) + str(E) + str(F)
                                sBEF = str(C) + str(F) + str(D)
                            else:
                                sBEF = str(A) + str(D) + str(E)
                                sCFD = str(B) + str(E) + str(F)
                                sADE = str(C) + str(F) + str(D)
                            s_result = sADE + sBEF + sCFD
                            result = int(s_result)
                            print "Total = {0}, Solution = {1}, {2}".format(ADE, result, [A, B, C, D, E, F])
                            if (answer < result):
                                answer = result
print "Answer = ", answer
print

# Key for 5-gon:
#               (A)
#                 \ 
#                 (F)       (B)
#              /      \    /
#           (J)         (G)
#         /  \           /
#      (E)    \         /
#             (I)-----(H)---(C)
#               \
#                (D)
#
# A, B, C, D, E: can be 1..10
# F, G, H, I, J: can be 1..9

print "Solving 5-gon"
answer = 0
for A in range(1,11):
    #print "A ", [A]

    for B in range(1,11):
        if (B in [A]):  continue
        #print "B ", [A, B]

        for C in range(1,11):
            if (C in [A, B]):  continue
            #print "C ", [A, B, C]

            for D in range(1,11):
                if (D in [A, B, C]):  continue
                #print "D ", [A, B, C, D]

                for E in range(1,11):
                    if (E in [A, B, C, D]):  continue
                    #print "E ", [A, B, C, D, E]

                    for F in range(1,10):
                        if (F in [A, B, C, D, E]):  continue
                        #print "F ", [A, B, C, D, E, F]

                        for G in range(1,10):
                            if (G in [A, B, C, D, E, F]):  continue
                            #print "G ", [A, B, C, D, E, F, G]

                            for H in range(1,10):
                                if (H in [A, B, C, D, E, F, G]):  continue
                                #print "H ", [A, B, C, D, E, F, G, H]

                                for I in range(1,10):
                                    if (I in [A, B, C, D, E, F, G, H]):  continue
                                    #print "I ", [A, B, C, D, E, F, G, H, I]

                                    for J in range(1,10):
                                        if (J in [A, B, C, D, E, F, G, H, I]):  continue
                                        #print "J ", [A, B, C, D, E, F, G, H, I, J]

                                        AFG = (A + F + G)
                                        BGH = (B + G + H)
                                        CHI = (C + H + I)
                                        DIJ = (D + I + J)
                                        EJF = (E + J + F)
                                        if (AFG == BGH == CHI == DIJ == EJF):
                                            #print [A, B, C, D, E, F, G, H, I, J]
                                            if   (A == min(A, B, C, D, E)):
                                                sAFG = str(A) + str(F) + str(G)
                                                sBGH = str(B) + str(G) + str(H)
                                                sCHI = str(C) + str(H) + str(I)
                                                sDIJ = str(D) + str(I) + str(J)
                                                sEJF = str(E) + str(J) + str(F)
                                            elif (B == min(A, B, C, D, E)):
                                                sEJF = str(A) + str(F) + str(G)
                                                sAFG = str(B) + str(G) + str(H)
                                                sBGH = str(C) + str(H) + str(I)
                                                sCHI = str(D) + str(I) + str(J)
                                                sDIJ = str(E) + str(J) + str(F)
                                            elif (C == min(A, B, C, D, E)):
                                                sDIJ = str(A) + str(F) + str(G)
                                                sEJF = str(B) + str(G) + str(H)
                                                sAFG = str(C) + str(H) + str(I)
                                                sBGH = str(D) + str(I) + str(J)
                                                sCHI = str(E) + str(J) + str(F)
                                            elif (D == min(A, B, C, D, E)):
                                                sCHI = str(A) + str(F) + str(G)
                                                sDIJ = str(B) + str(G) + str(H)
                                                sEJF = str(C) + str(H) + str(I)
                                                sAFG = str(D) + str(I) + str(J)
                                                sBGH = str(E) + str(J) + str(F)
                                            else:
                                                sBGH = str(A) + str(F) + str(G)
                                                sCHI = str(B) + str(G) + str(H)
                                                sDIJ = str(C) + str(H) + str(I)
                                                sEJF = str(D) + str(I) + str(J)
                                                sAFG = str(E) + str(J) + str(F)
                                            s_result = sAFG + sBGH + sCHI + sDIJ + sEJF
                                            result = int(s_result)
                                            print "Total = {0}, Solution = {1}, {2}".format(AFG, result, [A, B, C, D, E, F, G, H, I, J])
                                            if (answer < result):
                                                answer = result
print "Answer = ", answer
print
