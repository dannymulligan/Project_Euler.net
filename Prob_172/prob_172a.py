#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 172
#
# Investigating numbers with few repeated digits.
#
# How many 18-digit numbers n (without leading zeros) are there such
# that no digit occurs more than three times in n?
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

# This problem is all about combinations & permutations
#
# There are 10 numbers and 18 digits, so we must have one of the following combinations
#
#     (0 x3) + (9 x2) + (0 x1) = 18 digits,  9 numbers used
#     (0 x3) + (8 x2) + (2 x1) = 18 digits, 10 numbers used
#
#     (1 x3) + (7 x2) + (1 x1) = 18 digits,  9 numbers used
#     (1 x3) + (6 x2) + (3 x1) = 18 digits, 10 numbers used
#
#     (2 x3) + (6 x2) + (0 x1) = 18 digits,  8 numbers used
#     (2 x3) + (5 x2) + (2 x1) = 18 digits, 10 numbers used
#
#     (3 x3) + (4 x2) + (1 x1) = 18 digits,  8 numbers used
#     (3 x3) + (2 x2) + (3 x1) = 18 digits, 10 numbers used
#
#     (4 x3) + (3 x2) + (0 x1) = 18 digits,  7 numbers used
#     (4 x3) + (2 x2) + (2 x1) = 18 digits,  8 numbers used
#     (4 x3) + (1 x2) + (4 x1) = 18 digits,  9 numbers used
#     (4 x3) + (0 x2) + (6 x1) = 18 digits, 10 numbers used
#
#     (5 x3) + (1 x2) + (1 x1) = 18 digits,  7 numbers used
#     (5 x3) + (0 x2) + (3 x1) = 18 digits,  8 numbers used
#
#     (6 x3) + (0 x2) + (0 x1) = 18 digits,  6 numbers used
#
# Where x3 = number used 3 times, x2 = number used twice, etc.

import time
import sys


def perm(x3, x2, x1):
    digits = 3*x3 + 2*x2 + x1  # how many long is the number?
    numbers = x3 + x2 + x1     # what numbers are used in the number?
    #print "x3 =", x3, "x2 =", x2, "x1 =", x1, "digits =", digits, "numbers =", numbers
    ans = 1
    for i in range(digits,digits-(x3*3+x2*2),-1):
        ans *= i
        #print "    ans *=", i, "=", ans
    for i in range((x3*3+x2*2),1,-1):
        ans /= i
        #print "    ans /=", i, "=", ans
    for i in range((x3*3+x2*2), 1, -1):
        ans *= i
        #print "    ans *=", i, "=", ans
    for i in range(x3):
        ans /= 6
        #print "    ans /= 6 =", ans
    for i in range(x2):
        ans /= 2
        #print "    ans /= 2 =", ans
    return ans

# (0 x3) + (1 x2) + (3 x1) = 5 digits, 4 numbers used
#   AA***  A*A**  A**A*  A***A
#   *AA**  *A*A*  *A**A
#   **AA*  **A*A
#   ***AA = 5*4 / 2 = 10
#
# (0 x3) + (1 x2) + (4 x1) = 6 digits, 5 numbers used
#   AA****  A*A***  A**A**  A***A*  A****A
#   *AA***  *A*A**  *A**A*  A****A
#   **AA**  **A*A*  **A**A
#   ***AA*  ***A*A
#   ****AA = 6*5 / 2 = 15
#
# (1 x3) + (0 x2) + (3 x1) = 6 digits, 4 numbers used
#   AAA***  AA*A**  AA**A*  AA***A  A*AA**  A*A*A*  A*A**A  A**AA*  A**A*A  A***AA
#   *AAA**  *AA*A*  *AA**A  *A*AA*  *A*A*A  *A**AA
#   **AAA*  **AA*A  **A*AA
#   ***AAA = 6*5*4 / 3*2 = 20
#
# (0 x3) + (2 x2) + (2 x1) = 6 digits, 3 numbers used
#   AABB**  *6 for (AABB, ABAB, ABBA, BAAB, BABA, BBAA)
#   AAB*B*  *6...
#   AAB**B  *6...
#   AA*BB*  *6...
#   AA*B*B  *6...
#   AA**BB  *6...
#   A*ABB*  *6...
#   A*AB*B  *6...
#   A*A*BB  *6...
#   A**ABB  *6...
#   *AABB*  *6...
#   *AAB*B  *6...
#   *AA*BB  *6...
#   *A*ABB  *6...
#   **AABB  *6...
#   = (6*5*4*3 / 4*3*2) * (4*3*2 / 2 / 2) = 90
#
# (1 x3) + (1 x2) + (2 x1) = 7 digits, 4 numbers used
#   AAABB**  *10 for (AAABB, AABAB, AABBA, ABAAB, ABABA, ABBAA, BAAAB, BAABA, BABAA, BBAAA)
#   AAAB*B*  *10...
#   AAAB**B  *10...
#   AAA*BB*  *10...
#   AAA*B*B  *10...
#   AAA**BB  *10...
#   AA*ABB*  *10...
#   AA*AB*B  *10...
#   AA*A*BB  *10...
#   AA**ABB  *10...
#   A*AABB*  *10...
#   A*AAB*B  *10...
#   A*AA*BB  *10...
#   A*A*ABB  *10...
#   A**AABB  *10...
#   *AAABB*  *10...
#   *AAAB*B  *10...
#   *AAA*BB  *10...
#   *AA*ABB  *10...
#   *A*AABB  *10...
#   **AAABB  *10...
#   = (7*6*5*4*3 / 5*4*3*2) * (5*4*3*2 / 3*2 / 2) = 210
#
#print "perm(0,1,3) =", perm(0,1,3)
#print "perm(0,1,4) =", perm(0,1,4)
#print "perm(1,0,3) =", perm(1,0,3)
#print "perm(0,2,2) =", perm(0,2,2)
#print "perm(1,1,2) =", perm(1,1,2)

