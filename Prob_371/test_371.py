#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 371
#
# License plates
#
# Oregon licence plates consist of three letters followed by a three
# digit number (each digit can be from [0..9]).
#
# While driving to work Seth plays the following game: Whenever the
# numbers of two licence plates seen on his trip add to 1000 that's a
# win.
#
# E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500 too. (as
# long as he sees them in the same trip).
#
# Find the expected number of plates he needs to see for a win.
#
# Give your answer rounded to 8 decimal places behind the decimal
# point.
#
# Note: We assume that each licence plate seen is equally likely to
# have any three digit number on it.


LENGTH = 3

def ListNums(Length):
    for i in range(10**Length):
        nums = []
        n = i
        for d in range(LENGTH):
            nums.append(n % 10)
            n = n // 10
        nums.reverse()
        yield nums


Count = 0
WinCount = 0
PrevCount = 0
for n in ListNums(LENGTH):

    PrevWin = False
    for a in range(1,LENGTH-1):
        for b in range(a):
            if (n[a] + n[b]) == 10:
                PrevWin = True

    Win = False
    for p in range(LENGTH-1):
        if (n[p] + n[-1]) == 10:
            Win = True

    if PrevWin:
        PrevCount += 1
        print(n, "Prev")
    elif Win:
        WinCount += 1
        Count += 1
        print(n, "Win", WinCount)
    else:
        Count += 1
        print(n)

print("Count =", Count)
print("WinCount =", WinCount)
print("PrevCount =", PrevCount)
print("probability = {}".format(WinCount/Count))
