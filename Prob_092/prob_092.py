#!/usr/bin/python
#
# Project Euler.net Problem 92
#
# A number chain is created by continuously adding the square of the
# digits in a number to form a new number until it has been seen
# before.
# 
# For example,
# 
#     44 -> 32 -> 13 -> 10 -> 1 -> 1
#     85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
# 
# Therefore any chain that arrives at 1 or 89 will become stuck in an
# endless loop. What is most amazing is that EVERY starting number
# will eventually arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?
#
# Solved 10/22/09
# 82 problems solved
# Position #273 on level 2


LIMIT = 10000000

chain_next = [0]*(LIMIT+1)

# Calculate the next item in the chain
print "# Calculate the next item in the chain"
for i in range(LIMIT):
    if ((i % 100000) == 0):  print "Calculating {0}".format(i)
    digits = list(str(i))
    sum = 0
    for n in digits:
        sum += int(n)**2
    chain_next[i] = sum

print "max(chain_next) = ", max(chain_next)

# Count numbers that end in 89
print "# Count numbers that end in 89"
found_89 = 0
for i in range(1,LIMIT):
    if ((i % 100000) == 0):  print "Counting {0}".format(i)
    j = i
    if (j == 1):  continue
    while ((chain_next[j] != 89) & (chain_next[j] != 1)):
        j = chain_next[j]
    if (chain_next[j] == 89):
        found_89 += 1

print "Answer =", found_89

