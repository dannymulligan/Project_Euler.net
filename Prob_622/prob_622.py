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

# for s(n) = 8, the solutions are 18, 52, 86, 256
# n = 18, n-1 = 17
# n = 52, n-1 = 51 = 3 * 17
# n = 86, n-1 = 85 = 5 * 17
# n = 256, n-1 = 255 = 3 * 5 * 17
#
# all of the solutions are factors of 255, which is 2^8-1
# prime factors of 255 are 3, 5, 17
#
# the following are also factors of 255, but are not solutions...
#
# n = 4 , n-1 = 3, because s(4) = 2
# n = 6 , n-1 = 5, because s(6) = 4
# n = 16, n-1 = 15 = 3 * 5, because s(16) = 4
#


########################################

def riffle(n, deck_size=52):
    return 2*n % (deck_size-1)

def is_sorted(deck):
    return deck == sorted(deck)

def init_deck(size):
    return [n for n in range(1, size-1)]

def s(size, debug=False):
    history = [1]
    deck = init_deck(size)
    if debug:
        print("Start: {}".format(deck))

    for shuffle in range(61):
        deck = [riffle(card, size) for card in deck]
        history.append(deck[0])
        if debug:
            print("{}: {}".format(shuffle+1, deck))
        if is_sorted(deck):
            return shuffle+1
    return(history)

def slow_test(n, target, debug=False):
    return s(n, debug) == target

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
print(factors_of_n)

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
        
print("len(answers) = {}".format(len(answers)))
print("answers = {}".format(answers))
print("Answer = {:}".format(answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
