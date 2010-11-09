#!/usr/bin/python
#
# Project Euler.net Problem 69
# 
# Euler's Totient function, phi(n) [sometimes called the phi function],
# is used to determine the number of numbers less than n which are
# relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
# less than nine and relatively prime to nine, phi(9)=6.
# 
#     n    Relatively Prime    phi(n)    n/phi(n)
#     2    1                   1         2
#     3    1,2                 2         1.5
#     4    1,3                 2         2
#     5    1,2,3,4             4         1.25
#     6    1,5                 2         3
#     7    1,2,3,4,5,6         6         1.1666...
#     8    1,3,5,7             4         2
#     9    1,2,4,5,7,8         6         1.5
#     10   1,3,7,9             4         2.5
# 
# It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.
# 
# Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
# 
# Answer: 510510

LIMIT_D =      10
#LIMIT_D =    1000
#LIMIT_D =  100000
LIMIT_D = 1000000

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

max_nphi = 0.0
for n in range(2,LIMIT_D+1):
    phi = phi_table[n]
    tmp = float(n)/phi
    if (tmp > max_nphi):
        max_n = n
        max_nphi = tmp
        print "n = %d gives phi(n) = %d, n/phi(n) = %f" % (n, phi, tmp)

print "Answer = ", max_n
