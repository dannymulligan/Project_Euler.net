#!/usr/bin/python
#
# Project Euler.net Problem 73
#
# Consider the fraction, n/d, where n and d are positive integers. If
# n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# 
# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:
# 
#     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
#         5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 
# It can be seen that there are 3 fractions between 1/3 and 1/2.
# 
# How many fractions lie between 1/3 and 1/2 in the sorted set of
# reduced proper fractions for d <= 12,000?
# 
# Note: The upper limit has been changed recently.
#
# Answer: 7295372
# Solved 10/22/09
# 83 problems solved
# Position #266 on level 2


# For d <= 8, we have...
# 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8
# 1/7, 2/7, 3/7, 4/7, 5/7, 6/7
# 1/6, 2/6, 3/6, 4/6, 5/6
# 1/5, 2/5, 3/5, 4/5
# 1/4, 2/4, 3/4
# 1/3, 2/3
# 1/2
#
# Eliminating fractions where HCF(n,d) != 1, we have...
# 1/8, 3/8, 5/8, 7/8
# 1/7, 2/7, 3/7, 4/7, 5/7, 6/7
# 1/6, 5/6
# 1/5, 2/5, 3/5, 4/5
# 1/4, 3/4
# 1/3, 2/3
# 1/2
#
# Eliminating fractions less than or equal to 1/3, we have...
# 3/8, 5/8, 7/8
# 3/7, 4/7, 5/7, 6/7
# 5/6
# 2/5, 3/5, 4/5
# 3/4
# 2/3
# 1/2
#
# Eliminating fractions greater than or equal to 1/2, we have...
# 3/8
# 3/7
# 2/5
#
# So the answer is 3

LIMIT_D = 8
LIMIT_D = 12000

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

answer = 0
for d in range(1,LIMIT_D+1):
    for n in range(d/3,d/2+1):
        if (n == 0):        continue
        if (gcd(n,d) != 1): continue  # Eliminate because HCF(n,d) != 1
        if ((3*n) <= d):    continue  # Eliminate because <= 1/3
        if ((2*n) >= d):    continue  # Eliminate because >= 1/2
        #print "Found {0}/{1}".format(n/gcd(n,d), d/gcd(n,d))
        answer += 1
        if ((answer % 25000) == 0):
            print "Found {0} answers so far, latest one is {1}/{2}".format(answer, n/gcd(n,d), d/gcd(n,d))

print "Answer = ", answer
