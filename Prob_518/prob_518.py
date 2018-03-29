#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 518
#
# Prime triples and geometric sequences
#
# Let S(n) = sum( a+b+c ) over all triples (a,b,c) such that:
#
#    a, b, and c are prime numbers.
#    a < b < c < n.
#    a+1, b+1, and c+1 form a geometric sequence.
#
# For example, S(100) = 1035 with the following triples:
#
#    ( 2,  5, 11),
#    ( 2, 11, 47),
#    ( 5, 11, 23),
#    ( 5, 17, 53),
#    ( 7, 11, 17),
#    ( 7, 23, 71),
#    (11, 23, 47),
#    (17, 23, 31),
#    (17, 41, 97),
#    (31, 47, 71),
#    (71, 83, 97)
#
#Find S(10^8).

import sys
import time
start_time = time.clock()

########################################
#examples = [(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)]
#
#for example in examples:
#    (a, b, c) = example
#    print(a+1, b+1, c+1, (c+1)/(b+1), (b+1)/(a+1))

SIZE = 100    # Answer = 1035
#SIZE = 10**3  # Answer = 75019
#SIZE = 10**4  # Answer = 4225228
#SIZE = 4*10**4  # Answer = 48159907
#SIZE = 5*10**4  # Answer = 72290551
#SIZE = 10**5  # Answer = 249551109
#SIZE = 10**6  # Answer = 17822459735 in 1.99 seconds (previous code took 1091.25 seconds)
#SIZE = 10**7  # Answer = 1316768308545 in 19.59 seconds
SIZE = 10**8  # Answer in 192.13 seconds

# With SIZE = 10**8, it takes
# 40.44 seconds to calculate primes
# 67.74 seconds to calculate factors

############################################################
import primes
prime_table, prime_list = primes.calculate_primes(SIZE)


############################################################
factor_list = dict()
for prime in prime_list:
    factor_list[prime+1] = primes.factors(prime+1, prime_table)
    #print("factor_list[{}] = {}".format(prime+1, factor_list[prime+1]))
print("Finished calculating factor_list after {:.2f} seconds".format(time.clock() - start_time))
#print()


############################################################
reverse_factors = dict()
for factor in factor_list:
    this = sorted(factor_list[factor])
    that = list()
    i = 0
    while (i+1) < len(this):
        if this[i] == this[i+1]:
            i += 2  # skip pair of prime factors
        else:
            that.append(this[i])
            i += 1
    if i < len(this):
        that.append(this[i])
    that_hash = str(that)

    if that_hash in reverse_factors:
        reverse_factors[that_hash].append(factor)
    else:
        reverse_factors[that_hash] = [factor]

    #print("trimmed_factors[{}] = {}".format(factor, that))

#print()
#for that in reverse_factors:
#    print("reverse_factors[{}] = {}".format(that, reverse_factors[that]))

#print()
print("Finished calculating {} groups of reverse_factors after {:.2f} seconds".format(len(reverse_factors), time.clock() - start_time))


############################################################
import itertools
def candidates():
    for factor_list in reverse_factors:
        #print("Searching for results featuring factors {}".format(factor_list))
        for a, c in itertools.combinations(sorted(reverse_factors[factor_list]), 2):
            yield (a, c)


############################################################
def test_candidate(a, c):
    # Find the factors of m^2 = c / a    
    a_factors = primes.factors(a, prime_table)
    c_factors = primes.factors(c, prime_table)

    # Eliminate common factors 
    a_index = c_index = 0
    while (a_index < len(a_factors)) and (c_index < len(c_factors)):
        if a_factors[a_index] == c_factors[c_index]:
            a_factors[a_index] = 1
            c_factors[c_index] = 1
            a_index += 1
            c_index += 1
        elif a_factors[a_index] < c_factors[c_index]:
            a_index += 1
        else:
            c_index += 1
    a_factors = [x for x in a_factors if x != 1]
    c_factors = [x for x in c_factors if x != 1]

    # Get the square root m
    a_factors = a_factors[::2]
    c_factors = c_factors[::2]

    # Calculate b
    b = a
    for f in c_factors:
        b *= f
    for f in a_factors:
        b //= f

    if b in factor_list:
        return True, b
    else:
        return False, b

    
############################################################
answer = 0
for a, c in candidates():
    valid, b = test_candidate(a, c)
    if valid:
        #print("valid (a, b, c) = ({}, {}, {})".format(a-1, b-1, c-1))
        answer += a-1 + b-1 + c-1
    #else:
    #    print("    false (a, c) = ({},{})".format(a, c))

print("Answer = {}".format(answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
