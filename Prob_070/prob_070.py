#!/usr/bin/python
#
# Project Euler.net Problem 70
#
# Euler's Totient function, phi(n) [sometimes called the phi function],
# is used to determine the number of positive numbers less than or
# equal to n which are relatively prime to n. For example, as 1, 2, 4,
# 5, 7, and 8, are all less than nine and relatively prime to nine,
# phi(9)=6.
#
# The number 1 is considered to be relatively prime to every positive
# number, so phi(1)=1.
#
# Interestingly, phi(87109)=79180, and it can be seen that 87109 is a
# permutation of 79180.
#
# Find the value of n, 1 < n < 10^(7), for which phi(n) is a permutation
# of n and the ratio n/phi(n) produces a minimum.
#
# Answer: 9819823
# Solved 10/26/09
# 88 problems solved
# Position #174 on level 2

LIMIT_D =      100
LIMIT_D =   100000  # 0.37 seconds runtime for calculate_primes() & calculate_phi()
LIMIT_D =  1000000  # 3.7 seconds runtime for calculate_primes() & calculate_phi()
LIMIT_D = 10000000  # 38.7 seconds runtime for calculate_primes() & calculate_phi()

prime_table = [0]*(LIMIT_D+1)  # 0 => prime, non-zero indicated largest factor

phi_table = [0]*(LIMIT_D+1)


def calculate_primes():
    i = 2
    while (i <= (LIMIT_D/2)):
        if (prime_table[i] == 0):
            j = i
            while (j <= LIMIT_D):
                prime_table[j] = i
                j += i
        i += 1

def calculate_phis():
    for i in range(2, LIMIT_D+1):
        #print "Calculating phi({0})".format(i)
        if (prime_table[i] == 0):
            phi_table[i] = i-1
        else:
            n = i
            phi_table[i] = 1
            factors = []
            while (n > 1):
                factor = prime_table[n]
                factors.append(factor)
                phi_table[i] *= (factor - 1)
                n = n / factor
                while (prime_table[n] == factor):
                    factors.append(factor)
                    phi_table[i] *= factor
                    n = n / factor
                #print "Factors of {0} are {1}".format(i, factors)




print "LIMIT_D =", LIMIT_D

calculate_primes()
calculate_phis()

min_nphi = 10.0
for n in range(2,LIMIT_D+1):
    n_digits = list(str(n))
    n_digits.sort()
    phi = phi_table[n]
    phi_digits = list(str(phi))
    phi_digits.sort()
    if (n_digits == phi_digits):
        #print "phi({0}) = {1}".format(n, phi)

        tmp = float(n)/phi
        if (tmp < min_nphi):
            min_n = n
            min_nphi = tmp
            print "n = %d gives phi(n) = %d, n/phi(n) = %f" % (n, phi, tmp)

print "Answer = ", min_n
