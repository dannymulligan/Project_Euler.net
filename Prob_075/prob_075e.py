#!/usr/bin/python
#
# Project Euler.net Problem 75
#
# It turns out that 12 cm is the smallest length of wire that can be
# bent to form an integer sided right angle triangle in exactly one
# way, but there are many more examples.
# 
#     12 cm: (3,4,5)
#     24 cm: (6,8,10)
#     30 cm: (5,12,13)
#     36 cm: (9,12,15)
#     40 cm: (8,15,17)
#     48 cm: (12,16,20)
# 
# In contrast, some lengths of wire, like 20 cm, cannot be bent to
# form an integer sided right angle triangle, and other lengths allow
# more than one solution to be found; for example, using 120 cm it is
# possible to form exactly three different integer sided right angle
# triangles.
# 
#     120 cm: (30,40,50), (20,48,52), (24,45,51)
# 
# Given that L is the length of the wire, for how many values of L <=
# 1,500,000 can exactly one integer sided right angle triangle be
# formed?
# 
# Note: This problem has been changed recently, please check that you
# are using the right parameters.
#
# 10/9/09:
# Solved 76 problems, position 406 on Level 2 table


# If a triangle formed by points X, Y, & Z, and sides of length A, B,
# & C as follows...
#
#              Y
#             +
#            /|
#           / |
#       C  /  | B
#         /   | 
#        /    |
#       +-----+
#     Z    A   X
#
# ...with A as the shortest side, and C as the hypotenuse.  Now...
#
#     A + B + C = L
#
# ...and...
#
#     A^2 + B^2 = C^2
#
# Due to symmetry, we only look at triangles where angle XZY is >=45
# degrees.
#

# Generator function using M & N, with M > N
#    A = M^2 - N^2
#    B = 2MN
#    C = M^2 + N^2
#    L = A + B + C
#      = 2M^2 + 2MN
#
# Example: M = 2, & N = 1, gives (3, 4, 5) & L = 12
#
# The maximum value of L will be given when N = M - 1
#    MAX_L = 2M^2 + 2M(M-1)
#          = 2M^2 + 2M^2 - 2M
#          = 4M^2 - 2M
#
# Example: M = 7, & N = 6, gives (13, 84, 85) & L = 172
# Example: M = 8, & N = 7, gives (15, 112, 113) & L = 240
#
# 

MAX_L = 1500000

def gcd(a,b):
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a


# Create the L list
L_list = [0] * MAX_L

M_lim = 1 + int((MAX_L/2)**.5)

# Scan all possible combinations of N & M
for M in range(2, M_lim+1):
    for N in range (1, M):
        A = M*M - N*N
        B = 2*M*N
        C = M*M + N*N
        L = A + B + C
        if (gcd(A,B) == 1):
            if (L < MAX_L):
                L_list[L] += 1
                ##print "Found ({0}, {1}, {2}) L = {3}".format(A, B, C, L)
            for X in range(2, MAX_L/L+1):
                if (X*L < MAX_L):
                    L_list[X*L] += 1
                    ##print "Dup   ({0}, {1}, {2}) L = {3}".format(X*A, X*B, X*C, X*L)

# Report results
print "Found {0} solutions".format(L_list.count(1))

    
    
