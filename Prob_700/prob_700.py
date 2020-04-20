#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 700
#
# Eulercoin
#
# Leonhard Euler was born on 15 April 1707.
#
# Consider the sequence 1504170715041707n mod 4503599627370517.
#
# An element of this sequence is defined to be an Eulercoin if it is
# strictly smaller than all previously found Eulercoins.
#
# For example, the first term is 1504170715041707 which is the first
# Eulercoin. The second term is 3008341430083414 which is greater than
# 1504170715041707 so is not an Eulercoin. However, the third term is
# 8912517754604 which is small enough to be a new Eulercoin.
#
# The sum of the first 2 Eulercoins is therefore 1513083232796311.
#
# Find the sum of all Eulercoins.


import sys
#print(sys.version)
import time
start_time = time.clock()

A = 1504170715041707  # = 17 * 1249 * 12043 * 5882353
B = 4503599627370517  # prime
partition = 20000000
answer = 0


###############################################################################

def sequence():
    '''
    sequence[n] = ((A * n) % B)
    '''
    n = 0
    while True:
        n += 1
        yield n, (A * n) % B


###############################################################################

front_solutions = []
valid_ns = []
current_limit = A + 1
i = 0
for n, e in sequence():
    if e < partition:
        break
    if e < current_limit:
        current_limit = e
        answer += e
        i += 1
        valid_ns.append(n)
        print("{}: sequence[{:,}] = {:,}, answer = {:,}, time = {:.2f} seconds".format(i, n, e, answer, time.clock() - start_time))
        front_solutions.append((n, e))


###############################################################################
def ext_euclid(n, m, debug = False):
    '''
    Find A such that
       A * n = 1 (mod m)
    using the Extended Euclidean algorithm
    Reference: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    '''

    r_prev = m
    r_curr = n
    s_prev, s_curr = 1, 0
    t_prev, t_curr = 0, 1
    i = 1
    while ((r_prev % r_curr) != 0):
        i += 1
        q = r_prev // r_curr
        r = r_prev % r_curr
        s = s_prev - q * s_curr
        t = t_prev - q * t_curr

        r_prev, r_curr = r_curr, r
        s_prev, s_curr = s_curr, s
        t_prev, t_curr = t_curr, t
        if debug:
            print("{}: q = {}, r = {}, s = {}, t = {}".format(i, q, r, s, t))

    while t < 0:
        t += m
    if debug:
        print("ext_euclid(n={n}, m={m}) == {t}".format(n=n, m=m, t=t))
        print("    when x = {t}, x * {n} = 1 (mod {m})".format(t=t, n=n, m=m))
    return t

if False:
    _ = ext_euclid(46, 240)
    print()
    _ = ext_euclid(32, 47)
    print()
    _ = ext_euclid(A, B)
    print()
    sys.exit()


###############################################################################
# Calculate X such that
#     1504170715041707 * X mod 4503599627370517 = 1
x = ext_euclid(A, B)
print("x = {}".format(x))
# Given that, then
#     (X * 2) mod 4503599627370517 = 2
#     (X * 3) mod 4503599627370517 = 3
#     etc

rear_solutions = []
prev_n = B
i = 0
for e in range(1, partition):
    n = (e * x) % B
    if n < prev_n:
        prev_n = n
        answer += e
        i += 1
        print("{}: sequence[{:,}] = {:,}, answer = {:,}, time = {:.2f} seconds".format(i, n, e, answer, time.clock() - start_time))
        rear_solutions.insert(0, (n, e))

solutions = front_solutions + rear_solutions
print("{} Eulercoins = {}".format(len(solutions), solutions))

print("Answer = {:,}".format(answer))

print("Time taken = {:.2f} seconds".format(time.clock() - start_time))


# Valid N's = [
#          1 = prime
#          3 = prime
#        506 = 2 * 11 * 23
#       2527 = 7 * 19^2
#       4548 = 2^2 * 3 * 379
#      11117 = prime
#      17686 = 2 * 37 * 239
#      24255 = 3^2 * 5 * 7^2 * 11
#      55079 = prime
#      85903 = prime
#     202630 = 2 * 5 * 23 * 881
#     724617 =
#    1246604
#    6755007


