#!/usr/bin/python
#
# Project Euler.net Problem 66
#
# Consider quadratic Diophantine equations of the form:
#
#     x^2 - Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 649^2 - 13x180^2 = 1 
# 
# It can be assumed that there are no solutions in positive integers
# when D is square.
# 
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
# the following:
# 
#     3^2 - 2 x 2^2 = 1
#     2^2 - 3 x 1^2 = 1
#    <9>^2 - 5 x 4^2 = 1
#     5^2 - 6 x 2^2 = 1
#     8^2 - 7 x 3^2 = 1
# 
# Hence, by considering minimal solutions in x for D <= 7, the largest
# x is obtained when D=5.
# 
# Find the value of D <= 1000 in minimal solutions of x for which the
# largest value of x is obtained.
#
# Answer: 661
# Solved 10/31/09
# 94 problems solved
# Position #74 on level 2

# The solution here is based on the solution to problem 64.

ITER_LIMIT = 100

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


max_x = 0
max_D = 0
#for D in range(2,8):
for D in range(2,1001):
    if (sqrt_floor(D)**2 == D):  continue

    x = sqrt_floor(D)
    n1 = D
    n2 = -x
    d1 = 1
    #                sqrt(D) - x
    # sqrt(D) =  x + -----------
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

    solution = [x]

    found = False
    iteration = 0
    while ((iteration < ITER_LIMIT) & (not found)):
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

        solution.append(x)

        # Calculate the convergent
        cd = 1
        cn = solution[len(solution)-1]
        for i in range(len(solution)-2,-1,-1):
            (cn,cd) = (cd,cn)
            cn += cd * solution[i]
        #print "{0}: solution={1} convegent={2}/{3}".format(D, solution, cn, cd)

        # Test the convergent on the Diophantine equation
        (x,y) = (cn,cd)
        if ((x*x - D*y*y) == 1):
            found = True
            if (x > max_x):
                max_x = x
                max_D = D
                print "{0}^2 - {1} x {2}^2 = 1 (New max x)".format(x,D,y)
            else:
                print "{0}^2 - {1} x {2}^2 = 1".format(x,D,y)

    if (iteration == ITER_LIMIT):
        print "Warning: reached iteration limit"
    #print "sqrt({0}) = ".format(n), solution, "period =", period
    #print n, period


print "Answer = ", max_D, max_x
