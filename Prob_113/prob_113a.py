#!/usr/bin/python
#
# Project Euler.net Problem 113
#
# Working from left-to-right if no digit is exceeded by the digit to
# its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is
# called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor
# decreasing a "bouncy" number; for example, 155349.
#
# As n increases, the proportion of bouncy numbers below n increases
# such that there are only 12951 numbers below one-million that are
# not bouncy and only 277032 non-bouncy numbers below 10^10.
#
# How many numbers below a googol (10^100) are not bouncy?
#
# Answer: 51161058134250
# Solved 07/04/11
# 145 problems solved
# Position #107 on level 3

import sys

def num_cnt(l,r):
    if (r == 0):  return 1
    if (r == 1):  return l+1
    if (r == 2):  return (l+2)*(l+1)/2
    if (l == 0):  return 1
    if (l == 1):  return r+1
    if (l == 2):  return (r+2)*(r+1)/2

    #print "num_cnt({0},{1})".format(l,r)
    mid = l/2
    ans = 0
    for d in range(r+1):
        left  = num_cnt(mid,d)
        right = num_cnt(l-mid-1,r-d)
        ans += left * right
        #print "Splitting into num_cnt({0},{1}) * num_cnt({2},{3})".format(mid,d, l-mid-1,r-d),
        #print " = {0} * {1} = {2}".format(left, right, left*right)
        #ans += num_cnt(mid,d) * num_cnt((l-mid),r-d)
    return ans

# num_cnt(l,r) has a few flaws...
#
#     It incorrectly counts 0 as a rising or falling number, so we
#         need to subtract this out.
#
#     It correctly calculates rising numbers.
#
#     It requires several iterations to calculate falling numbers.  We
#         have to calculate N digit rising numbers, add in N-1 digit
#         rising numbers, N-2 digit rising numbers, etc
#
#     Repeating digits (e.g. 11111) are counted as both rising and
#         falling numbers, so we need to correct for this double
#         counting.


def rising(l):
    return num_cnt(l,9) - 1

def falling(l):
    ans = 0
    for i in range(1,l+1):
        ans += num_cnt(i,9) - 1
    return ans

def both(l):
    return l*9
    # 1 digit: 1, 2, 3, ..., 9
    # 2 digits: 11, 22, 33, ..., 99
    # 3 digits: 111, 222, 333, ..., 999
    # etc

print rising(3), falling(3), both(3), (rising(3)+falling(3)-both(3))
print rising(4), falling(4), both(4), (rising(4)+falling(4)-both(4))
print rising(5), falling(5), both(5), (rising(5)+falling(5)-both(5))
print rising(6), falling(6), both(6), (rising(6)+falling(6)-both(6))

print rising(10), falling(10), both(10), (rising(10)+falling(10)-both(10))

print "Answer =", (rising(100)+falling(100)-both(100))

# From brute force calculation in prob_113.py
# 1..   999:  Rising =  219, Falling =  282, Both =   27, Not bouncy =  474
# 1..  9999:  Rising =  714, Falling =  996, Both =   36, Not bouncy = 1674
# 1.. 99999:  Rising = 2001, Falling = 2997, Both =   45, Not bouncy = 4953
# 1..999999:  Rising = 5004, Falling = 8001, Both =   54, Not bouncy = 12951


sys.exit()


ans  = num_cnt(6,9)-1  # 0...6 digit rising numbers
ans  = 2*ans           # 6 digit falling numbers
ans += num_cnt(5,9)-1  # 5 digit falling numbers
ans += num_cnt(4,9)-1  # 4 digit falling numbers
ans += num_cnt(3,9)-1  # 3 digit falling numbers
ans += num_cnt(2,9)-1  # 2 digit falling numbers
ans += num_cnt(1,9)-1  # 1 digit falling numbers

print "Answer =", ans
sys.exit()



ans = num_cnt(4,0)
print "num_cnt(4,0) = {0}".format(ans)
if (ans != 1):  print "Error!"
# answer should be 1
# 0000

ans = num_cnt(2,1)
print "num_cnt(2,1) = {0}".format(ans)
if (ans != 3):  print "Error!"
# answer should be 3
# 11
# 10
# 00

ans = num_cnt(2,2)
print "num_cnt(2,2) = {0}".format(ans)
if (ans != 6):  print "Error!"
# answer should be 6
# 22
# 21
# 20
# 11
# 10
# 00

ans = num_cnt(3,2)
print "num_cnt(3,2) = {0}".format(ans)
if (ans != 10):  print "Error!"
# answer should be 10
# 222, 221,  220, 211,  210, 200
# 111,  110,  100
# 000

ans = num_cnt(3,3)
print "num_cnt(3,3) = {0}".format(ans)
if (ans != 20):  print "Error!"
# answer should be 20
# ?3? = 1 * 4 combinations = 333, 332, 331, 330
# ?2? = 2 * 3 combinations = 322, 321, 320, 222, 221, 220
# ?1? = 3 * 2 combinations = 311, 310, 211, 210, 111, 110
# ?0? = 4 * 1 combinations = 300, 200, 100, 000

