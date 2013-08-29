#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 128
#
# Which tiles in the hexagonal arrangement have prime differences with
# neighbours?
#
# A hexagonal tile with number 1 is surrounded by a ring of six
# hexagonal tiles, starting at "12 o'clock" and numbering the tiles 2
# to 7 in an anti-clockwise direction.
#
# New rings are added in the same fashion, with the next rings being
# numbered 8 to 19, 20 to 37, 38 to 61, and so on. The diagram below
# shows the first three rings.
#
# By finding the difference between tile n and each its six neighbours
# we shall define PD(n) to be the number of those differences which
# are prime.
#
# For example, working clockwise around tile 8 the differences are 12,
# 29, 11, 6, 1, and 13. So PD(8) = 3.
#
# In the same way, the differences around tile 17 are 1, 17, 16, 1,
# 11, and 10, hence PD(17) = 2.
#
# It can be shown that the maximum value of PD(n) is 3.
#
# If all of the tiles for which PD(n) = 3 are listed in ascending
# order to form a sequence, the 10th tile would be 271.
#
# Find the 2000th tile in this sequence.
#
# Solved 08/29/13
# 181 problems solved
# Position #301 on level 7

import sys
import time
start_time = time.clock()

RINGS = 5000  # The sum(answers) below counts on this being 5000
RINGS = 100000
TARGET = 2000

##############################
def first_num_in_ring(ring):
    if (ring == 0):
        return 1
    else:
        return 2 + 6 * (ring)*(ring-1)/2

