#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 231
#
# The prime factorisation of binomial coefficients
#
#                            ( 10 )
# The binomial coefficient C (    ) = 120.
#                            (  3 )
#
# 120 = 23 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.
#
#                                                         ( 10 )
# So the sum of the terms in the prime factorization of C (    ) is 14.
#                                                         (  3 )
# 
#                                                           ( 20000000 )
# Find the sum of the terms in the prime factorisation of C (          )
#                                                           ( 15000000 )
#
# Answer: 7526965179680
# Solved 05/14/11
# 137 problems solved
# Position #289 on level 3

# http://en.wikipedia.org/wiki/Binomial_coefficient
#
#   ( n )       n!
# C (   ) = -----------  for 0 <= k <= n
#   ( k )   k! * (n-k)!
#
#   ( 10 )     10!     10 * 9 * 8   5 * 3 * 8
# C (    ) = ------- = ---------- = --------- = 120
#   (  3 )   3! * 7!   3 * 2 * 1        1
#
#   ( 20,000,000 )          20,000,000!
# C (            ) = ------------------------
#   ( 15,000,000 )   15,000,000! * 5,000,000!
#
#   20,000,000 * ... * 15,000,001
# = ----------------------------
#      5,000,000 * ... * 1
#

TOP = 20000000
BOT = 15000000
LIMIT_PRIME = TOP+1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
factors = [0]*LIMIT_PRIME      # table of the factors of the binomial coefficient

def calculate_primes():
    count = 0
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            count += 1
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1
    return count

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

prime_count = calculate_primes()
print "There are", prime_count, "primes less than", LIMIT_PRIME


for i in range(BOT):
    t = i + 1 + TOP-BOT
    b = i + 1
    #print "t = {0} / b = {1}".format(t, b), 
    g = gcd(t,b)
    t /= g
    b /= g
    #if (g == 1):  print
    #else:         print ", simplified to t = {0} / b = {1}".format(t, b)

    while (t > 1):
        f = prime_table[t]
        if (f == 1):  f = t
        factors[f] += 1
        #print "t = {0}, factors[{1}] += 1".format(t, f)
        t /= f

    while (b > 1):
        f = prime_table[b]
        if (f == 1):  f = b
        factors[f] -= 1
        #print "b = {0}, factors[{1}] -= 1".format(b, f)
        b /= f

answer = 0
for i in range(len(factors)):
    answer += i * factors[i]
print "Answer =", answer
