#!/usr/bin/python
#
# Project Euler.net Problem 6
#
# The sum of the squares of the first ten natural numbers is,
#
#     1^(2) + 2^(2) + ... + 10^(2) = 385
#
# The square of the sum of the first ten natural numbers is,
#
#     (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
#
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.


LIMIT = 100

sum_sq = 0
sum = 0
for i in range(1,LIMIT+1):
    sum_sq += i**2
    sum += i

sq_sum = sum**2

answer = sq_sum - sum_sq

print("Sum of squares of 1 to {0} is {1}".format(LIMIT,sum_sq))
print("Square of sum of 1 to {0} is {1}".format(LIMIT,sq_sum))

print("Difference is {}".format(answer))
