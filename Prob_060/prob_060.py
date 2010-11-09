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

MAX_PRIME =  20000
factor_table = [1]*MAX_PRIME  # largest factor, 1 means this number is prime
primes = []
def calculate_primes():
    i = 2
    while (i < (MAX_PRIME/2)):
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
print "{0} primes found less than {1}".format(len(primes), MAX_PRIME)

def test_primes(a, b, c, d, e):
    (sa, sb, sc, sd, se) = (str(a), str(b), str(c), str(d), str(e))

    # ab & ba
    (x,y) = (sa+sb, sb+sa)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # ac & ca
    (x,y) = (sa+sc, sc+sa)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # ad & da
    (x,y) = (sa+sd, sd+sa)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # ae & ea
    (x,y) = (sa+se, se+sa)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # bc & cb
    (x,y) = (sb+sc, sc+sb)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # bd & db
    (x,y) = (sb+sd, sd+sb)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # be & eb
    (x,y) = (sb+se, se+sb)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # cd & dc
    (x,y) = (sc+sd, sd+sc)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # ce & ec
    (x,y) = (sc+se, se+sc)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    # de & ed
    (x,y) = (sd+se, se+sd)
    if ((x >= MAX_PRIME) | (y >= MAX_PRIME)):  return False
    if ((factor_table[int(x)] != 1) | (factor_table[int(y)] != 1)):  return False

    print "Solution found: {0}, {1}".format([a,b,c,d,e], (a+b+c+d+e))
    return True

for spaces in range(len(primes)/2 - 4):
    #print primes[0:5+spaces]
    top = 5 + spaces
    for a in range(0,top-4):
        pa = str(primes[a])

        for b in range(a+1,top-3):
            pb = str(primes[b])
            if (int(pa + pb) not in primes):  continue
            if (int(pb + pa) not in primes):  continue

            for c in range(b+1,top-2):
                pc = str(primes[c])
                if (int(pa + pc) not in primes):  continue
                if (int(pc + pa) not in primes):  continue
                if (int(pb + pc) not in primes):  continue
                if (int(pc + pb) not in primes):  continue

                for d in range(c+1,top-1):
                    pd = str(primes[d])
                    if (int(pa + pd) not in primes):  continue
                    if (int(pd + pa) not in primes):  continue
                    if (int(pb + pd) not in primes):  continue
                    if (int(pd + pb) not in primes):  continue
                    if (int(pc + pd) not in primes):  continue
                    if (int(pd + pc) not in primes):  continue

                    for e in range(d+1,top):
                        pe = str(primes[e])
                        print "Testing", [pa, pb, pc, pd, pe]
                        if (int(pa + pe) not in primes):  continue
                        if (int(pe + pa) not in primes):  continue
                        if (int(pb + pe) not in primes):  continue
                        if (int(pe + pb) not in primes):  continue
                        if (int(pc + pe) not in primes):  continue
                        if (int(pe + pc) not in primes):  continue
                        if (int(pd + pe) not in primes):  continue
                        if (int(pe + pd) not in primes):  continue

                        print "Found {0} ".format([primes[a], primes[b], primes[c], primes[d], primes[e]])
                        print "Answer = ", (primes[a] + primes[b] + primes[c] + primes[d] + primes[e])
