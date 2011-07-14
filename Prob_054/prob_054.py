#!/usr/bin/python
#
# Project Euler.net Problem 54
#
# In the card game poker, a hand consists of five cards and are
# ranked, from lowest to highest, in the following way:
# 
#     * High Card: Highest value card.
#     * One Pair: Two cards of the same value.
#     * Two Pairs: Two different pairs.
#     * Three of a Kind: Three cards of the same value.
#     * Straight: All cards are consecutive values.
#     * Flush: All cards of the same suit.
#     * Full House: Three of a kind and a pair.
#     * Four of a Kind: Four cards of the same value.
#     * Straight Flush: All cards are consecutive values of same suit.
#     * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# 
# The cards are valued in the order:
#     2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# 
# If two players have the same ranked hands then the rank made up of
# the highest value wins; for example, a pair of eights beats a pair
# of fives (see example 1 below). But if two ranks tie, for example,
# both players have a pair of queens, then highest cards in each hand
# are compared (see example 4 below); if the highest cards tie then
# the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
#     Hand    Player 1             Player 2              Winner
#      1      5H 5C 6S 7S KD       2C 3S 8S 8D TD        Player 2
#             Pair of Fives        Pair of Eights
#             
#      2      5D 8C 9S JS AC       2C 5C 7D 8S QH        Player 1
#             Highest card Ace     Highest card Queen
#             
#      3      2D 9C AS AH AC       3D 6D 7D TD QD        Player 2
#             Three Aces           Flush with Diamonds           
#             
#      4      4D 6S 9H QH QC       3D 6D 7H QD QS        Player 1
#             Pair of Queens       Pair of Queens    
#             Highest card Nine    Highest card Seven
# 
#      5      2H 2D 4C 4D 4S       3C 3D 3S 9S 9D        Player 1
#             Full House           Full House       
#             With Three Fours     with Three Threes
#
# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a
# single space): the first five are Player 1's cards and the last five
# are Player 2's cards. You can assume that all hands are valid (no
# invalid characters or repeated cards), each player's hand is in no
# specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?
#
# Wed 10/14/09
# This is my 77th problem solved
# I am ranked at position #382 in Level 2