ans = num_cnt(1,9)
print "num_cnt(1,9) = {0}".format(ans)
if (ans != 10):  print "Error!"
# answer should be 10
# 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

ans = num_cnt(2,9)
print "num_cnt(2,9) = {0}".format(ans)
if (ans != 55):  print "Error!"
# answer should be 55
# 99, 98, 97, 96, 95, 94, 93, 92, 91, 90
# 88, 87, 86, 85, 84, 83, 82, 81, 80
# 77, 76, 75, 74, 73, 72, 71, 70
# 66, 65, 64, 63, 62, 61, 60
# 55, 54, 53, 52, 51, 50
# 44, 43, 42, 41, 40
# 33, 32, 31, 30
# 22, 21, 20
# 11, 10
# 0

ans = num_cnt(3,4)
print "num_cnt(3,4) = {0}".format(ans)
if (ans != 35):  print "Error!"
# answer should be 35
# ?4? = 1 * 5 combinations = 444, 443, 442, 441, 440
# ?3? = 2 * 4 combinations = 433, 432, 431, 430, 333, 332, 331, 330
# ?2? = 3 * 3 combinations = 422, 421, 420, 322, 321, 320, 222, 221, 220
# ?1? = 4 * 2 combinations = 411, 410, 311, 310, 211, 210, 111, 110
# ?0? = 5 * 1 combinations = 400, 300, 200, 100, 000

ans = num_cnt(3,5)
print "num_cnt(3,5) = {0}".format(ans)
if (ans != 56):  print "Error!"
# answer should be 56
# ?5? = 1 * 6 combinations = 555, 554, 553, 552, 551, 550
# ?4? = 2 * 5 combinations = 544, 543, 542, 541, 540, 444, 443, 442, 441, 440
# ?3? = 3 * 4 combinations = 533, 532, 531, 530, 433, 432, 431, 430, 333, 332, 331, 330
# ?2? = 4 * 3 combinations = 522, 521, 520, 422, 421, 420, 322, 321, 320, 222, 221, 220
# ?1? = 5 * 2 combinations = 511, 510, 411, 410, 311, 310, 211, 210, 111, 110
# ?0? = 6 * 1 combinations = 500, 400, 300, 200, 100, 000

ans = num_cnt(3,6)
print "num_cnt(3,6) = {0}".format(ans)
if (ans != 84):  print "Error!"
# answer should be 84
# ?6? = 1 *  7 combinations = 666, 665, 664, 663, 662, 661, 660
# ?5? = 2 *  6 combinations = 655, 654, 653, 652, 651, 650, 555, 554, 553, 552, 551, 550
# ?4? = 3 *  5 combinations = ...
# ?3? = 4 *  4 combinations = ...
# ?2? = 5 *  3 combinations = ...
# ?1? = 6 *  2 combinations = 611, 610, 511, 510, 411, 410, 311, 310, 211, 210, 111, 110
# ?0? = 7 *  1 combinations = 600, 500, 400, 300, 200, 100, 000

ans = num_cnt(3,7)
print "num_cnt(3,7) = {0}".format(ans)
if (ans != 120):  print "Error!"
# answer should be 120
# ?7? = 1 *  8 combinations = 777, 776, 775, 774, 773, 772, 771, 770
# ?6? = 2 *  7 combinations = 766, 765, 764, 763, 762, 761, 760, 666, 665, 664, 663, 662, 661, 660
# ?5? = 3 *  6 combinations =
# ?4? = 4 *  5 combinations = ...
# ?3? = 5 *  4 combinations = ...
# ?2? = 6 *  3 combinations = ...
# ?1? = 7 *  2 combinations = 711, 710, 611, 610, 511, 510, 411, 410, 311, 310, 211, 210, 111, 110
# ?0? = 8 *  1 combinations = 700, 600, 500, 400, 300, 200, 100, 000

ans = num_cnt(3,9)
print "num_cnt(3,9) = {0}".format(ans)
if (ans != 220):  print "Error!"
# answer should be 220
# ?9? =  1 * 10 combinations = 999, 998, 997, 996, 995, 994, 993, 992, 991, 990
# ?8? =  2 *  9 combinations = 988, 987, 986, 985, 984, 983, 982, 981, 980, 888, 887, 886, 885, 884, 883, 882, 881, 880
# ?7? =  3 *  8 combinations = ...
# ?6? =  4 *  7 combinations = ...
# ?5? =  5 *  6 combinations = ...
# ?4? =  6 *  5 combinations = ...
# ?3? =  7 *  4 combinations = ...
# ?2? =  8 *  3 combinations = 922, 921, 920, 822, 821, 820, 722, 721, 720, 622, 621, 620, 522, 521, 520, 422, 421, 420, 322, 321, 320, 222, 221, 220
# ?1? =  9 *  2 combinations = 911, 910, 811, 810, 711, 710, 611, 610, 511, 510, 411, 410, 311, 310, 211, 210, 111, 110
# ?0? = 10 *  1 combinations = 900, 800, 700, 600, 500, 400, 300, 200, 100, 000

