#!/usr/bin/python
# coding=utf-8
#
# Project Euler.net Problem 315
#
# Digital root clocks
#
# Sam and Max are asked to transform two digital clocks into two
# "digital root" clocks.
#
# A digital root clock is a digital clock that calculates digital
# roots step by step.
#
# When a clock is fed a number, it will show it and then it will start
# the calculation, showing all the intermediate values until it gets
# to the result.
#
# For example, if the clock is fed the number 137, it will show: "137"
# → "11" → "2" and then it will go black, waiting for the next number.
#
# Every digital number consists of some light segments: three
# horizontal (top, middle, bottom) and four vertical (top-left,
# top-right, bottom-left, bottom-right).
#
# Number "1" is made of vertical top-right and bottom-right, number
# "4" is made by middle horizontal and vertical top-left, top-right
# and bottom-right. Number "8" lights them all.
#
#  %%%    ...    %%%    %%%    ...    %%%    %%%    %%%   %%%   %%%
# %   %  .   %  .   %  .   %  %   %  %   .  %   .  %   % %   % %   %
# %   %  .   %  .   %  .   %  %   %  %   .  %   .  %   % %   % %   %
# %   %  .   %  .   %  .   %  %   %  %   .  %   .  %   % %   % %   %
#  ...    ...    %%%    %%%    %%%    %%%    %%%    ...   %%%   %%%
# %   %  .   %  %   .  .   %  .   %  .   %  %   %  .   % %   % .   %
# %   %  .   %  %   .  .   %  .   %  .   %  %   %  .   % %   % .   %
# %   %  .   %  %   .  .   %  .   %  .   %  %   %  .   % %   % .   %
#  %%%    ...    %%%    %%%    ...    %%%    %%%    ...   %%%   %%%
#
# The clocks consume energy only when segments are turned on/off.
#
# To turn on a "2" will cost 5 transitions, while a "7" will cost only
# 4 transitions.
#
# Sam and Max built two different clocks.
#
# Sam's clock is fed e.g. number 137: the clock shows "137", then the
# panel is turned off, then the next number ("11") is turned on, then
# the panel is turned off again and finally the last number ("2") is
# turned on and, after some time, off.
#
# For the example, with number 137, Sam's clock requires:
#    "137" : (2 + 5 + 4) × 2 = 22 transitions ("137" on/off).
#    "11"  : (2 + 2) × 2 = 8 transitions ("11" on/off).
#    "2"   : (5) × 2 = 10 transitions ("2" on/off).
# For a grand total of 40 transitions.
#
# Max's clock works differently. Instead of turning off the whole
# panel, it is smart enough to turn off only those segments that won't
# be needed for the next number.
# For number 137, Max's clock requires:
#    "137" : 2 + 5 + 4 = 11 transitions ("137" on)
#            7 transitions (to turn off the segments that are not
#            needed for number "11").
#    "11"  : 0 transitions (number "11" is already turned on correctly)
#            3 transitions (to turn off the first "1" and the bottom
#            part of the second "1"; the top part is common with
#            number "2").
#    "2"   : 4 transitions (to turn on the remaining segments in order
#            to get a "2")
#            5 transitions (to turn off number "2").
# For a grand total of 30 transitions.
#
# Of course, Max's clock consumes less power than Sam's one.
#
# The two clocks are fed all the prime numbers between A = 10^7 and
# B = 2x10^7.
#
# Find the difference between the total number of transitions needed
# by Sam's clock and that needed by Max's one.
#

import sys
import time
start_time = time.clock()


############################################################
LOW = 10**7
HIGH = 2*10**7
#LOW = 10**3
#HIGH = 2*10**3


############################################################
LIMIT_PRIME = HIGH
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

def calculate_primes(limit=LIMIT_PRIME):
    if (limit>len(prime_table)):
        raise Exception("prime_table is too small ({} entries, need at least {})".format(len(prime_table), limit))

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    primes.append(i)
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            primes.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            primes.append(i)
        i += 2
    print("There are {} primes less than {}, calculated in {} seconds".format(len(primes), limit, (time.clock() - start_time)))

calculate_primes(LIMIT_PRIME)

def primes_between(x, y):
    for n in range(x, y):
        if prime_table[n] == 1:
            yield n


############################################################
def digital_root(x):
    ans = 0
    while x >= 10:
        ans +=  x % 10
        x /= 10
    return ans + x

assert digital_root(137) == 11
assert digital_root(11) == 2


