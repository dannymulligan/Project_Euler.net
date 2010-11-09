#!/usr/bin/python
#
# Project Euler.net Problem 118
#
# Exploring the number of ways in which sets containing prime elements
# can be made.
# 
# Using all of the digits 1 through 9 and concatenating them freely to
# form decimal integers, different sets can be formed. Interestingly
# with the set {2,5,47,89,631}, all of the elements belonging to it
# are prime.
# 
# How many distinct sets containing each of the digits one through
# nine exactly once contain only prime elements?
#
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import itertools

MAX =  10**6

factor_table = [1]*(1+MAX)  # largest factor, 1 means this number is prime
def calculate_factors():
    i = 2
    while (i <= (MAX/2)):
        if (factor_table[i] == 1):
            j = i*2
            while (j <= MAX):
                factor_table[j] = i
                #print "factor_table[{0}] = {1}".format(j, i)
                j += i
        i += 1


def is_prime(n):
    if (factor_table[n] == 1):  return True
    else:                       return False


print "Calculating factors with MAX={0}".format(MAX)
calculate_factors()

digits = range(1,6)

for n in itertools.permutations(digits):
    print n
    

def try (digits):
    for l in range(len(digits)-1):
        if digits
