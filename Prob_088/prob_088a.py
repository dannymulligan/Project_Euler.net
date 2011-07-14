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
# Solved 11/2/09
# 95 problems solved
# Position #57 on level 2

MAX_PRIME =  100000
MAX_K =  12000
MAX_N =  25000

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
    #print "Called all_partitions({0})".format(nums)
    yield nums

    if (len(nums) > 1):
        for i in range(len(nums)):
            # Pick which item to merge
            mult = nums[i]
            #print i, mult, nums

            # Skip this item is if it a repeat of the previous item in nums
            if (i > 0):
                if (nums[i-1] == nums[i]):  continue

            # Merge that item with every other item on the list
            nums1 = list(nums)
            del nums1[i]  # nums1 is a new list without the item we're merging
            #print nums1
            for j in range(i,len(nums1)):

                # Skip this item is if it a repeat of the previous item in nums1
                if (j > 0):
                    if (nums1[j-1] == nums1[j]):  continue

                nums2 = nums1[:j] + [mult*nums1[j]] + nums1[j+1:]
                nums2.sort()
                #print j, nums2

                # Recurse to shorter lists
                for nums3 in all_partitions(nums2):
                    yield nums3
                    #print nums3
    #print "Exited all_partitions({0})".format(nums)
      

##for nums in [[9], [4, 7], [2, 3, 4], [2, 3, 4, 5]]:
##    print "================"
##    cnt = 0
##    print "Looking for partitions of", nums
##    for nums1 in all_partitions(nums):
##        print "{0}: Got {1}".format(cnt, nums1)
##        cnt += 1
##
##print "================"
##for cnt in range(2,9):
##    xx = 0
##    for x in all_partitions([2]*cnt):
##        xx += 1
##    print "With a list of {0} identical items, all_partitions() produces {1} results".format(cnt, xx)
##
##print "================"
##for cnt in range(2,9):
##    xx = 0
##    for x in all_partitions(range(1,cnt+1)):
##        xx += 1
##    print "With a list of {0} different items, all_partitions() produces {1} results".format(cnt, xx)
##
##exit()
##
##def all_p_test():
##    print "Running all_p_test()"
##    #for i in all_partitions([3,2,2]):
##    cnt = 0
##    for i in all_partitions([2, 2, 3, 3]):
##        cnt += 1
##        print cnt, i
##    cnt = 0
##    cnt1 = 0
##    for i in all_partitions([2, 2, 2, 2, 3, 3, 3, 3]):
##        cnt += 1
##        if (i == [1296]):  cnt1 += 1
##    print cnt, cnt1, i
##
##    cnt = 0
##    cnt1 = 0
##    for i in all_partitions([2, 2, 2, 2, 2, 3, 3, 5]):
##        cnt += 1
##        if (i == [1440]):  cnt1 += 1
##        print i
##    print cnt, cnt1, i
##
##all_p_test()
##exit()

print "Running with MAX_PRIME={0}, MAX_K={1}, MAX_N={2}".format(MAX_PRIME, MAX_K, MAX_N)
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
    num_factors = len(factors)
    factors.sort()
    #if (N in [349, 350, 509, 510, 511, 512]):
    #    print "{0} factors of {1} are: {2}".format(num_factors,N,factors)

    # Find the product-sum numbers for N
    if (len(Ks_to_do) < 10):
        print "{0}: Trying partitions of {1}".format(N, factors)
    for p in all_partitions(factors):
        k = len(p) + N - sum(p)
        if (k <= MAX_K) & (len(p) > 1):
            if (best_N[k] == 0) | (N < best_N[k]):
                best_N[k] = N
                Ks_to_do.remove(k)
                sol = [1]*(N-sum(p)) + p
                sol.sort()
                sol.reverse()
                #print "best_N[{0}] = {1}, {2}".format(k, N, sol)
                #print "best_N[{0}] = {1}, {2} K's left to do".format(k, N, len(Ks_to_do))
                if ((len(Ks_to_do) % 100) == 0):
                    print "best_N[{0}] = {1}, {2} K's left to do".format(k, N, len(Ks_to_do))
                if (len(Ks_to_do) < 10):
                    print "best_N[{0}] = {1}, {2} K's left to do, {3}".format(k, N, len(Ks_to_do), Ks_to_do)

    if (len(Ks_to_do) == 0):
        print "Found all minimal product-sum numbers for 2 <= k <= {0}.  Finished search with N = {1}".format(MAX_K, N)
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
print "{0} values of K for which solution not found: {1}".format(len(Ks_to_do), Ks_to_do)
