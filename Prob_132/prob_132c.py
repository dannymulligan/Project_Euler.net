#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 132
#
# Determining the first forty prime factors of a very large repunit.
#
# A number consisting entirely of ones is called a repunit. We shall
# define R(k) to be a repunit of length k.
#
# For example, R(10) = 1111111111 = 11 x 41 x 271 x 9091, and the sum
# of these prime factors is 9414.
#
# Find the sum of the first forty prime factors of R(10^9).
#
# Answer: 843296
# Solved 05/11/10
# 136 problems solved
# Position #308 on level 3

# This version prob_132c.py runs in 4m48.
# The prior version prob_132b.py runs in about 1 hour.

import sys

LIMIT_PRIME = 200000
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


def digits_in (n):
    if (n < 0):
        print "N is < 0"
        sys.exit()
    elif (n <         10):  return 1
    elif (n <        100):  return 2
    elif (n <       1000):  return 3
    elif (n <      10000):  return 4
    elif (n <     100000):  return 5
    elif (n <    1000000):  return 6
    elif (n <   10000000):  return 7
    elif (n <  100000000):  return 8
    elif (n < 1000000000):  return 9
    else:
        print "N is too large"
        sys.exit()


def div_repunit_n (r_len, n):
    # Maximum integer is 2,147,483,647, which is 10 digits
    # We're going to deal with 9 digits at a time
    (r, num) = (r_len-9, 111111111)
    num %= n
    num_len = digits_in(num)

    # Keep dividing num by n and adding 1s at the right until no more digits to add
    while (r > 0):
        shift = 9 - num_len
        if (shift > r):  shift = r

        if   (shift == 1):  (r, num) = (r-1, num*10        + 1       )
        elif (shift == 2):  (r, num) = (r-2, num*100       + 11      )
        elif (shift == 3):  (r, num) = (r-3, num*1000      + 111     )
        elif (shift == 4):  (r, num) = (r-4, num*10000     + 1111    )
        elif (shift == 5):  (r, num) = (r-5, num*100000    + 11111   )
        elif (shift == 6):  (r, num) = (r-6, num*1000000   + 111111  )
        elif (shift == 7):  (r, num) = (r-7, num*10000000  + 1111111 )
        elif (shift == 8):  (r, num) = (r-8, num*100000000 + 11111111)

        num = num % n
        num_len = digits_in(num)
    return num


def divisible (r_len, n):
    # Maximum integer is 2,147,483,647, which is 10 digits
    # We're going to deal with 9 digits at a time
    (r, num) = (r_len-9, 111111111)
    num %= n
    num_len = digits_in(num)

    # Keep dividing num by n and adding digits at the right until no more digits to add
    while (r > 0):
        shift = 9 - num_len
        if (shift > r):  shift = r

        if   (shift == 1):  (r, num) = (r-1, num*10        + 1       )
        elif (shift == 2):  (r, num) = (r-2, num*100       + 11      )
        elif (shift == 3):  (r, num) = (r-3, num*1000      + 111     )
        elif (shift == 4):  (r, num) = (r-4, num*10000     + 1111    )
        elif (shift == 5):  (r, num) = (r-5, num*100000    + 11111   )
        elif (shift == 6):  (r, num) = (r-6, num*1000000   + 111111  )
        elif (shift == 7):  (r, num) = (r-7, num*10000000  + 1111111 )
        elif (shift == 8):  (r, num) = (r-8, num*100000000 + 11111111)

        num = num % n
        num_len = digits_in(num)

    return num


def div_10x_n (x, n):
    # Maximum integer is 2,147,483,647, which is 10 digits
    # We're going to deal with 9 digits at a time
    num = 1
    num_len = digits_in(num)

    # Keep dividing num by n and adding 0s at the right until no more digits to add
    while (x > 0):
        shift = 9 - num_len
        if (shift > x):  shift = x

        if   (shift == 1):  (x, num) = (x-1, num*10       )
        elif (shift == 2):  (x, num) = (x-2, num*100      )
        elif (shift == 3):  (x, num) = (x-3, num*1000     )
        elif (shift == 4):  (x, num) = (x-4, num*10000    )
        elif (shift == 5):  (x, num) = (x-5, num*100000   )
        elif (shift == 6):  (x, num) = (x-6, num*1000000  )
        elif (shift == 7):  (x, num) = (x-7, num*10000000 )
        elif (shift == 8):  (x, num) = (x-8, num*100000000)

        num = num % n
        num_len = digits_in(num)

    return num


def div_rep10x_n (r, x, n):
    div = div_10x_n(x, n)
    #if (div == 0):  return 1
    num = 1
    for i in range(r-1):
        num = 1 + num*div
        num %= n
    return num


def div_compound(r, n):
    rem1 = div_repunit_n(20000, n)
    if (rem1 == 0):  return 0
    rem2 = div_rep10x_n(50000, 20000, n)
    return (rem1 * rem2) % n


calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "primes =", primes


# R(10) = 1111111111 = 11 x 41 x 271 x 9091, sum = 9414
prime_count = 0
div_count = 0
answer = 0
#primes = [11, 17, 41, 73, 101, 137, 251, 257, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 10753, 15361, 16001, 19841, 21001, 21401, 24001, 25601, 27961, 37501, 40961, 43201, 60101, 62501, 69857, 76001, 76801, 160001 ]
for n in primes:
    prime_count += 1
    #print "Testing prime({0}) = {1}".format(prime_count, n)

    if (div_compound(1000000000, n) == 0):
        div_count += 1
        answer += n
        print "    R({0}) is divisible by prime({1}) which is {2}, {3} divisors fround".format(1000000000, prime_count, n, div_count)
        if (div_count == 40):
            break

print "Answer =", answer, "div_count =", div_count


#
# Find the sum of the first forty prime factors of R(10^9).

# 111 * 1001001 = 111111111
# 111 * 1001001 * 1000000001000000001 = 111111111111111111111111111
