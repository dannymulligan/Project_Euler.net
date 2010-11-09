#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 160
#
# Problem summary
#
# For any N, let f(N) be the last five digits before the trailing
# zeroes in N!. For example,
#
#     9! = 362880 so f(9)=36288
#     10! = 3628800 so f(10)=36288
#     20! = 2432902008176640000 so f(20)=17664
#
# Find f(1,000,000,000,000)
#
# Answer: 
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys

MAX = 1000000  # Strip off all but the last 5 digits

def fact_slow (x,y):
    ans = 1
    for i in range(x,y+1):
        for j in range(1,10):
            ans *= (i*10+j)
            while ((ans % 10) == 0):
                ans /= 10
            ans = (ans % 100000000)
            #print i*10+j, (ans % 100000)
    return (ans % 100000)

def pow_slow (x,y):
    ans = 1
    for i in range(y):
        ans *= x
        while ((ans % 10) == 0):
            ans /= 10
        ans = (ans % 100000)
    return ans

y = fact_slow(0,0) # 1..9
print "F({0}) = {1}".format(9, y)

y = (y*10) # 10
while ((y % 10) == 0):
    y /= 10
y = (y % 100000)
print "F({0}) = {1}".format(10, y)

y = fact_slow(0,1) # 1..9, 11.19
y = (y*10) # 10
y = (y*20) # 20
while ((y % 10) == 0):
    y /= 10
y = (y % 100000)
print "F({0}) = {1}".format(20, y)