start_time = time.clock()

ans = 0
print "# (0 x3) + (9 x2) + (0 x1) = 18 digits,  9 numbers used", perm(0,9,0)  # (0 x3) + (9 x2) + (0 x1) = 18 digits,  9 numbers used
print "# (0 x3) + (8 x2) + (2 x1) = 18 digits, 10 numbers used", perm(0,8,2)  # (0 x3) + (8 x2) + (2 x1) = 18 digits, 10 numbers used
print "# (1 x3) + (7 x2) + (1 x1) = 18 digits,  9 numbers used", perm(1,7,1)  # (1 x3) + (7 x2) + (1 x1) = 18 digits,  9 numbers used
print "# (1 x3) + (6 x2) + (3 x1) = 18 digits, 10 numbers used", perm(1,6,3)  # (1 x3) + (6 x2) + (3 x1) = 18 digits, 10 numbers used
print "# (2 x3) + (6 x2) + (0 x1) = 18 digits,  8 numbers used", perm(2,6,0)  # (2 x3) + (6 x2) + (0 x1) = 18 digits,  8 numbers used
print "# (2 x3) + (5 x2) + (2 x1) = 18 digits, 10 numbers used", perm(2,5,2)  # (2 x3) + (5 x2) + (2 x1) = 18 digits, 10 numbers used
print "# (3 x3) + (4 x2) + (1 x1) = 18 digits,  8 numbers used", perm(3,4,1)  # (3 x3) + (4 x2) + (1 x1) = 18 digits,  8 numbers used
print "# (3 x3) + (2 x2) + (3 x1) = 18 digits, 10 numbers used", perm(3,2,3)  # (3 x3) + (2 x2) + (3 x1) = 18 digits, 10 numbers used
print "# (4 x3) + (3 x2) + (0 x1) = 18 digits,  7 numbers used", perm(4,3,0)  # (4 x3) + (3 x2) + (0 x1) = 18 digits,  7 numbers used
print "# (4 x3) + (2 x2) + (2 x1) = 18 digits,  8 numbers used", perm(4,2,2)  # (4 x3) + (2 x2) + (2 x1) = 18 digits,  8 numbers used
print "# (4 x3) + (1 x2) + (4 x1) = 18 digits,  9 numbers used", perm(4,1,4)  # (4 x3) + (1 x2) + (4 x1) = 18 digits,  9 numbers used
print "# (4 x3) + (0 x2) + (6 x1) = 18 digits, 10 numbers used", perm(4,0,6)  # (4 x3) + (0 x2) + (6 x1) = 18 digits, 10 numbers used
print "# (5 x3) + (1 x2) + (1 x1) = 18 digits,  7 numbers used", perm(5,1,1)  # (5 x3) + (1 x2) + (1 x1) = 18 digits,  7 numbers used
print "# (5 x3) + (0 x2) + (3 x1) = 18 digits,  8 numbers used", perm(5,0,3)  # (5 x3) + (0 x2) + (3 x1) = 18 digits,  8 numbers used
print "# (6 x3) + (0 x2) + (0 x1) = 18 digits,  6 numbers used", perm(6,0,0)  # (6 x3) + (0 x2) + (0 x1) = 18 digits,  6 numbers used

