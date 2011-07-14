#!/usr/bin/python
#
# Project Euler.net Problem 87
#
# The smallest number expressible as the sum of a prime square, prime
# cube, and prime fourth power is 28. In fact, there are exactly four
# numbers below fifty that can be expressed in such a way:
# 
#     28 = 2^2 + 2^3 + 2^4
#     33 = 3^2 + 2^3 + 2^4
#     49 = 5^2 + 2^3 + 2^4
#     47 = 2^2 + 3^3 + 2^4
# 
# How many numbers below fifty million can be expressed as the sum of
# a prime square, prime cube, and prime fourth power?
# 
# Solved 10/27/09
# 90 problems solved
# Position #142 on level 2

# Run with:
#     python prob_087.py | awk '{print $1}' | sort -u | wc -l

# Only have to test up to 84, because...
#     84^2 + 84^3 + 84^4 = 50,386,896 > 50 million

LIMIT_D =     7075
prime_table = [1]*LIMIT_D  # table of largest factor

def calculate_primes():
    i = 2
    while (i < (LIMIT_D/2)):
        if (prime_table[i] == 1):
            j = i*2
            while (j < LIMIT_D):
                prime_table[j] = i
                j += i
        i += 1

calculate_primes()

answer = 0
for a in range(2,7073):  # 7072^2 = 50,013,184
    if (prime_table[a] != 1):  continue
    for b in range(2,370):  # 370^3 = 50,653,000
        if (prime_table[b] != 1):  continue
        for c in range(2,85):  # 85^4 = 52,200,625
            if (prime_table[c] != 1):  continue
            #if ((a**2 + b**3 + c**4) > 50):  continue
            if ((a**2 + b**3 + c**4) > 50000000):  continue
            print "{0:8} = {1:4} + {2:4} + {3:4} = {4:2}^2 + {5:2}^3 + {6:2}^4".format(a**2+b**3+c**4, a**2, b**3, c**4, a, b, c)
            answer += 1
