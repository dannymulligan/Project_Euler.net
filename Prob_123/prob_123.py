#!/usr/bin/python
#
# Project Euler.net Problem 123
# 
# Let p_(n) be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the
# remainder when (p(n)-1)^n + (p(n)+1)^n is divided by p(n)^2.
# 
# For example, when n = 3, p(3) = 5, and 4^3 + 6^3 = 280 == 5 mod 25.
# 
# The least value of n for which the remainder first exceeds 10^9 is
# 7037.
# 
# Find the least value of n for which the remainder first exceeds
# 10^10.
#
# Answer: 21035
# Solved 11/22/09
# 107 solved
# Position #944 on level 3

LIMIT_PRIME = 250000
primes = [0]  # Pad with a dummy item, to make primes[n] return the right thing

def calculate_primes():
    prime_table = [1]*LIMIT_PRIME  # table of largest factor
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
    del prime_table

def rem_p(n):
    p = primes[n]
    p_sq = p**2
    (pp, pm) = (1,1)
    for i in range(n):
        pp *= (p+1)
        pm *= (p-1)
        pp %= p_sq
        pm %= p_sq
    r = pp + pm
    r = r % p_sq
    return r

calculate_primes()
print "Found {0} primes".format(len(primes))

max_res = 0
for i in range(2,len(primes)):
    res = rem_p(i)
#    if (res > max_res):
#        max_res = res
#        print "Found p({0}) = {1}, remainder = {2}".format(i, primes[i], res)
    if (res > 10**10):
        print "Answer =", i
        exit()
print "Finished without finding result"
