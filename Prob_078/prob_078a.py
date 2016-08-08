#!/usr/bin/python
#
# Project Euler.net Problem 78
#
# Let p(n) represent the number of different ways in which n coins can
# be separated into piles. For example, five coins can separated into
# piles in exactly seven different ways, so p(5)=7.
#
#     OOOOO
#     OOOO O
#     OOO OO
#     OOO O O
#     OO OO O
#     OO O O O
#     O O O O O
#
# Find the least value of n for which p(n) is divisible by one million.
#
# This sequence is the same as...
#     http://www.research.att.com/~njas/sequences/b000041.txt
#     10001 terms of OEIS sequence A000041
#     Computed by David W. Wilson 2006/10/18

import cProfile

ways_cache = {(2,2):2, (3,3):3}

def ways(n, max_n):

    if ((n <= 1) | (max_n <= 1)):
        return 1

    if (n,max_n) in ways_cache:
        return ways_cache[(n,max_n)]

    ans = 0
    for i in range(min(n,max_n), 0, -1):
        if (n-i,i) in ways_cache:
            ans = ans + ways_cache[(n-i, i)]  # i coins, followed by all possible combinations of n-i
            ans = ans % 1000000
        else:
            ans = ans + ways(n-i, i)  # i coins, followed by all possible combinations of n-i
            ans = ans % 1000000
    ways_cache[(n,max_n)] = ans
    return ans



## # 1m19.124s - run time for non-optimized version
## # 0m17.066s - run time with simple (shortcut for n<=1, or max_n<=1) optimization
## # 0m0.101s - run time with lookup for previously calculated results
## for i in range(1000):
##     print "ways(%d,%d) = %d" %(i, i, ways(i,i))

# 6.493s - run time for range(500)
# 57.147s - run time for range(1000)
for i in range(0,3000,100):
    n = ways(i,i)
    if (n == 0):
        print "Found!!!   ways(%d,%d) %% 1000000 = %d" %(i, i, n)
    if ((i % 25) == 0):
        print "ways(%d,%d) %% 1000000 = %d" %(i, i, n)
        print "len(ways_cache) = %d" %(len(ways_cache))

for i in range(5000,25000):
    n = ways(i,i)
    if (n == 0):
        print "Found!!!   ways(%d,%d) %% 1000000 = %d" %(i, i, n)
    if ((i % 25) == 0):
        print "ways(%d,%d) %% 1000000 = %d" %(i, i, n)
        print "len(ways_cache) = %d" %(len(ways_cache))



# searched: 0 ... 3000

cProfile.run('ways(1001,1001)', 'fooprof')
import pstats
p = pstats.Stats('fooprof')
p.sort_stats('time').print_stats(10)
