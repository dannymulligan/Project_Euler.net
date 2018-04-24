#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 571
#
# Super Pandigital Numbers
#
# A positive number is pandigital in base b if it contains all digits
# from 0 to b - 1 at least once when written in base b.
#
# A n-super-pandigital number is a number that is simultaneously
# pandigital in all bases from 2 to n inclusively.
#
# For example 978 = 1111010010 base 2 = 1100020 base 3 = 33102 base 4
# = 12403 base 5 is the smallest 5-super-pandigital number.
#
# Similarly, 1093265784 is the smallest 10-super-pandigital number.
#
# The sum of the 10 smallest 10-super-pandigital numbers is
# 20319792309.
#
# What is the sum of the 10 smallest 12-super-pandigital numbers?


import sys
#print(sys.version)
import time
start_time = time.clock()

########################################


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
