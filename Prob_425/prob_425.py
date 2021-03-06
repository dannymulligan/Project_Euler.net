#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 425
#
# Prime connection
#
# Two positive numbers A and B are said to be connected (denoted by "A
# <-> B") if one of these conditions holds:
#
#    (1) A and B have the same length and differ in exactly one digit;
#    for example, 123 <-> 173.
#
#    (2) Adding one digit to the left of A (or B) makes B (or A); for
#    example, 23 <-> 223 and 123 <-> 23.
#
# We call a prime P a 2's relative if there exists a chain of
# connected primes between 2 and P and no prime in the chain exceeds
# P.
#
# For example, 127 is a 2's relative. One of the possible chains is
# shown below:
# 2 <-> 3 <-> 13 <-> 113 <-> 103 <-> 107 <-> 127
# However, 11 and 103 are not 2's relatives.
#
# Let F(N) be the sum of the primes <= N which are not 2's relatives.
# We can verify that F(10^3) = 431 and F(10^4) = 78728.
#
# Find F(10^7).

import primes
import time
start_time = time.clock()
SIZE = 7  # We evaluate F(10**SIZE)
NOT_CONNECTED = 10**SIZE + 1
DEBUG = False


########################################
def same_digit_primes(n, digits):
    # Yield numbers with the same number of digits as n
    # that differ in just one digit
    for d in range(digits):
        top = (n // (10**(d+1))) * (10**(d+1))
        bot = n % (10**d)
        for c in range(10):
            candidate = top + bot + c*(10**d)
            if (prime_table[candidate] == 1):
                yield candidate


########################################
def more_digit_primes(n, digits):
    # Yield numbers with one digits appended to the left of n
    if digits == SIZE:
        return None
    for p in range(1, 10):
        trial = n + p * (10**digits)
        if (prime_table[trial] == 1):
            yield trial


########################################
def less_digit_primes(n, digits):
    # Yield numbers with one digits chopped off the left of n
    trial = n % 10**(digits-1)
    if (prime_table[trial] == 1):
        yield trial


########################################

prime_table, prime_list = primes.calculate_primes(10**SIZE+1)

best_path = {p: NOT_CONNECTED for p in prime_list}
best_path[2] = 2

overall_done = False
while not overall_done:
    overall_done = True

    # Process primes with the <digits> digits
    for digits in range(1, SIZE+1):
        lower_limit = 10**(digits-1)
        upper_limit = 10**digits - 1
        print("Processing primes with {} digits".format(digits), end='')
        print(", between {} and {}".format(lower_limit, upper_limit))

        # Find all connected primes with the same number of digits
        for prime in prime_list:
            if (prime < lower_limit) or (prime > upper_limit):
                continue
            if best_path[prime] == NOT_CONNECTED:
                continue

            if DEBUG:
                print("    looking for same digit primes from {}".format(prime))
            for n in same_digit_primes(prime, digits):
                path_max = max(n, best_path[prime])
                if path_max < best_path[n]:
                    best_path[n] = path_max
                    if DEBUG:
                        print("        best_path[{}] = {}".format(n, path_max))
                    overall_done = False

        # Find all connected primes with the 1 more digits
        for prime in prime_list:
            if (prime < lower_limit) or (prime > upper_limit):
                continue
            if best_path[prime] == NOT_CONNECTED:
                continue

            if DEBUG:
                print("    looking for more digit primes from {}".format(prime))
            for n in more_digit_primes(prime, digits):
                path_max = max(n, best_path[prime])
                if path_max < best_path[n]:
                    best_path[n] = path_max
                    if DEBUG:
                        print("        best_path[{}] = {}".format(n, path_max))
                    overall_done = False

        # Find all connected primes with the 1 fewer digits
        for prime in prime_list:
            if (prime < lower_limit) or (prime > upper_limit):
                continue
            if best_path[prime] == NOT_CONNECTED:
                continue

            if DEBUG:
                print("    looking for less digit primes from {}".format(prime))
            for n in less_digit_primes(prime, digits):
                path_max = max(n, best_path[prime])
                if path_max < best_path[n]:
                    best_path[n] = path_max
                    if DEBUG:
                        print("        best_path[{}] = {}".format(n, path_max))
                    less_digit_done = False
                    overall_done = False

#DEBUG = True
answer = 0
for p in best_path:
    if best_path[p] > p:
        answer += p
    if DEBUG:
        if best_path[p] == NOT_CONNECTED:
            print("best_path[{}] = not connected".format(p))
        else:
            if best_path[p] > p:
                print("best_path[{}] = {} => not 2's relative".format(p, best_path[p]))
            else:
                print("best_path[{}] = {}".format(p, best_path[p]))
print("F({}) = {}".format(10**SIZE, answer))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
