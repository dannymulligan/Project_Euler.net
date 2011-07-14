#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 277
#
# A Modified Collatz sequence
#
# A modified Collatz sequence of integers is obtained from a starting
# value a_(1) in the following way:
# 
# a(n+1) = a(n)/3 if a(n) is divisible by 3. We shall denote this as a
# large downward step, "D".
# 
# a(n+1) = (4a(n) + 2)/3 if a(n) divided by 3 gives a remainder of
# 1. We shall denote this as an upward step, "U".
# 
# a(n+1) = (2a(n) - 1)/3 if a(n) divided by 3 gives a remainder of
# 2. We shall denote this as a small downward step, "d".
# 
# The sequence terminates when some a(n) = 1.
# 
# Given any integer, we can list out the sequence of steps.
# For instance if a(1)=231, then the sequence
# {a(n)}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps
# "DdDddUUdDD".
# 
# Of course, there are other sequences that begin with that same
# sequence "DdDddUUdDD....".  For instance, if a(1)=1004064, then the
# sequence is DdDddUUdDDDdUDUUUdDdUUDDDUdDD.  In fact, 1004064 is the
# smallest possible a(1) > 10^6 that begins with the sequence
# DdDddUUdDD.
# 
# What is the smallest a(1) > 10^15 that begins with the sequence
# "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?
# 
#
# Solved 07/05/10
# 112 problems solved
# Position #963 on level 3

pattern = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
#pattern = "UDDDUdd"
#pattern = "DdDddUUdDD"

def check (n):
    res = ""
    while ((n != 1) & (len(res)<len(pattern))):
        if   ((n % 3) == 0):
            print "D", n, "->",
            n = n / 3
            print n
            res += "D"
        elif ((n % 3) == 1):
            print "U", n, "->",
            n = (4*n + 2)/ 3
            print n
            res += "U"
        elif ((n % 3) == 2):
            print "d", n, "->",
            n = (2*n - 1)/ 3
            print n
            res += "d"
    print res
    return res


def try_out (n):
    for s in pattern[::-1]:
        #print s, n, "->",
        if   (s == "D"):
            n = 3*n
        elif (s == "U"):
            if (((3*n - 2) % 4) != 0):
                return False
            n = (3*n - 2)/4
        elif (s == "d"):
            if (((3*n + 1) % 2) != 0):
                return False
            n = (3*n + 1)/2
        #print n
    return True

def calculate_result (n):
    for s in pattern[::-1]:
        #print s, n, "->",
        if   (s == "D"):
            n = 3*n
        elif (s == "U"):
            if (((3*n - 2) % 4) != 0):
                return False
            n = (3*n - 2)/4
        elif (s == "d"):
            if (((3*n + 1) % 2) != 0):
                return False
            n = (3*n + 1)/2
        #print n
    return n


a = 1.0
for s in pattern[::-1]:
    print s, a, "->",
    if   (s == "D"):
        a = 3*a
    elif (s == "U"):
        a = (3*a - 2)/4
    elif (s == "d"):
        a = (3*a + 1)/2
    print a

print "result =", a
print "lowest possible starting value =", 1e15/a
start = int(1e15/a)
print "================"
print "Starting search at", start + 1

found = False
n = start
while (not found):
    n += 1
    valid = try_out(n)
    if (valid):
        result = calculate_result(n)
        if (result > 1e15):
            found = True
        

print "answer =", n
print "result =", result

if (check(result) == pattern):
    print "Success"
    print "Solution =", result
else:
    print "Failure"

