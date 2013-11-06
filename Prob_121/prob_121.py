#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 121
# 
# A bag contains one red disc and one blue disc. In a game of chance a
# player takes a disc at random and its colour is noted. After each
# turn the disc is returned to the bag, an extra red disc is added,
# and another disc is taken at random.
# 
# The player pays �1 to play and wins if they have taken more blue
# discs than red discs at the end of the game.
# 
# If the game is played for four turns, the probability of a player
# winning is exactly 11/120, and so the maximum prize fund the banker
# should allocate for winning in this game would be �10 before they
# would expect to incur a loss. Note that any payout will be a whole
# number of pounds and also includes the original �1 paid to play the
# game, so in the example given the player actually wins �9.
# 
# Find the maximum prize fund that should be allocated to a single
# game in which fifteen turns are played.
#
# Solved 09/11/10
# 125 problems solved
# Position #568 on level 3

############################################################
#
# To pick blue 3 times in 4 turns we need
# P(b, b, b, *) = 1/2 * 2/3 * 1/2 * 2/3 * 1/2 * 3/3 * 2/2 = 24/432 = 1/18
# P(b, b, r, b) = 1/2 * 2/3 * 1/2 * 2/3 * 1/2 * 2/3 * 1/2 =  8/432 = 1/54
# P(b, r, b, b) = 1/2 * 2/3 * 1/2 * 2/3 * 1/2 * 2/3 * 1/2 =  8/432 = 1/54
# P(r, b, b, b) = 1/2 * 2/3 * 1/2 * 2/3 * 1/2 * 2/3 * 1/2 =  8/432 = 1/54
# P(winning) = 48/432 = 1/9
#
# ???What is wrong with this???
# 

############################################################
#
# Turn 1: 1 red, 1 blue, p(b) = 1/2
# Turn 2: 2 red, 1 blue, p(b) = 1/3
# Turn 3: 3 red, 1 blue, p(b) = 1/4
# Turn 4: 4 red, 1 blue, p(b) = 1/5
#
# P(b, b, b, b) = 1/2 * 1/3 * 1/4 * 1/5 = 1/120
# P(b, b, b, r) = 1/2 * 1/3 * 1/4 * 4/5 = 4/120
# P(b, b, r, b) = 1/2 * 1/3 * 3/4 * 1/5 = 3/120
# P(b, r, b, b) = 1/2 * 1/3 * 3/4 * 1/5 = 2/120
# P(r, b, b, b) = 1/2 * 1/3 * 3/4 * 1/5 = 1/120
# P(winning) = 11/120
#
# With a prize of 10, the payoff for a loss is 1, and for a win is -9.
# Bankers return = (1 * 109/120) - (9 * 11/120) = 10/120

############################################################
#
# Turn  1:  1 red, 1 blue, p(b) = 1/2
# Turn  2:  2 red, 1 blue, p(b) = 1/3
# ...
# Turn 14: 14 red, 1 blue, p(b) = 1/15
# Turn 15: 15 red, 1 blue, p(b) = 1/16
#
# P(b, b, b, b) = 1/2 * 1/3 * ... * 1/15 *  1/16 =  1/(2*3*...*14*16)
# P(b, b, b, r) = 1/2 * 1/3 * ... * 1/15 * 15/16 = 15/(2*3*...*14*16)
# etc...

MAX = 15

div = 1
for n in range(2,MAX+2):
    div *= n
print "Divisor =", div

for n in range(MAX):
    print "b{0:-2}".format(n),
print

for n in range(MAX):
    print "---",
print

odds = 0
for i in range(2**MAX):
    rcnt = 0
    iodds = 1
    ii = i
    for n in range(MAX):
        if (ii % 2) == 1:
            #print " b ",
            rcnt += 1
            iodds *= 1
        else:
            #print " r ",
            iodds *= (n+2 - 1)
        ii /= 2
    #print "P = {0}/{1}".format(odds, div),
    if rcnt > MAX/2:
        #print "Winner"
        odds += iodds
    #else:  print

#print "Overall odds of winning are {0}/{1}".format(odds,div)

# Bankers return = (1 * 109/120) - (9 * 11/120) = 10/120
# If
#     (1 * (div-odds)/div) - (payoff * odds/div) = 0
#     (div-odds) = payoff * odds
#     payoff = (div-odds)/odds
payoff = (div-odds)/odds
print "Answer =", payoff+1
