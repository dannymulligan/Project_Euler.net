#!/usr/bin/python
#
# Project Euler.net Problem 3
#
# Find the largest prime factor of a composite number.
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857
# Solved ??/??/09
# ?? problems solved
# Position #??? on level ?

TARGET = 600851475143
SQRT_TARGET = 1 + int(TARGET**.5)

LIMIT_PRIME = SQRT_TARGET
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
i = LIMIT_PRIME - 1
while (answer == 0):
    if (prime_table[i] == 1):
        if ((TARGET % i) == 0):
            answer = i
    i -= 1
i += 1
print "Answer is", i
