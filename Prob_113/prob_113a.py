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

# < 1,000,000,000: 9 digit numbers

cnt = 0
# Count up
for d01 in range(0,10):
    for d02 in range(d01,10):
        for d03 in range(d02,10):
            for d04 in range(d03,10):
                for d05 in range(d04,10):
                    for d06 in range(d05,10):
                        for d07 in range(d06,10):
                            for d08 in range(d07,10):
                                for d09 in range(d08,10):
                                    cnt += 1
                                    print "up", d01, d02, d03, d04, d05, d06, d07, d08, d09
cnt -= 1 # Correct for "0 0 0 0 0 0 0 0 0", shouldn't be included
#print cnt

# Count down, 9 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        for d03 in range(d02,-1,-1):
            for d04 in range(d03,-1,-1):
                for d05 in range(d04,-1,-1):
                    for d06 in range(d05,-1,-1):
                        for d07 in range(d06,-1,-1):
                            for d08 in range(d07,-1,-1):
                                for d09 in range(d08,-1,-1):
                                    cnt += 1
                                    print "dn", d01, d02, d03, d04, d05, d06, d07, d08, d09
cnt -= 9 # Correct for "1 1 1 1 1 1 1 1 1", "2 2 2 2 2 2 2 2 2", etc, already covered by up count
#print cnt

# Count down, 8 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        for d03 in range(d02,-1,-1):
            for d04 in range(d03,-1,-1):
                for d05 in range(d04,-1,-1):
                    for d06 in range(d05,-1,-1):
                        for d07 in range(d06,-1,-1):
                            for d08 in range(d07,-1,-1):
                                cnt += 1
                                print "dn", d01, d02, d03, d04, d05, d06, d07, d08
cnt -= 9 # Correct for "1 1 1 1 1 1 1 1", "2 2 2 2 2 2 2 2", etc, already covered by up count
#print cnt

# Count down, 7 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        for d03 in range(d02,-1,-1):
            for d04 in range(d03,-1,-1):
                for d05 in range(d04,-1,-1):
                    for d06 in range(d05,-1,-1):
                        for d07 in range(d06,-1,-1):
                            cnt += 1
                            print "dn", d01, d02, d03, d04, d05, d06, d07
cnt -= 9 # Correct for "1 1 1 1 1 1 1", "2 2 2 2 2 2 2", etc, already covered by up count
#print cnt

# Count down, 6 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        for d03 in range(d02,-1,-1):
            for d04 in range(d03,-1,-1):
                for d05 in range(d04,-1,-1):
                    for d06 in range(d05,-1,-1):
                        cnt += 1
                        print "dn", d01, d02, d03, d04, d05, d06
cnt -= 9 # Correct for "1 1 1 1 1 1", "2 2 2 2 2 2", etc, already covered by up count
#print cnt

# Count down, 5 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        for d03 in range(d02,-1,-1):
            for d04 in range(d03,-1,-1):
                for d05 in range(d04,-1,-1):
                    cnt += 1
                    print "dn", d01, d02, d03, d04, d05
cnt -= 9 # Correct for "1 1 1 1 1", "2 2 2 2 2", etc, already covered by up count
#print cnt

# Count down, 4 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        for d03 in range(d02,-1,-1):
            for d04 in range(d03,-1,-1):
                cnt += 1
                print "dn", d01, d02, d03, d04
cnt -= 9 # Correct for "1 1 1 1", "2 2 2 2", etc, already covered by up count
#print cnt

# Count down, 3 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        for d03 in range(d02,-1,-1):
            cnt += 1
            print "dn", d01, d02, d03
cnt -= 9 # Correct for "1 1 1", "2 2 2", etc, already covered by up count
#print cnt

# Count down, 2 digits
for d01 in range(9,0,-1):
    for d02 in range(d01,-1,-1):
        cnt += 1
        print "dn", d01, d02
cnt -= 9 # Correct for "1 1", "2 2", etc, already covered by up count
print cnt

# Don't count 1 digit numbers, already covered in up count

