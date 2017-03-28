#!/usr/bin/env python3
#
# Project Euler.net Problem 25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
#    F_(n) = F_(n-1) + F_(n-2), where F_(1) = 1 and F_(2) = 1.
#
# Hence the first 12 terms will be:
#
#     F_(1) = 1
#     F_(2) = 1
#     F_(3) = 2
#     F_(4) = 3
#     F_(5) = 5
#     F_(6) = 8
#     F_(7) = 13
#     F_(8) = 21
#     F_(9) = 34
#     F_(10) = 55
#     F_(11) = 89
#     F_(12) = 144
#
# The 12th term, F_(12), is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

TARGET = 1000

def fibonacci():
    i0 = 0;
    i1 = 1;
    while True:
        yield i1
        i0, i1 = i1, i0+i1

for n, f in enumerate(fibonacci()):
    f_string = "{}".format(f)
    f_len = len(f_string)
    #print(n+1, f, f_len)
    if f_len >= TARGET:
        break

print("Answer = {}".format(n+1))
