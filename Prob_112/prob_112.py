#!/usr/bin/python
#
# Project Euler.net Problem 112
# 
# Working from left-to-right if no digit is exceeded by the digit to
# its left it is called an increasing number; for example, 134468.
# 
# Similarly if no digit is exceeded by the digit to its right it is
# called a decreasing number; for example, 66420.
# 
# We shall call a positive integer that is neither increasing nor
# decreasing a "bouncy" number; for example, 155349.
# 
# Clearly there cannot be any bouncy numbers below one-hundred, but
# just over half of the numbers below one-thousand (525) are
# bouncy. In fact, the least number for which the proportion of bouncy
# numbers first reaches 50% is 538.
# 
# Surprisingly, bouncy numbers become more and more common and by the
# time we reach 21780 the proportion of bouncy numbers is equal to
# 90%.
# 
# Find the least number for which the proportion of bouncy numbers is
# exactly 99%.
#
# Answer 1587000
# Solved 10/9/09
# 101 problems solved
# Position #1241 on level 3

found = False
nfound = 0
n = 100
while not found:
    nl=list(str(n))
    p = nl[0]
    up = False
    dn = False
    for i in range(1,len(nl)):
        if   (nl[i] > p):
            up = True
        elif (nl[i] < p):
            dn = True
        p = nl[i]
    if (up & dn):
        nfound += 1

    if ((n % 100000) == 0):
        print nfound, n, float(nfound)/float(n)

    if ((nfound * 100) == (n * 99)):
        found = True
    elif ((nfound * 100) > (n * 99)):
        found = True
        print "Error"
    else:
        n += 1

    

print "Solution found", nfound, n
print "Answer = ", n
