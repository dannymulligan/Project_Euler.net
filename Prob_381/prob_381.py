#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 381
#
# (prime-k) factorial
#
# For a prime p let S(p) = ((p-k)!) mod(p) for 1 <= k <= 5.
#
# For example, if p = 7,
#     (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)!
#   = 6! + 5! + 4! + 3! + 2!
#   = 720+120+24+6+2
#   = 872.
# As 872 mod(7) = 4, S(7) = 4.
#
# It can be verified that S(p) = 480 for 5 <= p <= 100.
#
# Find S(p) for 5 <= p <= 10^8.
#

# S(100)   = 480
# S(200)   = 2248
# S(500)   = 10623
# S(10**3) = 38140
# S(10**4) = 2882332
# S(10**5) = 226591981
# S(10**6) = 18773749932
# S(10**7) = 1601954022810

import sys
import time
start_time = time.clock()

########################################
LIMIT = 10**8


########################################
LIMIT_PRIME = LIMIT+1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []
#prime_table = [1,2]*(LIMIT_PRIME/2)  # table of largest factor
#primes = [2]

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

calculate_primes()
print("There are {} primes less than {}".format(len(primes), LIMIT_PRIME))
if len(primes) < 30:
    print("They are {}".format(primes))


def is_prime(x):
    return prime_table[x] == 1


########################################

# Simpler but slower
#def modinv(n, p):
#    return (n**(p-2)) % p

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#assert modinv(6, 7) == 6
#assert modinv(5, 7) == 3
#assert modinv(4, 7) == 2
#assert modinv(3, 7) == 5
#assert modinv(2, 7) == 4
#assert modinv(1, 7) == 1


########################################
def fact(n, p):
    f = 1
    for i in range(n, 1, -1):
        f = (f * i) % p
    return f

#assert fact(6, 7) == (720 % 7)
#assert fact(5, 7) == (120 % 7)
#assert fact(4, 7) == ( 24 % 7)
#assert fact(3, 7) == ( 6 % 7)
#assert fact(2, 7) == ( 2 % 7)


########################################

def s(p):
    #print("s({:3}) =".format(p)),
    answer = 0

    # fact(p-1,p) is always p-1
    # fact(p-2,p) is always 1
    # These two terms sum to p, or 0 after the modulus

    # fact(p-3,p) is equal to fact(p-2)/(p-2)
    x = (1 * modinv(p-2, p)) % p
    #print("+ {:3}".format(x)),
    answer = (answer + x) % p

    # fact(p-4,p) is equal to fact(p-3)/(p-3)
    x = (x * modinv(p-3, p)) % p
    #print("+ {:3}".format(x)),
    answer = (answer + x) % p

    # fact(p-5,p) is equal to fact(p-4)/(p-4)
    x = (x * modinv(p-4, p)) % p
    #print("+ {:3}".format(x)),
    answer = (answer + x) % p

    #print(" = {}".format(answer))

    return answer

#assert s(7) == 4


########################################
def sum_s(n):
    sum_s = 0
    for p in range(5, n+1):
        if (p % 100000) == 0:
            print p
        if not is_prime(p):
            continue
        x = s(p)
        sum_s += x
    return sum_s

#assert sum_s(100)  ==   480
#assert sum_s(200)  ==  2248
#assert sum_s(500)  == 10623
#assert sum_s(1000) == 38140


########################################

answer = sum_s(LIMIT)
print("Answer for 5 <= p <= {} is {}".format(LIMIT, answer))

print("Time taken = {0} seconds".format(time.clock() - start_time))
