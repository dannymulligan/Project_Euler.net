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
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys

LIMIT_PRIME = 20000
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
prime_mods = []

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


def divisible (n, r_len):
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

    if (num == 0):  return True
    return False


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


def calculate_divisors():
    for p in primes:
        n = 1
        r = 0
        for i in range(2,1000):
            n = n*10 + 1
            n = (n % p)
            if (n == 0):
                r = i
                break
            elif (n == 1):
                r = i-1
                break
            elif (n == 11):
                r = i-2
                break
        if (r != 0):
            print "{0} is a divisor of R({1})".format(p, r)
        prime_mods.append((p,r))

calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME
#print "primes =", primes
calculate_divisors()

# R(10) = 1111111111 = 11 x 41 x 271 x 9091, sum = 9414
SIZE = 1000000000
prime_count = 0
div_count = 0
answer = 0
for (n,r) in prime_mods:
    prime_count += 1
    print "Testing prime({0}) = {1}".format(prime_count, n)

    s = SIZE
    if (r != 0):  s = s % r

    if divisible(n,s):
        div_count += 1
        answer += n
        print "    R({0}) is divisible by prime({1}) which is {2}, {3} divisors fround".format(SIZE, prime_count, n, div_count)
        if (div_count == 20):
            print "Answer =", answer, "div_count =", div_count
            sys.exit()

print "Answer =", answer, "div_count =", div_count


#
# Find the sum of the first forty prime factors of R(10^9).
