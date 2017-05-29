#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 186
#
# Connectedness of a network
#
# Here are the records from a busy telephone system with one million users:
#
#     RecNr    Caller    Called
#       1    200007    100053
#       2    600183    500439
#       3    600863    701497
#      ...    ...       ...
# 
# The telephone number of the caller and the called number in record n
# are Caller(n) = S(2n-1) and Called(n) = S(2n) where S(1), S(2),
# S(3),... come from the "Lagged Fibonacci Generator":
# 
# For 1 <= k <= 55, S(k) = [100003 - 200003k + 300007k^3] (modulo 1000000)
# For 56 <= k, S(k) = [S(k-24) + S(k-55)] (modulo 1000000)
# 
# If Caller(n) = Called(n) then the user is assumed to have misdialled
# and the call fails; otherwise the call is successful.
# 
# From the start of the records, we say that any pair of users X and Y
# are friends if X calls Y or vice-versa. Similarly, X is a friend of
# a friend of Z if X is a friend of Y and Y is a friend of Z; and so
# on for longer chains.
# 
# The Prime Minister's phone number is 524287. After how many
# successful calls, not counting misdials, will 99% of the users
# (including the PM) be a friend, or a friend of a friend etc., of the
# Prime Minister?

import sys
import time
start_time = time.clock()

SIZE = 10**6
PM = 524287
TARGET = SIZE * 99 // 100

Debug = False
Update = 50000

VirginGroup = 0
PMGroup = 1
NextGroup = 2
FriendsOfPM = 1
Virgins = SIZE - 1
Groups = 1
Misdials = 0
Next = [0]*SIZE
Group = [VirginGroup]*SIZE
Group[PM % SIZE] = PMGroup
Next[PM % SIZE] = PM % SIZE


################################################################################
def S():
    results = list()
    k = 1
    while True:
        if k < 56:
            result = (100003 - 200003*k + 300007*(k**3)) % SIZE
            results.append(result)
        else:
            result = (results[-24] + results[-55]) % SIZE
            results.append(result)
            del(results[0])

        k += 1
        yield result


################################################################################
def pairS():
    Two = True
    for x in S():
        if Two == True:
            First = x
            Two = False
        else:
            Second = x
            Two = True
            yield First, Second


################################################################################
def PrintTable():
    if SIZE > 40:
        return
    
    print("      ", end='')
    for i in range(SIZE):
        print(" {:2},".format(i), end='')
    print()
    
    print("Group:", end='')
    for i in range(SIZE):
        if Group[i] == VirginGroup:
            print("   ,", end='')
        else:
            print(" {:2},".format(Group[i]), end='')
    print()
    
    print("Next: ", end='')
    for i in range(SIZE):
        if Group[i] == VirginGroup:
            print("   ,", end='')
        else:
            print(" {:2},".format(Next[i]), end='')
    print()


################################################################################

if Debug:
    PrintTable()

for n, (Caller, Callee) in enumerate(pairS(), start=1):

    if Debug:
        print("\nn={}, Caller = {} group {}, Callee = {} group {}".format(n, Caller, Group[Caller], Callee, Group[Callee]))
    
    if Caller == Callee:
        # Misdial
        Misdials += 1
        continue

    if (Group[Caller] == VirginGroup) or (Group[Callee] == VirginGroup):
        # Virgin caller or virgin callee
        if (Group[Caller] == VirginGroup) and (Group[Callee] == VirginGroup):
            # Both caller and callee are virgin
            Group[Caller] = NextGroup
            Group[Callee] = NextGroup
            Next[Caller] = Callee
            Next[Callee] = Caller
            NextGroup += 1
            Groups += 1
            Virgins -= 2
            if Debug:
                print("    Added a new group {}, groups={}".format(NextGroup-1, Groups))
            
        elif (Group[Callee] == VirginGroup):
            # Callee is virgin, caller is not
            Group[Callee] = Group[Caller]
            Next[Callee] = Next[Caller]
            Next[Caller] = Callee
            Virgins -= 1
            if Group[Caller] == PMGroup:
                FriendsOfPM += 1
            if Debug:
                print("    Added a callee virgin to group {}, virgins={}".format(Group[Caller], Virgins))
        elif (Group[Caller] == VirginGroup):
            # Caller is virgin, callee is not
            Group[Caller] = Group[Callee]
            Next[Caller] = Next[Callee]
            Next[Callee] = Caller
            Virgins -= 1
            if Group[Callee] == PMGroup:
                FriendsOfPM += 1
            if Debug:
                print("    Added a caller virgin to group {}, virgins={}".format(Group[Callee], Virgins))

    elif (Group[Caller] != Group[Callee]):
        # Both caller and callee are part of different groups
        if (Group[Caller] < Group[Callee]):
            # Merge callee group into caller group
            ToGroup = Group[Caller]
            FromGroup = Group[Callee]
            NextNumber = Next[Callee]
        else:
            # Merge caller group into callee group
            ToGroup = Group[Callee]
            FromGroup = Group[Caller]
            NextNumber = Next[Caller]

        MergedNumbers = 0
        while Group[NextNumber] == FromGroup:
            Group[NextNumber] = ToGroup
            MergedNumbers += 1
            NextNumber = Next[NextNumber]

        Next[Caller], Next[Callee] = Next[Callee], Next[Caller]
        Groups -= 1

        if ToGroup == PMGroup:
            FriendsOfPM += MergedNumbers
            
        if Debug:
            print("    Merged {} numbers from group {} to group {}".format(MergedNumbers, FromGroup, ToGroup))

    if (FriendsOfPM >= TARGET):
        break
        
    if (n % Update) == 0:
        Average = 1.0*(SIZE - Virgins)/Groups
        print("{:7,}: {:7,} virgins, {:7,} groups, avg {:7.3f}, {:,} friends of PM".format(n, Virgins, Groups, Average, FriendsOfPM))
        if Debug:
            PrintTable()
    

Average = 1.0*(SIZE - Virgins)/Groups
print("{:7,}: {:7,} virgins, {:7,} groups, avg {:7.3f}, {:,} friends of PM".format(n, Virgins, Groups, Average, FriendsOfPM))
print("With {:,} numbers, it takes {:,} calls and {:,} misdials until {:,} users are friends of the Prime Minister".format(SIZE, n, Misdials, FriendsOfPM))
print("Answer = {} (adjusted for misdials)".format(n-Misdials))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
