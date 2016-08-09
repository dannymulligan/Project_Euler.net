#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 185
#
# Number Mind
#
# The game Number Mind is a variant of the well known game Master
# Mind.
#
# Instead of coloured pegs, you have to guess a secret sequence of
# digits. After each guess you're only told in how many places you've
# guessed the correct digit. So, if the sequence was 1234 and you
# guessed 2036, you'd be told that you have one correct digit;
# however, you would NOT be told that you also have another digit in
# the wrong place.
#
# For instance, given the following guesses for a 5-digit secret
# sequence,
#
#     90342  2 correct
#     70794  0 correct
#     39458  2 correct
#     34109  1 correct
#     51545  2 correct
#     12531  1 correct
#
# The correct sequence 39542 is unique.
#
# Based on the following 22 guesses,
#
#     5616185650518293  2 correct
#     3847439647293047  1 correct
#     5855462940810587  3 correct
#     9742855507068353  3 correct
#     4296849643607543  3 correct
#     3174248439465858  1 correct
#     4513559094146117  2 correct
#     7890971548908067  3 correct
#     8157356344118483  1 correct
#     2615250744386899  2 correct
#     8690095851526254  3 correct
#     6375711915077050  1 correct
#     6913859173121360  1 correct
#     6442889055042768  2 correct
#     2321386104303845  0 correct
#     2326509471271448  2 correct
#     5251583379644322  2 correct
#     1748270476758276  3 correct
#     4895722652190306  1 correct
#     3041631117224635  3 correct
#     1841236454324589  3 correct
#     2659862637316867  2 correct
#
# Find the unique 16-digit secret sequence.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?


import sys
import time

start_time = time.clock()
now_time = start_time
prev_time = start_time


def divide(matches):
    for i in range(matches[0]+1):
        if len(matches) > 1:
            for (l, r) in divide(matches[1:]):
                yield [i] + l, [matches[0] - i] + r
        else:
                yield [i], [matches[0] - i]


def search(soln_so_far, clues, matches):
    #print("{} DEBUG: search({}, {})".format(soln_so_far, clues, matches))
    clue_depth = len(clues[0])

    for i in range(0,10):
        # Try all digits 0..9 for the first digit in the clues
        #print("{} Trying leading digit = {}".format(soln_so_far, i))

        if (clue_depth == 1):
            # Clues are of length 1, find a solution without recursion
            good_match = True
            for (clue, match) in zip(clues, matches):
                #print("{}Processing clue={}, match={}".format(soln_so_far, clue, match))
                if (clue[0] == i) and (match != 1):
                    good_match = False
                if (clue[0] != i) and (match != 0):
                    good_match = False

                if not good_match:
                    break

            if good_match:
                #print("FOUND match {}, clues={}, matches={}".format(soln_so_far + [i], clues, matches))
                yield [i]

        else:
            # Clues are of length > 1, look for solution by recursion
            good_match = True
            new_clues = []
            new_matches = []

            for (clue, match) in zip(clues, matches):
                #print("{} Processing clue {}".format(soln_so_far, clue))
                #print("{}     clue[0] = {}".format(soln_so_far, clue[0]))
                #print("{}     clue[1] = {}".format(soln_so_far, clue[1]))
                if (clue[0] == i):
                    if match > 0:
                        new_clues.append(clue[1:])
                        new_matches.append(match - 1)
                        #print("{} Adding new_clue={}, new_match={}".format(soln_so_far, clue[1:], match-1))
                    else:
                        good_match = False
                        break
                else:
                    if match < clue_depth:
                        new_clues.append(clue[1:])
                        new_matches.append(match)
                        #print("{} Adding new_clue={}, new_match={}".format(soln_so_far, clue[1:], match))
                    else:
                        good_match = False
                        break

            if good_match:
                for solution in search(soln_so_far + [i], new_clues, new_matches):
                    yield [i] + solution


# Test case: solution = 42
if False:
    clues = []              # 42  2 correct
    clues.append([ 4, 2 ])  # 42  2 correct
    clues.append([ 9, 4 ])  # 94  0 correct
    clues.append([ 5, 8 ])  # 58  0 correct
    clues.append([ 0, 9 ])  # 09  0 correct
    clues.append([ 4, 5 ])  # 45  1 correct
    clues.append([ 3, 1 ])  # 31  0 correct
    matches = [ 2, 0, 0, 0, 1, 0 ]


