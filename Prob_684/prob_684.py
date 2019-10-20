#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 684
#
# Inverse Digit sum
#
# Define s(n) to be the smallest number that has a digit sum of n. For
# example s(10)=19.
#
# Let S(k)=sum{n=1,k}s(n). You are given S(20)=1074.
#
# Further let f{i} be the Fibonacci sequence defined by f{0} = 0,
# f{1} = 1 and f{i} = f{i-2} + f{i−1} for all i >= 2.
#
# Find sum{i=2,90}S(f{i}). Give your answer modulo 1000000007.


import sys
#print(sys.version)
import time
start_time = time.clock()

MOD = 1000000007  # first prime number after 10^9
#MOD = 100000000000000000000000000000
SIZE = 63  # F90 = 2880067194370816120, which requires 62 bit to store


###############################################################################

def s_simple(n):
    result = 0
    power = 1
    while n > 9:
        result += 9* power
        n -= 9
        power *= 10
    result += n * power
    return result

def s(n):
    result = 0
    power = 1
    while n > 9:
        result = (result + 9* power) % MOD
        n -= 9
        power = (10 * power) % MOD
    result += n * power
    return result % MOD

if False:
    answer = 0
    for n in range(1, 210):
        s_n = s(n)
        ss_n = s_simple(n)
        answer += s_n
        same = (ss_n % MOD) == s_n
        print("s({}) = {}, s_simple({}) = {}, {}".format(n, s_n, n, ss_n, same))

###############################################################################

def log2(n):
    '''Return the log base 2 of n, rounded up to the next integer.
       Or, number of bits needed to store n as an unsigned integer.'''
    answer = 0
    while n > 0:
        answer += 1
        n //= 2
    return answer

###############################################################################

lookup_10_2n_mod = []
num = 10
for n in range(SIZE):
    lookup_10_2n_mod.append(num)  # 10^(2^n) % MOD
    num = (num * num) % MOD

if False:
    for n in range(SIZE):
        print(n, lookup_10_2n_mod[n])

lookup_2n_9s_mod = []
num = 9
for n in range(SIZE):
    lookup_2n_9s_mod.append(num)  # (2^n) 9's % MOD
    num = (num + (num * lookup_10_2n_mod[n])) % MOD

if False:
    for n in range(SIZE):
        print(n, lookup_2n_9s_mod[n])

def n9s_mod(n):
    '''Calculate n 9's % MOD'''
    answer = 0
    p = 0
    while (n > 0):
        if (n % 2) == 1:
            # Need to multiply by 10^(2^p), then add 2^p 9's
            # Example, if p=3, then we need to multiply by 10^8, then add 99999999
            answer = (answer * lookup_10_2n_mod[p]) % MOD
            #print("    answer = answer * {}".format(lookup_10_2n_mod[p]))
            answer = (answer + lookup_2n_9s_mod[p]) % MOD
            #print("    answer = answer + {} = {}".format(lookup_2n_9s_mod[p], answer))

        n = n // 2
        p += 1
    return answer

if False:
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1112]:
        ans = n9s_mod(x)
        num = int('9'*x) % MOD
        assert ans == num
        print(x, ans, num)

def _10n_mod(n):
    '''Calculate 10^n % MOD, with arbitrary n'''
    #print("_10n_mod({})".format(n))
    answer = 1
    p = 0
    while (n > 0):
        if (n % 2) == 1:
            # Need to multiply by 10^(2^p)
            # Example, if p=3, then we need to multiply by 10^8
            answer = (answer * lookup_10_2n_mod[p]) % MOD
            #print("    answer = answer * {}".format(lookup_10_2n_mod[p]))

        n = n // 2
        p += 1
    return answer

if False:
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1112]:
        ans = _10n_mod(x)
        num = 10**x % MOD
        print(x, ans, num)
        assert ans == num

def s(n):
    nines = n // 9
    first = n - (9*nines)

    if (n == 0):
        n_str = "0"
    elif (first == 0):
        n_str = "9"*nines
    else:
        n_str = "{}".format(first) + "9"*nines

    print("s({}) is {} followed by {} nines = {}".format(n, first, nines, n_str))
    return int(n_str)

answer = 0
for x in range(1, 21):
    answer += s(x)
print("S(20) = {}".format(answer))


###############################################################################

def f(n_max):
    n = 0
    fn_1 = 0
    yield fn_1  # f_0

    n += 1
    fn = 1
    yield fn  # f_1

    while n < n_max:
        _, fn_1, fn = fn_1, fn, fn_1+fn
        n += 1
        yield fn

if False:
    for n, fn in enumerate(f(90)):
        print("f({}) = {}".format(n, fn))

    sys.exit(0)

###############################################################################

answer = 0
for n, fn in enumerate(f(9)):
    if n > 2:
        print("f({}) = {}, {} bits required".format(n, fn, log2(fn)))
print("F{} = {}".format(n, fn))
print("{} bits required".format(log2(fn)))

print("Answer = {}".format(answer))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
