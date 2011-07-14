#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 265
#
# Binary Circles
#
# 2^N binary digits can be placed in a circle so that all the N-digit
# clockwise subsequences are distinct.
#
# For N=3, two such circular arrangements are possible, ignoring
# rotations:
#
#     0 0 0 1 0 1 1 1
#     0 0 0 1 1 1 0 1
#
# For the first arrangement, the 3-digit subsequences, in clockwise
# order, are: 000, 001, 010, 101, 011, 111, 110 and 100.
# 
# Each circular arrangement can be encoded as a number by
# concatenating the binary digits starting with the subsequence of all
# zeros as the most significant bits and proceeding clockwise. The two
# arrangements for N=3 are thus represented as 23 and 29:
#
#     b'00010111 = 23    b'00011101 = 29
# 
# Calling S(N) the sum of the unique numeric representations, we can
# see that S(3) = 23 + 29 = 52.
# 
# Find S(5).
#
# Solved 12/19/09
# 111 problems solved
# Position #813 on level 3

#
# For S(5) the following bits are predetermined...
#
#     000001xx xxxxxxxx xxxxxxxx xxxxxxx1
#
# Also, there are a predermined number of 1's and 0's in the bits.
# The following bit results need to be generated...
# 
#     00000 = 0 ones    10000 = 1 ones
#     00001 = 1 ones    10001 = 2 ones
#     00010 = 1 ones    10010 = 2 ones
#     00011 = 2 ones    10011 = 3 ones
#     00100 = 1 ones    10100 = 2 ones
#     00101 = 2 ones    10101 = 3 ones
#     00110 = 2 ones    10110 = 3 ones
#     00111 = 3 ones    10111 = 4 ones
#     01000 = 1 ones    11000 = 2 ones
#     01001 = 2 ones    11001 = 3 ones
#     01010 = 2 ones    11010 = 3 ones
#     01011 = 3 ones    11011 = 4 ones
#     01100 = 2 ones    11100 = 3 ones
#     01101 = 3 ones    11101 = 4 ones
#     01110 = 3 ones    11110 = 4 ones
#     01111 = 4 ones    11111 = 5 ones
#
#     70 ones total.
#
# Since each bit on the circle is used 5 times, this means we need a
# total of 14 ones on the circle.  So, in the sequence...
#
#     000001xx xxxxxxxx xxxxxxxx xxxxxxx1
#
# ...12 of the 25 x's must be 1, and 13 must be 0.  This means that
# there are C(12,25) possible values = 25!/12!*13! = 5.2 million
# possible combinations.
#
# However, it's probably more work to reject a possibility becaue it
# has the wrong number of ones, compared to just checking that
# possibility for being a match.

## # Solve the S(3) version of the problem
## PREFIX = "0001"
## POSFIX = "1000"  # Add an extra 3 zeros from the beginning of the ring
## # The bit sequence we're generating will look like this...
## #     0001xxx1 (but with an extra 000 on the end to facilitate testing)
## 
## dec2bin = ['000','001','010','011','100','101','110','111']
## tot = 0
## for i in range(8):
##     ring = PREFIX + dec2bin[i] + POSFIX
##     #print "{0}: trying {1}".format(i,ring)
## 
##     found = True
##     for t in dec2bin:
##         if not t in ring:
##             found = False
##             break
##     if found:
##         res = i*2 + 2**0 + 2**4
##         tot += res
##         print "{0} = {1} is a match".format(ring, res)
## 
## print "Answer is", tot


# Solve the S(5) version of the problem
PREFIX = '000001'
POSFIX = '100000'  # Add an extra 5 zeros from the beginning of the ring
# The bit sequence we're generating will look like this...
#     0000 01xx xxxx xxxx xxxx xxxx xxxx xxx1 (but with an extra 00000 on the end to facilitate testing)
# So we need to generate 2**25 = 33,554,432 cases to cover the 25 x's.

str2tst = [
    #'00000', # in PREFIX
    #'00001', # in PREFIX
    '00010',
    '00011',
    '00100',
    '00101',
    '00110',
    '00111',
    '01000',
    '01001',
    '01010',
    '01011',
    '01100',
    '01101',
    '01110',
    '01111',
    #'10000', # in POSFIX
    '10001',
    '10010',
    '10011',
    '10100',
    '10101',
    '10110',
    '10111',
    '11000',
    '11001',
    '11010',
    '11011',
    '11100',
    '11101',
    '11110',
    '11111'
]

tot = 0
for i in range(2**25):
    ts = ''
    ti = i
    for j in range(25):
        #print i, ti, ts
        if ((ti % 2) == 1):  ts = '1' + ts
        else:                ts = '0' + ts
        ti /= 2

    ring = PREFIX + ts + POSFIX
    #print "{0}: trying {1}".format(i,ring)

    found = True
    for t in str2tst:
        if not t in ring:
            found = False
            break
    if found:
        res = i*2 + 2**0 + 2**26
        tot += res
        print "{0} = {1} is a match".format(ring, res)

    if ((i % 2**20) == 0):
        print "Testing i={0}, ring={1}".format(i,ring)

print "Answer is", tot