# d = any digit 0..9
# n = any digit 1..9 that factors into calculation
# x = any digit 1..9 that does not factor into calculation
#
#                  n  (value_1 * 1)
#                 dn  (value_2 * 1)
#                ddn  (value_3 * 1)
#              d,ddn  (value_4 * 1)
#             dd,ddn  (value_5 * 1)
#            xdd,ddn  (value_5 * 10)
#          x,xdd,ddn  (value_5 * 100)
#         xx,xdd,ddn  (value_5 * 1000)
#        xxx,xdd,ddn  (value_5 * 10000)
#      x,xxx,xdd,ddn  (value_5 * 100000)
#     xx,xxx,xdd,ddn  (value_5 * 1000000)
#    xxx,xxx,xdd,ddn  (value_5 * 10000000)
#   
#                 n0  (value_1 * 1)
#                dn0  (value_2 * 1)
#              d,dn0  (value_3 * 1)
#             dd,dn0  (value_4 * 1)
#            ddd,dn0  (value_5 * 1)
#          x,ddd,dn0  (value_5 * 10)
#         xx,ddd,dn0  (value_5 * 100)
#        xxx,ddd,dn0  (value_5 * 1000)
#      x,xxx,ddd,dn0  (value_5 * 10000)
#     xx,xxx,ddd,dn0  (value_5 * 100000)
#    xxx,xxx,ddd,dn0  (value_5 * 1000000)
#   
#                n00  (value_1 * 1)
#              d,n00  (value_2 * 1)
#             dd,n00  (value_3 * 1)
#            ddd,n00  (value_4 * 1)
#          d,ddd,n00  (value_5 * 1)
#         xd,ddd,n00  (value_5 * 10)
#        xxd,ddd,n00  (value_5 * 100)
#      x,xxd,ddd,n00  (value_5 * 1000)
#     xx,xxd,ddd,n00  (value_5 * 10000)
#    xxx,xxd,ddd,n00  (value_5 * 100000)
#
#              n,000  (value_1 * 1)
#             dn,000  (value_2 * 1)
#            ddn,000  (value_3 * 1)
#          d,ddn,000  (value_4 * 1)
#         dd,ddn,000  (value_5 * 1)
#        xdd,ddn,000  (value_5 * 10)
#      x,xdd,ddn,000  (value_5 * 100)
#     xx,xdd,ddn,000  (value_5 * 1000)
#    xxx,xdd,ddn,000  (value_5 * 10000)
#
#             n0,000  (value_1 * 1)
#            dn0,000  (value_2 * 1)
#          d,dn0,000  (value_3 * 1)
#         dd,dn0,000  (value_4 * 1)
#        ddd,dn0,000  (value_5 * 1)
#      x,ddd,dn0,000  (value_5 * 10)
#     xx,ddd,dn0,000  (value_5 * 100)
#    xxx,ddd,dn0,000  (value_5 * 1000)
#
#            n00,000  (value_1 * 1)
#          d,n00,000  (value_2 * 1)
#         dd,n00,000  (value_3 * 1)
#        ddd,n00,000  (value_4 * 1)
#      d,ddd,n00,000  (value_5 * 1)
#     xd,ddd,n00,000  (value_5 * 10)
#    xxd,ddd,n00,000  (value_5 * 100)
#
#          n,000,000  (value_1 * 1)
#         dn,000,000  (value_2 * 1)
#        ddn,000,000  (value_3 * 1)
#      d,ddn,000,000  (value_4 * 1)
#     dd,ddn,000,000  (value_5 * 1)
#    xdd,ddn,000,000  (value_5 * 10)
#
#         n0,000,000  (value_1 * 1)
#        dn0,000,000  (value_2 * 1)
#      d,dn0,000,000  (value_3 * 1)
#     dd,dn0,000,000  (value_4 * 1)
#    ddd,dn0,000,000  (value_5 * 1)
#
#        n00,000,000  (value_1 * 1)
#      d,n00,000,000  (value_2 * 1)
#     dd,n00,000,000  (value_3 * 1)
#    ddd,n00,000,000  (value_4 * 1)
#
#      n,000,000,000  (value_1 * 1)
#     dn,000,000,000  (value_2 * 1)
#    ddn,000,000,000  (value_3 * 1)
#
#     n0,000,000,000  (value_1 * 1)
#    dn0,000,000,000  (value_2 * 1)
#   
#    n00,000,000,000  (value_1 * 1)
#
#  1,000,000,000,000  (doesn't change answer)
#  
# Rearranging...
#                                               
#                 n  (value_1 * 1)               
#                n0  (value_1 * 1)               
#               n00  (value_1 * 1)               
#             n,000  (value_1 * 1)               
#            n0,000  (value_1 * 1)               
#           n00,000  (value_1 * 1)               
#         n,000,000  (value_1 * 1)               
#        n0,000,000  (value_1 * 1)               
#       n00,000,000  (value_1 * 1)               
#     n,000,000,000  (value_1 * 1)               
#    n0,000,000,000  (value_1 * 1)               
#   n00,000,000,000  (value_1 * 1)               
#                                               
#                dn  (value_2 * 1)               
#               dn0  (value_2 * 1)               
#             d,n00  (value_2 * 1)               
#            dn,000  (value_2 * 1)               
#           dn0,000  (value_2 * 1)               
#         d,n00,000  (value_2 * 1)               
#        dn,000,000  (value_2 * 1)               
#       dn0,000,000  (value_2 * 1)               
#     d,n00,000,000  (value_2 * 1)               
#    dn,000,000,000  (value_2 * 1)               
#   dn0,000,000,000  (value_2 * 1)               
#                                               
#               ddn  (value_3 * 1)               
#             d,dn0  (value_3 * 1)               
#            dd,n00  (value_3 * 1)               
#           ddn,000  (value_3 * 1)               
#         d,dn0,000  (value_3 * 1)               
#        dd,n00,000  (value_3 * 1)               
#       ddn,000,000  (value_3 * 1)               
#     d,dn0,000,000  (value_3 * 1)               
#    dd,n00,000,000  (value_3 * 1)               
#   ddn,000,000,000  (value_3 * 1)               
#                                               
#             d,ddn  (value_4 * 1)               
#            dd,dn0  (value_4 * 1)               
#           ddd,n00  (value_4 * 1)               
#         d,ddn,000  (value_4 * 1)               
#        dd,dn0,000  (value_4 * 1)               
#       ddd,n00,000  (value_4 * 1)               
#     d,ddn,000,000  (value_4 * 1)               
#    dd,dn0,000,000  (value_4 * 1)               
#   ddd,n00,000,000  (value_4 * 1)               
#                                               
#            dd,ddn  (value_5 * 1)               
#           ddd,dn0  (value_5 * 1)               
#         d,ddd,n00  (value_5 * 1)               
#        dd,ddn,000  (value_5 * 1)               
#       ddd,dn0,000  (value_5 * 1)               
#     d,ddd,n00,000  (value_5 * 1)               
#    dd,ddn,000,000  (value_5 * 1)               
#   ddd,dn0,000,000  (value_5 * 1)               
#           xdd,ddn  (value_5 * 10)              
#         x,ddd,dn0  (value_5 * 10)              
#        xd,ddd,n00  (value_5 * 10)              
#       xdd,ddn,000  (value_5 * 10)              
#     x,ddd,dn0,000  (value_5 * 10)              
#    xd,ddd,n00,000  (value_5 * 10)              
#   xdd,ddn,000,000  (value_5 * 10)              
#         x,xdd,ddn  (value_5 * 100)             
#        xx,ddd,dn0  (value_5 * 100)             
#       xxd,ddd,n00  (value_5 * 100)             
#     x,xdd,ddn,000  (value_5 * 100)             
#    xx,ddd,dn0,000  (value_5 * 100)             
#   xxd,ddd,n00,000  (value_5 * 100)             
#        xx,xdd,ddn  (value_5 * 1000)            
#       xxx,ddd,dn0  (value_5 * 1000)            
#     x,xxd,ddd,n00  (value_5 * 1000)            
#    xx,xdd,ddn,000  (value_5 * 1000)            
#   xxx,ddd,dn0,000  (value_5 * 1000)            
#       xxx,xdd,ddn  (value_5 * 10000)           
#     x,xxx,ddd,dn0  (value_5 * 10000)           
#    xx,xxd,ddd,n00  (value_5 * 10000)           
#   xxx,xdd,ddn,000  (value_5 * 10000)           
#     x,xxx,xdd,ddn  (value_5 * 100000)          
#    xx,xxx,ddd,dn0  (value_5 * 100000)          
#   xxx,xxd,ddd,n00  (value_5 * 100000)          
#    xx,xxx,xdd,ddn  (value_5 * 1000000)         
#   xxx,xxx,ddd,dn0  (value_5 * 1000000)         
#   xxx,xxx,xdd,ddn  (value_5 * 10000000)        
#
# Rearranging...
#                                               
#     (value_1 *       12)
#     (value_2 *       11)
#     (value_3 *       10)
#     (value_4 *        9)
#     (value_5 *        8)
#     (value_5 *       70)
#     (value_5 *      600)
#     (value_5 *     5000)
#     (value_5 *    40000)
#     (value_5 *   300000)
#     (value_5 *  2000000)
#     (value_5 * 10000000)
# where
#          n = value_1
#         dn = value_2
#        ddn = value_3
#      d,ddn = value_4
#     dd,ddn = value_5

