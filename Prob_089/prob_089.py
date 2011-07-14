#!/usr/bin/python
#
# Project Euler.net Problem 89
#
# The rules for writing Roman numerals allow for many ways of writing
# each number (see FAQ: Roman Numerals). However, there is always a
# "best" way of writing a particular number.
# 
# For example, the following represent all of the legitimate ways of
# writing the number sixteen:
# 
#     IIIIIIIIIIIIIIII
#     VIIIIIIIIIII
#     VVIIIIII
#     XIIIIII
#     VVVI
#     XVI
# 
# The last example being considered the most efficient, as it uses the
# least number of numerals.
# 
# The 11K text file, roman.txt (right click and 'Save Link/Target
# As...'), contains one thousand numbers written in valid, but not
# necessarily minimal, Roman numerals; that is, they are arranged in
# descending units and obey the subtractive pair rule (see FAQ for the
# definitive rules for this problem).
# 
# Find the number of characters saved by writing each of these in
# their minimal form.
# 
# Note: You can assume that all the Roman numerals in the file contain
# no more than four consecutive identical units.
# 
# Solved 10/27/09
# 91 problems solved
# Position #125 on level 2

rfile = open("./roman.txt", "r")
rlist = rfile.readlines()

print len(rlist)

chars_saved = 0
for snum in rlist:
    snum_chars = list(snum)
    num = 0
    prev = ' '
    num_len = 0
    for i in snum_chars:
        if   (i == 'M'):
             num     += 1000
             num_len += 1
        elif (i == 'D'):
             num     += 500
             num_len += 1
        elif (i == 'C'):
             num     += 100
             num_len += 1
        elif (i == 'L'):
             num     += 50
             num_len += 1
        elif (i == 'X'):
             num     += 10
             num_len += 1
        elif (i == 'V'):
             num     += 5
             num_len += 1
        elif (i == 'I'):
             num     += 1
             num_len += 1

        if   ((i == 'M') & (prev == 'C')):  num -= 2*100
        elif ((i == 'D') & (prev == 'C')):  num -= 2*100
        elif ((i == 'C') & (prev == 'X')):  num -= 2* 10
        elif ((i == 'L') & (prev == 'X')):  num -= 2* 10
        elif ((i == 'X') & (prev == 'I')):  num -= 2*  1
        elif ((i == 'V') & (prev == 'I')):  num -= 2*  1

        prev = i

    orig_num = num
    new_num = ''
    while (num >= 1000):
        new_num += 'M'
        num -= 1000

    if (num >= 900):
        new_num += 'CM'
        num -= 900
    if (num >= 500):
        new_num += 'D'
        num -= 500
    if (num >= 400):
        new_num += 'CD'
        num -= 400
    while (num >= 100):
        new_num += 'C'
        num -= 100

    if (num >= 90):
        new_num += 'XC'
        num -= 90
    if (num >= 50):
        new_num += 'L'
        num -= 50
    if (num >= 40):
        new_num += 'XL'
        num -= 40
    while (num >= 10):
        new_num += 'X'
        num -= 10

    if (num >= 9):
        new_num += 'IX'
        num -= 9
    if (num >= 5):
        new_num += 'V'
        num -= 5
    if (num >= 4):
        new_num += 'XL'
        num -= 4
    while (num >= 1):
        new_num += 'I'
        num -= 1

    chars_saved += (num_len - len(new_num))
    print snum, num_len, orig_num, len(new_num), new_num, (len(new_num) - num_len)

print "Answer =", chars_saved
