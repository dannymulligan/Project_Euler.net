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
# Answer: 
# Solved
# ?? problems solved
# Position #??? on level 2

MAX_PRIME =  1000000
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

calculate_primes()
print "{0} primes found less than {1} (largest is {2})".format(len(primes), MAX_PRIME, primes[len(primes)-1])
primes.remove(2)  # Any number ending in 2 is not prime, so eliminate 2 from search
primes.remove(5)  # Any number ending in 5 is not prime, so eliminate 5 from search

i = 1
while (int(str(primes[i]) + str(primes[i-1])) < (primes[len(primes)-1])):
    i += 1
search_limit = i - 1
print "Searching primes[0:{0}] = [{1}, ..., {2}, {3}]".format(search_limit, primes[0], primes[search_limit-1], primes[search_limit])
spaces = search_limit - 5
print "Will skip {0} of these primes in any set we try".format(spaces)

top = 5 + spaces
for a in range(0,top-4):
    pa = str(primes[a])

    for b in range(a+1,top-3):
        pb = str(primes[b])
        #print "    2 primes {0}, trying {1}".format([int(pa), int(pb)], [int(pa+pb), int(pb+pa)])
        if (factor_table[int(pa + pb)] != 1):  continue
        if (factor_table[int(pb + pa)] != 1):  continue

        for c in range(b+1,top-2):
            pc = str(primes[c])
            #print "    3 primes {0}, trying {1}".format([int(pa), int(pb), int(pc)], [int(pa+pc), int(pc+pa), int(pb+pc), int(pc+pb)])
            if (factor_table[int(pa + pc)] != 1):  continue
            if (factor_table[int(pc + pa)] != 1):  continue
            if (factor_table[int(pb + pc)] != 1):  continue
            if (factor_table[int(pc + pb)] != 1):  continue

            for d in range(c+1,top-1):
                pd = str(primes[d])
                #print "    4 primes {0}, trying {1}".format([int(pa), int(pb), int(pc), int(pd)], [int(pa+pd), int(pd+pa), int(pb+pd), int(pd+pb), int(pc+pd), int(pd+pc)])
                if (factor_table[int(pa + pd)] != 1):  continue
                if (factor_table[int(pd + pa)] != 1):  continue
                if (factor_table[int(pb + pd)] != 1):  continue
                if (factor_table[int(pd + pb)] != 1):  continue
                if (factor_table[int(pc + pd)] != 1):  continue
                if (factor_table[int(pd + pc)] != 1):  continue

                for e in range(d+1,top):
                    pe = str(primes[e])
                    print "    5 primes {0}, trying {1}".format([int(pa), int(pb), int(pc), int(pd), int(pe)], [int(pa+pe), int(pe+pa), int(pb+pe), int(pe+pb), int(pc+pe), int(pe+pc), int(pd+pe), int(pe+pd)])
                    if (factor_table[int(pa + pe)] != 1):  continue
                    if (factor_table[int(pe + pa)] != 1):  continue
                    if (factor_table[int(pb + pe)] != 1):  continue
                    if (factor_table[int(pe + pb)] != 1):  continue
                    if (factor_table[int(pc + pe)] != 1):  continue
                    if (factor_table[int(pe + pc)] != 1):  continue
                    if (factor_table[int(pd + pe)] != 1):  continue
                    if (factor_table[int(pe + pd)] != 1):  continue

                    print "Found {0} (sum = {1})".format([primes[a], primes[b], primes[c], primes[d], primes[e]], (primes[a] + primes[b] + primes[c] + primes[d] + primes[e]))
                    exit()