# n = value_1
value_1 = fact_slow(0,0)
print "value_1 =", value_1
# should equal 1*2*3*4*5*6*7*8*9 / 10

# dn = value_2
value_2 = fact_slow(1,9)
print "value_2 =", value_2
# should equal 11*12*13*14*15*16*17*18*19 / 10   = 3352212864
#         *    21*22*23*24*25*26*27*28*29 / 100  = 36342450144
#         *    31*32*33*34*35*36*37*38*39 / 10   = 7689976310016
#         *    41*42*43*44*45*46*47*48*49 / 10   = 74552086046592
#         *    51*52*53*54*55*56*57*58*59 / 10   = 455983078719168
#         *    61*62*63*64*65*66*67*68*69 / 10   = 2056516253535744
#         *    71*72*73*74*75*76*77*78*79 / 100  = 746848821150432
#         *    81*82*83*84*85*86*87*88*89 / 10   = 23065642583032896
#         *    91*92*93*94*95*96*97*98*99 / 10   = 62815650955529472

# should equal 95452416
#         *    12265472
#         *    25940992
#         *    20611072
#         *    55529472

# should equal 35780352
#         *    53863424
#         *    55529472

# should equal 49056


# ddn = value_3
value_3 = fact_slow(10,99)
print "value_3 =", value_3

# d,ddn = value_4
value_4 = fact_slow(100,999)
print "value_4 =", value_4


# dd,ddn = value_5
value_5 = fact_slow(1000,9999)
print "value_5 =", value_5


answer = 1

#     (value_1 *       12)
value_1_12 = 1
for i in range(12):
    value_1_12  *= value_1
    while ((value_1_12 % 10) == 0):
        value_1_12 /= 10
    value_1_12 = (value_1_12 % 100000000)
value_1_12 = (value_1_12 % 100000)
print "value_1_12 =", value_1_12

#     (value_2 *       11)
value_2_11 = 1
for i in range(11):
    value_2_11  *= value_2
    while ((value_2_11 % 10) == 0):
        value_2_11 /= 10
    value_2_11 = (value_2_11 % 100000000)
value_2_11 = (value_2_11 % 100000)
print "value_2_11 =", value_2_11

#     (value_3 *       10)
value_3_10 = 1
for i in range(10):
    value_3_10  *= value_3
    while ((value_3_10 % 10) == 0):
        value_3_10 /= 10
    value_3_10 = (value_3_10 % 100000000)
value_3_10 = (value_3_10 % 100000)
print "value_3_10 =", value_3_10

#     (value_4 *        9)
value_4_9 = 1
for i in range(9):
    value_4_9  *= value_4
    while ((value_4_9 % 10) == 0):
        value_4_9 /= 10
    value_4_9 = (value_4_9 % 100000000)
value_4_9 = (value_4_9 % 100000)
print "value_4_9 =", value_4_9

#     (value_5 *        8)
value_5_8 = 1
for i in range(8):
    value_5_8  *= value_5
    while ((value_5_8 % 10) == 0):
        value_5_8 /= 10
    value_5_8 = (value_5_8 % 100000000)
value_5_8 = (value_5_8 % 100000)
print "value_5_8 =", value_5_8

value_5_10 = 1
for i in range(10):
    value_5_10  *= value_5
    while ((value_5_10 % 10) == 0):
        value_5_10 /= 10
    value_5_10 = (value_5_10 % 100000000)