# bash-3.2$ ./prob_700.py
# 1: sequence[1] = 1,504,170,715,041,707, answer = 1,504,170,715,041,707, time = 0.00 seconds
# 2: sequence[3] = 8,912,517,754,604, answer = 1,513,083,232,796,311, time = 0.00 seconds
# 3: sequence[506] = 2,044,785,486,369, answer = 1,515,128,018,282,680, time = 0.00 seconds
# 4: sequence[2,527] = 1,311,409,677,241, answer = 1,516,439,427,959,921, time = 0.00 seconds
# 5: sequence[4,548] = 578,033,868,113, answer = 1,517,017,461,828,034, time = 0.00 seconds
# 6: sequence[11,117] = 422,691,927,098, answer = 1,517,440,153,755,132, time = 0.01 seconds
# 7: sequence[17,686] = 267,349,986,083, answer = 1,517,707,503,741,215, time = 0.01 seconds
# 8: sequence[24,255] = 112,008,045,068, answer = 1,517,819,511,786,283, time = 0.01 seconds
# 9: sequence[55,079] = 68,674,149,121, answer = 1,517,888,185,935,404, time = 0.03 seconds
# 10: sequence[85,903] = 25,340,253,174, answer = 1,517,913,526,188,578, time = 0.04 seconds
# 11: sequence[202,630] = 7,346,610,401, answer = 1,517,920,872,798,979, time = 0.09 seconds
# 12: sequence[724,617] = 4,046,188,430, answer = 1,517,924,918,987,409, time = 0.31 seconds
# 13: sequence[1,246,604] = 745,766,459, answer = 1,517,925,664,753,868, time = 0.53 seconds
# 14: sequence[6,755,007] = 428,410,324, answer = 1,517,926,093,164,192, time = 2.80 seconds
# 15: sequence[12,263,410] = 111,054,189, answer = 1,517,926,204,218,381, time = 5.07 seconds
# 16: sequence[42,298,633] = 15,806,432, answer = 1,517,926,220,024,813, time = 17.43 seconds
# 17: sequence[326,125,654] = 15,397,267, answer = 1,517,926,235,422,080, time = 133.97 seconds
# 18: sequence[609,952,675] = 14,988,102, answer = 1,517,926,250,410,182, time = 250.53 seconds
# 19: sequence[893,779,696] = 14,578,937, answer = 1,517,926,264,989,119, time = 367.13 seconds
# 20: sequence[1,177,606,717] = 14,169,772, answer = 1,517,926,279,158,891, time = 487.39 seconds
# 21: sequence[1,461,433,738] = 13,760,607, answer = 1,517,926,292,919,498, time = 614.31 seconds
# 22: sequence[1,745,260,759] = 13,351,442, answer = 1,517,926,306,270,940, time = 734.92 seconds
# 23: sequence[2,029,087,780] = 12,942,277, answer = 1,517,926,319,213,217, time = 855.93 seconds
# 24: sequence[2,312,914,801] = 12,533,112, answer = 1,517,926,331,746,329, time = 976.58 seconds
# 25: sequence[2,596,741,822] = 12,123,947, answer = 1,517,926,343,870,276, time = 1097.54 seconds
# 26: sequence[2,880,568,843] = 11,714,782, answer = 1,517,926,355,585,058, time = 1217.98 seconds
# 27: sequence[3,164,395,864] = 11,305,617, answer = 1,517,926,366,890,675, time = 1338.50 seconds
# 28: sequence[3,448,222,885] = 10,896,452, answer = 1,517,926,377,787,127, time = 1462.01 seconds
# 29: sequence[3,732,049,906] = 10,487,287, answer = 1,517,926,388,274,414, time = 1586.50 seconds
# 30: sequence[4,015,876,927] = 10,078,122, answer = 1,517,926,398,352,536, time = 1710.84 seconds
# 31: sequence[4,299,703,948] = 9,668,957, answer = 1,517,926,408,021,493, time = 1835.29 seconds
# 32: sequence[4,583,530,969] = 9,259,792, answer = 1,517,926,417,281,285, time = 1959.63 seconds
# 33: sequence[4,867,357,990] = 8,850,627, answer = 1,517,926,426,131,912, time = 2084.02 seconds
# 34: sequence[5,151,185,011] = 8,441,462, answer = 1,517,926,434,573,374, time = 2208.46 seconds
# 35: sequence[5,435,012,032] = 8,032,297, answer = 1,517,926,442,605,671, time = 2332.91 seconds
# 36: sequence[5,718,839,053] = 7,623,132, answer = 1,517,926,450,228,803, time = 2458.74 seconds
# 37: sequence[6,002,666,074] = 7,213,967, answer = 1,517,926,457,442,770, time = 2587.03 seconds
# 38: sequence[6,286,493,095] = 6,804,802, answer = 1,517,926,464,247,572, time = 2712.50 seconds
# 39: sequence[6,570,320,116] = 6,395,637, answer = 1,517,926,470,643,209, time = 2838.12 seconds
# 40: sequence[6,854,147,137] = 5,986,472, answer = 1,517,926,476,629,681, time = 2963.13 seconds
# 41: sequence[7,137,974,158] = 5,577,307, answer = 1,517,926,482,206,988, time = 3087.57 seconds
# 42: sequence[7,421,801,179] = 5,168,142, answer = 1,517,926,487,375,130, time = 3212.03 seconds
# 43: sequence[7,705,628,200] = 4,758,977, answer = 1,517,926,492,134,107, time = 3336.85 seconds
# 44: sequence[7,989,455,221] = 4,349,812, answer = 1,517,926,496,483,919, time = 3461.41 seconds
# 45: sequence[8,273,282,242] = 3,940,647, answer = 1,517,926,500,424,566, time = 3585.56 seconds
# 46: sequence[8,557,109,263] = 3,531,482, answer = 1,517,926,503,956,048, time = 3710.69 seconds
# 47: sequence[8,840,936,284] = 3,122,317, answer = 1,517,926,507,078,365, time = 3835.61 seconds
# 48: sequence[9,124,763,305] = 2,713,152, answer = 1,517,926,509,791,517, time = 3961.07 seconds
# 49: sequence[9,408,590,326] = 2,303,987, answer = 1,517,926,512,095,504, time = 4086.39 seconds
# 50: sequence[9,692,417,347] = 1,894,822, answer = 1,517,926,513,990,326, time = 4211.41 seconds
# 51: sequence[9,976,244,368] = 1,485,657, answer = 1,517,926,515,475,983, time = 4336.49 seconds
# 52: sequence[10,260,071,389] = 1,076,492, answer = 1,517,926,516,552,475, time = 4461.89 seconds
# 53: sequence[10,543,898,410] = 667,327, answer = 1,517,926,517,219,802, time = 4587.54 seconds
# 54: sequence[10,827,725,431] = 258,162, answer = 1,517,926,517,477,964, time = 4717.52 seconds
# 55: sequence[21,939,277,883] = 107,159, answer = 1,517,926,517,585,123, time = 9969.74 seconds
# 56: sequence[54,990,108,218] = 63,315, answer = 1,517,926,517,648,438, time = 24503.06 seconds
# 57: sequence[88,040,938,553] = 19,471, answer = 1,517,926,517,667,909, time = 39692.55 seconds
# 58: sequence[297,173,645,994] = 14,569, answer = 1,517,926,517,682,478, time = 131232.49 seconds
# 59: sequence[506,306,353,435] = 9,667, answer = 1,517,926,517,692,145, time = 222997.74 seconds

