#!/usr/bin/python
#
# Project Euler.net Problem 60
#
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any
# two primes and concatenating them in any order the result will
# always be prime. For example, taking 7 and 109, both 7109 and 1097
# are prime. The sum of these four primes, 792, represents the lowest
# sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two
# primes concatenate to produce another prime.
#
# Answer: 26033
# Solved 10/28/09
# 93 problems solved
# Position #106 on level 2

MAX_PRIME =  10000
factor_table = [1]*MAX_PRIME  # largest factor, 1 means this number is prime
primes = []
def calculate_primes():
    i = 2
    while (i < (MAX_PRIME**.5)):
        if (factor_table[i] == 1):
            j = i*2
            while (j < MAX_PRIME):
                factor_table[j] = i
                j += i
        i += 1
    for i in range(2,MAX_PRIME):
        if (factor_table[i] == 1):
            primes.append(i)

def prime_test(pa,pb):
    ab = int(pa + pb)
    if (ab < MAX_PRIME):
        if (ab not in primes):  return False
    else:
        i = 0
        while (primes[i]**2 < ab):
            if ((ab % primes[i]) == 0):
                return False
            i += 1

    ba = int(pb + pa)
    if (ba < MAX_PRIME):
        if (ba not in primes):  return False
    else:
        i = 0
        while (primes[i]**2 < ba):
            if ((ba % primes[i]) == 0):
                return False
            i += 1

    return True

calculate_primes()
print "{0} primes found less than {1} (largest is {2})".format(len(primes), MAX_PRIME, primes[len(primes)-1])
#primes.remove(2)  # Any number ending in 2 is not prime, so eliminate 2 from search
#primes.remove(5)  # Any number ending in 5 is not prime, so eliminate 5 from search

search_limit = len(primes) - 1
print "Searching primes[0:{0}] = [{1}, ..., {2}, {3}]".format(search_limit, primes[0], primes[search_limit-1], primes[search_limit])
spaces = search_limit - 5
print "Will skip {0} of these primes in any set we try".format(spaces)

top = 5 + spaces
for a in range(0,top-4):
    pa = str(primes[a])

    for b in range(a+1,top-3):
        pb = str(primes[b])
        #print "    2 primes {0}, trying {1}".format([int(pa), int(pb)], [int(pa+pb), int(pb+pa)])
        if (not prime_test(pa, pb)):  continue

        for c in range(b+1,top-2):
            pc = str(primes[c])
            #print "    3 primes {0}, trying {1}".format([int(pa), int(pb), int(pc)], [int(pa+pc), int(pc+pa), int(pb+pc), int(pc+pb)])
            if (not prime_test(pa, pc)):  continue
            if (not prime_test(pb, pc)):  continue

            for d in range(c+1,top-1):
                pd = str(primes[d])
                #print "    4 primes {0}, trying {1}".format([int(pa), int(pb), int(pc), int(pd)], [int(pa+pd), int(pd+pa), int(pb+pd), int(pd+pb), int(pc+pd), int(pd+pc)])
                if (not prime_test(pa, pd)):  continue
                if (not prime_test(pb, pd)):  continue
                if (not prime_test(pc, pd)):  continue

                for e in range(d+1,top):
                    pe = str(primes[e])
                    print "    5 primes {0}, trying {1}".format([int(pa), int(pb), int(pc), int(pd), int(pe)], [int(pa+pe), int(pe+pa), int(pb+pe), int(pe+pb), int(pc+pe), int(pe+pc), int(pd+pe), int(pe+pd)])
                    if (not prime_test(pa, pe)):  continue
                    if (not prime_test(pb, pe)):  continue
                    if (not prime_test(pc, pe)):  continue
                    if (not prime_test(pd, pe)):  continue

                    print "Found {0} (sum = {1})".format([primes[a], primes[b], primes[c], primes[d], primes[e]], (primes[a] + primes[b] + primes[c] + primes[d] + primes[e]))
                    exit()
