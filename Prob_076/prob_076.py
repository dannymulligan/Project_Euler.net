#!/usr/bin/python
#
# Project Euler.net Problem 76
#
# How many different ways can one hundred be written as a sum of at
# least two positive integers?
#
# It is possible to write five as a sum in exactly six different ways:
# 
#     4 + 1
#     3 + 2
#     3 + 1 + 1
#     2 + 2 + 1
#     2 + 1 + 1 + 1
#     1 + 1 + 1 + 1 + 1
# 
# How many different ways can one hundred be written as a sum of at
# least two positive integers?
# 
#
# Solved ??/??/09
# ?? problems solved
# Position #??? on level ?

def partitions(n, total, max):
    #print "running partitions({0}, {1}, {2})".format(n, total, max)

    if ((n > total) | (total == 0) | (n == 0)):
        return 0

    if ((n == 1) & (total > max)):
        #print "return 0 because ((n == 1) & (total > max))"
        return 0

    if ((n == 1) | (n == total)):
        return 1

    if (n == 2):
        max_possible = min(total-1,max)
        min_possible = total - max_possible
        possible_range = max_possible - min_possible
        if (possible_range <= 0):  return 0
        else:                      return (1 + (possible_range/2))

    count = 0
    for i in range(1,max+1):
        x = partitions(n-1, total-i, min(max,i))
        count += x
        #print "recursing to {0} + partitions({1}, {2}, {3}) = {4}".format(i, n-1, total-i, min(max,i), x)
    return count

MAX = 100
answer = 0
for i in range(2,MAX+1):
    x = partitions(i,MAX,MAX)
    answer += x
    print "partitions({0},{1},{2}) = {3}".format(i,MAX,MAX, x)
print "Answer =", answer

