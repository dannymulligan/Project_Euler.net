#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 148
#
# Problem summary
#
# We can easily verify that none of the entries in the first seven
# rows of Pascal's triangle are divisible by 7:
#
#                      1
#                   1     1
#                1     2     1
#             1     3     3     1
#          1     4     6     4     1
#       1     5    10    10     5     1
#    1     6    15    20    15     6     1
#
# However, if we check the first one hundred rows, we will find that
# only 2361 of the 5050 entries are not divisible by 7.
#
# Find the number of entries which are not divisible by 7 in the first
# one billion (10^9) rows of Pascal's triangle.
#
# Solved 08/24/10
# 118 problems solved
# Position #775 on level 3

# From the brute force solution
#
# When n =      7 Answer =        28
# When n =     14 Answer =        84
# When n =     49 Answer =       784  (7**2 =    49, 28**2 =     784)
# When n =    100 Answer =     2,361
# When n =    343 Answer =    21,952  (7**3 =   343, 28**3 =  21,952)
# When n =  1,000 Answer =   118,335
# When n =  2,401 Answer =   614,656  (7**4 = 2,401, 28**4 = 614,656)
# When n = 10,000 Answer = 6,264,360

def brute_force_soln (rows):
    res = 0

    pascal = [1]  # Row 1
    # print 1, pascal
    res += 1

    pascal = [1, 1]  # Row 2
    # print 2, pascal
    if (rows >= 2):
        res += 2

    for n in range(3,rows+1):
        pascal_next = [1]
        res += 1
        for i in range(0,(len(pascal)-1)):
            t = (pascal[i] + pascal[i+1]) % 7
            pascal_next.append(t)
            if (t != 0):
                res += 1
        pascal_next.append(1)
        res += 1

        pascal = pascal_next
        # print n, pascal
    return res

#for n in (7, 14, 7**2, 100, 7**3, 1000, 7**4, 10000):
#    answer = brute_force_soln(n)
#    print "When n =", n, "Answer =", answer


# Check out the pattern in a spreadsheet
# The pattern is recursive, and yields solutions of 28**n for rows = 7**n

