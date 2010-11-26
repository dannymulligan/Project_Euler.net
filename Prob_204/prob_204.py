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
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

LIMIT = 10**8
primes = [2, 3, 5]

def hamming(pr, po):
    result = 1
    for i in range(len(pr)):
       result *= pr[i]**po[i]
    return result

pow = [0, 0, 0]

ans = hamming(primes, pow)

while

#primes100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


