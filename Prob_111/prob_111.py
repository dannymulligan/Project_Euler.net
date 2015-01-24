#!/usr/bin/python
#
# Project Euler.net Problem 111
#
# Considering 4-digit primes containing repeated digits it is clear
# that they cannot all be the same: 1111 is divisible by 11, 2222 is
# divisible by 22, and so on. But there are nine 4-digit primes
# containing three ones:
#
#     1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
#
# We shall say that M(n, d) represents the maximum number of repeated
# digits for an n-digit prime where d is the repeated digit, N(n, d)
# represents the number of such primes, and S(n, d) represents the sum
# of these primes.
#
# So M(4, 1) = 3 is the maximum number of repeated digits for a
# 4-digit prime where one is the repeated digit, there are N(4, 1) = 9
# such primes, and the sum of these primes is S(4, 1) = 22275. It
# turns out that for d = 0, it is only possible to have M(4, 0) = 2
# repeated digits, but there are N(4, 0) = 13 such cases.
#
# In the same way we obtain the following results for 4-digit primes.
#     Digit,d   M(4,d)   N(4,d)    S(4,d)
#       0         2        13      67061
#       1         3        9       22275
#       2         3        1       2221
#       3         3        12      46214
#       4         3        2       8888
#       5         3        1       5557
#       6         3        1       6661
#       7         3        9       57863
#       8         3        1       8887
#       9         3        7       48073
#
# For d = 0 to 9, the sum of all S(4, d) is 273700.
#
# Find the sum of all S(10, d).
#
# Solved ??/??/10
# ??? problems solved
# Position #??? on level 3

import random
import sys
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
    s = 0
    d = n - 1
    while ((d % 2) == 0):
        d /= 2
        s += 1
    # n-1 = (2**s)*d
    return miller_rabin_primality_test(n,s,d,4)


############################################################
def digits_excluding(n, x):
    # n = number of digits in the number
    # x = digit that is excluded
    if n == 1:
        for i in range(10):
            if i == x:
                continue
            yield [i]
    else:
        for i in range(10):
            if i == x:
                continue
            for j in digits_excluding(n-1, x):
                yield [i] + j

if False:
    print("digits_excluding(3,7)")
    for x in digits_excluding(3,7):
        print x


############################################################
def mixin(s, l):
    # s = sum of list
    # l = length of list
    if l == 1:
        yield [s]
    else:
        for i in range(s+1):
            for r in mixin(s-i, l-1):
                yield [i] + r

if False:
    print("mixin(5,3)")
    for x in mixin(5,3):
        print x


############################################################
def list_to_int(num):
    # num = list of digits
    res = 0
    for x in num:
        res *= 10
        res += x
    return res


############################################################
def build_num(d, r, l):
    # d = repeated digit
    # r = number of times it is repeated
    # l = length of complete number

    for mix in mixin(s=r, l=(l-r+1)):
        if ((mix[0] != 0) & (d == 0)):
            # Skip because leading zero from repeated digit
            #print("Skip because leading zero from repeated digit: mix={}, d={}".format(mix,d))
            continue
        for xxx in digits_excluding(n=(l-r), x=d):
            if ((mix[0] == 0) & (xxx[0] == 0)):
                # Skip because leading zero from xxx
                #print("Skip because leading zero from xxx: mix={}, xxx={}".format(mix, xxx))
                continue
            num = []
            for i in range(l-r):
                for j in range(mix[i]):
                    num.append(d)
                num.append(xxx[i])
            for j in range(mix[-1]):
                num.append(d)
            yield list_to_int(num)

if False:
    print("build_num(d=0, r=3, l=4)")
    for x in build_num(d=0, r=3, l=4):
        print x

if False:
    print("build_num(d=1, r=3, l=4)")
    for x in build_num(d=1, r=3, l=4):
        print x

if False:
    print("build_num(d=0, r=3, l=5)")
    for x in build_num(d=0, r=3, l=5):
        print x

if False:
    print("build_num(d=1, r=3, l=5)")
    for x in build_num(d=1, r=3, l=5):
        print x


############################################################
def calculate_primes_with_repeated_digits(repeated_digit, repeat_count, total_length):
    primes = list()
    for x in build_num(d=repeated_digit, r=repeat_count, l=total_length):
        if is_prime(x):
            primes.append(x)
    return primes

if False:
    l = 4
    for d in range(10):
        #print("calculate_primes_with_repeated_digits(repeated_digit={d}, repeat_count=3, total_length={l})".format(d=d, l=l))
        x = calculate_primes_with_repeated_digits(repeated_digit=d, repeat_count=3, total_length=l)
        print("d={d}, M({l},{d})={m}, N({l},{d})={n}, S({l},{d})={s}, primes={x}".format(d=d, l=l, m=3, n=len(x), s=sum(x), x=x))


############################################################
def calculate_max_repeat(repeated_digit, total_length):
    for repeat_count in range(total_length-1,1,-1):
        #print("calculate_primes_with_repeated_digits(repeated_digit={}, repeat_count={}, total_length={})".format(repeated_digit, repeat_count, total_length))
        x = calculate_primes_with_repeated_digits(repeated_digit, repeat_count, total_length)
        if len(x) > 0:
            return (repeat_count, x)

if False:
    l = 4
    answer = 0
    for d in range(10):
        (m, x) = calculate_max_repeat(repeated_digit=d, total_length=l)
        print("d={d}, M({l},{d})={m}, N({l},{d})={n}, S({l},{d})={s}".format(d=d, l=l, m=m, n=len(x), s=sum(x)))
        answer += sum(x)
    print("Answer = {}".format(answer))


############################################################
l = 10
answer = 0
for d in range(10):
    (m, x) = calculate_max_repeat(repeated_digit=d, total_length=l)
    print("d={d}, M({l},{d})={m}, N({l},{d})={n}, S({l},{d})={s}".format(d=d, l=l, m=m, n=len(x), s=sum(x)))
    answer += sum(x)


print "Answer =", answer
print "Time taken = {0} seconds".format(time.clock() - start_time)