#     1 = High Card: Highest value card.
#     2 = One Pair: Two cards of the same value.
#     3 = Two Pairs: Two different pairs.
#     4 = Three of a Kind: Three cards of the same value.
#     5 = Straight: All cards are consecutive values.
#     6 = Flush: All cards of the same suit.
#     7 = Full House: Three of a kind and a pair.
#     8 = Four of a Kind: Four cards of the same value.
#     9 = Straight Flush: All cards are consecutive values of same suit.
#    10 = Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
def eval_hand(hand):
    print hand,

    cards_suit = []
    cards_rank = []
    for card in hand:
        cards_suit.append(card[1])
        if   (card[0] == 'T'):  cards_rank.append(10)
        elif (card[0] == 'J'):  cards_rank.append(11)
        elif (card[0] == 'Q'):  cards_rank.append(12)
        elif (card[0] == 'K'):  cards_rank.append(13)
        elif (card[0] == 'A'):  cards_rank.append(14)
        else:                   cards_rank.append(int(card[0]))
    cards_rank.sort()

    high = True
    high_rank = max(cards_rank)

    flush = ((cards_suit == ['S']*5)
           | (cards_suit == ['H']*5)
           | (cards_suit == ['D']*5)
           | (cards_suit == ['C']*5))
    flush_rank = max(cards_rank)

    straight = False
    straight_rank = 0
    if ((cards_rank[0]+4) == (cards_rank[1]+3) == (cards_rank[2]+2) == (cards_rank[3]+1) == (cards_rank[4])):
        straight = True
        straight_rank = cards_rank[4]
        high_rank = max(cards_rank)

    full_house = False
    if ((cards_rank[0] == cards_rank[1] == cards_rank[2]) & (cards_rank[3] == cards_rank[4])):
        full_house = True
        full_house_rank = cards_rank[0]
        high_rank = cards_rank[3]
    if ((cards_rank[0] == cards_rank[1]) & (cards_rank[2] == cards_rank[3] == cards_rank[4])):
        full_house = True
        full_house_rank = cards_rank[2]
        high_rank = cards_rank[0]

    four_of_a_kind = False
    if (cards_rank[0] == cards_rank[1] == cards_rank[2] == cards_rank[3]):
        four_of_a_kind = True
        four_of_a_kind_rank = cards_rank[0]
        high_rank = cards_rank[4]
    if (cards_rank[1] == cards_rank[2] == cards_rank[3] == cards_rank[4]):
        four_of_a_kind = True
        four_of_a_kind_rank = cards_rank[1]
        high_rank = cards_rank[0]

    three_of_a_kind = False
    if (cards_rank[0] == cards_rank[1] == cards_rank[2]):
        three_of_a_kind = True
        three_of_a_kind_rank = cards_rank[0]
        high_rank = max(cards_rank[3], cards_rank[4])
    if (cards_rank[1] == cards_rank[2] == cards_rank[3]):
        three_of_a_kind = True
        three_of_a_kind_rank = cards_rank[1]
        high_rank = max(cards_rank[0], cards_rank[4])
    if (cards_rank[2] == cards_rank[3] == cards_rank[4]):
        three_of_a_kind = True
        three_of_a_kind_rank = cards_rank[2]
        high_rank = max(cards_rank[0], cards_rank[1])

    two_pair = False
    if ((cards_rank[0] == cards_rank[1]) & (cards_rank[2] == cards_rank[3])):
        two_pair = True
        two_pair_rank = max(cards_rank[0], cards_rank[2])
        high_rank = min(cards_rank[0], cards_rank[2])
    if ((cards_rank[0] == cards_rank[1]) & (cards_rank[3] == cards_rank[4])):
        two_pair = True
        two_pair_rank = max(cards_rank[0], cards_rank[3])
        high_rank = min(cards_rank[0], cards_rank[3])
    if ((cards_rank[1] == cards_rank[2]) & (cards_rank[3] == cards_rank[4])):
        two_pair = True
        two_pair_rank = max(cards_rank[1], cards_rank[3])
        high_rank = min(cards_rank[1], cards_rank[3])

    pair = False
    if (cards_rank[0] == cards_rank[1]):
        pair = True
        pair_rank = cards_rank[0]
        high_rank = cards_rank[4]
    if (cards_rank[1] == cards_rank[2]):
        pair = True
        pair_rank = cards_rank[1]
        high_rank = cards_rank[4]
    if (cards_rank[2] == cards_rank[3]):
        pair = True
        pair_rank = cards_rank[2]
        high_rank = cards_rank[4]
    if (cards_rank[3] == cards_rank[4]):
        pair = True
        pair_rank = cards_rank[3]
        high_rank = cards_rank[2]

    result = []
    if   (flush & straight):
    #     9 = Straight Flush: All cards are consecutive values of same suit.
    #       + Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        result = [9]

    elif (four_of_a_kind):
    #     8 = Four of a Kind: Four cards of the same value.
        result = [8, four_of_a_kind_rank]

    elif (full_house):
    #     7 = Full House: Three of a kind and a pair.
        result = [7, full_house_rank]

    elif (flush):
    #     6 = Flush: All cards of the same suit.
        result = [6, flush_rank]

    elif (straight):
    #     5 = Straight: All cards are consecutive values.
        result = [5, straight_rank]

    elif (three_of_a_kind):
    #     4 = Three of a Kind: Three cards of the same value.
        result = [4, three_of_a_kind_rank, high_rank]

    elif (two_pair):
    #     3 = Two Pairs: Two different pairs.
        result = [3, two_pair_rank, high_rank]

    elif (pair):
    #     2 = One Pair: Two cards of the same value.
        result = [2, pair_rank, high_rank]

    elif (high):
    #     1 = High Card: Highest value card.
        result = [1, high_rank]


    if   (flush & straight & (straight_rank == 14)):  print ", royal flush",
    elif (flush & straight):  print ", straight flush",
    elif (flush):             print ", flush",
    elif (straight):          print ", straight", straight_rank,
    elif (full_house):        print ", full_house", full_house_rank,
    elif (four_of_a_kind):    print ", four_of_a_kind", four_of_a_kind_rank,
    elif (three_of_a_kind):   print ", three_of_a_kind", three_of_a_kind_rank,
    elif (two_pair):          print ", two_pair", two_pair_rank,
    elif (pair):              print ", pair", pair_rank,
    elif (high):              print ", high", high_rank,
    print

    return result


