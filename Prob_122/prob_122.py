#!/usr/bin/python
#
# Project Euler.net Problem 122
# 
# The most naive way of computing n^(15) requires fourteen
# multiplications:
# 
#     n x n x ... x n = n^(15)
# 
# But using a "binary" method you can compute it in six
# multiplications:
# 
#     n x n = n^(2)
#     n^(2) x n^(2) = n^(4)
#     n^(4) x n^(4) = n^(8)
#     n^(8) x n^(4) = n^(12)
#     n^(12) x n^(2) = n^(14)
#     n^(14) x n = n^(15)
# 
# However it is yet possible to compute it in only five
# multiplications:
# 
#     n x n = n^(2)
#     n^(2) x n = n^(3)
#     n^(3) x n^(3) = n^(6)
#     n^(6) x n^(6) = n^(12)
#     n^(12) x n^(3) = n^(15)
# 
# We shall define m(k) to be the minimum number of multiplications to
# compute n^(k); for example m(15) = 5.
# 
# For 1 <= k <= 200, find sum(m(k)).
#
# Answer: 
# Solved ??/??/10
# ??? problems solved
# Position #??? on level 3

best = [999]*201
freebie = [999]*201

best[1] = 0
best[2] = 1
for i in range(3,16):
    print "Looking for best x^",i
    for j in range(1,(i/2+1)):
        if (j == (i - j)):
            lbest = 1 + best[j]
        else:
            lbest = 1 + best[j] + best[i-j]
        if (lbest < best[i]):
            best[i] = lbest

for i in range(1,16):
    print "best[{0}] = {1}".format(i, best[i])

