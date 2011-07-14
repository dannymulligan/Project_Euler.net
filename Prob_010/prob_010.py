#!/usr/bin/python
#
# Project Euler.net Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
#

#include <stdio.h>

LIMIT_PRIME = 2000000
prime_table = [1]*LIMIT_PRIME  # table of largest factor

def calculate_primes():
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1

calculate_primes()

answer = 0
for i in range(2,LIMIT_PRIME):
    if (prime_table[i] == 1):
            answer += i

print "Answer is", answer
