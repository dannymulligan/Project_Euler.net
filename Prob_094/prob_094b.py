#!/usr/bin/python
#
# Project Euler.net Problem 94
#
# It is easily proved that no equilateral triangle exists with
# integral length sides and integral area. However, the almost
# equilateral triangle 5-5-6 has an area of 12 square units.
# 
# We shall define an almost equilateral triangle to be a triangle for
# which two sides are equal and the third differs by no more than one
# unit.
# 
# Find the sum of the perimeters of all almost equilateral triangles
# with integral side lengths and area and whose perimeters do not
# exceed one billion (1,000,000,000).
#
# Answer: 518408346
# Solved 11/5/09
# 96 problems solved
# Position #43 on level 2

# From http://mathschallenge.net/index.php?section=problems&show=true&titleid=almost_equilateral_triangles&full=true#solution
#
# By the definition an almost equilateral triangles measuring a-a-b is isosceles.
#
#            /|\
#           / | \
#          /  |  \
#         /   |   \
#      a /    |h   \ a
#       /     |     \
#      /      |      \
#     --------+--------
#             b
# 
# Using the Pythagorean Theorem: a^2 = (b/2)^2 + h^2, so 4a^2 = b^2 + 4h^2.
# 
# As b = a +/- 1, therefore b^2 = a^2 +/- 2a + 1
# 
# therefore
#     4a^2 = a^2 +/- 2a + 1 + 4h^2
#     3a^2 +/- 2a - 1 - 4h2 = 0  (note: correction to original source)
#     9a^2 +/- 6a - 3 - 12h^2 = 0
#     9a^2 +/- 6a + 1 - 12h^2 = 4
#     (3a +/- 1)^2 - 12h^2 = 4
#
# therefore ((3a +/- 1)/2)^2 - 3h^2 = 1
# 
# By writing x = (3a +/- 1)/2 and y = h, we get the Pell equation: x^2 - 3y^2 = 1.
# Given one solution, it is well known that Pell equations have
# infinitely many solutions.
#
# However, we must first show that integer x corresponds to an integer
# solutions for a; b being integer follows as b = a +/- 1.
#
# As x = (3a +/- 1)/2, we get a = (2x +/- 1)/3
#
# It should be clear that x cannot be divisible by 3, otherwise 
# x^2 - 3y^2 would be a multiple of 3 and could not be equal to 1.
#
# So given that x =congruent= +/-1 mod 3, 2x =congruent= +/-1 mod 3,
# and so one of 2x+1 or 2x-1 will be a multiple of 3. Hence for every
# integer solution of the equation x^2 - 3y2 = 1, we have an
# integer solution for a and b. Now we shall prove that infinitely
# many solutions exist.
#
# Given (x,y), a solution pair to the Pell equation x^2 - 3y^2 = 1,
# consider the larger pair (x^2+3y^2,2xy):
#
#  (x^2+3y^2)^2 - 3(2xy)^2 = x^4 + 6x^2y^2 + 9y^4 -12x^2y^2
#                          = x^4 - 6x^2y^2 + 9y^4
#                          = (x^2 - 3y^2)2
#                          = 1
#
# In other words, if (x,y) is a solution then (x^2+3y^2,2xy) will also
# be a solution, and as (7,4) leads to the first solution 5-5-6, we
# prove that infinitely many almost equilateral triangles with
# integral length sides and area exist.
#
# Note that although the infinite solution set of the Pell equation
# x^2 - 3y^2 = 1 is in a one-to-one mapping with the set of almost
# equilateral triangles we are seeking, this particular iterative
# method: (x,y) maps (x2+3y2,2xy), will NOT produce every solution.

# From http://en.wikipedia.org/wiki/Triangle
#
# Area of a triangle with sides of length A, B, & C
#     S = sqrt(s * (s - A) * (s - B) * (s - C))
# where s = (A + B + C)/2

# We solved equations of the form x^2 - Dy^2 in problem 66
# (diophantine equations) so this solution is derived from that one.
# The solution in problem 66 was in turn derived from the solution for
# problem 64.