print "ans += 9*9*8*7*6*5*4*3*2 * perm(0,9,0)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4*3*2 * perm(0,8,2)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4*3*2 * perm(1,7,1)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4*3*2 * perm(1,6,3)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4*3   * perm(2,6,0)", 9*9*8*7*6*5*4*3  
print "ans += 9*9*8*7*6*5*4*3*2 * perm(2,5,2)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4*3   * perm(3,4,1)", 9*9*8*7*6*5*4*3  
print "ans += 9*9*8*7*6*5*4*3*2 * perm(3,2,3)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4     * perm(4,3,0)", 9*9*8*7*6*5*4    
print "ans += 9*9*8*7*6*5*4*3   * perm(4,2,2)", 9*9*8*7*6*5*4*3  
print "ans += 9*9*8*7*6*5*4*3*2 * perm(4,1,4)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4*3*2 * perm(4,0,6)", 9*9*8*7*6*5*4*3*2
print "ans += 9*9*8*7*6*5*4     * perm(5,1,1)", 9*9*8*7*6*5*4    
print "ans += 9*9*8*7*6*5*4*3   * perm(5,0,3)", 9*9*8*7*6*5*4*3  
print "ans += 9*9*8*7*6*5       * perm(6,0,0)", 9*9*8*7*6*5      

ans += 9*9*8*7*6*5*4*3*2 * perm(0,9,0)  # (0 x3) + (9 x2) + (0 x1) = 18 digits,  9 numbers used
ans += 9*9*8*7*6*5*4*3*2 * perm(0,8,2)  # (0 x3) + (8 x2) + (2 x1) = 18 digits, 10 numbers used
ans += 9*9*8*7*6*5*4*3*2 * perm(1,7,1)  # (1 x3) + (7 x2) + (1 x1) = 18 digits,  9 numbers used
ans += 9*9*8*7*6*5*4*3*2 * perm(1,6,3)  # (1 x3) + (6 x2) + (3 x1) = 18 digits, 10 numbers used
ans += 9*9*8*7*6*5*4*3   * perm(2,6,0)  # (2 x3) + (6 x2) + (0 x1) = 18 digits,  8 numbers used
ans += 9*9*8*7*6*5*4*3*2 * perm(2,5,2)  # (2 x3) + (5 x2) + (2 x1) = 18 digits, 10 numbers used
ans += 9*9*8*7*6*5*4*3   * perm(3,4,1)  # (3 x3) + (4 x2) + (1 x1) = 18 digits,  8 numbers used
ans += 9*9*8*7*6*5*4*3*2 * perm(3,2,3)  # (3 x3) + (2 x2) + (3 x1) = 18 digits, 10 numbers used
ans += 9*9*8*7*6*5*4     * perm(4,3,0)  # (4 x3) + (3 x2) + (0 x1) = 18 digits,  7 numbers used
ans += 9*9*8*7*6*5*4*3   * perm(4,2,2)  # (4 x3) + (2 x2) + (2 x1) = 18 digits,  8 numbers used
ans += 9*9*8*7*6*5*4*3*2 * perm(4,1,4)  # (4 x3) + (1 x2) + (4 x1) = 18 digits,  9 numbers used
ans += 9*9*8*7*6*5*4*3*2 * perm(4,0,6)  # (4 x3) + (0 x2) + (6 x1) = 18 digits, 10 numbers used
ans += 9*9*8*7*6*5*4     * perm(5,1,1)  # (5 x3) + (1 x2) + (1 x1) = 18 digits,  7 numbers used
ans += 9*9*8*7*6*5*4*3   * perm(5,0,3)  # (5 x3) + (0 x2) + (3 x1) = 18 digits,  8 numbers used
ans += 9*9*8*7*6*5       * perm(6,0,0)  # (6 x3) + (0 x2) + (0 x1) = 18 digits,  6 numbers used

print "Answer =", ans
print "Time taken =", time.clock() - start_time, "seconds"
sys.exit()
