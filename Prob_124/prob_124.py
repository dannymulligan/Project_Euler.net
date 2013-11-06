#!/usr/bin/python
#
# Project Euler.net Problem 124
# 
# The radical of n, rad(n), is the product of distinct prime factors
# of n. For example:
#     504 = 2^3 x 3^2 x 7
# so
#     rad(504) = 2 x 3 x 7 = 42.
# 
# If we calculate rad(n) for 1 <= n <= 10, then sort them on rad(n),
# and sorting on n if the radical values are equal, we get:
#
#     Unsorted        Sorted
#     n  rad(n)     n  rad(n) k
#     1    1        1    1    1
#     2    2        2    2    2
#     3    3        4    2    3
#     4    2        8    2    4
#     5    5        3    3    5
#     6    6        9    3    6
#     7    7        5    5    7
#     8    2        6    6    8
#     9    3        7    7    9
#    10   10       10   10   10
# 
# Let E(k) be the kth element in the sorted n column; for example,
# E(4) = 8 and E(6) = 9.
# 
# If rad(n) is sorted for 1 <= n <= 100000, find E(10000).
#
# Solved 09/05/10
# 122 problems solved
# Position #656 on level 3

MAX =  100000+1

factor_table = [1]*(1+MAX)  # largest factor, 1 means this number is prime
def calculate_factors():
    i = 2
    while i <= (MAX/2):
        if factor_table[i] == 1:
            j = i*2
            while j <= MAX:
                factor_table[j] = i
                #print "factor_table[{0}] = {1}".format(j, i)
                j += i
        i += 1

print "Calculating factors with MAX={0}".format(MAX)
calculate_factors()

rad_table = []
for n in range(1,MAX):
    nn = n
    factors = []
    prev_factor = n

    # Prime number
    if factor_table[nn] == 1:
        factors.append(nn)

    # Not a prime number
    while factor_table[nn] != 1:
        #print "    {0} is divisible by {1}".format(nn, factor_table[nn])
        if factor_table[nn] != prev_factor:
            factors.append(factor_table[nn])
            prev_factor = factor_table[nn]
        nn /= factor_table[nn]

    if nn != prev_factor:
        factors.append(nn)

    # Calculate rad(n)
    rad = 1
    for nn in factors:
        rad *= nn

    # Add to the list
    rad_table.append([rad, n])

rad_table.sort()

(rad, n) = rad_table[9999]
print rad_table[9999]
print "Answer =", n
