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
# Answer: 
# Solved 12/??/09
# ??? problems solved
# Position #??? on level 3

# 3102 = 2*3*11*47
# There are 42 primes less than 190
# They are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
# 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
# 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]

import math
import operator

MOD = 10**16
LIMIT_PRIME = 100
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = [1]  # Put a 1 at the start of the list of primes
logs = []     # So that we can have a 0 at the start of the list of logs
A_cnt = 0

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

    if (logs[j] > Y):
        ans = A(j-1,Y)
    else:
        a = A(j-1,Y)
        b = A(j-1,Y-logs[j])
        rem = b[0] + logs[j]
        if (a[0] > rem):
            ans = a
        else:
            sol = b[1]
            sol.append(primes[j])
            ans = (rem, sol)

    if ((A_cnt % 1000000) == 0):
        print "A({0},{1}) = {2}".format(j, Y, ans)

    return ans
# Tried keeping a cache of results of calls to A(j,Y), but the cache
# never ended up providing a result, it was a 'write-only' data structure

calculate_primes()
# 3102 = 2*3*11*47
#primes = [1, 2, 3, 11, 47]
calculate_logs()
target = sum(logs)/2


print "There are", len(primes), "primes less than", LIMIT_PRIME
print "MOD =", MOD
print "primes =", primes
print "logs =", logs
print "target =", target

#target = target * 0.1
print "Running A({0},{1})".format(len(logs)-1, target)
res = A(len(logs)-1, target)
print res[0]
print res[1]

print "A_cnt =", A_cnt
target = reduce(operator.mul, primes)
print "Target =", target, "=", primes
print "sqrt(Target) =", float(target)**.5
result = reduce(operator.mul, res[1])
print "Result =", result, "=", res[1]
print "Result mod {0} = {1}".format(MOD, result % MOD)

#selftest()