# Test case: solution = 39542
elif False:
    clues = []                       # 39542  5 correct
    clues.append([ 9, 0, 3, 4, 2 ])  # 90342  2 correct
    clues.append([ 7, 0, 7, 9, 4 ])  # 70794  0 correct
    clues.append([ 3, 9, 4, 5, 8 ])  # 39458  2 correct
    clues.append([ 3, 4, 1, 0, 9 ])  # 34109  1 correct
    clues.append([ 5, 1, 5, 4, 5 ])  # 51545  2 correct
    clues.append([ 1, 2, 5, 3, 1 ])  # 12531  1 correct
    matches = [ 2, 0, 2, 1, 2, 1 ]


# Test case: solution = 12345678
elif False:
    clues = []                                #  12345678  8 correct
    clues.append([ 1, 1, 1, 1, 1, 1, 1, 1 ])  #  11111111  1 correct
    clues.append([ 1, 2, 2, 2, 2, 2, 2, 2 ])  #  12222222  2 correct
    clues.append([ 1, 2, 3, 3, 3, 3, 3, 3 ])  #  12333333  3 correct
    clues.append([ 1, 2, 3, 4, 4, 4, 4, 4 ])  #  12344444  4 correct
    clues.append([ 1, 2, 3, 4, 5, 5, 5, 5 ])  #  12345555  5 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 6, 6 ])  #  12345666  6 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 7, 7 ])  #  12345677  7 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 7, 8 ])  #  12345678  8 correct
    matches = [ 1, 2, 3, 4, 5, 6, 7, 8 ]


# Test case: solution = 12345678, many other solutions
elif False:
    clues = []                                #  12345678  8 correct
    clues.append([ 1, 1, 1, 1, 1, 1, 1, 1 ])  #  11111111  1 correct
    clues.append([ 2, 2, 2, 2, 2, 2, 2, 2 ])  #  22222222  1 correct
    clues.append([ 3, 3, 3, 3, 3, 3, 3, 3 ])  #  33333333  1 correct
    clues.append([ 4, 4, 4, 4, 4, 4, 4, 4 ])  #  44444444  1 correct
    clues.append([ 5, 5, 5, 5, 5, 5, 5, 5 ])  #  55555555  1 correct
    clues.append([ 6, 6, 6, 6, 5, 6, 6, 6 ])  #  66665666  2 correct
    clues.append([ 7, 7, 7, 7, 5, 6, 7, 7 ])  #  77775677  3 correct
    clues.append([ 8, 8, 8, 8, 5, 6, 7, 8 ])  #  88885678  4 correct
    matches = [ 1, 1, 1, 1, 1, 2, 3, 4 ]


# Test case: solution = 1234567890
elif False:
    clues = []                                      #  1234567890  10 correct
    clues.append([ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ])  #  1111111111   1 correct
    clues.append([ 1, 2, 2, 2, 2, 2, 2, 2, 2, 2 ])  #  1222222222   2 correct
    clues.append([ 1, 2, 3, 3, 3, 3, 3, 3, 3, 3 ])  #  1233333333   3 correct
    clues.append([ 1, 2, 3, 4, 4, 4, 4, 4, 4, 4 ])  #  1234444444   4 correct
    clues.append([ 1, 2, 3, 4, 5, 5, 5, 5, 5, 5 ])  #  1234555555   5 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 6, 6, 6, 6 ])  #  1234566666   6 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 7, 7, 7, 7 ])  #  1234567777   7 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 7, 8, 8, 8 ])  #  1234567888   8 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 9 ])  #  1234567899   9 correct
    clues.append([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ])  #  1234567890  10 correct
    matches = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]


# The real problem:
elif True:
    clues = []
    clues.append([ 5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3 ])  # 5616185650518293  2 correct
    clues.append([ 3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7 ])  # 3847439647293047  1 correct
    clues.append([ 5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7 ])  # 5855462940810587  3 correct
    clues.append([ 9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3 ])  # 9742855507068353  3 correct
    clues.append([ 4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3 ])  # 4296849643607543  3 correct
    clues.append([ 3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8 ])  # 3174248439465858  1 correct
    clues.append([ 4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7 ])  # 4513559094146117  2 correct
    clues.append([ 7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7 ])  # 7890971548908067  3 correct
    clues.append([ 8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3 ])  # 8157356344118483  1 correct
    clues.append([ 2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9 ])  # 2615250744386899  2 correct
    clues.append([ 8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4 ])  # 8690095851526254  3 correct
    clues.append([ 6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0 ])  # 6375711915077050  1 correct
    clues.append([ 6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0 ])  # 6913859173121360  1 correct
    clues.append([ 6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8 ])  # 6442889055042768  2 correct
    clues.append([ 2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5 ])  # 2321386104303845  0 correct
    clues.append([ 2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8 ])  # 2326509471271448  2 correct
    clues.append([ 5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2 ])  # 5251583379644322  2 correct
    clues.append([ 1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6 ])  # 1748270476758276  3 correct
    clues.append([ 4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6 ])  # 4895722652190306  1 correct
    clues.append([ 3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5 ])  # 3041631117224635  3 correct
    clues.append([ 1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9 ])  # 1841236454324589  3 correct
    clues.append([ 2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7 ])  # 2659862637316867  2 correct
    matches = [ 2, 1, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 0, 2, 2, 3, 1, 3, 3, 2 ]

    lclues = []
    rclues = []
    for clue in clues:
        lclues.append(clue[:8])
        rclues.append(clue[8:])

