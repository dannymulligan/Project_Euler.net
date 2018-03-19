#!/usr/bin/python

import time

############################################################
def calculate_primes(limit, prime_table, prime_list):
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



############################################################
def find_factors(n, prime_list):
    factors = []
    for prime in prime_list:
        while (n % prime) == 0:
            factors.append(prime)
            n = n // prime
        if n == 1:
            return factors
    return factors


############################################################
def exp_by_sq(x,y,z):
    # return (x**y % z)
    if (y == 1):
        # y is 1
        ans = x
    elif ((y % 2) == 0):
        # y is even
        ans = exp_by_sq(x,y/2,z)
        ans = (ans * ans) % z
    else:
        # l is odd
        ans = exp_by_sq(x,(y-1)/2,z)
        ans = (ans * ans) % z
        ans = (x * ans) % z
    return ans


############################################################
def factors(n):
    answer = []
    while (prime_table[n] != 1):
        answer.append(prime_table[n])
        n //= prime_table[n]
        
    answer.append(n)
    answer.sort()
    return answer
