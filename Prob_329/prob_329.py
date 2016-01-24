#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 329
#
# Prime Frog
#
# Susan has a prime frog.
#
# Her frog is jumping around over 500 squares numbered 1 to 500. He
# can only jump one square to the left or to the right, with equal
# probability, and he cannot jump outside the range [1;500].
#
# (if it lands at either end, it automatically jumps to the only
# available square on the next move.)
#
# When he is on a square with a prime number on it, he croaks 'P'
# (PRIME) with probability 2/3 or 'N' (NOT PRIME) with probability 1/3
# just before jumping to the next square.
#
# When he is on a square with a number on it that is not a prime he
# croaks 'P' with probability 1/3 or 'N' with probability 2/3 just
# before jumping to the next square.
#
# Given that the frog's starting position is random with the same
# probability for every square, and given that she listens to his
# first 15 croaks, what is the probability that she hears the sequence
# PPPPNNPPPNPPNPN?
#
# Give your answer as a fraction p/q in reduced form.

import sys
import time
start_time = time.clock()

from fractions import Fraction

############################################################
SIZE = 500
target = 'PPPPNNPPPNPPNPN'


############################################################
LIMIT_PRIME = SIZE + 1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

def calculate_primes(limit=LIMIT_PRIME):
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    primes.append(i)
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 2
    print("There are {} primes less than {}, calculated in {} seconds".format(len(primes), limit, (time.clock() - start_time)))

def is_prime(x):
    if x == 0:
        return False
    elif x == 1:
        return False
    else:
        return prime_table[x] == 1

calculate_primes(LIMIT_PRIME)


############################################################
def chirp(what, probs):
    #print("chirp({},{})".format(what, probs))
    for i in range(len(probs)):
        if is_prime(i):
            if what == 'P':
                probs[i] *= Fraction(2, 3)
            else:
                probs[i] *= Fraction(1, 3)
        else:
            if what == 'P':
                probs[i] *= Fraction(1, 3)
            else:
                probs[i] *= Fraction(2, 3)
    return probs


############################################################
def move(probs):
    #print("move({})".format(probs))
    new_probs = [Fraction(0, 1)] * len(probs)
    for i in range(len(probs)):
        if i == 0:
            new_probs[0] = probs[0]
        elif i == 1:
            new_probs[2] += probs[1]
        elif i == SIZE:
            new_probs[SIZE-1] += probs[SIZE]
        else:
            new_probs[i-1] += probs[i] * Fraction(1, 2)
            new_probs[i+1] += probs[i] * Fraction(1, 2)
    return new_probs


############################################################
print("Running with SIZE={}".format(SIZE))
history = []

# Initialize prob to 0, 1/SIZE,
prob = [Fraction(0,SIZE)] + [Fraction(1,SIZE)]*SIZE
history.append(prob)

for i in range(1, len(target)+1):
    #print("The frog chirped {}".format(target[i-1]))
    prob = chirp(target[i-1], prob)
    history.append(prob)
    #print("chirp", prob)

    prob = move(prob)
    history.append(prob)
    #print("move", prob)

    #print("Probability so far = {} = {:g}".format(sum(prob), float(sum(prob))))

print("Answer = {} = {:g}".format(sum(prob), float(sum(prob))))

print("Time taken = {0} seconds".format(time.clock() - start_time))