############################################################
# Calculate the savings for each digit transition on Max's clock
save = [[0 for x in range(10)] for y in range(10)]

save[0][1] = 2
save[0][2] = 4
save[0][3] = 4
save[0][4] = 3
save[0][5] = 4
save[0][6] = 5
save[0][7] = 4
save[0][8] = 6
save[0][9] = 5

save[1][2] = 1
save[1][3] = 2
save[1][4] = 2
save[1][5] = 1
save[1][6] = 1
save[1][7] = 2
save[1][8] = 2
save[1][9] = 2

save[2][3] = 4
save[2][4] = 2
save[2][5] = 3
save[2][6] = 4
save[2][7] = 2
save[2][8] = 5
save[2][9] = 4

save[3][4] = 3
save[3][5] = 4
save[3][6] = 4
save[3][7] = 3
save[3][8] = 5
save[3][9] = 5

save[4][5] = 3
save[4][6] = 3
save[4][7] = 3
save[4][8] = 4
save[4][9] = 4

save[5][6] = 5
save[5][7] = 3
save[5][8] = 5
save[5][9] = 5

save[6][7] = 3
save[6][8] = 6
save[6][9] = 5

save[7][8] = 4
save[7][9] = 4

save[8][9] = 6

save[0][0] = 6
save[1][1] = 2
save[2][2] = 5
save[3][3] = 5
save[4][4] = 4
save[5][5] = 5
save[6][6] = 6
save[7][7] = 4
save[8][8] = 7
save[9][9] = 6

for x in range(10):
    for y in range(x,10):
        save[y][x] = save[x][y]

#for x in range(10):
#    for y in range(10):
#        print(save[x][y]),
#    print

# 6 2 4 4 3 4 5 4 6 5
# 2 2 1 2 2 1 1 2 2 2
# 4 1 5 4 2 3 4 2 5 4
# 4 2 4 5 3 4 4 3 5 5
# 3 2 2 3 4 3 3 3 4 4
# 4 1 3 4 3 5 5 3 5 5
# 5 1 4 4 3 5 6 3 6 5
# 4 2 2 3 3 3 3 4 4 4
# 6 2 5 5 4 5 6 4 7 6
# 5 2 4 5 4 5 5 4 6 6


############################################################
def power_saving(x, y):
    #print("power_saving({x},{y})".format(x=x, y=y))
    ans = 0
    while (x > 0) & (y > 0):
        x0 = x % 10  # lowest digit
        y0 = y % 10  # lowest digit
        ans += 2*save[x0][y0]
        #print("x0={x0} y0={y0} x={x} y={y} ans={a}".format(x0=x0, y0=y0, x=x, y=y, a=ans))
        x /= 10
        y /= 10
    return ans

#assert power_saving(137, 11) + power_saving(11, 2) == 10
#assert power_saving(17, 8) == 8
#print("power_saving(37, 10) = {}".format(power_saving(37, 10)))
#assert power_saving(37, 10) == 12
#print("power_saving(10, 1) = {}".format(power_saving(10, 1)))
#assert power_saving(10, 1) == 4
#print("power_saving(1999, 28) = {}".format(power_saving(1999, 28)))
#assert  power_saving(1999, 28) == 20


############################################################
def count_savings(n):
    ans = 0
    while (n >= 10):
        prev = n
        n = digital_root(n)
        ans += power_saving(prev, n)
        #print("prev={p} n={n} ans={a}".format(p=prev, n=n, a=ans))
    return ans

#assert count_savings(17) == 8
#assert count_savings(19) == 18
#assert count_savings(23) == 8
#assert count_savings(29) == 8
#assert count_savings(31) == 4
#assert count_savings(37) == 16
#assert count_savings(41) == 2
#assert count_savings(43) == 6
#assert count_savings(47) == 10
#assert count_savings(53) == 10
#assert count_savings(59) == 16
#assert count_savings(137) == 10
#assert count_savings(1999993) == 38


############################################################
answer = 0
prime_count = 0
for p in primes_between(LOW, HIGH):
    prime_count += 1
    answer += count_savings(p)
    #if prime_count < 100:
    #    print("p={p} answer={a} count_savings({p})={c}".format(p=p, a=answer, c=count_savings(p)))

print("Found {p} primes between {low} and {high}".format(p=prime_count, low=LOW, high=HIGH))
print("Answer = {}".format(answer))


############################################################
print("Time taken = {0} seconds".format(time.clock() - start_time))
