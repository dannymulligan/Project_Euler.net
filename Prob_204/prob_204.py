#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 204
#
# Generalized Hamming Numbers
#
# A Hamming number is a positive number which has no prime factor
# larger than 5.  So the first few Hamming numbers are 1, 2, 3, 4, 5,
# 6, 8, 9, 10, 12, 15.  There are 1105 Hamming numbers not exceeding
# 10^8.
#
# We will call a positive number a generalised Hamming number of type
# n, if it has no prime factor larger than n.  Hence the Hamming
# numbers are the generalised Hamming numbers of type 5.
#
# How many generalised Hamming numbers of type 100 are there which
# don't exceed 10^9?
#
# Answer: 2944730
# Solved 05/14/10
# 139 problems solved
# Position #232 on level 3

# There are 2 primes <=5, they are 2, 3, 5
# There are 25 primes <=100, they are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

#LIMIT = 10**8
LIMIT = 10**9


def hamming(primes, powers):
    result = 1
    for i in range(len(primes)):
       result *= primes[i]**powers[i]
    return result

def is_hamming(primes, powers):
    if (hamming(primes,powers) <= LIMIT):
        return True
    else:
       return False


#primes = [2, 3, 5]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_count = len(primes)
powers = [0] * prime_count

answer = 0
while (True):
    res = hamming(primes,powers)
    if (res <= LIMIT):
        answer += 1
        if ((answer % 10000) == 0):
            print "{0} solutions found, hamming{1} = {2}".format(answer, powers, res)
    

    for i in range(prime_count):
        powers[i] += 1
        if is_hamming(primes,powers):
            break
        powers[i] = 0
    if (powers == [0]*prime_count):
        break

print "Answer =", answer

#primes100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


