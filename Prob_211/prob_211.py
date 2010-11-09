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
# Answer: 1922364685
# Solved 09/07/10
# 123 problems solved
# Position #636 on level 3

# n = 63950000 divisors = [1, 1279, 5, 6395, 25, 31975, 125, 159875, 625, 799375, 3125, 3996875, 2, 2558, 10, 12790, 50, 63950, 250, 319750, 1250, 1598750, 6250, 7993750, 4, 5116, 20, 25580, 100, 127900, 500, 639500, 2500, 3197500, 12500, 15987500, 8, 10232, 40, 51160, 200, 255800, 1000, 1279000, 5000, 6395000, 25000, 31975000, 16, 20464, 80, 102320, 400, 511600, 2000, 2558000, 10000, 12790000, 50000, 63950000] phi2 = 5674460039420172
# n = 63975000 divisors = [1, 853, 5, 4265, 25, 21325, 125, 106625, 625, 533125, 3125, 2665625, 3, 2559, 15, 12795, 75, 63975, 375, 319875, 1875, 1599375, 9375, 7996875, 2, 1706, 10, 8530, 50, 42650, 250, 213250, 1250, 1066250, 6250, 5331250, 6, 5118, 30, 25590, 150, 127950, 750, 639750, 3750, 3198750, 18750, 15993750, 4, 3412, 20, 17060, 100, 85300, 500, 426500, 2500, 2132500, 12500, 10662500, 12, 10236, 60, 51180, 300, 255900, 1500, 1279500, 7500, 6397500, 37500, 31987500, 8, 6824, 40, 34120, 200, 170600, 1000, 853000, 5000, 4265000, 25000, 21325000, 24, 20472, 120, 102360, 600, 511800, 3000, 2559000, 15000, 12795000, 75000, 63975000] phi2 = 6291386896431000
# Answer = 1922364685
# 
# real	81m22.805s
# user	62m50.519s
# sys	1m19.214s

SIZE =  64000000
#SIZE =  1000000

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


def calculate_divisors(factors):
    if (factors == [(1, 1)]):
        return [1]

    if (len(factors) == 1):
        (x, y) = factors[0]
        answer = []
        for i in range(y+1):
            answer.append(x**i)
        return answer

    (x, y) = factors[0]
    answer = []
    for i in calculate_divisors(factors[1:]):
        for j in range(y+1):
            answer.append(i * x**j)
    return answer

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

    divisors = calculate_divisors(factors)

    phi2 = 0
    for i in divisors:
        phi2 += i**2

    if (is_square(phi2)):
        answer += n

    if ((n % 25000) == 0):
        print "n =", n,
        print "divisors =", divisors,
        print "phi2 =", phi2

    
print "Answer =", answer

