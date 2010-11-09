#!/usr/bin/python
#
# Project Euler.net Problem 100
#
# If a box contains twenty-one coloured discs, composed of fifteen blue
# discs and six red discs, and two discs were taken at random, it can be
# seen that the probability of taking two blue discs, P(BB) =
# (15/21)x(14/20) = 1/2.
#
# The next such arrangement, for which there is exactly 50% chance of
# taking two blue discs at random, is a box containing eighty-five blue
# discs and thirty-five red discs.
#
# By finding the first arrangement to contain over 10^(12) =
# 1,000,000,000,000 discs in total, determine the number of blue discs
# that the box would contain.
#

# Notes:
# Given B blue disks out of N disks
# P(BB) = B/N * (B-1)/(N-1)
#       = B * (B-1) / (N * (N-1))
#
# P(BB) = 0.5
#
# 0.5 = B*(B-1) / (N*(N-1))
# N*(N-1) = 2 B*(B-1)
# or N^2 - N = 2B^2 - 2B
#
# For B = 15, N = 21
#    21 * 20 = 2 * 15 * 14  True
#
# For B = 85, N = 120
#    120 * 119 = 2 * 85 * 84  True
#
# N = 10^12 = 1000^4 ~= 40 bits
# N^2 will be 80 bits, too large for a standard int
#
# Solution: N = 21, B = 15
# Solution: N = 120, B = 85
# Solution: N = 697, B = 493
# Solution: N = 4060, B = 2871
# Solution: N = 23661, B = 16731
# Solution: N = 137904, B = 97513
# Solution: N = 803761, B = 568345
# Solution: N = 4684660, B = 3312555

# Solution: N = 1,070,379,110,497, B = 756,872,327,473


import math, sys

search_start = 1070379110000
#search_end   = search_start + 100000000  # + 10^9
#search_start = 20
search_end   = search_start + 10000

iter_tot = 0
iter_num = 0

for n in range(search_start, search_end):
    if ((n % 1000000) == 0):
        print "Trying n = %d" % (n)

    b_u = int(n)               # _u = upper bound
    b_l = int(n/2)             # _l = lower bound
    b_g = int((b_l + b_u)/2)   # _g = guess

    rem_u = (n*(n-1)) - (2*b_u*(b_u-1))  # _u = upper bound
    rem_l = (n*(n-1)) - (2*b_l*(b_l-1))  # _g = guess
    rem_g = (n*(n-1)) - (2*b_g*(b_g-1))  # _l = lower bound

    if (rem_u > 0) | (rem_l < 0):
        print "Initial guesses for b_l & b_u don't work"
        sys.exit()

    iter_num += 1
    n_n_1 = n*(n-1)
    while ((rem_g != 0) & ((b_u-b_l) > 1)):
        iter_tot += 1
        if rem_g > 0:
            b_l = b_g
            rem_l = rem_g
        else:
            b_u = b_g
            rem_u = rem_g

        b_g = (b_l + b_u)/2
        rem_g = (n_n_1 - (2*b_g*(b_g-1)))

    if (rem_g == 0):
        print "Solution: N = %d, B = %d" % (n, b_g)

print "Average num of iterations = %6.2f" % (float(iter_tot)/float(iter_num))
print "Tot iterations = %d, Count of iterations = %d" % (iter_tot, iter_num)

## import pdb
##
## def try_clue(limit, poss, clue, dof, cb0, cb1):
##     for i in range(dof+1):
##
##         nposs = poss + '0'*i
##         if (i == 0):
##             nlimit = limit
##         elif (limit[0:i].find('1') == -1):
##             nlimit = limit[i:]
##         else:
##             continue
##
##         nposs = nposs + '1'*clue[0]
##         if ((clue[0] == 1) & (nlimit[0] == '0')):
##             nlimit = nlimit[1:]
##         elif (nlimit[0:clue[0]].find('0') == -1):
##             nlimit = nlimit[clue[0]:]
##         else:
##             continue
##
##         if (len(clue) > 1):
##
##             nposs = nposs + '0'
##
##             if (nlimit[0].find('1') == -1):
##                 nlimit = nlimit[1:]
##             else:
##                 continue
##
##             try_clue(nlimit, nposs, clue[1:], dof-i, cb0, cb1)
##         else:
##             nposs = nposs + '0'*(dof-i)
##
##             if ((dof-i) == 0):
##                 nlimit = ""
##             elif (nlimit[0:i].find('1') == -1):
##                 nlimit = nlimit[i:]
##             else:
##                 continue
##
##             print nposs
##             for j in range(len(nposs)):
##                 #print "nposs[%d] = \'%c\'" % (j, nposs[j])
##                 if (nposs[j] == '1'):
##                     cb1[j] = '1'
##                 else:
##                     cb0[j] = '0'
##
## print "Hello, world!"
##
## size = [15, 10]
## a = [ 8, 1, 1 ]
##
## length = 0
## for i in a:
##     length += i
## length += len(a) - 1
## dof = size[0] - length
##
## if __name__ == '__main__':
##     #pdb.set_trace()
##     poss = ""
##     limit = "...1.1........."
##     print limit + " <- limit"
##     cb1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
##     cb0 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
##     try_clue(limit, poss, a, dof, cb0, cb1)
##     print "cb0 = \'%s\'" % cb0
##     print "cb1 = \'%s\'" % cb1
##
##
## # tot_a = sum of elements in list a
## # tot_b = count of elements in list a
## # spaces = tot_b - 1
## # tot_c = tot_a + spaces
## # room = len - tot_c
##
## # distribute room across spaces
## # compare each distribution candidate with constraint
## # if passes constraint, compare with accumulated result
## # accumulated result has 0 for conflicted, 1 for definitely black, -1 for definitely white
