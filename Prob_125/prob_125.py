#!/usr/bin/python
#
# Project Euler.net Problem 125
# 
# The palindromic number 595 is interesting because it can be written
# as the sum of consecutive squares: 6^(2) + 7^(2) + 8^(2) + 9^(2) +
# 10^(2) + 11^(2) + 12^(2).
# 
# There are exactly eleven palindromes below one-thousand that can be
# written as consecutive square sums, and the sum of these palindromes
# is 4164. Note that 1 = 0^(2) + 1^(2) has not been included as this
# problem is concerned with the squares of positive integers.
# 
# Find the sum of all the numbers less than 10^(8) that are both
# palindromic and can be written as the sum of consecutive squares.
#
# Answer 2906969179
# Solved 11/10/09
# 104 problems solved
# Position #1067 on level 3

#MAX_SUM = 1000
#MAX_SQ  = 25  # Needs to be sqrt(MAX_SUM/2) at a minimum
MAX_SUM = 100000000
MAX_SQ  = 7500  # Needs to be sqrt(MAX_SUM/2) at a minimum

def is_pali(n):
    digits = list(str(n))
    l = len(digits)
    for j in range(l/2):
        if digits[j] != digits[l-1-j]:
            return False
    return True

squares = [0]*(MAX_SQ+1)
for i in range(1,MAX_SQ+1):
    squares[i] = i**2

count = 0
found = []
for end in range(2,MAX_SQ+1):
    sq_sum = squares[end]
    for start in range(end-1,0,-1):
        if sq_sum > MAX_SUM:  continue
        sq_sum += squares[start]
        #print "{0} = {1}^2 + .. + {2}^2".format(sum, start, end)
        if (sq_sum > 0) & (sq_sum < MAX_SUM) & (is_pali(sq_sum)):
            count += 1
            print "{0}: {1} = {2}^2 + .. + {3}^2".format(count, sq_sum, start, end)
            if sq_sum not in found:
                found.append(sq_sum)

# Have to use a list of all found numbers, with duplicates eliminated,
# because some numbers are found more than once

total = reduce(lambda x, y: x+y, found)
print "Answer =", total
