#!/usr/bin/env python3
#
# Project Euler.net Problem 4
#
# A palindromic number reads the same both ways.
#
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome(candidate_int):
    # Convert the candidate number to a string
    candidate_str = "{}".format(candidate_int)
    candidate_str_rev = candidate_str[::-1]

    # Check if it is a palindrome
    return candidate_str == candidate_str_rev


max_palindrome = 0
max_i = max_j = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        candidate = i * j
        if ((candidate > max_palindrome) and palindrome(candidate)):
            max_palindrome = candidate;
            (max_i, max_j) = (i, j)
            print("i = {}, j = {}, candidate = {}".format(i, j, candidate))


print("Largest palindrome is {} from multiplying {} by {}.".format(max_palindrome, max_i, max_j))
