#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 193
#
# Squarefree Numbers
#
# A positive integer n is called squarefree, if no square of a prime
# divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4,
# 8, 9, 12.
#
# How many squarefree numbers are there below 250?
#
# Solved 12/18/14
# 193 problems solved
# Position #56 on level 7

#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import sys
import time
start_time = time.clock()

########################################
LIMIT_PRIME = 2**25
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

def calculate_primes(limit=LIMIT_PRIME):
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    prime_table[i] = i
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

    print("There are {} primes less than {}".format(len(primes), limit))
    #print "They are", primes
    #print prime_table
    print "Time taken to calculate primes = {0} seconds".format(time.clock() - start_time)

########################################
LIMIT_SQUARE = 2**25
square_table = [1]*LIMIT_SQUARE

def calculate_squares(limit=LIMIT_SQUARE):
    if (limit>len(square_table)):
        raise Exception("square_table is too small ({} entries, need at least {})".format(len(square_table), limit))
    for p in primes:
        for i in range(p**2, limit, p**2):
            square_table[i] = p


def count_squarefree(limit=LIMIT_SQUARE):
    answer = 0
    for i in range(1,limit):
        if (square_table[i] == 1):
            answer += 1
    return answer


########################################

def div_by_at_least_n_prime_squares(min_prime, limit, existing, prime_count, debug=0):
    answer = 0

    if (prime_count > 1):
        # Recursion
        for p in primes:
            if (p < min_prime):
                # p is below our limit, need a bigger prime
                continue
            if (existing*(p**2)*(p**2) > limit):
                # existing * p^2 * q^2 would be too large
                # where q is another prime at least as large as p
                break
            answer += div_by_at_least_n_prime_squares(p+1, limit, existing*(p**2), prime_count-1, debug)

    else:

        for p in primes:
            if (p < min_prime):
                continue
            if (existing*(p**2) >= limit):
                break
            answer += (limit-1)/(existing*(p**2))

            if (debug >= 3):
                print("{}^2={}:".format(p,p**2)),
                for n in range((limit-1)/(existing*(p**2))):
                    print("{},".format((n+1)*existing*(p**2))),
                print

    if debug >= 2:
        print("Return: div_by_at_least_n_prime_squares(min_prime={}, limit={}, existing={}, prime_count={}, debug={}) = {}".format(
            min_prime, limit, existing, prime_count, debug, answer))

    return answer


########################################
def div_by_prime_square(limit, debug=0):
    answer = 0
    depth = 1
    while True:
        if debug >= 1:
            print("\nCalling: div_by_at_least_n_prime_squares(min_prime={}, limit={}, existing={}, prime_count={}, debug={})".format(
                             2, limit, 1, depth, debug))

        partial_answer = div_by_at_least_n_prime_squares(min_prime=2, limit=limit, existing=1, prime_count=depth, debug=debug)

        if partial_answer == 0:
            break

        answer += (-1)**(depth+1) * partial_answer
        depth += 1
    return answer


#########################################
## Calculating the slow way...
#limit = 2**10
#calculate_primes(limit)
#calculate_squares(limit)
#for limit in [13, 20, 100, 1000]:
#    print("there are {} squarefree numbers below {}".format(count_squarefree(limit), limit))
#
#########################################
## Calculating the fast way...
#for limit in [13, 20, 100, 1000]:
#    n = div_by_prime_square(limit, debug=0)
#    print("there are {} squarefree numbers below {}".format(limit-1-n, limit))
#
#sys.exit(0)


########################################
#limit = 2**10
#calculate_primes(limit)
#assert div_by_prime_square(2**10, debug=0) == 399
#assert div_by_prime_square(100, debug=0) == 38
#sys.exit(0)


########################################
limit_power = 50
limit = 2**limit_power
calculate_primes(2**(limit_power/2))
n = div_by_prime_square(limit, debug=1)
print("with limit = 2^{}, answer = {}".format(limit_power, limit - n - 1))


print "Time taken = {0} seconds".format(time.clock() - start_time)

# 58.07 seconds to do 2**34
# 92.76 seconds to do 2**35
# 143.58 seconds to do 2**36
# An increase of 1 in the power of 2 results in 1.55x longer runtime
# Predicted runtime for 2**50 is a little over 19 hours
# Actually, that calculation doesn't factor in the constant runtime
# spent calculating primes, the predicted run time is actually far worse