# x = 3451657199285664
# 1: sequence[3,451,657,199,285,664] = 1, answer = 0, time = 0.00 seconds
# 2: sequence[2,399,714,771,200,811] = 2, answer = 1, time = 0.00 seconds
# 3: sequence[1,347,772,343,115,958] = 3, answer = 3, time = 0.00 seconds
# 4: sequence[295,829,915,031,105] = 4, answer = 6, time = 0.00 seconds
# 5: sequence[131,377,232,039,567] = 17, answer = 10, time = 0.00 seconds
# 6: sequence[98,301,781,087,596] = 47, answer = 27, time = 0.00 seconds
# 7: sequence[65,226,330,135,625] = 77, answer = 74, time = 0.00 seconds
# 8: sequence[32,150,879,183,654] = 107, answer = 151, time = 0.00 seconds
# 9: sequence[31,226,307,415,337] = 244, answer = 258, time = 0.00 seconds
# 10: sequence[30,301,735,647,020] = 381, answer = 502, time = 0.00 seconds
# 11: sequence[29,377,163,878,703] = 518, answer = 883, time = 0.00 seconds
# 12: sequence[28,452,592,110,386] = 655, answer = 1,401, time = 0.00 seconds
# 13: sequence[27,528,020,342,069] = 792, answer = 2,056, time = 0.00 seconds
# 14: sequence[26,603,448,573,752] = 929, answer = 2,848, time = 0.00 seconds
# 15: sequence[25,678,876,805,435] = 1,066, answer = 3,777, time = 0.00 seconds
# 16: sequence[24,754,305,037,118] = 1,203, answer = 4,843, time = 0.00 seconds
# 17: sequence[23,829,733,268,801] = 1,340, answer = 6,046, time = 0.00 seconds
# 18: sequence[22,905,161,500,484] = 1,477, answer = 7,386, time = 0.00 seconds
# 19: sequence[21,980,589,732,167] = 1,614, answer = 8,863, time = 0.00 seconds
# 20: sequence[21,056,017,963,850] = 1,751, answer = 10,477, time = 0.00 seconds
# 21: sequence[20,131,446,195,533] = 1,888, answer = 12,228, time = 0.00 seconds
# 22: sequence[19,206,874,427,216] = 2,025, answer = 14,116, time = 0.00 seconds
# 23: sequence[18,282,302,658,899] = 2,162, answer = 16,141, time = 0.00 seconds
# 24: sequence[17,357,730,890,582] = 2,299, answer = 18,303, time = 0.00 seconds
# 25: sequence[16,433,159,122,265] = 2,436, answer = 20,602, time = 0.00 seconds
# 26: sequence[15,508,587,353,948] = 2,573, answer = 23,038, time = 0.00 seconds
# 27: sequence[14,584,015,585,631] = 2,710, answer = 25,611, time = 0.00 seconds
# 28: sequence[13,659,443,817,314] = 2,847, answer = 28,321, time = 0.00 seconds
# 29: sequence[12,734,872,048,997] = 2,984, answer = 31,168, time = 0.00 seconds
# 30: sequence[11,810,300,280,680] = 3,121, answer = 34,152, time = 0.00 seconds
# 31: sequence[10,885,728,512,363] = 3,258, answer = 37,273, time = 0.00 seconds
# 32: sequence[9,961,156,744,046] = 3,395, answer = 40,531, time = 0.00 seconds
# 33: sequence[9,036,584,975,729] = 3,532, answer = 43,926, time = 0.00 seconds
# 34: sequence[8,112,013,207,412] = 3,669, answer = 47,458, time = 0.00 seconds
# 35: sequence[7,187,441,439,095] = 3,806, answer = 51,127, time = 0.00 seconds
# 36: sequence[6,262,869,670,778] = 3,943, answer = 54,933, time = 0.00 seconds
# 37: sequence[5,338,297,902,461] = 4,080, answer = 58,876, time = 0.00 seconds
# 38: sequence[4,413,726,134,144] = 4,217, answer = 62,956, time = 0.00 seconds
# 39: sequence[3,489,154,365,827] = 4,354, answer = 67,173, time = 0.00 seconds
# 40: sequence[2,564,582,597,510] = 4,491, answer = 71,527, time = 0.00 seconds
# 41: sequence[1,640,010,829,193] = 4,628, answer = 76,018, time = 0.00 seconds
# 42: sequence[715,439,060,876] = 4,765, answer = 80,646, time = 0.00 seconds
# Answer = 85,411
# Ultimate answer = 1,517,926,517,777,556
