#!/usr/bin/python
#
# Project Euler.net Problem 109
#
# In the game of darts a player throws three darts at a target board
# which is split into twenty equal sized sections numbered one to
# twenty.
#
# The score of a dart is determined by the number of the region that
# the dart lands in. A dart landing outside the red/green outer ring
# scores zero. The black and cream regions inside this ring represent
# single scores. However, the red/green outer ring and middle ring
# score double and treble scores respectively.
#
# At the centre of the board are two concentric circles called the
# bull region, or bulls-eye. The outer bull is worth 25 points and the
# inner bull is a double, worth 50 points.
#
# There are many variations of rules but in the most popular game the
# players will begin with a score 301 or 501 and the first player to
# reduce their running total to zero is a winner. However, it is
# normal to play a "doubles out" system, which means that the player
# must land a double (including the double bulls-eye at the centre of
# the board) on their final dart to win; any other dart that would
# reduce their running total to one or lower means the score for that
# set of three darts is "bust".
#
# When a player is able to finish on their current score it is called
# a "checkout" and the highest checkout is 170: T20 T20 D25 (two
# treble 20s and double bull).
#
# There are exactly eleven distinct ways to checkout on a score of 6:
#
#     D3
#     D1    D2
#     S2    D2
#     D2    D1
#     S4    D1
#     S1    S1    D2
#     S1    T1    D1
#     S1    S3    D1
#     D1    D1    D1
#     D1    S2    D1
#     S2    S2    D1
#
# Note that D1 D2 is considered different to D2 D1 as they finish on
# different doubles. However, the combination S1 T1 D1 is considered
# the same as T1 S1 D1.
#
# In addition we shall not include misses in considering combinations;
# for example, D3 is the same as 0 D3 and 0 0 D3.
#
# Incredibly there are 42336 distinct ways of checking out in total.
#
# How many distinct ways can a player checkout with a score less than
# 100?
#
# Solved:
# ? problems solved
# Position #??? on level ?

import time
start_time = time.clock()

single = ['S1',  'S2',  'S3',  'S4',  'S5',  'S6',  'S7',  'S8',  'S9',  'S10',
          'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S25']
double = ['D1',  'D2',  'D3',  'D4',  'D5',  'D6',  'D7',  'D8',  'D9',  'D10',
          'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D25']
treble = ['T1',  'T2',  'T3',  'T4',  'T5',  'T6',  'T7',  'T8',  'T9',  'T10',
          'T11', 'T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20']

def score(dart):
    if (dart[0] == 'S'):
        return 1 * int(dart[1:])
    elif (dart[0] == 'D'):
        return 2 * int(dart[1:])
    elif (dart[0] == 'T'):
        return 3 * int(dart[1:])
    else:
        assert False, "First character in a dart should be S, D, or T"

# ways will count the ways of checking out for each score
ways = [0] * 171

# Single dart checkouts
for d1 in double:
    s1 = score(d1)
    s = s1
    #print "{:3}: {}".format(s, d1)
    ways[s] += 1

# Two dart checkouts
for d1 in double:
    s1 = score(d1)
    for d2 in single + double + treble:
        s2 = score(d2)
        s = s1 + s2
        #print "{:3}: {} {}".format(s, d2, d1)
        ways[s] += 1

# Three dart checkouts
for d1 in double:
    s1 = score(d1)
    for d2 in single + double + treble:
        s2 = score(d2)
        for d3 in single + double + treble:
            if (single + double + treble).index(d2) < (single + double + treble).index(d3):
                continue
            s3 = score(d3)
            s = s1 + s2 + s3
            #print "{:3}: {} {} {}".format(s, d3, d2, d1)
            ways[s] += 1

print "There are {} distinct ways of checking out on a score of {}".format(ways[6], 6)
print "There are {} distinct ways of checking out in total".format(sum(ways))
print "There are {} distinct ways of checking out on a score of less than {}".format(sum(ways[:100]), 100)

print "Time taken = {0} seconds".format(time.clock() - start_time)