# Solutions found...
# (a,b,c) perimeter
# (5,5,6) 16
# (17,17,16) 50
# (65,65,66) 196
# (241,241,240) 722
# (901,901,902) 2704
# (3361,3361,3360) 10082
# (12545,12545,12546) 37636
# (46817,46817,46816) 140450
# (174725,174725,174726) 524176
# (652081,652081,652080) 1956242
# (2433601,2433601,2433602) 7300804
# (9082321,9082321,9082320) 27246962
# (33895685,33895685,33895686) 101687056
# (126500417,126500417,126500416) 379501250
# Answer = 518408350


ITER_LIMIT = 40  # actually, 33 is enough iterations to get above 1 billion
SIZE_LIMIT = 1000000000

def sqrt_floor(n):
    i = int(float(n)**0.5) - 10
    if (i <= 0):  i = 1
    while (i**2 <= n):
        i += 1
    return (i - 1)

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a

def test_IAT(a,b,c):
    # Test if triangle with lengths a, b, c is an Integer Area Triangle (IAT)

    # If any side is 0, then area is 0
    if ((a*b*c) == 0):  return False

    # If any side is too long, then not a triangle
    if ((a>=(b+c)) | (b>=(a+c)) | (c>=(a+b))):  return False

    # From above, area X is given by
    #     X = sqrt(s * (s - A) * (s - B) * (s - C))
    # where s = (A + B + C)/2
    # Thus
    #     4*X = 4 * sqrt(s * (s - A) * (s - B) * (s - C))
    #     4*X = sqrt(16 * s * (s - A) * (s - B) * (s - C))
    #     4*X = sqrt(2*s * 2*(s - A) * 2*(s - B) * 2*(s - C))
    #     4*X = sqrt(2*s * (2*s - 2*A) * (2*s - 2*B) * (2*s - 2*C))
    #     4*X = sqrt(2*s * (2*s - 2*A) * (2*s - 2*B) * (2*s - 2*C))
    #     16*X^2 = (2*s * (2*s - 2*A) * (2*s - 2*B) * (2*s - 2*C))
    s2 = (a + b + c)
    s2a2 = s2 - 2*a
    s2b2 = s2 - 2*b
    s2c2 = s2 - 2*c
    XX16 = s2 * s2a2 * s2b2 * s2c2

    # This is an IAT if X is integer
    if ((XX16 % 16) != 0):  return False
    XX = XX16 / 16
    #X = int(float(XX)**0.5)
    X = sqrt_floor(XX)
    if (X**2 != XX):  return False
    return True


answer = 0
D = 3
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
    print "sqrt({0}): convegent = {1} / {2}".format(D, cn, cd)

    # Test the convergent on the Diophantine equation
    (x,y) = (cn,cd)
    if ((x*x - D*y*y) == 1):
        print "{0}^2 - {1} x {2}^2 = 1".format(x,D,y)
        print "(x,y) = ({0},{1})".format(x,y)

        if (((2*x + 1) % 3) == 0):
            a = (2*x + 1)/3
            b = a - 1
            perimeter = a + a + b
            print "Trying +- ({0},{0},{1}) {2}".format(a,b, perimeter),
            if (perimeter < SIZE_LIMIT) & test_IAT(a, a, b):
                answer += perimeter
                print "integer area"
            else:
                print

            b = a + 1
            perimeter = a + a + b
            print "Trying ++ ({0},{0},{1}) {2}".format(a,b, perimeter),
            if (perimeter < SIZE_LIMIT) & test_IAT(a, a, b):
                answer += perimeter
                print "integer area"
            else:
                print

        if (((2*x - 1) % 3) == 0):
            a = (2*x - 1)/3
            b = a - 1
            perimeter = a + a + b
            print "Trying -- ({0},{0},{1}) {2}".format(a,b, perimeter),
            if (perimeter < SIZE_LIMIT) & test_IAT(a, a, b):
                answer += perimeter
                print "integer area"
            else:
                print

            b = a + 1
            perimeter = a + a + b
            print "Trying -+ ({0},{0},{1}) {2}".format(a,b, perimeter),
            if (perimeter < SIZE_LIMIT) & test_IAT(a, a, b):
                answer += perimeter
                print "integer area"
            else:
                print

        if (perimeter > SIZE_LIMIT):
            found = True

if (iteration == ITER_LIMIT):
    print "Warning: reached iteration limit"
#print "sqrt({0}) = ".format(n), solution, "period =", period
#print n, period


print "Answer = ", answer
