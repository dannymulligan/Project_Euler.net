#!/usr/bin/python
#
# Project Euler.net Problem 62
#
# The cube, 41063625 (345^3), can be permuted to produce two other
# cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is
# the smallest cube which has exactly three permutations of its digits
# which are also cube.
#
# Find the smallest cube for which exactly five permutations of its
# digits are cube.
#
# Solved 10/20/09
# 79 problems solved
# Position #338 on level 2

# 1 to 2 produce 1 digit cubes
# 3 to 4 produce 2 digit cubes
# 5 to 9 produce 3 digit cubes
# 10 to 21 produce 4 digit cubes
# 22 to 46 produce 5 digit cubes
# 47 to 99 produce 6 digit cubes
# 100 to 215 produce 7 digit cubes
# 216 to 464 produce 8 digit cubes
# 465 to 999 produce 9 digit cubes
# 1000 to 2154 produce 10 digit cubes
# 2155 to 4641 produce 11 digit cubes
# 4642 to 9999 produce 12 digit cubes
# 10000 to 21544 produce 13 digit cubes
# 21545 to 46415 produce 14 digit cubes
# 46416 to 99999 produce 15 digit cubes
# 100000 to 215443 produce 16 digit cubes
# 215444 to 464158 produce 17 digit cubes
# 464159 to 999999 produce 18 digit cubes
# 1000000 to 2154434 produce 19 digit cubes
# 2154435 to 4641588 produce 20 digit cubes
# 4641589 to 9999999 produce 21 digit cubes


hash_list = {}  # Dictionary data structure
cube_list = []
search_range = []
prev_len = 1
prev_i = 1
found_len = 1

for i in range(10000):
    result = i**3
    cube_list.append(result)
    curr_len = len(str(result))

    key = list(str(result))
    key.sort()
    skey = ''
    for j in range(len(key)):
        skey += key[j]

    if skey in hash_list:
        (hash_list[skey]).append(i)
        if (len(hash_list[skey]) > found_len):
            found_len = len(hash_list[skey])
            print "                FOUND group of {0}: {1}".format(found_len, hash_list[skey])
            for k in hash_list[skey]:
                print "                    {0}^3 = {1}".format(k, k**3)
    else:
        hash_list[skey] = [i]

    if (curr_len > prev_len):
        search_range.append((prev_i,i-1))
        print "    {0}^3 = {1}".format(i-1, (i-1)**3)
        print "{0} to {1} produce {2} digit cubes".format(prev_i, i-1, prev_len)
        prev_len = curr_len
        prev_i = i
        print "    {0}^3 = {1}".format(i, result)
        print "    ...."
    
#for i in [345, 384, 405]:
#    print "{0}^3 = {1}".format(i, cubes[i])

#for i in range(len(search_range)):
#    print "Searching range", search_range[i]
#    for j in range(search_range[i][0], search_range[i][1]):
#        print "    Testing {0}^3 = {1}".format(j, cube_list[j])
