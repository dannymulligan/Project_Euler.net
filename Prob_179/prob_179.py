#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 179
#
# Consecutive positive divisors
#
# Find the number of integers 1 < n < 10^7, for which n and n + 1 have
# the same number of positive divisors. For example, 14 has the
# positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
#
# Solved 08/24/10
# 119 problems solved
# Position #754 on level 3

MAX =  10**7

factor_table = [1]*(1+MAX)  # largest factor, 1 means this number is prime
def calculate_factors():
    i = 2
    while (i <= (MAX/2)):
        if (factor_table[i] == 1):
            j = i*2
            while (j <= MAX):
                factor_table[j] = i
                #print "factor_table[{0}] = {1}".format(j, i)
                j += i
        i += 1

def all_perms(nums):
    if len(nums) <= 1:
        yield nums
    else:
        for perm in all_perms(nums[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + nums[0:1] + perm[i:]


print "Calculating factors with MAX={0}".format(MAX)
calculate_factors()

prev_divisors = 0
answer = 0

for n in range(2,MAX):
    nn = n
    factors = []
    while (factor_table[nn] != 1):
        factors.append(factor_table[nn])
        nn /= factor_table[nn]
    factors.append(nn)

    perms = 1
    prev_factor = 0
    for nnn in factors:
        if (nnn == prev_factor):
            perms /= (factor_cnt+1)
            factor_cnt += 1
            perms *= (factor_cnt+1)
        else:
            factor_cnt = 1
            perms *= (factor_cnt+1)
        prev_factor = nnn

    #print n, factors, perms

    if (prev_divisors == perms):
        #print (n-1), "and", n, "have", perms, "divisors"
        answer += 1
    prev_divisors = perms

print "Answer =", answer
