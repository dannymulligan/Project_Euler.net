#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 190
#
# Maximizing a weighted product
#
# Let Sm = (x1, x2, ... , xM) be the m-tuple of positive real numbers
# with x1 + x2 + ... + xm = m for which Pm = x1 * x2^2 * ... * xm^m is
# maximised.
#
# For example, it can be verified that [P10] = 4112 (where [ ] is the
# integer part function).
#
# Find Sum[Pm] for 2 <= m <= 15.


# Assume x1 = m - x2 - x3 ... - xm
#
# To maximize Pm, we pick starting values for x2, x3, ..., xm.
# Calculate the gradient d(Pm)/d(xi), for i in 2...m
# Adjust each xi by temp*d(Pm)/d(xi)
# Gradually decrease temp, and check for convergence
#
# Pm = (m - x2 - ... - xm - ... - xm) * x2^2 * ... * xi^i * ... * xm^m
#
# Pm = ((m - x2 - ... xm) * x2^2 * ... * xm^m * xi^i)
#      - (x2^2 * ... * xm^m * xi^(i+1))
#
# d(Pm)/d(xI) = ((m - x2 - ... xm) * x2^2 * ... * xm^m * i * xi^(i-1))
#               - (x2^2 * ... * xm^m * (i+1) * xi^i)

import sys
import numpy as np
import math

SIZE = 2

def distance(x, y):
    dist = [(a-b)**2 for a, b in zip(x, y)]
    dist = math.sqrt(sum(dist))
    return dist

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

    >>> angle_between((1, 0, 0), (0, 1, 0))
    1.5707963267948966
    >>> angle_between((1, 0, 0), (1, 0, 0))
    0.0
    >>> angle_between((1, 0, 0), (-1, 0, 0))
    3.141592653589793
    Taken from: https://stackoverflow.com/questions/2827393/angles-between-two-n-dimensional-vectors-in-python/13849249#13849249
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

                     
def dPm_xi (x, m):
    result = [0.0 for x in range(m+1)]
    for i in range(2, m+1):
        product = 1.0
        for n in range(2, m+1):
            if n == i:
                continue
            product *= x[n]**n
        x1 = (m - sum(x[2:m+1]) + x[i])
        result[i] = (x1 * product *  i      * x[i]**(i-1.0)
                     -    product * (i+1.0) * x[i]**i      )
    return result

def print_it(name, x, m):
    x1 = m - sum(x[2:])
    print("{}1 = {:10.7f}".format(name, x1), end='')
    for i in range(2, len(x)):
        print(", {}{} = {:10.7f}".format(name, i, x[i]), end='')
    
    
def norm(gradient):
    x = sum(gradient[2:])**2
    for i in gradient[2:]:
        x += i**2
    return x ** 0.5


def Pm(m, temp = 1e-3, decay = 0.99, Debug = False):
    x = [1.0 for x in range(m+1)]
    x[0] = 0.0
    P = x[1]
    for i in range(2, m+1):
        P *= x[i] ** i
    delta_P = 0.0

    gradient_norm = 999.0
    n = 1
    while gradient_norm > 1e-6:
        gradient = dPm_xi(x, m)
        gradient_norm = norm(gradient)

        previous_P = P
        P = x[1]
        for i in range(2, m+1):
            P *= x[i] ** i
        delta_P = P - previous_P

        if Debug:
            print("{:4}: ".format(n), end='')
            print_it('x', x, m)
            #print(",  P    = {:.12f}, delta_p = {:.12f}, distance = {:.12f}".format(P, delta_P, distance(x, solution)))
            print(",  P    = {:.12f}, distance = {:.12f}".format(P, distance(x[1:], solution)))
            
            print("      ", end='')
            print_it('g', gradient, 0)
            print(",  norm = {:.12f}, angle = {:.12f}".format(gradient_norm, angle(x[1:], solution)))

            print()

        for i in range(2, m+1):
            x[i] += temp*gradient[i]
        x[1] = m - sum(x[2:])
        n += 1
        if (n % 10) == 0:
            temp *= decay

        if n > 25000:
            return P

    print("Calculated {} in {} iterations".format(P, n))
    print("x = {}".format(x[1:]))
    return P


#solution = [2.0/3.0, 4.0/3.0]
#m = 2
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-2)))
#
#solution = [2.0/4.0, 4.0/4.0, 6.0/4.0]
#m = 3
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-2)))
#
#solution = [2.0/5.0, 4.0/5.0, 6.0/5.0, 8.0/5.0]
#m = 4
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-2)))
#
#solution = [2.0/6.0, 4.0/6.0, 6.0/6.0, 8.0/6.0, 10.0/6.0]
#m = 5
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-2)))
#
#solution = [2.0/7.0, 4.0/7.0, 6.0/7.0, 8.0/7.0, 10.0/7.0, 12.0/7.0]
#m = 6
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-3)))

solution = [2.0/8.0, 4.0/8.0, 6.0/8.0, 8.0/8.0, 10.0/8.0, 12.0/8.0]
m = 7
print("Pm({}) = {}".format(m, Pm(m, temp=1e-3, Debug=True)))

#solution = [2.0/9.0, 4.0/9.0, 6.0/9.0, 8.0/9.0, 10.0/9.0, 12.0/9.0, 14.0/9, 16.0/9.0]
#m = 8
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-3, Debug=True)))

#m = 8
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4, Debug=False)))

#solution = [2.0/9.0, 4.0/9.0, 6.0/9.0, 8.0/9.0, 10.0/9.0, 12.0/9.0, 14.0/9, 16.0/9.0]
#m = 9
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4, Debug=False)))  # Doesn't work

#m = 10
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4)))  # Doesn't work

#m = 11
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4)))  # Doesn't work

#m = 12
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4)))  # Doesn't work

#m = 13
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4)))  # Doesn't work

#m = 14
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4)))  # Doesn't work

#m = 15
#print("Pm({}) = {}".format(m, Pm(m, temp=1e-4)))  # Doesn't work

