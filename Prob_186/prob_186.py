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
SIZE = 10**3

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
def MergeGroups(FromGroup, ToGroup):
    global Directory
    MergeCount = 0
    for i in range(SIZE):
        if Directory[i] == FromGroup:
            Directory[i] = ToGroup
            MergeCount += 1
    return MergeCount

    
################################################################################
VirginGroup = 0
PMGroup = 1
GroupNumber = PMGroup + 1
Directory = [VirginGroup]*SIZE
Directory[524287%SIZE] = PMGroup  # PM is group 1
Target = SIZE * 99 //100

FriendsOfPM = 1
Virgins = SIZE - 1
Groups = 1
Misdials = 0

#print("[                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1]")
#print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
#print(Directory)

prev_time = time.clock()

for n, (Caller, Callee) in enumerate(pairS(), start=1):

    #print("\nn={}, Caller = {} group {}, Callee = {} group {}".format(n, Caller, Directory[Caller], Callee, Directory[Callee]))
    
    if Caller == Callee:
        # Misdial
        Misdials += 1
        continue
    
    if (Directory[Caller] == 0) or (Directory[Callee] == 0):
        # Virgin caller or virgin callee
        if (Directory[Caller] == 0) and (Directory[Callee] == 0):
            # Both caller and callee are virgin
            Directory[Caller] = GroupNumber
            Directory[Callee] = GroupNumber
            GroupNumber += 1
            Groups += 1
            Virgins -= 2
            #print("    Created a new group {}".format(GroupNumber-1))
        elif (Directory[Callee] == VirginGroup):
            # Callee is virgin
            Directory[Callee] = Directory[Caller]
            Virgins -= 1
            #print("    Added a virgin to group {}".format(Directory[Caller]))
            if Directory[Caller] == PMGroup:
                FriendsOfPM += 1
        elif (Directory[Caller] == VirginGroup):
            # Caller is virgin
            Directory[Caller] = Directory[Callee]
            Virgins -= 1
            #print("    Added a virgin to group {}".format(Directory[Callee]))
            if Directory[Callee] == PMGroup:
                FriendsOfPM += 1

    elif (Directory[Caller] != Directory[Callee]):
        # Both caller and callee are part of different groups
        if (Directory[Caller] < Directory[Callee]):
            FromGroup, ToGroup = Directory[Callee], Directory[Caller]
        else:
            FromGroup, ToGroup = Directory[Caller], Directory[Callee]

        MergedNumbers = MergeGroups(FromGroup, ToGroup)
        Groups -= 1

        if ToGroup == PMGroup:
            FriendsOfPM += MergedNumbers
            
        #print("    Merged {} numbers from group {} to group {}".format(MergedNumbers, FromGroup, ToGroup))
        
    if (FriendsOfPM >= Target):
        break

    if (n % 1000) == 0:
        Average = 1.0*(SIZE - Virgins)/Groups
        Now = time.clock()
        LoopTime = Now - prev_time
        prev_time = Now
        print("{:7,}: {:7,} virgins, {:7,} groups, avg {:7.3f}, {:,} friends of PM, {:.2f} seconds".format(n, Virgins, Groups, Average, FriendsOfPM, LoopTime))
        #print("[                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1]")
        #print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
        #print(Directory)

TotalTime = time.clock() - start_time
Average = 1.0*(SIZE - Virgins)/Groups
print("{:7,}: {:7,} virgins, {:7,} groups, avg {:7.3f}, {:,} friends of PM, {:.2f} seconds".format(n, Virgins, Groups, Average, FriendsOfPM, TotalTime))
print("Answer = {}".format(n-Misdials))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
