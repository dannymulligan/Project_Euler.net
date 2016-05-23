#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 336
#
# Maximix Arrangements
#
# A train is used to transport four carriages in the order:
# ABCD. However, sometimes when the train arrives to collect the
# carriages they are not in the correct order.

# To rearrange the carriages they are all shunted on to a large
# rotating turntable. After the carriages are uncoupled at a specific
# point the train moves off the turntable pulling the carriages still
# attached with it. The remaining carriages are rotated 180
# degrees. All of the carriages are then rejoined and this process is
# repeated as often as necessary in order to obtain the least number
# of uses of the turntable.
#
# Some arrangements, such as ADCB, can be solved easily: the carriages
# are separated between A and D, and after DCB are rotated the correct
# order has been achieved.
#
# However, Simple Simon, the train driver, is not known for his
# efficiency, so he always solves the problem by initially getting
# carriage A in the correct place, then carriage B, and so on.
#
# Using four carriages, the worst possible arrangements for Simon,
# which we shall call maximix arrangements, are DACB and DBAC; each
# requiring him five rotations (although, using the most efficient
# approach, they could be solved using just three rotations). The
# process he uses for DACB is shown below.
#
#     Train --- D -|- A --- C --- B
#     Train -|- D --- B --- C --- A
#     Train --- A --- C -|- B --- D
#     Train --- A -|- C --- D --- B
#     Train --- A --- B -|- D --- C
#     Train --- A --- B --- C --- D
#
# It can be verified that there are 24 maximix arrangements for six
# carriages, of which the tenth lexicographic maximix arrangement is
# DFAECB.
#
# Find the 2011th lexicographic maximix arrangement for eleven
# carriages.

import itertools
import sys
import time
start_time = time.clock()

################################################################################
SIZE = 6
GOAL = 10
SIZE = 11
GOAL = 2011


################################################################################
def to_ascii(perm):
    """Convert a carriage permutation to a printable form"""
    ans = ""
    for i in perm:
        ans += chr(i+ord('A'))
    return ans


################################################################################
def swaps(perm):
    """Calculate the number of swaps needed to fix the order of the carriages
    using the 'simple' method"""
    ans = 0
    plen = len(perm)
    #print("plen={}".format(plen))
    for i in range(plen-1):

        if perm[i] == i:
            # Swap not needed
            # By definition this can't be a maximix arrangement, so stop looking
            return 0

        # Swap is needed, search for the next item
        for j in range(i+1, plen-1):
            if perm[j] == i:
                for k in range(j, j+(plen-j)//2):
                    perm[k], perm[plen-k+j-1] = perm[plen-k+j-1], perm[k]
                ans += 1

        # Swap is needed, swap next item into correct place
        for k in range(i, i+(plen-i)//2):
            perm[k], perm[plen-k+i-1] = perm[plen-k+i-1], perm[k]
        ans += 1

    return ans


################################################################################
print("Running with SIZE = {} and GOAL = {}".format(SIZE, GOAL))

carriages = [x for x in range(SIZE)]

maxi_size = (SIZE-2)*2+1
maxi_count = 0

for cnt, p in enumerate(itertools.permutations(carriages)):
    #print("Processing {}, {}".format(p, to_ascii(p)))

    p_swaps = swaps(list(p))
    if p_swaps == maxi_size:
        maxi_count += 1
        if (maxi_count % 100) == 0:
            print("Working on {} = {}".format(p, to_ascii(p)), end='')
            print("    cnt={}, p_swaps={}, maxi_count={}".format(cnt, p_swaps, maxi_count))
        if maxi_count == GOAL:
            print("Found {} = {}".format(p, to_ascii(p)), end='')
            print("    cnt={}, p_swaps={}, maxi_count={}".format(cnt, p_swaps, maxi_count))
            print("Time taken = {0} seconds".format(time.clock() - start_time))
            sys.exit(0)


print("{} permutations examined without finding {} maximix".format(cnt, GOAL))

print("Time taken = {0} seconds".format(time.clock() - start_time))
