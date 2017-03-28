#!/usr/bin/env python3
#
# Project Euler.net Problem 24
#
# What is the millionth lexicographic permutation of the digits 0, 1,
# 2, 3, 4, 5, 6, 7, 8 and 9?
#
# A permutation is an ordered arrangement of objects. For example,
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all
# of the permutations are listed numerically or alphabetically, we
# call it lexicographic order. The lexicographic permutations of 0, 1
# and 2 are:
# 
#     012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1,
# 2, 3, 4, 5, 6, 7, 8 and 9?


import itertools

N = 1000000

nums = range(10)

for n, perm in enumerate(itertools.permutations(nums)):
    if (n == (N-1)):
        break

Answer = ''
for j in perm:
    Answer += str(j)
print("Answer = {}".format(Answer))


# Numbers like 0xxxxxxxxx: 9! = 362,880 possibilities => #1 to #362,880
# Numbers like 1xxxxxxxxx: 9! = 362,880 possibilities => #362,881 to #725,760
# Numbers like 20xxxxxxxx: 8! = 40,320 possibilities => #725,761 to #766,080
# Numbers like 21xxxxxxxx: 8! = 40,320 possibilities => #766,081 to #806,400
# Numbers like 23xxxxxxxx: 8! = 40,320 possibilities => #806,401 to #846,720
# Numbers like 24xxxxxxxx: 8! = 40,320 possibilities => #846,721 to #887,040
# Numbers like 25xxxxxxxx: 8! = 40,320 possibilities => #887,041 to #927,360
# Numbers like 26xxxxxxxx: 8! = 40,320 possibilities => #927,361 to #967,680
# Numbers like 270xxxxxxx: 7! = 5,040 possibilities => #967,680 to #972,720
# Numbers like 271xxxxxxx: 7! = 5,040 possibilities => #972,721 to #977,760
# Numbers like 273xxxxxxx: 7! = 5,040 possibilities => #977,761 to #982,800
# Numbers like 274xxxxxxx: 7! = 5,040 possibilities => #982,801 to #987,840
# Numbers like 275xxxxxxx: 7! = 5,040 possibilities => #987,841 to #992,880
# Numbers like 276xxxxxxx: 7! = 5,040 possibilities => #992,881 to #997,920
# Numbers like 2780xxxxxx: 6! = 720 possibilities => #997,921 to #998,640
# Numbers like 2781xxxxxx: 6! = 720 possibilities => #998,641 to #999,360
# Numbers like 27830xxxxx: 5! = 120 possibilities => #999,361 to #999,480
# Numbers like 27831xxxxx: 5! = 120 possibilities => #999,481 to #999,600
# Numbers like 27834xxxxx: 5! = 120 possibilities => #999,601 to #999,720
# Numbers like 27835xxxxx: 5! = 120 possibilities => #999,721 to #999,840
# Numbers like 27836xxxxx: 5! = 120 possibilities => #999,841 to #999,960
# Numbers like 278390xxxx: 4! = 24 possibilities => #999,961 to #999,984
# Numbers like 2783910xxx: 3! = 6 possibilities => #999,985 to #999,990
# Numbers like 2783914xxx: 3! = 6 possibilities => #999,991 to #999,996
# Numbers like 2783915xxx: 3! = 6 possibilities => #999,997 to #1,000,002
# 2783915046 => #999,997
# 2783915064 => #999,998
# 2783915406 => #999,999
# 2783915460 => #1,000,000
# 2783915604 => #1,000,001
# 2783915640 => #1,000,002
