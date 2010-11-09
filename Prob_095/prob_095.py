#!/usr/bin/python
#
# Project Euler.net Problem 95
#
# The proper divisors of a number are all the divisors excluding the
# number itself. For example, the proper divisors of 28 are 1, 2, 4,
# 7, and 14. As the sum of these divisors is equal to 28, we call it a
# perfect number.
# 
# Interestingly the sum of the proper divisors of 220 is 284 and the
# sum of the proper divisors of 284 is 220, forming a chain of two
# numbers. For this reason, 220 and 284 are called an amicable pair.
# 
# Perhaps less well known are longer chains. For example, starting
# with 12496, we form a chain of five numbers:
# 
#     12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)
# 
# Since this chain returns to its starting point, it is called an
# amicable chain.
# 
# Find the smallest member of the longest amicable chain with no
# element exceeding one million.
#
# Answer: 14316
# Solved 10/22/09
# 81 problems solved
# Position #290 on level 2

#LIMIT = 200
LIMIT = 15500
LIMIT = 1000000

# Generate a list of divisors
print "# Generate a list of divisors"
hash_list = {}  # Dictionary data structure
for i in range(1,LIMIT+1):
    hash_list[i] = [1]

for i in range(2,1+LIMIT/2):
    for n in range(2,1+LIMIT/i):
        (hash_list[i*n]).append(i)

# Sum those divisors to calculate the next entry in the chain
print "# Sum those divisors to calculate the next entry in the chain"
def add(x,y): return (x+y)
sum_list = [0]*(LIMIT+1)  # List data structure
for i in range(1,LIMIT+1):
    sum_list[i] = reduce(add, hash_list[i])

# Find the chains
print "# Find the chains"
max_length = 0
max_chain = []
chain_list = [0]*(LIMIT+1)  # List data structure
for i in range(1,LIMIT+1):
    if (chain_list[i] == 0):
        # Look for a loop or chain
        j = i
        while ((chain_list[j] == 0) & (sum_list[j] <= LIMIT)):
            chain_list[j] = -1
            j = sum_list[j]

        # Found limit chain
        if (sum_list[j] > LIMIT):
            chain_list[j] = 3  # Exceeded limit chain
            j = i  # Go back to start of chain
            while (chain_list[j] == -1):
                chain_list[j] = 3  # Exceeded limit chain
                j = sum_list[j]
            #print "Chain found", loop

        # Found a chain
        if ((chain_list[j] == 1) | (chain_list[j] == 2) | (chain_list[j] == 3)):
            j = i  # Go back to start of chain
            while (chain_list[j] == -1):
                chain_list[j] = 2  # Chain
                j = sum_list[j]

        # Found a loop
        if (chain_list[j] == -1):
            loop = []
            while (chain_list[j] == -1):
                loop.append(j)
                chain_list[j] = 1  # Loop
                j = sum_list[j]
            j = i  # Go back to start of chain
            while (chain_list[j] == -1):
                chain_list[j] = 2  # Chain
                j = sum_list[j]
            if (len(loop) > max_length):
                print "Loop found", loop
                max_length = len(loop)
                max_loop = loop
            if (loop[0] == 12496):
                print "Specific loop found, started at {0}: {1}".format(i, loop)
        
print "max_length = {0}, max_loop = {1}".format(max_length, max_loop)
print "answer = {0}".format(min(max_loop))
