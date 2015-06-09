#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 19
#
# Counting Sundays
#
# You are given the following information, but you may prefer to do
# some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly
#         divisible by 4, but not on a century
#         unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?
#

#import numpy as np
#import scipy as sp
#import matplotlib as mpl

#import cProfile
#cProfile.run('main()')

#import pdb
#pdb.set_trace()

import sys
import time
start_time = time.clock()

########################################

debug = False
year = 1900
month = 1
day = 1
day_of_week = 1

sunday_count = 0

done = False

while not done:
    if debug:
        print("{y}-{m}-{d} was a {dow}".format(y=year, m=month, d=day, dow=day_of_week))

    if (year >= 1901) and (year <= 2000) and (day_of_week == 0):
        sunday_count += 1


    if   month ==  0:  # Jan
        day_of_week = (day_of_week + 31) % 7

    elif month ==  1:  # Feb
        day_of_week = (day_of_week + 28) % 7

        leap_year = False
        if ((year %   4) == 0):
            leap_year == True
        if ((year % 100) == 0):
            leap_year == False
        if ((year % 400) == 0):
            leap_year == True

        if leap_year:
            day_of_week = (day_of_week + 28) % 7  # leap day

    elif month ==  2:  # Mar
        day_of_week = (day_of_week + 31) % 7

    elif month ==  3:  # Apr
        day_of_week = (day_of_week + 30) % 7

    elif month ==  4:  # May
        day_of_week = (day_of_week + 31) % 7

    elif month ==  5:  # Jun
        day_of_week = (day_of_week + 30) % 7

    elif month ==  6:  # Jul
        day_of_week = (day_of_week + 31) % 7

    elif month ==  7:  # Aug
        day_of_week = (day_of_week + 31) % 7

    elif month ==  8:  # Sep
        day_of_week = (day_of_week + 30) % 7

    elif month ==  9:  # Oct
        day_of_week = (day_of_week + 31) % 7

    elif month == 10:  # Nov
        day_of_week = (day_of_week + 30) % 7

    elif month == 11:  # Dec
        day_of_week = (day_of_week + 31) % 7
        year += 1

    month = (month + 1) % 12

    if (year == 2001):
        done = True

print("Answer = {} Sundays".format(sunday_count))
print("Time taken = {0} seconds".format(time.clock() - start_time))
