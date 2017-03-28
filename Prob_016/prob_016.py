#!/usr/bin/python
#
# Project Euler.net Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?
#

num = 2**1000
snum = str(num)
lnum = list(snum)
answer = 0
for i in lnum:
    answer += int(i)

print("Answer = {}".format(answer))
