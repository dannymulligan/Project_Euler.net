#!/usr/bin/python

import time

############################################################
def calculate_primes(limit):
    """calculate a table of primes < limit"""

    prime_table = [1]*limit
    prime_list = []
    start_time = time.clock()
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    prime_list.append(i)
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            prime_list.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            prime_list.append(i)
        i += 2
    print("There are {:,} primes less than {:,}, calculated in {:.2f} seconds".format(len(prime_list), limit, (time.clock() - start_time)))
    return prime_table, prime_list

# Example call:
#     prime_table, prime_list = primes.calculate_primes(SIZE)


############################################################
def exp_by_sq(x,y,z):
    '''Calculate (x**y % z) efficiently, using recursion'''
    if (y == 1):
        ans = x
    elif ((y % 2) == 0):
        # y is even
        ans = exp_by_sq(x, y/2, z)
        ans = (ans * ans) % z
    else:
        # l is odd
        ans = exp_by_sq(x, (y-1)/2, z)
        ans = (ans * ans) % z
        ans = (x * ans) % z
    return ans


############################################################
import random
def miller_rabin_primality_test(n,s,d,k):
    # True  = n might be prime
    # False = n not prime
    #
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    for kk in range(k):
        a = random.randint(2,n-2)
        x = exp_by_sq(a,d,n)
        if ((x == 1) or (x == n-1)):
            continue
        for r in range(1,s):
            x = ((x*x) % n)
            if (x == 1):  return False
            if (x == n-1):  break
        if (x != n-1):  return False
    return True


############################################################
def is_prime(n, prime_table):
    if n < len(prime_table):
        return prime_table[n] == 1
    s = 0
    d = n - 1
    while ((d % 2) == 0):
        d /= 2
        s += 1
    # n-1 = (2**s)*d
    return miller_rabin_primality_test(n,s,d,4)

if False:
    # Debug test
    prime_table, prime_list = calculate_primes(10*3)
    assert is_prime(51, prime_table) == False
    assert is_prime(53, prime_table) == True
    assert is_prime(5678027, prime_table) == False
    assert is_prime(5678039, prime_table) == True


############################################################


# From: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# There is a deterministic version of the Miller-Rabin primality test that provides an authorative answer
# after testing a smallish number of possible witnesses a
#
#    if n < 2,047, it is enough to test a = 2;
#    if n < 1,373,653, it is enough to test a = 2 and 3;
#    if n < 9,080,191, it is enough to test a = 31 and 73;
#    if n < 25,326,001, it is enough to test a = 2, 3, and 5;
#    if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
#    if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
#    if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
#    if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
#    if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17;
#    if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23.
#
# 3,825,123,056,546,413,051 > 2^61


############################################################
def factors(n, prime_table):
    answer = []
    while (prime_table[n] != 1):
        answer.append(prime_table[n])
        n //= prime_table[n]

    answer.append(n)
    answer.sort()
    return answer


############################################################
import itertools
import operator
import functools
def divisors(n, prime_table):
    n_factors = factors(n, prime_table)
    for l in range(1, len(n_factors)):
        for c in itertools.combinations(n_factors, l):
            yield functools.reduce(operator.mul, c)
