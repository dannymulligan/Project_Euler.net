#!/usr/bin/python
#
# Project Euler.net Problem 216
#
# Investigating the primality of numbers of the form 2n^2-1
#
# Consider numbers t(n) of the form t(n) = 2n^(2)-1 with n > 1.
# The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
# It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
# For n <= 10000 there are 2202 numbers t(n) that are prime.
# 
# How many numbers t(n) are prime for n <= 50,000,000 ?
#
# Answer: 
# Solved ??/??/09
# ?? problems solved
# Position #??? on level ?

N = 50000000
#N = 10000  # answer should be 2202
#N = 9  # Answer should be 6

MAX = 2*N*N-1
LIMIT_PRIME = 1+int(MAX**.5)
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

def is_prime(n):
    if (n < LIMIT_PRIME):
        return (prime_table[n] == 1)
    else:
        for i in range(2,LIMIT_PRIME):
            if (prime_table[i] == 1):
                if ((n % i) == 0):
                    return False
        return True

def t(n):
    return 2*n*n-1

calculate_primes()
print "Done calculating primes"

answer = 0
for i in range(2,N+1):
    if (is_prime(t(i))):
        answer += 1
    if ((i % 10000) == 0):
        print "Working on i=", i

print "Answer =", answer
