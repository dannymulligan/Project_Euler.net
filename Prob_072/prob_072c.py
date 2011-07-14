#!/usr/bin/python
#
# Project Euler.net Problem 72
#
# Consider the fraction, n/d, where n and d are positive integers. If
# n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# 
# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:
# 
#     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
#         5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 
# It can be seen that there are 21 elements in this set.
# 
# How many elements would be contained in the set of reduced proper
# fractions for d <= 1,000,000?
# 
#
# Solved 10/26/09
# 87 problems solved
# Position #194 on level 2

#          D           Answer
#          8               21
#         10               31
#         50              773
#        100            3,043
#        500           76,115
#      1,000          304,191
#      5,000        7,600,457
#     10,000       30,397,485
#     50,000      759,924,263
#    100,000    3,039,650,753
#    500,000   75,991,039,675
#  1,000,000  303,963,552,391

LIMIT_D =       8
LIMIT_D =      10
LIMIT_D =      50
LIMIT_D =     100
LIMIT_D =     500
LIMIT_D =    1000
LIMIT_D =    5000
LIMIT_D =   10000
LIMIT_D =   50000
LIMIT_D =  100000
LIMIT_D =  500000
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

answer = 0
for i in range(2,LIMIT_D+1):
    answer += phi_table[i]

print "Answer = ", answer
