#!/usr/bin/python
#
# Project Euler.net Problem 103
#
# Let S(A) represent the sum of elements in set A of size n. We shall
# call it a special sum set if for any two non-empty disjoint subsets,
# B and C, the following properties are true:
#
#    1. S(B) != S(C); that is, sums of subsets cannot be equal.
#    2. If B contains more elements than C then S(B) > S(C).
#
# If S(A) is minimised for a given n, we shall call it an optimum
# special sum set. The first five optimum special sum sets are given
# below.
#
#     n = 1: {1}
#     n = 2: {1, 2}
#     n = 3: {2, 3, 4}
#     n = 4: {3, 5, 6, 7}
#     n = 5: {6, 9, 11, 12, 13}
#
# It seems that for a given optimum set, A = {a_(1), a_(2), ... ,
# a_(n)}, the next optimum set is of the form B = {b, a_(1)+b,
# a_(2)+b, ... ,a_(n)+b}, where b is the "middle" element on the
# previous row.
#
# By applying this "rule" we would expect the optimum set for n = 6 to
# be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is
# not the optimum set, as we have merely applied an algorithm to
# provide a near optimum set. The optimum set for n = 6 is A = {11,
# 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string:
# 111819202225.
#
# Given that A is an optimum special sum set for n = 7, find its set string.
#
# NOTE: This problem is related to problems 105 and 106.
#
# Solved: 09/09/13
# 186 problems solved
# Position #222 on level 7

import sys
import itertools
import time

TEST0 = False
TEST1 = False
TEST2 = False
TEST3 = False
TEST4 = False

start_time = time.clock()

########################################
def valid_set(sA):
    lA = len(sA)

    for i in range(1, (lA-1)/2):
        if sum(sA[:i+1]) <= sum(sA[-i:]):
            return False

    for x in itertools.product('ABC', repeat=lA):
        (lB,lC) = (0,0)    # Length of the sub-sets
        (tB,tC) = (0,0)    # Total of the sub-sets
        (sB,sC) = ([],[])  # The actual sub-set themselves
        # A means don't use this item
        # B means put this item in the first sub-set
        # C means put this item in the second sub-set
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
            #print "    Fail", sB, sC
            return False
    return True


########################################
def set_string(s):
    s_string = ''
    for n in s:
        s_string = s_string + "{}".format(n)
    return s_string


########################################
def generate_sets(size, total, front, back):
    #print "generate_sets({}, {}, {}, {})".format(size, total, front, back)
    # yield a set that has size elements, sum total, is a valid set by itself,
    # is a valid set when prepended by front, and is a valid set when postpended by back

    if (size == 1):
        if ((len(front) > 0) and (total <= front[-1])):
            return
        if ((len(back) > 0) and (total >= back[0])):
            return
        yield [total]

    elif (len(front) <= len(back)):
        # add an element to the front of the set

        # must be greater than previous number in set
        if (len(front) > 0):
            min_f = front[-1]+1
        else:
            min_f = 1

        # sum(front) + f must be must be greater than sum(back)
        if (len(front) > 0):
            min_f = max(min_f, sum(back) - sum(front) + 1)

        # will exceed total if bigger than this
        climb = size*(size-1)/2
        max_f = (total-climb)/size

        if (len(back) > 0):
            max_f = min(max_f, back[0]-1)

        if (len(back) > 0):
            min_f = max(min_f, back[-1]+1-front[0])  # front[0] + f must be greater than back[-1]

        for f in range(min_f, max_f+1):
            for mid in generate_sets(size-1, total-f, front + [f], back):
                yield [f] + mid

    else:
        # add an element to the back of the set

        # must be greater than previous number in set
        min_b = front[-1]+size

        # will exceed total if bigger than this
        climb = size*(size-1)/2
        climb += (size-1)*front[-1]  # climb is the smallest the numbers before back can be
        max_b = (total-climb)

        if (len(back) > 0):
            max_b = min(max_b, back[0]-1)

        for b in range(min_b, max_b+1):
            for mid in generate_sets(size-1, total-b, front, [b] + back):
                yield mid + [b]



########################################
if TEST0:
    should_fail = [42, 65, 75, 81, 84, 86, 87, 88]
    should_pass = [79, 119, 139, 150, 157, 158, 159, 161, 164]
    A3best = [2, 3, 4]
    A4best = [3, 5, 6, 7]
    A5best = [6, 9, 11, 12, 13]
    A6init = [ 11, 17, 20, 22, 23, 24 ]
    A6best = [ 11, 18, 19, 20, 22, 25 ]
    A6bad  = [ 11, 17, 19, 20, 22, 25 ]
    A7init = [ 20, 20+11, 20+18, 20+19, 20+20, 20+22, 20+25 ]

    for this in [should_fail, should_pass,
                 A3best, A4best, A5best,
                 A6init, A6best, A6bad, A7init,
                 A7init[:5], A7init[:4], A7init[:3], A7init[:2],
                 A7init[1:], A7init[2:], A7init[3:], A7init[4:], A7init[5:]]:
        if valid_set(this):
            print "{} is a valid set, len = {}, sum = {}".format(this, len(this), sum(this))
        else:
            print "NOT a valid set {}, len = {}, sum = {}".format(this, len(this), sum(this))

    end_time = time.clock()
    print "Run time =", end_time - start_time, "seconds"
    sys.exit(0)

