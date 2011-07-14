#!/usr/bin/python
#
# Project Euler.net Problem 65
#
# The square root of 2 can be written as an infinite continued fraction.
#
#     sqrt(2) = 1 +        1
#                  ---------------------
#                  2 +        1
#                     ------------------
#                      2 +       1
#                         --------------
#                          2 +     1
#                             ----------
#                              2 + .....
#
# The infinite continued fraction can be written, sqrt(2) = [1;(2)],
# (2) indicates that 2 repeats ad infinitum. In a similar way,
# sqrt(23) = [4;(1,3,1,8)].
#
# It turns out that the sequence of partial values of continued
# fractions for square roots provide the best rational
# approximations. Let us consider the convergents for sqrt(2).
#
#     1 +  1
#         ---  = 3/2
#          2
#
#     1 +    1
#         ------  = 7/5
#         2 + 1 
#            ---
#             2
#
#     1 +    1
#         ----------  = 41/29
#         2 +   1 
#            -------
#             2 + 1
#                ---
#                 2
#
# Hence the sequence of the first ten convergents for sqrt(2) are:
#
#     1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985,
#     3363/2378, ...
#
# What is most surprising is that the important mathematical constant,
#
#     e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#
# The first ten terms in the sequence of convergents for e are:
#
#     2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#
# The sum of digits in the numerator of the 10^(th) convergent is
# 1+4+5+7=17.
#
# Find the sum of digits in the numerator of the 100th convergent of
# the continued fraction for e.
#
# Solved 10/26/09
# 89 problems solved
# Position #156 on level 2


# run the sqrt(2) case
print "# run the sqrt(2) case"
e_terms = [1]
for i in range(1,30):
    e_terms.append(2)

for x in range(1,10):
    sn = 1
    sd = e_terms[x]
    for i in range (x-1,0,-1):
        n = e_terms[i]*sd + sn
        d = sd
        sn = d
        sd = n
        #print "i = {4}: sn = {0}, sd = {1}, n = {2}, d = {3}".format(sn, sd, n, d, i)
    sn += sd*e_terms[0]
    print "{0}: {1}/{2}".format(x+1, sn, sd)

# Run the e case
print "# Run the e case"
e_terms = [2]
for i in range(1,35):
    e_terms.append(1)
    e_terms.append(i*2)
    e_terms.append(1)

for x in range(1,100):
    sn = 1
    sd = e_terms[x]
    for i in range (x-1,0,-1):
        n = e_terms[i]*sd + sn
        d = sd
        sn = d
        sd = n
        #print "i = {4}: sn = {0}, sd = {1}, n = {2}, d = {3}".format(sn, sd, n, d, i)
    sn += sd*e_terms[0]
    print "{0}: {1}/{2}".format(x+1, sn, sd)

n_digits = list(str(sn))
print n_digits

Answer = 0
for n in n_digits:
    Answer += int(n)
print "Answer =", Answer
