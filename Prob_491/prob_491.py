#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 491
#
# Double pandigital number divisible by 11
#
# We call a positive integer double pandigital if it uses all the
# digits 0 to 9 exactly twice (with no leading zero). For example,
# 40561817703823564929 is one such number.
#
# How many double pandigital numbers are divisible by 11?
#

import math
import sys
import time
start_time = time.clock()

DIGITS = 10

########################################
def digit_combination(target, num_digits, limit_digit, debug):
    #print("digit_combination(target={}, num_digits={}, limit_digit={}, debug={})".format(target, num_digits, limit_digit, debug))
    if num_digits == 1:
        if limit_digit >= target:
            yield [target]  # Only possible solution
        else:
            return  # There are no possible solutions

    # num_digits > 1
    for digit in range(limit_digit, -1, -1):
        remaining_digits = (limit_digit-1) * limit_digit
        if (num_digits > 2):
            # Try with 2 copies of digit
            #print("{}*2, remaining={}, target={}".format(digit, remaining_digits, target))
            if (digit*2 <= target) and (remaining_digits+digit*2 >= target):
                for subsequence in digit_combination(target-digit*2, num_digits-2, digit-1, debug + [digit, digit]):
                    yield [digit, digit] + subsequence

        elif (num_digits == 2):
            if ((target % 2) == 0) and (digit*2 == target):
                yield [digit, digit]  # Only possible solution
                
         # Try with 1 copy of digit
        if (digit <= target) and (remaining_digits+digit >= target):
            for subsequence in digit_combination(target-digit, num_digits-1, digit-1, debug + [digit]):
                yield [digit] + subsequence

    return


########################################
def compliment(left):
    digits = [2]*DIGITS
    for digit in left:
        digits[digit] -= 1
    result = []
    
    for digit in range(DIGITS-1, -1, -1):
        if digits[digit] == 2:
            result = result + [digit, digit]
        elif digits[digit] == 1:
            result = result + [digit]
    return result
            

########################################
def count_left(left):
    digit_count = [0]*DIGITS
    for digit in left:
        digit_count[digit] += 1

    first_digit_possibilities = DIGITS - digit_count[0]
    rest_digits_possibilities = math.factorial(DIGITS-1)
    possibilities = first_digit_possibilities * rest_digits_possibilities

    for digit in digit_count:
        if digit == 2:
            possibilities //= 2

    return possibilities
            

########################################
def count_right(right):
    digit_count = [0]*DIGITS
    for digit in right:
        digit_count[digit] += 1

    possibilities = math.factorial(DIGITS)

    for digit in digit_count:
        if digit == 2:
            possibilities //= 2

    return possibilities
            

########################################
Answer = 0
digit_sum = DIGITS * (DIGITS - 1) // 2

target = digit_sum
print("================================================================================")
print("target = {}".format(target))
for n, left in enumerate(digit_combination(target=target, num_digits=DIGITS, limit_digit=DIGITS-1, debug=[])):
    right = compliment(left)
    left_possibilities = count_left(left)
    right_possibilities = count_right(right)
    possibilities = left_possibilities * right_possibilities
    Answer += possibilities
    print(">>>>  {}: {} (count = {}) and {} (count = {}) {:,} possible solutions".format(n, left, left_possibilities, right, right_possibilities, possibilities))

for target in range(digit_sum - 11, 0, -11):
    print("================================================================================")
    print("target = {}".format(target))
    for n, left in enumerate(digit_combination(target=target, num_digits=DIGITS, limit_digit=DIGITS-1, debug=[])):
        right = compliment(left)
        left_possibilities = count_left(left)
        right_possibilities = count_right(right)
        possibilities = left_possibilities * right_possibilities
        Answer += possibilities
        print(">>>>  {}: {} (count = {}) and {} (count = {}) {:,} possible solutions".format(n, left, left_possibilities, right, right_possibilities, possibilities))
    

for target in range(digit_sum + 11, digit_sum*2, 11):
    print("================================================================================")
    print("target = {}".format(target))
    for n, left in enumerate(digit_combination(target=target, num_digits=DIGITS, limit_digit=DIGITS-1, debug=[])):
        right = compliment(left)
        left_possibilities = count_left(left)
        right_possibilities = count_right(right)
        possibilities = left_possibilities * right_possibilities
        Answer += possibilities
        print(">>>>  {}: {} (count = {}) and {} (count = {}) {:,} possible solutions".format(n, left, left_possibilities, right, right_possibilities, possibilities))
    


print("Answer = {}".format(Answer))
print("Time taken = {:.2f} seconds".format(time.clock() - start_time))


# If we have a number X00, then we can convert it to 00X by adding
# 0XX, then subtracting XX0.  Since the numbers we added and
# subtracted were both divisible by 11, we haven't changed the overall
# divisibility by 11 by doing this.
#
# Thus we can move any digit 2 places to the right, until we've summed
# all of the odd position digits to position 1 (i.e. the 10's position
# in the number), and all of the even position digits to position 0
# (i.e. the 1's position in the number), at which point the number is
# divisible by 11 only if position 1 and position 0 are equal, or
# differ by some multiple of 11.
#
# So to be divisible by 11, all of the odd position digits must sum to
# the same as all of the even position digits, although either odd or
# even can have an additional multiple of 11.
#
# In other words we need
#   sum(odd)  = n + x * 11
#   sum(even) = n - x * 11
# which is the same as
#   sum(odd)  = n - x * 11
#   sum(even) = n - x * 11
# plus
#   sum(odd)  = 2x * 11
#   sum(even) = 0
# or 
#   sum(odd) = 0
#   sum(even)  = 2x * 11
# both of which are divisible by 11.