# Should generate the following output...
#
# NOT a valid set [42, 65, 75, 81, 84, 86, 87, 88], len = 8, sum = 608
# [79, 119, 139, 150, 157, 158, 159, 161, 164] is a valid set, len = 9, sum = 1286
# [2, 3, 4] is a valid set, len = 3, sum = 9
# [3, 5, 6, 7] is a valid set, len = 4, sum = 21
# [6, 9, 11, 12, 13] is a valid set, len = 5, sum = 51
# [11, 17, 20, 22, 23, 24] is a valid set, len = 6, sum = 117
# [11, 18, 19, 20, 22, 25] is a valid set, len = 6, sum = 115
# NOT a valid set [11, 17, 19, 20, 22, 25], len = 6, sum = 114
# [20, 31, 38, 39, 40, 42, 45] is a valid set, len = 7, sum = 255
# [20, 31, 38, 39, 40] is a valid set, len = 5, sum = 168
# [20, 31, 38, 39] is a valid set, len = 4, sum = 128
# [20, 31, 38] is a valid set, len = 3, sum = 89
# [20, 31] is a valid set, len = 2, sum = 51
# [31, 38, 39, 40, 42, 45] is a valid set, len = 6, sum = 235
# [38, 39, 40, 42, 45] is a valid set, len = 5, sum = 204
# [39, 40, 42, 45] is a valid set, len = 4, sum = 166
# [40, 42, 45] is a valid set, len = 3, sum = 127
# [42, 45] is a valid set, len = 2, sum = 87


########################################
if TEST1:
    print "A3best = [2, 3, 4]"
    count = 0
    for s in generate_sets(3, 9, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        else:
            print "{} not valid".format(s)
    print "Checked {} sets for validity".format(count)
    print


    print "A4best = [3, 5, 6, 7]"
    count = 0
    for s in generate_sets(4, 21, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        else:
            print "{} not valid".format(s)
    print "Checked {} sets for validity".format(count)
    print


    print "A5best =  [6, 9, 11, 12, 13]"
    count = 0
    for s in generate_sets(5, 51, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        else:
            print "{} not valid".format(s)
    print "Checked {} sets for validity".format(count)
    print


    print "A6init =  [ 11, 17, 20, 22, 23, 24 ]"
    count = 0
    for s in generate_sets(6, 117, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        else:
            print "{} not valid".format(s)
    print "Checked {} sets for validity".format(count)
    print


    end_time = time.clock()
    print "Run time =", end_time - start_time, "seconds"
    sys.exit(0)


########################################
if TEST2:
    print "A6best = [ 11, 18, 19, 20, 22, 25 ]"
    count = 0
    for s in generate_sets(6, 115, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        #else:
        #    print "{}".format(s)
    print "Checked {} sets for validity".format(count)
    print

    end_time = time.clock()
    print "Run time =", end_time - start_time, "seconds"
    sys.exit(0)


########################################
if TEST3:
    print "should find A7bad1 = [23, 40, 41, 42, 44, 47, 54]"
    count = 0
    for s in generate_sets(7, 291, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        #else:
        #    print "{}".format(s)
    print "Checked {} sets for validity".format(count)
    print

    print "should find A7bad2 = [23, 34, 41, 44, 46, 47, 48]"
    count = 0
    for s in generate_sets(7, 283, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        #else:
        #    print "{}".format(s)
    print "Checked {} sets for validity".format(count)
    print

    end_time = time.clock()
    print "Run time =", end_time - start_time, "seconds"
    sys.exit(0)


########################################
if TEST4:
    count = 0
    print "should find optimum solution = [20, 31, 38, 39, 40, 42, 45]"
    for s in generate_sets(7, 255, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        #else:
        #    print "{}".format(s)
    print "Checked {} sets for validity".format(count)
    print

    end_time = time.clock()
    print "Run time =", end_time - start_time, "seconds"
    sys.exit(0)


########################################
for best in range(255, 250, -1):
#for best in range(250, 225, -1):
#for best in range(225, 200, -1):
#for best in range(200, 175, -1):
#for best in range(175, 150, -1):
#for best in range(150, 100, -1):
    print "looking for solutions with best = {}".format(best)
    count = 0
    for s in generate_sets(7, best, [], []):
        count += 1
        if (valid_set(s)):
            print "{} is Valid, sum = {}, set string = {}".format(s, sum(s), set_string(s))
        #else:
        #    print "{}".format(s)
    print "Checked {} sets for validity".format(count)
    print


########################################
end_time = time.clock()
print "Run time =", end_time - start_time, "seconds"