def elegant_soln (rows):
    if   (rows == 0):          return 0
    elif (rows <  1*(7** 1)):  return rows*(rows+1)/2
    elif (rows == 1*(7** 1)):  return 28**1
    elif (rows <  2*(7** 1)):  return ( 1*elegant_soln(7** 1) + 2*elegant_soln(rows - 1*(7** 1)))
    elif (rows <  3*(7** 1)):  return ( 3*elegant_soln(7** 1) + 3*elegant_soln(rows - 2*(7** 1)))
    elif (rows <  4*(7** 1)):  return ( 6*elegant_soln(7** 1) + 4*elegant_soln(rows - 3*(7** 1)))
    elif (rows <  5*(7** 1)):  return (10*elegant_soln(7** 1) + 5*elegant_soln(rows - 4*(7** 1)))
    elif (rows <  6*(7** 1)):  return (15*elegant_soln(7** 1) + 6*elegant_soln(rows - 5*(7** 1)))
    elif (rows <  7*(7** 1)):  return (21*elegant_soln(7** 1) + 7*elegant_soln(rows - 6*(7** 1)))

    elif (rows == 1*(7** 2)):  return 28**2
    elif (rows <  2*(7** 2)):  return ( 1*elegant_soln(7** 2) + 2*elegant_soln(rows - 1*(7** 2)))
    elif (rows <  3*(7** 2)):  return ( 3*elegant_soln(7** 2) + 3*elegant_soln(rows - 2*(7** 2)))
    elif (rows <  4*(7** 2)):  return ( 6*elegant_soln(7** 2) + 4*elegant_soln(rows - 3*(7** 2)))
    elif (rows <  5*(7** 2)):  return (10*elegant_soln(7** 2) + 5*elegant_soln(rows - 4*(7** 2)))
    elif (rows <  6*(7** 2)):  return (15*elegant_soln(7** 2) + 6*elegant_soln(rows - 5*(7** 2)))
    elif (rows <  7*(7** 2)):  return (21*elegant_soln(7** 2) + 7*elegant_soln(rows - 6*(7** 2)))

    elif (rows == 1*(7** 3)):  return 28** 3
    elif (rows <  2*(7** 3)):  return ( 1*elegant_soln(7** 3) + 2*elegant_soln(rows - 1*(7** 3)))
    elif (rows <  3*(7** 3)):  return ( 3*elegant_soln(7** 3) + 3*elegant_soln(rows - 2*(7** 3)))
    elif (rows <  4*(7** 3)):  return ( 6*elegant_soln(7** 3) + 4*elegant_soln(rows - 3*(7** 3)))
    elif (rows <  5*(7** 3)):  return (10*elegant_soln(7** 3) + 5*elegant_soln(rows - 4*(7** 3)))
    elif (rows <  6*(7** 3)):  return (15*elegant_soln(7** 3) + 6*elegant_soln(rows - 5*(7** 3)))
    elif (rows <  7*(7** 3)):  return (21*elegant_soln(7** 3) + 7*elegant_soln(rows - 6*(7** 3)))

    elif (rows == 1*(7** 4)):  return 28** 4
    elif (rows <  2*(7** 4)):  return ( 1*elegant_soln(7** 4) + 2*elegant_soln(rows - 1*(7** 4)))
    elif (rows <  3*(7** 4)):  return ( 3*elegant_soln(7** 4) + 3*elegant_soln(rows - 2*(7** 4)))
    elif (rows <  4*(7** 4)):  return ( 6*elegant_soln(7** 4) + 4*elegant_soln(rows - 3*(7** 4)))
    elif (rows <  5*(7** 4)):  return (10*elegant_soln(7** 4) + 5*elegant_soln(rows - 4*(7** 4)))
    elif (rows <  6*(7** 4)):  return (15*elegant_soln(7** 4) + 6*elegant_soln(rows - 5*(7** 4)))
    elif (rows <  7*(7** 4)):  return (21*elegant_soln(7** 4) + 7*elegant_soln(rows - 6*(7** 4)))

    elif (rows == 1*(7** 5)):  return 28** 5
    elif (rows <  2*(7** 5)):  return ( 1*elegant_soln(7** 5) + 2*elegant_soln(rows - 1*(7** 5)))
    elif (rows <  3*(7** 5)):  return ( 3*elegant_soln(7** 5) + 3*elegant_soln(rows - 2*(7** 5)))
    elif (rows <  4*(7** 5)):  return ( 6*elegant_soln(7** 5) + 4*elegant_soln(rows - 3*(7** 5)))
    elif (rows <  5*(7** 5)):  return (10*elegant_soln(7** 5) + 5*elegant_soln(rows - 4*(7** 5)))
    elif (rows <  6*(7** 5)):  return (15*elegant_soln(7** 5) + 6*elegant_soln(rows - 5*(7** 5)))
    elif (rows <  7*(7** 5)):  return (21*elegant_soln(7** 5) + 7*elegant_soln(rows - 6*(7** 5)))

    elif (rows == 1*(7** 6)):  return 28** 6
    elif (rows <  2*(7** 6)):  return ( 1*elegant_soln(7** 6) + 2*elegant_soln(rows - 1*(7** 6)))
    elif (rows <  3*(7** 6)):  return ( 3*elegant_soln(7** 6) + 3*elegant_soln(rows - 2*(7** 6)))
    elif (rows <  4*(7** 6)):  return ( 6*elegant_soln(7** 6) + 4*elegant_soln(rows - 3*(7** 6)))
    elif (rows <  5*(7** 6)):  return (10*elegant_soln(7** 6) + 5*elegant_soln(rows - 4*(7** 6)))
    elif (rows <  6*(7** 6)):  return (15*elegant_soln(7** 6) + 6*elegant_soln(rows - 5*(7** 6)))
    elif (rows <  7*(7** 6)):  return (21*elegant_soln(7** 6) + 7*elegant_soln(rows - 6*(7** 6)))

    elif (rows == 1*(7** 7)):  return 28** 7
    elif (rows <  2*(7** 7)):  return ( 1*elegant_soln(7** 7) + 2*elegant_soln(rows - 1*(7** 7)))
    elif (rows <  3*(7** 7)):  return ( 3*elegant_soln(7** 7) + 3*elegant_soln(rows - 2*(7** 7)))
    elif (rows <  4*(7** 7)):  return ( 6*elegant_soln(7** 7) + 4*elegant_soln(rows - 3*(7** 7)))
    elif (rows <  5*(7** 7)):  return (10*elegant_soln(7** 7) + 5*elegant_soln(rows - 4*(7** 7)))
    elif (rows <  6*(7** 7)):  return (15*elegant_soln(7** 7) + 6*elegant_soln(rows - 5*(7** 7)))
    elif (rows <  7*(7** 7)):  return (21*elegant_soln(7** 7) + 7*elegant_soln(rows - 6*(7** 7)))

    elif (rows == 1*(7** 8)):  return 28** 8
    elif (rows <  2*(7** 8)):  return ( 1*elegant_soln(7** 8) + 2*elegant_soln(rows - 1*(7** 8)))
    elif (rows <  3*(7** 8)):  return ( 3*elegant_soln(7** 8) + 3*elegant_soln(rows - 2*(7** 8)))
    elif (rows <  4*(7** 8)):  return ( 6*elegant_soln(7** 8) + 4*elegant_soln(rows - 3*(7** 8)))
    elif (rows <  5*(7** 8)):  return (10*elegant_soln(7** 8) + 5*elegant_soln(rows - 4*(7** 8)))
    elif (rows <  6*(7** 8)):  return (15*elegant_soln(7** 8) + 6*elegant_soln(rows - 5*(7** 8)))
    elif (rows <  7*(7** 8)):  return (21*elegant_soln(7** 8) + 7*elegant_soln(rows - 6*(7** 8)))

    elif (rows == 1*(7** 9)):  return 28** 9
    elif (rows <  2*(7** 9)):  return ( 1*elegant_soln(7** 9) + 2*elegant_soln(rows - 1*(7** 9)))
    elif (rows <  3*(7** 9)):  return ( 3*elegant_soln(7** 9) + 3*elegant_soln(rows - 2*(7** 9)))
    elif (rows <  4*(7** 9)):  return ( 6*elegant_soln(7** 9) + 4*elegant_soln(rows - 3*(7** 9)))
    elif (rows <  5*(7** 9)):  return (10*elegant_soln(7** 9) + 5*elegant_soln(rows - 4*(7** 9)))
    elif (rows <  6*(7** 9)):  return (15*elegant_soln(7** 9) + 6*elegant_soln(rows - 5*(7** 9)))
    elif (rows <  7*(7** 9)):  return (21*elegant_soln(7** 9) + 7*elegant_soln(rows - 6*(7** 9)))

    elif (rows == 1*(7**10)):  return 28**10
    elif (rows <  2*(7**10)):  return ( 1*elegant_soln(7**10) + 2*elegant_soln(rows - 1*(7**10)))
    elif (rows <  3*(7**10)):  return ( 3*elegant_soln(7**10) + 3*elegant_soln(rows - 2*(7**10)))
    elif (rows <  4*(7**10)):  return ( 6*elegant_soln(7**10) + 4*elegant_soln(rows - 3*(7**10)))
    elif (rows <  5*(7**10)):  return (10*elegant_soln(7**10) + 5*elegant_soln(rows - 4*(7**10)))
    elif (rows <  6*(7**10)):  return (15*elegant_soln(7**10) + 6*elegant_soln(rows - 5*(7**10)))
    elif (rows <  7*(7**10)):  return (21*elegant_soln(7**10) + 7*elegant_soln(rows - 6*(7**10)))


#for n in (7, 14, 7**2, 100, 7**3, 7**4):
#right = 0
#wrong = 0
#for n in range(1, 1000):
#    answer1 = brute_force_soln(n)
#    answer2 = elegant_soln(n)
#    if (answer1 != answer2):
#        print "ERROR:", "When n =", n, "Brute force answer =", answer1, "Elegant answer =", answer2
#        wrong += 1
#    else:
#        right += 1
#print "Right =", right, "wrong =", wrong

for n in (10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9):
    print "N =", n, "answer =", elegant_soln(n)
