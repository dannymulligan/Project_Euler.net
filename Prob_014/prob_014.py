#!/usr/bin/python
#
# Project Euler.net Problem 14
#
# The following iterative sequence is defined for the set of positive
# integers:
# 
#     n -> n/2 (n is even)
#     n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following
# sequence:
#
#     13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 
# It can be seen that this sequence (starting at 13 and finishing at
# 1) contains 10 terms.  Although it has not been proved yet (Collatz
# Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
# 
# Calculated in 42 seconds


LIMIT = 1000000
#LIMIT = 100

def seq_len(n):
    len = 0
    while (n != 1):
        if ((n % 2) == 0):
            n /= 2
        else:
            n = 3*n + 1
        len += 1
    return len

max_len = 0
max_n = 0
for n in range(1,LIMIT):
    len = seq_len(n)
    if (len > max_len):
        max_len = len
        max_n   = n
        print "seq({0}) had length {1}".format(n,len)

print "Answer =", max_n
