#!/usr/bin/python
#
# Project Euler.net Problem 86
#
# In the game, Monopoly, the standard board is set up in the following
# way:
#
#     GO    A1   CC1  A2   T1   R1   B1   CH1  B2   B3   JAIL
#     H2                                                 C1
#     T2                                                 U1
#     H1                                                 C2
#     CH3                                                C3
#     R4                                                 R2
#     G3                                                 D1
#     CC3                                                CC2
#     G2                                                 D2
#     G1                                                 D3
#     G2J   F3   U2   F2   F1   R3   E3   E2   CH2  E1   FP
# 
# A player starts on the GO square and adds the scores on two 6-sided
# dice to determine the number of squares they advance in a clockwise
# direction. Without any further rules we would expect to visit each
# square with equal probability: 2.5%. However, landing on G2J (Go To
# Jail), CC (community chest), and CH (chance) changes this
# distribution.
# 
# In addition to G2J, and one card from each of CC and CH, that orders
# the player to go directly to jail, if a player rolls three
# consecutive doubles, they do not advance the result of their 3rd
# roll. Instead they proceed directly to jail.
# 
# At the beginning of the game, the CC and CH cards are shuffled. When
# a player lands on CC or CH they take a card from the top of the
# respective pile and, after following the instructions, it is
# returned to the bottom of the pile. There are sixteen cards in each
# pile, but for the purpose of this problem we are only concerned with
# cards that order a movement; any instruction not concerned with
# movement will be ignored and the player will remain on the CC/CH
# square.
# 
#     * Community Chest (2/16 cards):
#          1. Advance to GO
#          2. Go to JAIL
#     * Chance (10/16 cards):
#          1. Advance to GO
#          2. Go to JAIL
#          3. Go to C1
#          4. Go to E3
#          5. Go to H2
#          6. Go to R1
#          7. Go to next R (railway company)
#          8. Go to next R
#          9. Go to next U (utility company)
#         10. Go back 3 squares.
# 
# The heart of this problem concerns the likelihood of visiting a
# particular square. That is, the probability of finishing at that
# square after a roll. For this reason it should be clear that, with
# the exception of G2J for which the probability of finishing on it is
# zero, the CH squares will have the lowest probabilities, as 5/8
# request a movement to another square, and it is the final square
# that the player finishes at on each roll that we are interested
# in. We shall make no distinction between "Just Visiting" and being
# sent to JAIL, and we shall also ignore the rule about requiring a
# double to "get out of jail", assuming that they pay to get out on
# their next turn.
# 
# By starting at GO and numbering the squares sequentially from 00 to
# 39 we can concatenate these two-digit numbers to produce strings
# that correspond with sets of squares.
# 
# Statistically it can be shown that the three most popular squares,
# in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and
# GO (3.09%) = Square 00. So these three most popular squares can be
# listed with the six-digit modal string: 102400.
# 
# If, instead of using two 6-sided dice, two 4-sided dice are used,
# find the six-digit modal string.
#
# Answer: 101524
# Solved 11/6/09
# 97 problems solved
# Position #31 on level 2

#  00 - GO
#  01 - A1
#  02 - CC1  Community chest
#  03 - A2
#  04 - T1
#  05 - R1   Railway
#  06 - B1
#  07 - CH1  Chance
#  08 - B2
#  09 - B3
#  10 - JAIL
#  11 - C1
#  12 - U1   Utility
#  13 - C2
#  14 - C3
#  15 - R2   Railway
#  16 - D1
#  17 - CC2  Community chest
#  18 - D2
#  19 - D3
#  20 - FP
#  21 - E1
#  22 - CH2  Chance
#  23 - E2
#  24 - E3
#  25 - R3   Railway
#  26 - F1
#  27 - F2
#  28 - U2   Utility
#  29 - F3
#  30 - G2J  Go to jail
#  31 - G1 
#  32 - G2 
#  33 - CC3  Community chest
#  34 - G3 
#  35 - R4   Railway
#  36 - CH3  Chance
#  37 - H1 
#  38 - T2 
#  39 - H2 


