#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 387
#
# Harshad Numbers
#
# A Harshad or Niven number is a number that is divisible by the sum
# of its digits.
#
# 201 is a Harshad number because it is divisible by 3 (the sum of its
# digits.)
#
# When we truncate the last digit from 201, we get 20, which is a
# Harshad number.
#
# When we truncate the last digit from 20, we get 2, which is also a
# Harshad number.
#
# Let's call a Harshad number that, while recursively truncating the
# last digit, always results in a Harshad number a right truncatable
# Harshad number.
#
# Also:
# 201/3=67 which is prime.
#
# Let's call a Harshad number that, when divided by the sum of its
# digits, results in a prime a strong Harshad number.
#
# Now take the number 2011 which is prime.
#
# When we truncate the last digit from it we get 201, a strong Harshad
# number that is also right truncatable.
#
# Let's call such primes strong, right truncatable Harshad primes.
#
# You are given that the sum of the strong, right truncatable Harshad
# primes less than 10000 is 90619.
#
# Find the sum of the strong, right truncatable Harshad primes less
# than 10^14.
#
# Solved ??/??/14
# ??? problems solved
# Position #??? on level ?

import time
start_time = time.clock()

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
import random
def miller_rabin_primality_test(n,s,d,k):
    # True  = n might be prime
    # False = n not prime
    #
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    for kk in xrange(k):
        a = random.randint(2,n-2)
        x = exp_by_sq(a,d,n)
        if ((x == 1) or (x == n-1)):
            continue
        for r in xrange(1,s):
            x = ((x*x) % n)
            if (x == 1):  return False
            if (x == n-1):  break
        if (x != n-1):  return False
    return True


############################################################
def is_prime(n):
    #print("is_prime({})".format(n))
    if (n == 1) or (n == 2) or (n ==3):
        return True
    s = 0
    d = n - 1
    while ((d % 2) == 0):
        d /= 2
        s += 1
    # n-1 = (2**s)*d
    return miller_rabin_primality_test(n,s,d,4)


############################################################
def is_harshad(num):
    sum_of_digits = 0
    n = num
    while n > 0:
        sum_of_digits += n % 10
        n /= 10
    return ((num % sum_of_digits) == 0)


############################################################
def is_strong_harshad(num):
    #print("is_strong_harshad({})".format(num))
    sum_of_digits = 0
    n = num
    while n > 0:
        sum_of_digits += n % 10
        n /= 10

    if ((num % sum_of_digits) != 0):
        return False

    return is_prime(num / sum_of_digits)


############################################################
def right_truncatable_harshad(n_limit):
    '''Generate right truncatable harshad
    numbers < n_limit'''

    next_round = []
    for i in range(1,10):
        next_round.append(i)
        # 1..9 are harshad numbers,
        # but not right truncatable

    while len(next_round) > 0:
        this_round = next_round[:]
        next_round = []
        for n in this_round:
            if n*10 >= n_limit:
                break
            #print("Trying to create Harshad numbers that truncate to {}".format(n))
            for i in range(10):
                if n*10+i >= n_limit:
                    #print("n*10+i = {}".format(n*10+i))
                    break
                #if (n > 200):
                #    print("testing {}".format(n*10+i))
                if is_harshad(n*10+i):
                    next_round.append(n*10+i)
                    yield n*10+i


############################################################
LIMIT = 10**14
rth_numbers = []
srth_numbers = []
for i in right_truncatable_harshad(LIMIT/10):
    rth_numbers.append(i)
    if is_strong_harshad(i):
        srth_numbers.append(i)

print("Found {} right truncatable harshad numbers less than {}".format(len(rth_numbers), LIMIT/10))
if len(rth_numbers) < 50:
    print("They are {}".format(rth_numbers))
print("")

print("Found {} strong right truncatable harshad numbers less than {}".format(len(srth_numbers), LIMIT/10))
if len(srth_numbers) < 50:
    print("They are {}".format(srth_numbers))
print("")

srth_primes = []
for n in srth_numbers:
    for i in range(10):
        if is_prime(n*10+i) and (n >= 10):
            #print("{} is a strong, right truncatable Harshad prime".format(n*10+i))
            srth_primes.append(n*10+i)

print("Found {} right truncatable harshad primes less than {}".format(len(srth_primes), LIMIT))
if len(srth_primes) < 50:
    print("They are {}".format(srth_primes))
print("")

answer = sum(srth_primes)
print("The sum of all strong right truncatable harshad primes below {} is {}".format(LIMIT, answer))
print("Answer = {}".format(answer))


print("time taken {:.1f} seconds".format(time.clock() - start_time))