##############################
LIMIT_PRIME = first_num_in_ring(RINGS+2) - 1 - first_num_in_ring(RINGS)
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
def calculate_primes():
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1
    while (i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 1

calculate_primes()
print "We will check the first {} rings of the pattern,".format(RINGS),
print "this requires us to deal with primes up to {}.".format(LIMIT_PRIME)
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "primes =", primes


##############################
def all_prime(numbers):
    result = 0
    for num in numbers:
        if (prime_table[num] != 1):
            return False
    return True


##############################
answers = []
ans_cnt = 0
for ring in range(1, RINGS+1):

    n = first_num_in_ring(ring)

    # Optimization
    # The 12:00 number and the last number in the ring are neighbors
    # If the difference between them is not prime, then neither one can have P(n) = 3
    d = ring*6-1
    if (prime_table[d] != 1):
        continue
    
    # 12:00 number in this ring
    #     diff to 12:00 is (ring*6), not prime
    #     diff to 10:00 is (ring*6) + 1, could be prime
    #     diff to 8:00 is 1, not prime
    #     diff to 6:00 is (ring-1)*6, not prime
    #     diff to 4:00 is (ring*6) - 1, could be prime
    #     diff to 2:00 is (ring*6) + (ring+1)*6 - 1, could be prime
    # 3 differences could be prime, so have to check
    diffs = [ring*6+1, ring*6-1, 2*ring*6+5]
    if all_prime(diffs):
        #print diffs
        ans_cnt += 1
        print "{}: PD({}) == 3".format(ans_cnt, n)
        answers.append(n)
        if (ans_cnt == TARGET):
            print "Answer =", n
            print "Time taken = {0} seconds".format(time.clock() - start_time)
            sys.exit(1)

    # last digit in this ring
    n += 6*ring-1
    #     diff to 12:00 is (ring*6) + 6, not prime
    #     diff to 10:00 is (ring*6) - 1, could be prime
    #     diff to 8:00 is (ring*6 - 1) + (ring-1)*6, could be prime
    #     diff to 6:00 is ((ring-1)*6 + 4), not prime
    #     diff to 4:00 is 1, not prime
    #     diff to 2:00 is (ring*6) + 5, could be prime
    # 3 differences could be prime, so have to check
    diffs = [ring*6-1, 2*ring*6-7, ring*6+5]
    if all_prime(diffs):
        #print diffs
        ans_cnt += 1
        print "{}: PD({}) == 3".format(ans_cnt, n)
        answers.append(n)
        if (ans_cnt == TARGET):
            print "Answer =", n
            print "Time taken = {0} seconds".format(time.clock() - start_time)
            sys.exit(1)
            
    # numbers between 12:00 and 10:00
    #     diff to 2:00 is 1, not prime
    #     diff to 8:00 is 1, not prime
    #     one of diff to 12:00 or diff to 10:00 is even, not prime
    #     one of diff to 6:00 or diff to 4:00 is even, not prime
    # At most 2 differences could be prime, don't have to check

    # 10:00 digit in this ring
    #     diff to 12:00 is (ring*6), not prime
    #     diff to 8:00 is (ring*6) + 2, not prime
    #     diff to 6:00 is 1, not prime
    #     diff to 2:00 is 1, not prime
    # At most 2 differences could be prime, don't have to check

    # numbers between 10:00 and 8:00
    #     diff to 12:00 is 1, not prime
    #     diff to 6:00 is 1, not prime
    #     one of diff to 10:00 or diff to 8:00 is even, not prime
    #     one of diff to 4:00 or diff to 2:00 is even, not prime
    # At most 2 differences could be prime, don't have to check

    # 8:00 digit in this ring
    #     diff to 12:00 is 1, not prime
    #     diff to 10:00 is (ring*6) + 1, could be prime
    #     diff to 8:00 is (ring*6) + 2, not prime
    #     diff to 6:00 is (ring*6) + 3, could be prime
    #     diff to 4:00 is 1, not prime
    #     diff to 2:00 is ((ring-1)*6 + 2), not prime
    # At most 2 differences could be prime, don't have to check

    # numbers between 8:00 and 6:00
    #     diff to 10:00 is 1, not prime
    #     diff to 4:00 is 1, not prime
    #     one of diff to 8:00 or diff to 6:00 is even, not prime
    #     one of diff to 2:00 or diff to 12:00 is even, not prime
    # At most 2 differences could be prime, don't have to check

    # 6:00 digit in this ring
    #     diff to 12:00 is ((ring-1)*6 + 3), could be prime
    #     diff to 10:00 is 1, not prime
    #     diff to 8:00 is (ring*6) + 2, not prime
    #     diff to 6:00 is (ring*6) + 3, could be prime
    #     diff to 4:00 is (ring*6) + 4, not prime
    #     diff to 2:00 is 1, not prime
    # At most 2 differences could be prime, don't have to check

    # numbers between 6:00 and 4:00
    #     diff to 8:00 is 1, not prime
    #     diff to 2:00 is 1, not prime
    #     one of diff to 12:00 or diff to 10:00 is even, not prime
    #     one of diff to 6:00 or diff to 4:00 is even, not prime
    # At most 2 differences could be prime, don't have to check

    # 4:00 digit in this ring
    #     diff to 12:00 is 1, not prime
    #     diff to 10:00 is ((ring-1)*6 + 4), not prime
    #     diff to 8:00 is 1, not prime
    #     diff to 6:00 is (ring*6) + 3, could be prime
    #     diff to 4:00 is (ring*6) + 4, not prime
    #     diff to 2:00 is (ring*6) + 5, could be prime
    # At most 2 differences could be prime, don't have to check

    # numbers between 4:00 and 2:00
    #     diff to 12:00 is 1, not prime
    #     diff to 6:00 is 1, not prime
    #     one of diff to 10:00 or diff to 8:00 is even, not prime
    #     one of diff to 4:00 or diff to 2:00 is even, not prime
    # At most 2 differences could be prime, don't have to check

    # 2:00 digit in this ring
    #     diff to 12:00 is (ring*6) + 6, not prime
    #     diff to 10:00 is 1, not prime
    #     diff to 8:00 is ((ring-1)*6 + 5), could be prime
    #     diff to 6:00 is 1, not prime
    #     diff to 4:00 is (ring*6) + 4, not prime
    #     diff to 2:00 is (ring*6) + 5, could be prime
    # At most 2 differences could be prime, don't have to check

    # numbers between 2:00 and 12:00, except for the last one in the ring
    #     diff to 10:00 is 1, not prime
    #     diff to 4:00 is 1, not prime
    #     one of diff to 12:00 or diff to 2:00 is even, not prime
    #     one of diff to 8:00 or diff to 6:00 is even, not prime
    # At most 2 differences could be prime, don't have to check

    
print "Answer not found, try a larger of RINGS than {}".format(RINGS)
print "Print sum(answers) =", sum(answers)
print "Time taken = {0} seconds".format(time.clock() - start_time)
if sum(answers) != 5753182777:
    print "sum(answers) has changed!"
