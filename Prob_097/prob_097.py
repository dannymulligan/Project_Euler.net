#!/usr/bin/python
#
# Project Euler.net Problem 97
#
# The first known prime found to exceed one million digits was
# discovered in 1999, and is a Mersenne prime of the form 2^(6972593)-1;
# it contains exactly 2,098,960 digits. Subsequently other Mersenne
# primes, of the form 2^(p)-1, have been found which contain more
# digits.
# 
# However, in 2004 there was found a massive non-Mersenne prime which
# contains 2,357,207 digits: 28433x2^(7830457)+1.
# 
# Find the last ten digits of this prime number.
# 
# Answer

#define PRECISION 10
#define LIMIT 1000

#   28,433 x 2^7,830,457 + 1
# = 28,433 x 2 x 2^7,830,456 + 1
# = 56,866 x 2^7,830,456 + 1
# = 56,866 x (2^8)^978,807 + 1
# = 56,866 x 256^978,807 + 1
# = 56,866 x 256 x 256^978,806 + 1
# = 14,557,696 x 256^978,806 + 1
# = 14,557,696 x (256^2)^489,403 + 1
# = 14,557,696 x 65,536^489,403 + 1
# = 14,557,696 x 65,536 x 65,536^489,402 + 1
# = 954,053,165,056 x x (65,536^2)^244,701 + 1

# Initialize with 4,053,165,065 (10 digits)
d = 4053165065

for i in range(244701):
   d *= 65536
   d %= 10**10

d += 1
d %= 10**10

print "Answer =", d
