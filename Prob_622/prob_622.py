#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 622
#
# Riffle shuffles
#
#  A riffle shuffle is executed as follows: a deck of cards is split
#  into two equal halves, with the top half taken in the left hand and
#  the bottom half taken in the right hand. Next, the cards are
#  interleaved exactly, with the top card in the right half inserted
#  just after the top card in the left half, the 2nd card in the right
#  half just after the 2nd card in the left half, etc. (Note that this
#  process preserves the location of the top and bottom card of the
#  deck)
#
# Let s(n) be the minimum number of consecutive riffle shuffles needed
# to restore a deck of size n to its original configuration, where n
# is a positive even number.
#
# Amazingly, a standard deck of 52 cards will first return to its
# original configuration after only 8 perfect shuffles, so s(52)=8. It
# can be verified that a deck of 86 cards will also return to its
# original configuration after exactly 8 shuffles, and the sum of all
# values of n that satisfy s(n)=8 is 412.
#
# Find the sum of all values of n that satisfy s(n)=60.

import sys
#print(sys.version)
import time
start_time = time.clock()

# Discussion of solution
#
# If the deck of cards has DECK cards, we can track the location of
# each card with an integer 0 and DECK-1.  Ignoring the last card
# (which doesn't move anyway), each riffle shuffle will change the
# location of a card at location N as follows...
#
#    N -> N * 2 mod (DECK - 1)
#
# Which means we are looking for values of DECK where iterating
# through 60 riffle shuffles will return the card back to it's
# original location, or where
#
#   N -> N * (2**60) mod (DECK - 1)
#
# or where
#
#    2**60 mod (DECK - 1) = 1
#    (2**60 - 1) mode (DECK - 1) = 0
#
# so the solutions will be values of (DECK - 1) that are factors of
# 2**60 - 1.  Thus we need to find all of the factors of 2**60 - 1
# and then test them as possible parts of the solution.
#
# Note that sometimes when 60 steps returns all cards to their
# original locations there will be a smaller number of steps that also
# return all cards to their original locations.  We need to test each
# possible part of the solution and eliminate it if it has a shorter
# number of steps.
#
# Minor detail: DECK must be even or else it's not possible to do a
# riffle shuffle.  Thus we can eliminate all possible solutions where
# DECK is odd.

# Worked example for the 8 shuffle case
#
# for s(n) = 8, the solutions are 18, 52, 86, 256
#
#     n = 18, n-1 = 17
#     n = 52, n-1 = 51 = 3 * 17
#     n = 86, n-1 = 85 = 5 * 17
#     n = 256, n-1 = 255 = 3 * 5 * 17
#
# All solutions are factors of 255, which is 2^8-1.
# The prime factors of 255 are 3, 5, 17, so the following possible solutions
#
#    1 * 1 *  1 =   1  =>  DECK =   2,  S(  2) = 2, eliminated
#    1 * 1 * 17 =  17  =>  DECK =  18,  S( 18) = 8, part of the solution
#    1 * 5 *  1 =   5  =>  DECK =   6,  S(  6) = 4, eliminated
#    1 * 5 * 17 =  85  =>  DECK =  86,  S( 86) = 8, part of the solution
#    3 * 1 *  1 =   3  =>  DECK =   4,  S(  4) = 2, eliminated
#    3 * 1 * 17 =  51  =>  DECK =  52,  S( 52) = 8, part of the solution
#    3 * 5 *  1 =  15  =>  DECK =  16,  S( 16) = 4, eliminated
#    3 * 5 * 17 = 255  =>  DECK = 256,  S(256) = 8, part of the solution
#
# So the answer is 18 + 86 + 52 + 256 = 412


########################################

def riffle(n, deck_size=52):
    return 2*n % (deck_size-1)

def is_sorted(deck):
    return deck == sorted(deck)

def init_deck(size):
    return [n for n in range(1, size-1)]

def s(size, limit, debug=False):
    history = [1]
    deck = init_deck(size)
    if debug:
        print("Start: {}".format(deck))

    for shuffle in range(limit):
        deck = [riffle(card, size) for card in deck]
        history.append(deck[0])
        if debug:
            print("{}: {}".format(shuffle+1, deck))
        if is_sorted(deck):
            return shuffle+1
    return(history)

def fs(size, limit, debug=False):
    n = 1
    history = [n]
    for i in range(limit):
        n = riffle(n, size)
        history.append(n)
        if n == 1:
            if debug:
                print("True, n = {}, i = {}, target = {}".format(n, i, target), history)
            return (i+1)
    if debug:
        print("False, n = {}".format(n), history)
    return None

def slow_test(n, target, limit, debug=False):
    return s(n, limit, debug) == target

def fast_test(deck_size, target, debug=False):
    n = 1
    history = [n]
    for i in range(target):
        n = riffle(n, deck_size)
        history.append(n)
        if n == 1:
            if debug:
                print("True, n = {}, i = {}, target = {}".format(n, i, target), history)
            return (i+1) == target
    if debug:
        print("False, n = {}".format(n), history)
    return False

import primes
LIMIT_PRIME = 2**16
prime_table = [1]*LIMIT_PRIME  # table of largest factor
prime_list = []
primes.calculate_primes(limit=LIMIT_PRIME, prime_table=prime_table, prime_list=prime_list)


n = 2 ** 60 - 1
factors_of_n = primes.find_factors(n, prime_list)
print("Factors of 2**60 - 1 = {} are {}".format(n, factors_of_n))

# This code is hard coded for the factors of 2**60-1, if I had more time to spend
# I'd write code to generate the candidates automatically from those factors.
candidates = []
for n_3 in range(3):
    for n_5 in range(3):
        for n_7 in range(2):
            for n_11 in range(2):
                for n_13 in range(2):
                    for n_31 in range(2):
                        for n_41 in range(2):
                            for n_61 in range(2):
                                for n_151 in range(2):
                                    for n_331 in range(2):
                                        for n_1321 in range(2):
                                            candidate = 1 + (3**n_3   *  5**n_5  *  7**n_7  * 11**n_11 \
                                                          * 13**n_13  * 31**n_31 * 41**n_41 * 61**n_61 \
                                                         * 151**n_151 * 331**n_331 * 1321**n_1321)
                                            if ((candidate % 2) == 0) and (candidate > 2):
                                                candidates.append(candidate)

target = 60
answer = 0
answers = []
for candidate in candidates:
    #print("Trying {}".format(candidate))
    if fast_test(candidate, target):
        print("s({:,}) = {}".format(candidate, target), end='')
        answer += candidate
        answers.append(candidate)
        print("    {:,} answers totaling to {:,}".format(len(answers), answer))
    else:
        print("    s({:,}) = {}, not a part of the answer".format(candidate, fs(candidate, target)))
        
        
print("len(answers) = {}".format(len(answers)))
print("answers = {}".format(answers))
print("Answer = {:}".format(answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
