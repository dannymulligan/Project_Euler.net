#!/usr/bin/python
#
# Project Euler.net Problem 55
#
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# 
# Not all numbers produce palindromes so quickly. For example,
# 
#      349 +  943 = 1292
#     1292 + 2921 = 4213
#     4213 + 3124 = 7337
# 
# That is, 349 took three iterations to arrive at a palindrome.
# 
# Although no one has proved it yet, it is thought that some numbers,
# like 196, never produce a palindrome. A number that never forms a
# palindrome through the reverse and add process is called a Lychrel
# number. Due to the theoretical nature of these numbers, and for the
# purpose of this problem, we shall assume that a number is Lychrel
# until proven otherwise. In addition you are given that for every
# number below ten-thousand, it will either (i) become a palindrome in
# less than fifty iterations, or, (ii) no one, with all the computing
# power that exists, has managed so far to map it to a palindrome. In
# fact, 10677 is the first number to be shown to require over fifty
# iterations before producing a palindrome:
# 4668731596684224866951378664 (53 iterations, 28-digits).
# 
# Surprisingly, there are palindromic numbers that are themselves
# Lychrel numbers; the first example is 4994.
# 
# How many Lychrel numbers are there below ten-thousand?
# 
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise
# the theoretical nature of Lychrel numbers.
#
# Answer: 249

def lychrel(num):
    cnt = 0
    while (cnt<=50):
        #print "{0}: {1}".format(cnt, num)
        snum = '{0}'.format(num)
        lnum = len(snum)
        rnum = ''
        for i in range(lnum):
            rnum += snum[lnum-i-1]  # String append
        if ((snum == rnum) & (cnt != 0)):
            return False
        else:
            num = int(snum) + int(rnum)
            cnt += 1
    return True


answer = 0
for n in range(10,10000,1):
    if lychrel(n):
        answer += 1
        print "    {0} is lychrel".format(n)
    if ((n % 1000) == 0):
        print "{0}: found {1} lychrel numbers so far".format(n, answer)

print "Done - found {0} lychrel numbers below {1}".format(answer, n+1)