value_5_10 = (value_5_10 % 100000)
print "value_5_10 =", value_5_10

value_5_100 = 1
for i in range(10):
    value_5_100  *= value_5_10
    while ((value_5_100 % 10) == 0):
        value_5_100 /= 10
    value_5_100 = (value_5_100 % 100000000)
value_5_100 = (value_5_100 % 100000)
print "value_5_100 =", value_5_100

value_5_1000 = 1
for i in range(10):
    value_5_1000  *= value_5_100
    while ((value_5_1000 % 10) == 0):
        value_5_1000 /= 10
    value_5_1000 = (value_5_1000 % 100000000)
value_5_1000 = (value_5_1000 % 100000)
print "value_5_1000 =", value_5_1000

value_5_10000 = 1
for i in range(10):
    value_5_10000  *= value_5_1000
    while ((value_5_10000 % 10) == 0):
        value_5_10000 /= 10
    value_5_10000 = (value_5_10000 % 100000000)
value_5_10000 = (value_5_10000 % 100000)
print "value_5_10000 =", value_5_10000

value_5_100000 = 1
for i in range(10):
    value_5_100000  *= value_5_10000
    while ((value_5_100000 % 10) == 0):
        value_5_100000 /= 10
    value_5_100000 = (value_5_100000 % 100000000)
value_5_100000 = (value_5_100000 % 100000)
print "value_5_100000 =", value_5_100000

value_5_1000000 = 1
for i in range(10):
    value_5_1000000  *= value_5_100000
    while ((value_5_1000000 % 10) == 0):
        value_5_1000000 /= 10
    value_5_1000000 = (value_5_1000000 % 100000000)
value_5_1000000 = (value_5_1000000 % 100000)
print "value_5_1000000 =", value_5_1000000

#     (value_5 *       70)
value_5_70 = 1
for i in range(7):
    value_5_70  *= value_5_10
    while ((value_5_70 % 10) == 0):
        value_5_70 /= 10
    value_5_70 = (value_5_70 % 100000000)
value_5_70 = (value_5_70 % 100000)
print "value_5_70 =", value_5_70

#     (value_5 *      600)
value_5_600 = 1
for i in range(6):
    value_5_600  *= value_5_100
    while ((value_5_600 % 10) == 0):
        value_5_600 /= 10
    value_5_600 = (value_5_600 % 100000000)
value_5_600 = (value_5_600 % 100000)
print "value_5_600 =", value_5_600

#     (value_5 *     5000)
value_5_5000 = 1
for i in range(5):
    value_5_5000  *= value_5_1000
    while ((value_5_5000 % 10) == 0):
        value_5_5000 /= 10
    value_5_5000 = (value_5_5000 % 100000000)
value_5_5000 = (value_5_5000 % 100000)
print "value_5_5000 =", value_5_5000

#     (value_5 *    40000)
value_5_40000 = 1
for i in range(4):
    value_5_40000  *= value_5_10000
    while ((value_5_40000 % 10) == 0):
        value_5_40000 /= 10
    value_5_40000 = (value_5_40000 % 100000000)
value_5_40000 = (value_5_40000 % 100000)
print "value_5_40000 =", value_5_40000

#     (value_5 *   300000)
value_5_300000 = 1
for i in range(3):
    value_5_300000  *= value_5_100000
    while ((value_5_300000 % 10) == 0):
        value_5_300000 /= 10
    value_5_300000 = (value_5_300000 % 100000000)
value_5_300000 = (value_5_300000 % 100000)
print "value_5_300000 =", value_5_300000

#     (value_5 *  2000000)
value_5_2000000 = 1
for i in range(2):
    value_5_2000000  *= value_5_1000000
    while ((value_5_2000000 % 10) == 0):
        value_5_2000000 /= 10
    value_5_2000000 = (value_5_2000000 % 100000000)
value_5_2000000 = (value_5_2000000 % 100000)
print "value_5_2000000 =", value_5_2000000

#     (value_5 * 10000000)
value_5_10000000 = 1
for i in range(10):
    value_5_10000000  *= value_5_1000000
    while ((value_5_10000000 % 10) == 0):
        value_5_10000000 /= 10
    value_5_10000000 = (value_5_10000000 % 100000000)
value_5_10000000 = (value_5_10000000 % 100000)
print "value_5_10000000 =", value_5_10000000

answer = 1
for i in (value_1_12, value_2_11, value_3_10, value_4_9, value_5_8, value_5_70, value_5_600, value_5_5000, value_5_40000, value_5_300000, value_5_2000000, value_5_10000000):
    answer *= i
    while ((answer % 10) == 0):
        answer /= 10
    answer = (answer % 100000000)
answer = (answer % 100000)

print "answer =", answer

sys.exit()
