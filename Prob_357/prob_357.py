#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 357
#
# Prime generating integers
#
# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
#
# It can be seen that for every divisor d of 30, d+30/d is prime.
#
# Find the sum of all positive integers n not exceeding 100,000,000
# such that for every divisor d of n, d+n/d is prime.
#
# Solved ??/??/14
# ??? problems solved
# Position #??? on level ?

import time
start_time = time.clock()


############################################################
LIMIT_PRIME = 10**8+1
#LIMIT_PRIME = 10**6+1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []


############################################################
def calculate_primes(limit=LIMIT_PRIME):
    start_time = time.clock()
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    primes.append(i)
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 2
    print("There are {} primes less than {}".format(len(primes), limit))
    print("time taken {:.1f} seconds".format(time.clock() - start_time))


def prime(n):
    if prime_table[n] == 1:
        return True
    else:
        return False


def factors(n):
    answer = []
    while True:
        if prime_table[n] == 1:
            answer.append(n)
            answer.sort()
            return answer
        answer.append(prime_table[n])
        n /= prime_table[n]


calculate_primes(limit=LIMIT_PRIME)


############################################################
def eliminate(p, d):
    n = p - 1
    if ((n % d) != 0):
        return False
    p1 = ((n / d) + d)
    if prime_table[p1] != 1:
        #print("    p={p}, n={n}, {d} + {n}/{d} ={p1} not prime".format(p=p, n=n, d=d, p1=p1))
        return True

def gen_possible_n(n_limit):
    for p in primes:
        if p > n_limit:
            return
        if eliminate(p,2):
            continue
        if eliminate(p,3):
            continue
        if eliminate(p,5):
            continue
        if eliminate(p,7):
            continue
        if eliminate(p,11):
            continue
        if eliminate(p,13):
            continue
        if eliminate(p,17):
            continue
        if eliminate(p,19):
            continue
        if eliminate(p,23):
            continue
        if eliminate(p,29):
            continue
        if eliminate(p,31):
            continue
        if eliminate(p,37):
            continue
        if eliminate(p,41):
            continue
        if eliminate(p,43):
            continue
        if eliminate(p,47):
            continue
        yield p-1


############################################################
def product(l):
    n = 1
    for i in l:
        n *= i
    return n


############################################################
import itertools

def test_357(n):
    factor_list = factors(n)
    factor_list.append(1)
    factor_list.sort()
    #print("Factors of {} are {}".format(n, factor_list))
    for l in range(1, len(factor_list)):
        for sublist in itertools.permutations(factor_list, l):
            d = product(sublist)
            if not prime(d + n/d):
            #    print("n={n}, {d} + {n}/{d} = {res} NOT PRIME".format(n=n, d=d, res=d+(n/d)))
                return False
            #else:
            #    print("n={n}, {d} + {n}/{d} = {res} prime".format(n=n, d=d, res=d+(n/d)))
    return True


############################################################
lim = 10**8
answer = 0
for n in gen_possible_n(lim):
    if test_357(n):
        #print("n={n} passes the test".format(n=n))
        answer += n
print("Answer = {}".format(answer))


############################################################
print("time taken {:.1f} seconds".format(time.clock() - start_time))
