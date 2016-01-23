#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 381
#
# (prime-k) factorial
#
# For a prime p let S(p) = ((p-k)!) mod(p) for 1<=k<=5.
#
# For example, if p=7,
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

import sys
import time
start_time = time.clock()

########################################
LIMIT = 10**5


########################################
LIMIT_PRIME = LIMIT
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
    #x = fact(p-1, p)
    #answer = (answer + x) % p
    #print(" {:3}".format(x)),

    # fact(p-2,p) is always 1
    #x = fact(p-2, p)
    #answer = (answer + x) % p
    #print("+ {:3}".format(x)),

    # fact(p-3,p) is always (p-1)/2
    x = (p-1)/2
    #x = fact(p-3, p)
    answer = (answer + x) % p
    #print("+ {:3}".format(x)),

    # fact(p-5,p) varies
    x = fact(p-5, p)
    answer = (answer + x) % p
    #print("+ {:3}".format(x)),

    # fact(p-4,p) varies
    #x = fact(p-4, p)
    x = (x * (p - 4)) % p
    answer = (answer + x) % p
    #print("+ {:3}".format(x)),

    #print(" = {}".format(answer))

    return answer

#assert s(7) == 4


########################################

answer = 0
for p in range(5, LIMIT):
    if (p % 1000) == 0:
        print p
    if not is_prime(p):
        continue
    x = s(p)
    #print("s({}) = {}".format(p, x))
    answer += x

print("Answer = {}".format(answer))

print("Time taken = {0} seconds".format(time.clock() - start_time))
