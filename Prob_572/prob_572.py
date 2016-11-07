#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 572
#
# Idempotent matrices
#
# A matrix M is called idempotent if M^2=M.
#
#                                        / a  b  c \
# Let M be a three by three matrix : M = | d  e  f |
#                                        \ g  h  i /
#
# Let C(n) be the number of idempotent three by three matrices M with
# integer elements such that −n <= a, b, c, d, e, f, g, h, i <= n
#
# C(1)=164 and C(2)=848.
#
# Find C(200).
#
# Solved ??/??/16

import sys
#print(sys.version)
import time
start_time = time.clock()

########################################


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))


#
#     / a  b  c \
# M = | d  e  f |
#     \ g  h  i /
#
# M * M = M
# / a  b  c \   / a  b  c \   / a  b  c \
# | d  e  f | * | d  e  f | = | d  e  f |
# \ g  h  i /   \ g  h  i /   \ g  h  i /
#
# a = a*a + b*d + c*g
# b = a*b + b*e + c*h
# c = a*c + b*f + c*i
#
# d = d*a + e*d + f*g
# e = d*b + e*e + f*h
# f = d*c + e*f + f*i
#
# g = g*a + h*d + i*g
# h = g*b + h*e + i*h
# i = g*c + h*f + i*i
#
