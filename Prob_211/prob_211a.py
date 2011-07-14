#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 211
#
# Divisor Square Sum
#
# For a positive integer n, let phi2(n) be the sum of the squares of
# its divisors. For example,
#
#     phi2(10) = 1 + 4 + 25 + 100 = 130.
#
# Find the sum of all n, 0 < n < 64,000,000 such that phi2(n) is a
# perfect square.
#
# Solved 09/07/10
# 123 problems solved
# Position #636 on level 3

# n = 63975000 phi2 = 6291386896431000
# Answer = 1922364685
# 
# real	47m49.253s
# user	34m18.937s
# sys	0m47.914s


#SIZE =  64000000
SIZE =  500000

factor_table = [1]*(1+SIZE)  # largest factor, 1 means this number is prime
def calculate_factors():
    i = 2
    while (i <= (SIZE/2)):
        if (factor_table[i] == 1):
            j = i*2
            while (j <= SIZE):
                factor_table[j] = i
                #print "factor_table[{0}] = {1}".format(j, i)
                j += i
        i += 1

def is_square(n):
    i = 1
    lower = 1
    while (i**2 < n):
        lower = i
        i *= 2

    upper = i
    while ((upper**2 > n) & (lower**2 < n) & ((upper-lower) > 1)):
        #print "n =", n, "is between the square of", lower, "and", upper
        mid = (upper + lower) / 2
        #print "trying ", mid
        if (mid**2 > n):
            upper = mid
        else:
            lower = mid

    if (lower**2 == n):
        #print "{0}**2 = {1}".format(lower,n)
        return True
    elif (upper**2 == n):
        #print "{0}**2 = {1}".format(upper,n)
        return True
    else:
        return False


def calculate_phi2(factors):
    phi2 = 1
    for (x, y) in factors:
        z = 0
        for p in range(y+1):
            z += (x**p)**2
        if ((x, y) == (1, 1)):  z = 1
        phi2 *= z
    return phi2

print "Calculating factors with SIZE={0}".format(SIZE)
calculate_factors()

print "Calculating phi2 with SIZE={0}".format(SIZE)
answer = 0
for n in range(1,SIZE):
    nn = n
    factors = []
    prev_factor = 0
    prev_power = 0

    while (factor_table[nn] != 1):
        #print "    {0} is divisible by {1}".format(nn, factor_table[nn])
        if (factor_table[nn] == prev_factor):
            prev_power += 1

        else:
            if (prev_power != 0):
                factors.append((prev_factor, prev_power))
            prev_factor = factor_table[nn]
            prev_power = 1
        nn /= factor_table[nn]

    if (nn == prev_factor):
        prev_power += 1
        factors.append((prev_factor, prev_power))
    else:
        if (prev_power != 0):
            factors.append((prev_factor, prev_power))
        factors.append((nn, 1))

    phi2 = calculate_phi2(factors)

    if (is_square(phi2)):
        answer += n

    if ((n % 25000) == 0):
        print "n =", n,
        print "phi2 =", phi2

print "Answer =", answer