ans = num_cnt(4,2)
print "num_cnt(4,2) = {0}".format(ans)
if (ans != 15):  print "Error!"
# answer should be 15
# ?2?? = 1 * 6 combinations = 2222, 2221, 2220, 2211, 2210, 2200
# ?1?? = 2 * 3 combinations = 2111, 2110, 2100, 1111, 1110, 1100
# ?0?? = 3 * 1 combinations = 2000, 1000, 0000

ans = num_cnt(4,3)
print "num_cnt(4,3) = {0}".format(ans)
if (ans != 35):  print "Error!"
# answer should be 35
# ??3? =  1 * 4 combinations = 33** + **3* + (***3, ***2, ***1, ***0)
# ??2? =  3 * 3 combinations = (33**, 32**, 22**) + **2* + (***2, ***1, ***0)
# ??1? =  6 * 2 combinations = (33** 32**, 31**, 22**, 21**, 11**) + **1* + (***1 ***0)
# ??0? = 10 * 1 combinations = (33**, 32**, 31**, 30**, 22**, 21**, 20**, 11**, 10**, 00**) + **0* + ***0

ans = num_cnt(4,4)
print "num_cnt(4,4) = {0}".format(ans)
if (ans != 70):  print "Error!"
# answer should be 70
# ??4? =  1 * 5 combinations = 44** + **4* + (***4, ***3, ***2, ***1, ***0)
# ??3? =  3 * 4 combinations = (44**, 43**, 33**) + **3* + (***3, ***2, ***1, ***0)
# ??2? =  6 * 3 combinations = (44**, 43**, 42**, 33**, 32**, 22**) + **2* + (***2, ***1, ***0)
# ??1? = 10 * 2 combinations = (44**, 43**, 42**, 41**, 33** 32**, 31**, 22**, 21**, 11**) + **1* + (***1 ***0)
# ??0? = 15 * 1 combinations = (44**, 43**, 42**, 41**, 40**, 33**, 32**, 31**, 30**, 22**, 21**, 20**, 11**, 10**, 00**) + **0* + ***0

ans = num_cnt(4,5)
print "num_cnt(4,5) = {0}".format(ans)
if (ans != 126):  print "Error!"
# answer should be 126
# ??5? =  1 * 6 combinations = 44** + **5* + (***5, ***4, ***3, ***2, ***1, ***0)
# ??4? =  3 * 5 combinations = (55**, 54**, 44**) + **4* + (***4, ***3, ***2, ***1, ***0)
# ??3? =  6 * 4 combinations = (55**, 54**, 53**, 44**, 43**, 33**) + **3* + (***3, ***2, ***1, ***0)
# ??2? = 10 * 3 combinations = (55**, 54**, 53**, 52**, 44**, 43**, 42**, 33**, 32**, 22**) + **2* + (***2, ***1, ***0)
# ??1? = 15 * 2 combinations = (55**, 54**, 53**, 52**, 51**, 44**, 43**, 42**, 41**, 33** 32**, 31**, 22**, 21**, 11**) + **1* + (***1 ***0)
# ??0? = 21 * 1 combinations = (55**, 54**, 53**, 52**, 51**, 50**, 44**, 43**, 42**, 41**, 40**, 33**, 32**, 31**, 30**, 22**, 21**, 20**, 11**, 10**, 00**) + **0* + ***0

ans = num_cnt(5,3)
print "num_cnt(5,3) = {0}".format(ans)
if (ans != 56):  print "Error!"
# answer should be 56
# ??3?? =  1 * 10 combinations = 33*** + **3** + (***33, ***32, ***31, ***30, ***22, ***21, ***20, ***11, ***10, ***00)
# ??2?? =  3 *  6 combinations = (33***, 32***, 22***) + **2** + (***22, ***21, ***20, ***11, ***10, ***00)
# ??1?? =  6 *  3 combinations = (33***, 32***, 31***, 22***, 21***, 11***) + **1** + (***11, ***10, ***00)
# ??0?? = 10 *  1 combinations = (33***, 32***, 31***, 30***, 22***, 21***, 20***, 11***, 10***, 00***) + **0** + ***00

ans = num_cnt(4,9)
print "num_cnt(4,9) = {0}".format(ans)
if (ans != 715):  print "Error!"
# answer should be 715 (from excel spreadsheet)

ans = num_cnt(5,9)
print "num_cnt(5,9) = {0}".format(ans)
if (ans != 2002):  print "Error!"
# answer should be 2002 (from excel spreadsheet)

ans = num_cnt(6,9)
print "num_cnt(6,9) = {0}".format(ans)
if (ans != 5005):  print "Error!"
# answer should be 5005 (from excel spreadsheet)
