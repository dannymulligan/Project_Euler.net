#!/usr/bin/python
#
# Project Euler.net Problem 266
#
# Pseudo Square Root
#
# The divisors of 12 are: 1,2,3,4,6 and 12.
# The largest divisor of 12 that does not exceed the square root of 12
# is 3.
# We shall call the largest divisor of an integer n that does not
# exceed the square root of n the pseudo square root (PSR) of n.  It
# can be seen that PSR(3102)=47.
# 
# Let p be the product of the primes below 190.
# Find PSR(p) mod 10^16.
#
# Answer: 1096883702440585
# Solved 12/18/09
# 110 problems solved
# Position #853 on level 3

# 3102 = 2*3*11*47
# There are 42 primes less than 190
# They are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
# 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
# 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]

import itertools
import math
import operator

MOD = 10**16
LIMIT_PRIME = 190
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = [1]  # Put a 1 at the start of the list of primes
logs = []     # So that we can have a 0 at the start of the list of logs
A_cnt = 0
A_cache_cnt = 0

A_cache = []
A_cache_threshold = 0

def calculate_primes():
    i = 2
    while (i < (LIMIT_PRIME/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i*2
            while (j < LIMIT_PRIME):
                prime_table[j] = i
                j += i
        i += 1
    while (i < LIMIT_PRIME):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 1

def calculate_logs():
    for i in primes:
        logs.append(math.log(i))

# This problem is a variation of the Knapsack problem.  From Wikipedia...
# http://en.wikipedia.org/wiki/Knapsack_problem
#
# 0-1 knapsack problem
#
# A similar dynamic programming solution for the 0-1 knapsack problem
# also runs in pseudo-polynomial time. As above, assume w1, ..., wn, W
# are strictly positive integers. Define A(j, Y) to be the maximum
# value that can be attained with weight less than or equal to Y using
# items up to j.
# 
# We can define A(j,Y) recursively as follows:
#
#     * A(0, Y) = 0
#     * A(j, 0) = 0
#     * A(j, Y) = A(j - 1, Y)  if wj > Y
#     * A(j, Y) = max { A(j - 1, Y),  pj + A(j - 1, Y - wj) }  if wj <= Y.
#
# The solution can then be found by calculating A(n, W). To do this
# efficiently we can use a table to store previous computations. This
# solution will therefore run in O(nW) time and O(nW) space.
def A(j,Y):
    #print "=> A({0},{1})".format(j,Y)
    global A_cnt
    A_cnt += 1
    if (j == 0):  return (0.0, [])
    if (Y == 0.0):  return (0.0, [])
    if (j == A_cache_threshold):  return lookup_A_cache(Y)

    if (logs[j] > Y):
        ans = A(j-1,Y)
    else:
        a = A(j-1,Y)
        b = A(j-1,Y-logs[j])
        rem = b[0] + logs[j]
        if (a[0] > rem):
            ans = a
        else:
            sol = list(b[1])
            sol.append(primes[j])
            ans = (rem, sol)

    if ((A_cnt % 100000) == 0):
        print "A({0},{1}) = {2}".format(j, Y, ans)

    return ans
# Tried keeping a cache of results of calls to A(j,Y), but the cache
# never ended up providing a result, it was a 'write-only' data structure

def fill_A_cache():
    print "Generating A_cache"
    global A_cache_threshold
    cutoff_point = len(primes)/2
    A_cache_threshold = cutoff_point
    print "cutoff_point =", cutoff_point
    print "A_cache_threshold = {0}, prime[{0}] == {1}".format(A_cache_threshold,primes[A_cache_threshold])
    A_cache.append((0,[]))
    for n in range(cutoff_point-1):
        #print "Filling with combinations of", n+1, "items from", primes[1:cutoff_point]
        for i in itertools.combinations(primes[1:cutoff_point],n+1):
            result = math.log(reduce(operator.mul, i))
            A_cache.append((result, list(i)))
    A_cache.sort()
    print "Finished generating A_cache"


def lookup_A_cache(Y):
    #print "=> lookup_A_cache({0})".format(Y)
    global A_cache_cnt
    A_cache_cnt += 1
    if (Y > A_cache[-1][0]):
        return A_cache[-1]

    top = len(A_cache)-1
    bot = 0
    # until ((A_cache[bot][0] < Y) & (A_cache[top][0] > Y) & ((top-bot)==1)):
    while ((A_cache[bot][0] > Y) | (A_cache[top][0] < Y) | (top-bot>1)):
        mid = (top + bot)/2
        #print "A_cache[{0}] = {3}, A_cache[{1}] = {4}, A_cache[{2}] = {5}".format(bot,mid,top,A_cache[bot],A_cache[mid],A_cache[top])
        if (A_cache[mid][0] > Y):
            top = mid
        else:
            bot = mid
    #print "A_cache[{0}] = {3}, A_cache[{2}] = {5}".format(bot,mid,top,A_cache[bot],A_cache[mid],A_cache[top])
    return A_cache[bot]

calculate_primes()
# 3102 = 2*3*11*47
#primes = [1, 2, 3, 11, 47]
calculate_logs()
target = sum(logs)/2

fill_A_cache()

print "There are", len(primes), "primes less than", LIMIT_PRIME
print "MOD =", MOD
print "primes =", primes
print "logs =", logs
print "target =", target

print A(22,79.3171764428)

print "Running A({0},{1})".format(len(logs)-1, target)
res = A(len(logs)-1, target)
#res = (0.0, [1])
print res[0]
print res[1]

print "A_cnt =", A_cnt
print "A_cache_cnt =", A_cache_cnt
target = reduce(operator.mul, primes)
print "Target =", target, "=", primes
print "sqrt(Target) =", float(target)**.5
result = reduce(operator.mul, res[1])
print "Result =", result, "=", res[1]
print "Result mod {0} = {1}".format(MOD, result % MOD)

print "Answer is {0}".format(result % MOD)

#selftest()


# From the forum at: http://eulersolutions.49.forumer.com/viewtopic.php?f=3&t=28
# The answer is 2323218950659046189161096883702440585
# = 5 * 464643790131809237832219376740488117
# = 5 * 11 * 42240344557437203439292670612771647
# = 5 * 11 * 17 * 2484726150437482555252510036045391
# = 5 * 11 * 17 * 23 * 108031571758151415445761305915017
# = 5 * 11 * 17 * 23 * 29 * 3725226612350048808474527790173
# = 5 * 11 * 17 * 23 * 29 * 31 * 120168600398388671241113799683
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 3247800010767261384894967559
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 69102127888665135848829097
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 1303813733748398789600549
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 22098537860142352366111
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 329828923285706751733
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 4645477792756433123
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 55969611960920881
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 89 * 628872044504729
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 89 * 97 * 6483216953657
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 89 * 97 * 103 * 62943853919
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 89 * 97 * 103 * 107 * 588260317
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 89 * 97 * 103 * 107 * 127 * 4631971
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 89 * 97 * 103 * 107 * 127 * 157 * 29503
# = 5 * 11 * 17 * 23 * 29 * 31 * 37 * 47 * 53 * 59 * 67 * 71 * 83 * 89 * 97 * 103 * 107 * 127 * 157 * 163 * 181