lclues = []
rclues = []
divide_point = len(clues[0])/2
for clue in clues:
    lclues.append(clue[:divide_point])
    rclues.append(clue[divide_point:])

#print("lclues = {}".format(lclues))
#print("rclues = {}".format(rclues))

loops = 0
for (lmatches, rmatches) in divide(matches):
    loops += 1
    if (loops % 1000) == 0:
        print("<<loops={} lmatches={}, rmatches={}>>".format(loops, lmatches, rmatches))

    lsolutions = []
    for l in search([], lclues, lmatches):
        lsolutions.append(l)
        #print("Left soution = {}".format(l))
        if len(lsolutions) > 1:
            break

    if len(lsolutions) == 1:
        print("Found lsolution={} with lmatches={}, rmatches={}".format(lsolutions[0], lmatches, rmatches))
        rsolutions = []
        for r in search([], rclues, rmatches):
            rsolutions.append(r)
            print("Left soution = {}".format(r))

            if len(rsolutions) == 1:
                print("Matching left and right solutions found = {}".format(lsolutions[0] + rsolutions[0]))
                now_time = time.clock()
                print "Total time taken =", now_time - start_time
                sys.exit()

#print "clues =", clues
#print "len(clues) =", len(clues)
#print "clues[0] =", clues[0]
#print "len(clues[0]) =", len(clues[0])
#print "clues[0][0] =", clues[0][0]
#print "clues[0][1] =", clues[0][1]


now_time = time.clock()
print "Total time taken =", now_time - start_time
sys.exit()



#     5616 1.56 5051 8293  2 correct
#     3847 4396 4729 .0.7  1 correct
#     5855 4629 4081 0587  3 correct
#     9742 8555 .706 8353  3 correct
#     4296 8496 436. 75.3  3 correct
#     3174 2484 3946 5.58  1 correct
#     4513 5590 9.14 6117  2 correct
#     7890 9715 489. 8067  3 correct
#     8157 .563 4.11 8483  1 correct
#     .615 2507 4..8 6.99  2 correct
#     8690 0958 5152 6254  3 correct
#     6.75 7119 1507 7050  1 correct
#     6913 859. 7312 1360  1 correct
#     6442 8.90 5504 2768  2 correct
#     .... .... .... ....  0 correct
#     ...6 5094 7127 14.8  2 correct
#     525. 5.33 7964 4322  2 correct
#     1748 2704 7675 8276  3 correct
#     4895 7226 5219 0306  1 correct
#     304. 631. 1722 463.  3 correct
#     184. 23.4 5..2 4589  3 correct
#     .659 8626 37.1 6.67  2 correct

# Used at least once
#     .0.0 0000 .00. 0000
#     111. 111. 1111 111.
#     .2.2 222. .222 2222
#     3..3 .333 33.. .333
#     4444 44.4 4.44 44.4
#     5555 5555 5555 555.
#     66.6 66.6 .666 6666
#     7777 77.7 7777 7777
#     88.8 8.88 .888 8.88
#     9999 9999 9999 ..99
#
#     8959 9978 6998 8898
# = 263,303,591,362,560 possibilities
#
# reduction in search space
# 0.3240 * 0.4536 * 0.3888 * 0.4608
# = 0.0263

# But we can't eliminate the 9's, because the solution could
# still use the missing number and be unambiguous!




#     5616 1.56 5051 8293  2 correct
#     3847 4396 4729 .0.7  1 correct
#     5855 4629 4081 0587  3 correct
#     9742 8555 .706 8353  3 correct
#     4296 8496 436. 75.3  3 correct
#     3174 2484 3946 5.58  1 correct
#     4513 5590 9.14 6117  2 correct
#     7890 9715 489. 8067  3 correct
#     8157 .563 4.11 8483  1 correct
#     .615 2507 4..8 6.99  2 correct
#     8690 0958 5152 6254  3 correct
#     6.75 7119 1507 7050  1 correct
#     6913 859. 7312 1360  1 correct
#     6442 8.90 5504 2768  2 correct
#     .... .... .... ....  0 correct
#     ...6 5094 7127 14.8  2 correct
#     525. 5.33 7964 4322  2 correct
#     1748 2704 7675 8276  3 correct
#     4895 7226 5219 0306  1 correct
#     304. 631. 1722 463.  3 correct
#     184. 23.4 5..2 4589  3 correct
#     .659 8626 37.1 6.67  2 correct

