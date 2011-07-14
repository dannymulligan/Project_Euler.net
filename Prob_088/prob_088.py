#!/usr/bin/python
#
# Project Euler.net Problem 88
#
# A natural number, N, that can be written as the sum and product of a
# given set of at least two natural numbers, {a1, a2, ... , ak} is
# called a product-sum number: N = a1 + a2 + ... + a_(k) = a1 x a2 x
# ... x ak.
# 
# For example, 6  =  1 + 2 + 3  =  1 x 2 x 3.
# 
# For a given set of size, k, we shall call the smallest N with this
# property a minimal product-sum number. The minimal product-sum
# numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
# 
#     k=2:  4  = 2 x 2                  =  2 + 2
#     k=3:  6  = 1 x 2 x 3              =  1 + 2 + 3
#     k=4:  8  = 1 x 1 x 2 x 4          =  1 + 1 + 2 + 4
#     k=5:  8  = 1 x 1 x 2 x 2 x 2      =  1 + 1 + 2 + 2 + 2
#     k=6: 12  = 1 x 1 x 1 x 1 x 2 x 6  =  1 + 1 + 1 + 1 + 2 + 6
# 
# Hence for 2 <= k <= 6, the sum of all the minimal product-sum
# numbers is 4+6+8+12 = 30; note that 8 is only counted once in the
# sum.
# 
# In fact, as the complete set of minimal product-sum numbers for 2 <=
# k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
# 
# What is the sum of all the minimal product-sum numbers for 2 <= k <=
# 12000?
#
# Solved ??/??/09
# ?? problems solved
# Position #?? on level 2

MAX_PRIME =  100000
MAX_K =  12000
MAX_N =  15000

factor_table = [1]*(1+MAX_PRIME)  # largest factor, 1 means this number is prime
def calculate_factors():
    i = 2
    while (i <= (MAX_PRIME/2)):
        if (factor_table[i] == 1):
            j = i*2
            while (j <= MAX_PRIME):
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

##for p in all_perms([2, 2, 2]):
##    print p

def all_partitions(nums):
    yield nums
    if len(nums) > 1:
        for i in range(len(nums)):
            mult = nums[i]
            nums1 = nums[:i] + nums[i+1:]
            for part in all_partitions(nums1):
                for i in range(len(part)):
                    yield part[:i] + [mult*part[i]] + part[i+1:]

##for nums in [[9], [4, 7], [2, 3, 4], [2, 3, 4, 5], range(1,6)]:
##    print "================"
##    cnt = 0
##    print "Looking for partitions of", nums
##    for nums in all_partitions(nums):
##        print "{0}: Got {1}".format(cnt, nums)
##        cnt += 1


calculate_factors()

best_N = [0] * (MAX_K+1)
Ks_to_do = range(2,MAX_K+1)
for N in range(2, MAX_N+1):

    # Find the factors for N
    i = N
    factors = []
    while (i != 1):
        if (factor_table[i] == 1):
            factors.append(i)
            i = 1
        else:
            factors.append(factor_table[i])
            i = i / factor_table[i]
    #print "Factors of {0} are: {1}".format(N,factors)
    num_factors = len(factors)

    # Find the product-sum numbers for N
    for p in all_partitions(factors):
        #print "{0}: Trying {1}".format(N, p)
        k = len(p) + N - sum(p)
        if ((best_N[k] == 0) & (len(p) > 1)):
            print "best_N[{0}] = {1}, ({1} has {2} factors)".format(k, N, num_factors)
            best_N[k] = N
            Ks_to_do.remove(k)

    if (len(Ks_to_do) == 0):
        print "Found best Ns for all k's <= {0}.  Finished search with N = {1}".format(MAX_K, N)
        best_N.sort()
        answer = 0
        prev = best_N[0]
        for i in best_N[1:]:
            if i != prev:
                answer += i
                prev = i
        print "Answer =", answer
        exit()


print "Answer not found with MAX_N = {0}, MAX_K = {1}, try larger MAX_N".format(MAX_N, MAX_K)
print "{0} values of K for which solution not found".format(len(Ks_to_do))
