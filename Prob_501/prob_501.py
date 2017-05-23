#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 501
#
# Eight Divisors
#
# The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24.
#
# The ten numbers not exceeding 100 having exactly eight divisors are
# 24, 30, 40, 42, 54, 56, 66, 70, 78 and 88.
#
# Let f(n) be the count of numbers not exceeding n with exactly eight
# divisors.
#
# You are given f(100) = 10, f(1000) = 180 and f(10^6) = 224427.
#
# Find f(10^12).

import time

TARGET = 10**12
TARGET = 10**6
TARGET = 10**2

LIMIT_PRIME = TARGET+1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

############################################################
def calculate_primes(limit=LIMIT_PRIME):
    start_time = time.clock()
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
    print("There are {:,} primes less than {:,}, calculated in {:.2f} seconds".format(len(primes), limit, (time.clock() - start_time)))

calculate_primes(limit = TARGET//4)


############################################################
# Calculate answers of the form a * b * c
x = primes[0] * primes[1] * primes[2]
i = 3
while x <= TARGET:
    i += 1
    x = primes[i-3] * primes[i-2] * primes[i-1]
    #print("{} * {} * {} = {:,} < {:,}".format(primes[i-2], primes[i-1], primes[i], x, TARGET))
i -= 1
x = primes[i-3] * primes[i-2] * primes[i-1]
print("{} * {} * {} = {:,} <= {:,}".format(primes[i-3], primes[i-2], primes[i-1], x, TARGET))

print("We can make numbers out of {} primes up to ...{}, {}, {}".format(i, primes[i-3], primes[i-2], primes[i-1]))
AnswerA = i * (i-1) * (i-2) // 6
print("This yields {:,} solutions of type A\n".format(AnswerA))


############################################################
# Calculate answers of the form a^3 * b
AnswerB = 0

a = 0
while primes[a]**3 <= TARGET:
    remainder = TARGET // primes[a]**3
    if remainder >= primes[0]:
        print("{}^3 = {:,} < {:,}, remainder = {}".format(primes[a], primes[a]**3, TARGET, remainder))

        b = 0
        while primes[b] <= remainder:
            print("primes[{}] = {} < {}".format(b, primes[b], remainder))
            b += 1
        if b >= a:
            print("{} solutions of the form {}^3 * {} ".format(b-1, primes[a], primes[:a] + primes[a+1:b]))
            AnswerB += b-1
        else:
            print("{} solutions of the form {}^3 * {} ".format(b, primes[a], primes[:b]))
            AnswerB += b

    a += 1
        
print("This yields {:,} solutions of type B\n".format(AnswerB))
    

############################################################
# Calculate answers of the form a^7
AnswerC = 0

if primes[0]**7 > TARGET:
    AnswerC = 0
else:
    a = 0
    while primes[a]**7 <= TARGET:
        a += 1
    a -= 1
    
    print("{}^7 = {:,} < {:,}".format(primes[a], primes[a]**7, TARGET))
    AnswerC = a+1
    
print("This yields {:,} solutions of type C\n".format(AnswerC))


############################################################
# Final answer
Answer = AnswerA + AnswerB + AnswerC
print("The overall answer is f({}) = {:,}".format(TARGET, Answer))


############################################################
#
# To have 8 divisors, the number has to be one of the following three forms
# 
#    a * b * c  (where a, b, & c are prime)
# 
# or
# 
#    a^3 * b (where a, & b are prime)
#
# or
# 
#    a^7 (where a is prime)
# 
# a*b*c has the following 8 factors
# 
#    000 = a^0 * b^0 * c^0 = 1 * 1 * 1
#    001 = a^0 * b^0 * c^1 = 1 * 1 * c
#    010 = a^0 * b^1 * c^0 = 1 * b * 1
#    011 = a^0 * b^1 * c^1 = 1 * b * c
#    100 = a^1 * b^0 * c^0 = a * 1 * 1
#    101 = a^1 * b^0 * c^1 = a * 1 * c
#    110 = a^1 * b^1 * c^0 = a * b * 1
#    111 = a^1 * b^1 * c^1 = a * b * c
# 
# a^3 * b has the following 8 factors
# 
#    00 = a^0 * b^0 = 1   * 1
#    01 = a^0 * b^1 = 1   * b
#    10 = a^1 * b^0 = a   * 1
#    11 = a^1 * b^1 = a   * b
#    20 = a^2 * b^0 = a^2 * 1
#    21 = a^2 * b^1 = a^2 * b
#    30 = a^3 * b^0 = a^3 * 1
#    31 = a^3 * b^1 = a^3 * b
# 
# a^7 has the following 8 factors
# 
#    0 = a^0
#    1 = a^1
#    2 = a^2
#    3 = a^3
#    4 = a^4
#    5 = a^5
#    6 = a^6
#    7 = a^7
#
# for f(100)...
# Examples of type A (a*b*c) solutions are
#
# 13 * 3 * 2 = 78
# 11 * 3 * 2 = 66
#  7 * 5 * 2 = 70
#  7 * 3 * 2 = 42
#  5 * 3 * 2 = 30
#
# Examples of type B (a^3*b) solutions are
#
# 3^3 *  2 = 54
# 2^3 * 11 = 88
# 2^3 *  7 = 56
# 2^3 *  5 = 40
# 2^3 *  3 = 24
#
# Examples of type C (a^7) solutions are
#
# none
#
# So 10 solutions in total
