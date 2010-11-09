#!/usr/bin/python
#
# Project Euler.net Problem 64
#
# All square roots are periodic when written as continued fractions
# and can be written in the form:
#
#     sqrt(N) = a0 +	     1
#                   -----------------
#                   a1 +      1
#                       -------------
#                       a2 +     1
#                           ---------
#                           a3 +  ...
#
# For example, let us consider sqrt(23):
#
#     sqrt(23) = 4 + sqrt(23) - 4
#
#                            1
#              = 4 +  ----------------
#                              1
#                         ------------
#                         sqrt(23) - 4
#
#                            1
#              = 4 +  ----------------
#                         sqrt(23) - 3
#                     1 + ------------
#                              7
#
# If we continue we would get the following expansion:
#
#     sqrt(23) = 4 + 	     1
#                   -----------------
#                   1 +       1
#                      --------------
#                      3 +     1
#                         -----------
#                         1 +   1
#                            --------
#                            8 + ...
#
# The process can be summarised as follows:
#
#                 1         sqrt(23) + 4       sqrt(23) - 3
#    a0 = 4, ------------ = ------------ = 1 + ------------
#            sqrt(23) - 4          7                7
#
#                 7         7(sqrt(23) + 3)       sqrt(23) - 3
#    a1 = 1, ------------ = --------------- = 3 + ------------
#            sqrt(23) - 3          14                  2
#
#                 2         2(sqrt(23) + 3)       sqrt(23) - 4
#    a2 = 3, ------------ = --------------- = 1 + ------------
#            sqrt(23) - 3          14                  7
#
#                 7         7(sqrt(23) + 4)       
#    a3 = 1, ------------ = --------------- = 8 + sqrt(23) - 4
#            sqrt(23) - 4          7                  
#
#                 1         sqrt(23) + 4       sqrt(23) - 3
#    a4 = 8, ------------ = ------------ = 1 + ------------
#            sqrt(23) - 4         7                  7
#
#                 7         7(sqrt(23) + 3)       sqrt(23) - 3
#    a5 = 1, ------------ = --------------- = 3 + ------------
#            sqrt(23) - 3         14                   2
#
#                 2         2(sqrt(23) + 3)       sqrt(23) - 4
#    a6 = 3, ------------ = --------------- = 1 + ------------
#            sqrt(23) - 3         14                   7
#
#                 7         7(sqrt(23) + 4)       
#    a7 = 1, ------------ = --------------- = 8 + sqrt(23) - 4
#            sqrt(23) - 4          7                  
#
# It can be seen that the sequence is repeating. For conciseness, we
# use the notation sqrt(23) = [4;(1,3,1,8)], to indicate that the
# block (1,3,1,8) repeats indefinitely.
#
# The first ten continued fraction representations of (irrational)
# square roots are:
# 
#     sqrt(2)  = [1;(2)],          period=1
#     sqrt(3)  = [1;(1,2)],        period=2
#     sqrt(5)  = [2;(4)],          period=1
#     sqrt(6)  = [2;(2,4)],        period=2
#     sqrt(7)  = [2;(1,1,1,4)],    period=4
#     sqrt(8)  = [2;(1,4)],        period=2
#     sqrt(10) = [3;(6)],          period=1
#     sqrt(11) = [3;(3,6)],        period=2
#     sqrt(12) = [3;(2,6)],        period=2
#     sqrt(13) = [3;(1,1,1,1,6)],  period=5
# 
# Exactly four continued fractions, for N <= 13, have an odd period.
# 
# How many continued fractions for N <= 10000 have an odd period?
#
# Answer: 1322
# Solved 10/28/09
# 93 problems solved
# Position #85 on level 2

def sqrt_floor(n):
    i = 1
    while (i**2 <= n):
        i += 1
    return (i - 1)

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a


answer = 0
#for n in range(2,14):
for n in range(2,10001):
    if (sqrt_floor(n)**2 == n):  continue

    x = sqrt_floor(n)
    n1 = n
    n2 = -x
    d1 = 1
    #                sqrt(n) - x
    # sqrt(n) =  x + -----------
    #                     1
    #
    #                sqrt(n1) + n2
    #         =  x + -------------
    #                     d1
    #
    #                      1
    #         =  x + -----------------
    #                       d1
    #                  -------------
    #                  sqrt(n1) + n2
    #

    solution = [(x,n1,n2,d1)]

    found = False
    iteration = 0
    while ((iteration < 1000) & (not found)):
        iteration += 1
        #       d1                d1 * (sqrt(n1) - n2)
        #  ------------- =  ---------------------------------
        #  sqrt(n1) + n2    (sqrt(n1) + n2) * (sqrt(n1) - n2)
        #
        #                   d1 * (sqrt(n1) - n2)
        #                =  --------------------
        #                        n1 - n2**2
        #
        #                   sqrt(in1) + in2
        #                =  ---------------
        #                         id1
        id1 = n1 - (n2**2)
        fac = gcd(id1,d1)
        id1 = id1 / fac
        d1  = d1 / fac
        in1 = n1 * (d1**2)
        in2 = -n2 * d1

        # sqrt(in1) + in2        sqrt(in1) + in2 - x*id1
        # --------------- =  x + -----------------------
        #       id1                         id1
        #
        #                        sqrt(n1) + n2
        #                 =  x + -------------
        #                             d1
        #
        # where x is the max value that still keeps this equation > 0
        #
        #                              1
        #                 =  x + -----------------
        #                               d1
        #                          -------------
        #                          sqrt(n1) + n2
        x = sqrt_floor(in1)
        x = (x + in2) / id1
        d1 = id1
        n1 = in1
        n2 = in2 - id1*x

        solution.append((x,n1,n2,d1))

        i = 0
        while (solution[i] != (x,n1,n2,d1)):
            i += 1
            if ((i != iteration) & (solution[i] == (x,n1,n2,d1))):
                found = True
                period = iteration - i
                if ((period % 2) == 1):
                    answer += 1

    #print "sqrt({0}) = ".format(n), solution, "period =", period
    #print n, period

print "Answer = ", answer
