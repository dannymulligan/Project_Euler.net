#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 500
#
# Problem 500!!!
#
# The number of divisors of 120 is 16.
#
# In fact 120 is the smallest number having 16 divisors.
#
# Find the smallest number with 2^500500 divisors.
#
# Give your answer modulo 500500507.
#
# Solved 02/06/15
# 197 problems solved
# Position #19 on level 7

import time
start_time = time.clock()

############################################################
LIMIT_PRIME = 738*10**4
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

def calculate_primes(limit=LIMIT_PRIME):
    start_time = time.clock()
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    prime_table[i] = i
    primes.append(i)
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 2
    print("There are {} primes less than {}, calculated in {} seconds".format(len(primes), limit, (time.clock() - start_time)))

calculate_primes()
############################################################

import math
log_primes = list()
log_log_primes = list()
for prime in primes:
    log_prime = math.log(prime)
    log_log_prime = math.log(log_prime)
    log_primes.append(log_prime)
    log_log_primes.append(log_log_prime)

############################################################

def evaluation_function(i):
    #print("evaluation_function({})".format(i))
    return log_log_primes[i] + (1+solution[i])*math.log(2)

############################################################

def improve_solution():
    # Evaluate P_z
    best_i = solution_len - 1
    best_val = log_log_primes[best_i]
    #print("solution[{}] = 1, val = {}".format(solution_len-1, best_val))

    # Search P_1...P_n for a better location
    for i in range(len(solution)):
        val = evaluation_function(i)
        #print("solution[{}] = {}, val = {}".format(i, solution[i]+1, val))
        if val < best_val:
            best_i = i
            best_val = val

    # Look at extending to P_(n+1)
    if (solution[-1] != 0):
        solution.append(0)
        i = len(solution)-1
        val = evaluation_function(i)
        #print("solution[{}] = {}, val = {}".format(i, solution[i]+1, val))
        if val < best_val:
            best_i = i
            best_val = val

    if (best_i == solution_len - 1):
        #print("unable to improve answer")
        return False
    else:
        solution[best_i] += 1
        #print("Improved answer by increasing solution[{}] to {}, solution[{}] to 0\n".format(best_i, solution[best_i]+1, solution_len-1))
        return True

############################################################

target = 500500
print("Looking for smallest number with 2^{} divisors.".format(target))
solution = [0]
solution_len = target
possible_to_improve = True
while (sum(solution) < target) & possible_to_improve:
    possible_to_improve = improve_solution()
    if possible_to_improve:
        solution_len -= 1
print solution

############################################################

m = 500500507
print "solution_len =", solution_len
answer = 1
#print("{}".format(answer))
for i in range(solution_len):
    if i < len(solution):
        n = 2**(solution[i] + 1) - 1
    else:
        n = 1
    #print("* {}^{}".format(primes[i], n))
    for j in range(n):
        answer = (answer * primes[i]) % m

print("Answer = {}".format(answer))
print "Time taken = {0} seconds".format(time.clock() - start_time)