import random

ITER_MAX = 5000000

CC_cards = ['A2G', 'G2J', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo']
random.shuffle(CC_cards)
CC_ptr = 0

CH_cards = ['A2G', 'G2J', 'G2C1', 'G2E3', 'G2H2', 'G2R1', 'G2R', 'G2R', 'G2U', 'GB3', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
random.shuffle(CH_cards)
CH_ptr = 0

hist = [0] * 40
pos = 0
dcount = 0
for i in range(ITER_MAX):
    if ((i % 100000) == 0):
        print i

    # Roll the dice
    d1 = random.randint(1,4)  # use (1,4) for 4 sided die, (1,6) for six sided die
    d2 = random.randint(1,4)  # use (1,4) for 4 sided die, (1,6) for six sided die
    pos += (d1 + d2)
    if (pos >= 40):  pos -= 40

    # Check for 3 doubles in a row
    if (d1 == d2):
        if (dcount == 2):
            pos = 10  # Go to jail for 3 doubles
            dcount = 0
        else:
            dcount += 1
    else:
        dcount = 0

    # Chance
    if ((pos == 7) | (pos == 22) | (pos == 36)):
        if   (CH_cards[CH_ptr] == 'A2G'):   pos = 0   # Advance to GO
        elif (CH_cards[CH_ptr] == 'G2J'):   pos = 10  # Go to JAIL
        elif (CH_cards[CH_ptr] == 'G2C1'):  pos = 11  # Go to C1
        elif (CH_cards[CH_ptr] == 'G2E3'):  pos = 24  # Go to E3
        elif (CH_cards[CH_ptr] == 'G2H2'):  pos = 39  # Go to H2
        elif (CH_cards[CH_ptr] == 'G2R1'):  pos = 05  # Go to R1
        elif (CH_cards[CH_ptr] == 'G2R'):             # Go to next R (railway company)
            if   (pos < 5):   pos = 5
            elif (pos < 15):  pos = 15
            elif (pos < 25):  pos = 25
            elif (pos < 35):  pos = 35
            else:             pos = 5
        elif (CH_cards[CH_ptr] == 'G2U'):             # Go to next U (utility company)
            if   (pos < 12):  pos = 12
            elif (pos < 28):  pos = 28
            else:             pos = 12
        elif (CH_cards[CH_ptr] == 'Gb3'):   pos -= 3  # Go back 3 squares.

        CH_ptr += 1
        if (CH_ptr >= 16):  CH_ptr -= 16
        # Note, go back 3 spaces could result in also taking a CC card

    # Community Chest
    if ((pos == 2) | (pos == 17) | (pos == 33)):
        if   (CC_cards[CC_ptr] == 'A2G'):  pos = 0   # Advance to GO
        elif (CC_cards[CC_ptr] == 'G2J'):  pos = 10  # Go to JAIL

        CC_ptr += 1
        if (CC_ptr >= 16):  CC_ptr -= 16

    # Go to jail
    if (pos == 30):
        pos = 10

    # Update statistics
    hist[pos] = hist[pos] + 1

# Report result
max = 0
ans0 = -1
for i in range(40):
   if hist[i] > max:
        max = hist[i]
        ans0 = i
print ans0, 100.0*hist[ans0]/ITER_MAX
hist[ans0] = 0

max = 0
ans1 = -1
for i in range(40):
   if hist[i] > max:
        max = hist[i]
        ans1 = i
print ans1, 100.0*hist[ans1]/ITER_MAX
hist[ans1] = 0

max = 0
ans2 = -1
for i in range(40):
   if hist[i] > max:
        max = hist[i]
        ans2 = i
print ans2, 100.0*hist[ans2]/ITER_MAX

print "The answer is {0:02}{1:02}{2:02}".format(ans0, ans1, ans2)
