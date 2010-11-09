#!/usr/bin/python
#
# Project Euler.net Problem 74
#
# The number 145 is well known for the property that the sum of the
# factorial of its digits is equal to 145:
# 
#     1! + 4! + 5! = 1 + 24 + 120 = 145
# 
# Perhaps less well known is 169, in that it produces the longest
# chain of numbers that link back to 169; it turns out that there are
# only three such loops that exist:
# 
#     169 -> 363601 -> 1454 -> 169
#     871 -> 45361 -> 871
#     872 -> 45362 -> 872
# 
# It is not difficult to prove that EVERY starting number will
# eventually get stuck in a loop. For example,
# 
#     69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
#     78 -> 45360 -> 871 -> 45361 (-> 871)
#     540 -> 145 (-> 145)
# 
# Starting with 69 produces a chain of five non-repeating terms, but
# the longest non-repeating chain with a starting number below one
# million is sixty terms.
# 
# How many chains, with a starting number below one million, contain
# exactly sixty non-repeating terms?
#
# Answer: 402
# Solved 10/22/09
# 84 problems solved
# Position #242 on level 2

#LIMIT = 100000
LIMIT = 1000000

def factorial(n):
    if (n == 0): return 1
    if (n == 1): return 1
    answer = 1
    for i in range(2,n+1):
        answer *= i
    return answer

answer = 0
for i in range(LIMIT):
    if ((i % 25000) == 0):
        print "Testing {0}".format(i)
    j = i
    chain = []
    while j not in chain:
        chain.append(j)
        digits = list(str(j))
        sum = 0
        for n in digits:
            sum += factorial(int(n))
        j = sum
    if (len(chain) == 60):
        answer += 1
        if ((answer % 100) == 0):
            print "Found {0} so far, latest one: start = {1}, chain = {2}".format(answer, i, chain)

print "Answer =", answer