#     2321 3861 0430 3845  0 correct



#     5616 1856 5051 8293  2 correct A
#     3847 4396 4729 3047  1 correct B
#     5855 4629 4081 0587  3 correct C
#     9742 8555 0706 8353  3 correct D
#     4296 8496 4360 7543  3 correct E
#     3174 2484 3946 5858  1 correct F
#     4513 5590 9414 6117  2 correct G
#     7890 9715 4890 8067  3 correct H
#     8157 3563 4411 8483  1 correct I
#     2615 2507 4438 6899  2 correct J
#     8690 0958 5152 6254  3 correct K
#     6375 7119 1507 7050  1 correct L
#     6913 8591 7312 1360  1 correct M
#     6442 8890 5504 2768  2 correct N
#     2321 3861 0430 3845  0 correct O
#     2326 5094 7127 1448  2 correct P
#     5251 5833 7964 4322  2 correct Q
#     1748 2704 7675 8276  3 correct R
#     4895 7226 5219 0306  1 correct S
#     3041 6311 1722 4635  3 correct T
#     1841 2364 5432 4589  3 correct U
#     2659 8626 3731 6867  2 correct V


#     2321 3861 0430 3845  0 correct O

#     3847 4396 4729 3047  1 correct B
#     3174 2484 3946 5858  1 correct F
#     8157 3563 4411 8483  1 correct I
#     6375 7119 1507 7050  1 correct L
#     6913 8591 7312 1360  1 correct M
#     4895 7226 5219 0306  1 correct S

#     5616 1856 5051 8293  2 correct A
#     4513 5590 9414 6117  2 correct G
#     2615 2507 4438 6899  2 correct J
#     6442 8890 5504 2768  2 correct N
#     2326 5094 7127 1448  2 correct P
#     5251 5833 7964 4322  2 correct Q
#     2659 8626 3731 6867  2 correct V

#     5855 4629 4081 0587  3 correct C
#     9742 8555 0706 8353  3 correct D
#     4296 8496 4360 7543  3 correct E
#     7890 9715 4890 8067  3 correct H
#     8690 0958 5152 6254  3 correct K
#     1748 2704 7675 8276  3 correct R
#     3041 6311 1722 4635  3 correct T
#     1841 2364 5432 4589  3 correct U

##Comparisons
#     3847 4396 4729 3047  1 correct B
#     3174 2484 3946 5858  1 correct F
      |

#     3847 4396 4729 3047  1 correct B
#     8157 3563 4411 8483  1 correct I
         |      |

#     3847 4396 4729 3047  1 correct B
#     6375 7119 1507 7050  1 correct L
                      |

#     3847 4396 4729 3047  1 correct B
#     6913 8591 7312 1360  1 correct M
             |

#     3847 4396 4729 3047  1 correct B
#     4895 7226 5219 0306  1 correct S
       |      |    |

#     3174 2484 3946 5858  1 correct F
#     8157 3563 4411 8483  1 correct I
       |

#     3174 2484 3946 5858  1 correct F
#     6375 7119 1507 7050  1 correct L
        |

#     3174 2484 3946 5858  1 correct F
#     6913 8591 7312 1360  1 correct M


#     3174 2484 3946 5858  1 correct F
#     4895 7226 5219 0306  1 correct S


#     8157 3563 4411 8483  1 correct I
#     6375 7119 1507 7050  1 correct L


#     8157 3563 4411 8483  1 correct I
#     6913 8591 7312 1360  1 correct M
            |     |

#     8157 3563 4411 8483  1 correct I
#     4895 7226 5219 0306  1 correct S
                  |

#     6375 7119 1507 7050  1 correct L
#     6913 8591 7312 1360  1 correct M
      |                 |

#     6375 7119 1507 7050  1 correct L
#     4895 7226 5219 0306  1 correct S
         | |

#     6913 8591 7312 1360  1 correct M
#     4895 7226 5219 0306  1 correct S
                  |   |

#     8157 3563 4411 8483  1 correct I
#     6913 8591 7312 1360  1 correct M
#     4895 7226 5219 0306  1 correct S
#     4513 5590 9414 6117  2 correct G
                  |