hand_0 = ['2H', '3H', '4H', '7H', 'AH']  # Flush
hand_1 = ['2C', '2H', '7H', '7D', '7S']  # Full House 2+3
hand_2 = ['2C', '2H', '2S', '7D', '7S']  # Full House 3+2
hand_3 = ['8H', '9H', 'TH', 'JH', 'QH']  # Straight Flush
hand_4 = ['TH', 'JH', 'QH', 'KH', 'AH']  # Royal Flush
hand_5 = ['TS', 'TH', 'QH', 'QD', '2H']  # Two pair
hand_6 = ['TS', 'TH', 'QH', '3D', '2H']  # Pair

hand_ex1_1 = ['5H', '5C', '6S', '7S', 'KD']  # Example 1, player 1
hand_ex2_1 = ['5D', '8C', '9S', 'JS', 'AC']  # Example 2, player 1
hand_ex3_1 = ['2D', '9C', 'AS', 'AH', 'AC']  # Example 3, player 1
hand_ex4_1 = ['4D', '6S', '9H', 'QH', 'QC']  # Example 4, player 1
hand_ex5_1 = ['2H', '2D', '4C', '4D', '4S']  # Example 5, player 1

hand_ex1_2 = ['2C', '3S', '8S', '8D', 'TD']  # Example 1, player 2
hand_ex2_2 = ['2C', '5C', '7D', '8S', 'QH']  # Example 2, player 2
hand_ex3_2 = ['3D', '6D', '7D', 'TD', 'QD']  # Example 3, player 2
hand_ex4_2 = ['3D', '6D', '7H', 'QD', 'QS']  # Example 4, player 2
hand_ex5_2 = ['3C', '3D', '3S', '9S', '9D']  # Example 5, player 2

hands = [hand_0, hand_1, hand_2, hand_3, hand_4, hand_5, hand_6, hand_ex1_1, hand_ex2_1, hand_ex3_1, hand_ex4_1, hand_ex5_1, hand_ex1_2, hand_ex2_2, hand_ex3_2, hand_ex4_2, hand_ex5_2 ]

for hand in hands:
    #print "eval_hand({0}) = {1}".format(hand, eval_hand(hand))
    eval_hand(hand)


eval_hand_ex1_1 = eval_hand(hand_ex1_1)
eval_hand_ex2_1 = eval_hand(hand_ex2_1)
eval_hand_ex3_1 = eval_hand(hand_ex3_1)
eval_hand_ex4_1 = eval_hand(hand_ex4_1)
eval_hand_ex5_1 = eval_hand(hand_ex5_1)

eval_hand_ex1_2 = eval_hand(hand_ex1_2)
eval_hand_ex2_2 = eval_hand(hand_ex2_2)
eval_hand_ex3_2 = eval_hand(hand_ex3_2)
eval_hand_ex4_2 = eval_hand(hand_ex4_2)
eval_hand_ex5_2 = eval_hand(hand_ex5_2)

if (eval_hand_ex1_1 > eval_hand_ex1_2):  print "Player 1"
else:                                    print "Player 2"

if (eval_hand_ex2_1 > eval_hand_ex2_2):  print "Player 1"
else:                                    print "Player 2"

if (eval_hand_ex3_1 > eval_hand_ex3_2):  print "Player 1"
else:                                    print "Player 2"

if (eval_hand_ex4_1 > eval_hand_ex4_2):  print "Player 1"
else:                                    print "Player 2"

if (eval_hand_ex5_1 > eval_hand_ex5_2):  print "Player 1"
else:                                    print "Player 2"

if ((eval_hand_ex1_1 == eval_hand_ex1_2)
  | (eval_hand_ex2_1 == eval_hand_ex2_2)
  | (eval_hand_ex3_1 == eval_hand_ex3_2)
  | (eval_hand_ex4_1 == eval_hand_ex4_2)
  | (eval_hand_ex5_1 == eval_hand_ex5_2)):
    print "Error: hands compare equal"

hand_file = open("poker.txt")
hand_table = hand_file.readlines()

result = 0
for line in hand_table:
    two_hands = line.split()
    eval_p1 = eval_hand(two_hands[0:5])
    eval_p2 = eval_hand(two_hands[5:10])
    if (eval_p1 == eval_p2):
        print "Error: two hands evaluate to the same result", two_hands
    if (eval_p1 > eval_p2):
        result += 1

print "result = Player 1 wins this many hands:", result
