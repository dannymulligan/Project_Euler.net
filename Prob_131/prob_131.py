#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 131
#
# Determining primes, p, for which n^3 + p*n^2 is a perfect cube.
#
# There are some prime values, p, for which there exists a positive
# integer, n, such that the expression n^3 + p*n^2 is a perfect cube.
#
# For example, when p = 19, 83 + 82×19 = 123.
# 
# What is perhaps most surprising is that for each prime with this
# property the value of n is unique, and there are only four such
# primes below one-hundred.
#
# How many primes below one million have this remarkable property?
#
# Solved ??/??/11
# 139 problems solved
# Position #232 on level 3

LIMIT_PRIME = 1000000  # There are 78,498 primes less than 1,000,000
LIMIT_PRIME = 100000   # There are 9,592 primes less than 100,000
LIMIT_PRIME = 10000    # There are 1,229 primes less than 10,000
LIMIT_PRIME = 1000     # There are 168 primes less than 1,000
LIMIT_PRIME = 100      # There are 25 primes less than 100
#LIMIT_PRIME = 25       # There are 9 primes less than 25
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

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


calculate_primes()
print "There are", len(primes), "primes less than", LIMIT_PRIME


def l_eqn(p, n):
    return p * n**2

def r_eqn(n, m):
    return 3*(n**2 * m) + 3*(n * m**2) + m**3

# Assume X^3 is a perfect cube, and X = (M + N)
# Then
#     X^3 = (N + M)^3 = N^3 + 3(N^2 * M) + 3(N * M^2) + M^3
#
# If we have N^3 + P * N^2 as a perfect cube, then we have
#
#      N^3 + P * N^2 = N^3 + 3*N^2*M + 3*N*M^2 + M^3
#            P * N^2 =       3*N^2*M + 3*N*M^2 + M^3
#            P * N^2 = N^2*3*M + 3*N*M^2 + M^3
#            P * N^2 = N^2(3*M - P) + 3*N*M^2 + M^3
#    N^2 * (P - 3*M) = M^3
#
# For every value of P, we need to search N and M looking for cases
# where this equation is true.
# We fix P and N, and increment M looking for a solution.
# If the right side is larger than the left, we need to move to the next N.
# If the right side is larger then the left when M = 1, we need to go to the next P.
# If we run out of P then we are done.

solns = []
answer = 0
for p in primes:
    print "**** Searching with p = {0}".format(p)
    n = 1
    m = 1
    l = l_eqn(p,n)
    r = r_eqn(n,m)

    #print "Trying (n,m,p) = ({0},{1},{2}), l={3}, r={4}".format(n,m,p,l,r)
    if (l == r):
       solns.append((n,m,p))
       print "    Found solution ({0},{1},{2})".format(n,m,p)
       continue

    while ((l > r) & (n < p)):
        # Searching larger value of N

        while (l > r):
            # Searching larger values of M
            m += 1
            r = r_eqn(n,m)
            #print "Trying (n,m,p) = ({0},{1},{2}), l={3}, r={4}".format(n,m,p,l,r)
            if (l == r):
               solns.append((n,m,p))
               print "    Found solution ({0},{1},{2})".format(n,m,p)

        n += 1
        m = 1
        l = l_eqn(p,n)
        r = r_eqn(n,m)
        #print "Trying (n,m,p) = ({0},{1},{2}), l={3}, r={4}".format(n,m,p,l,r)

print solns
