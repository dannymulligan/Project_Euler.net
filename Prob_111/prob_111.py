#!/usr/bin/python
#
# Project Euler.net Problem 111
# 
# Considering 4-digit primes containing repeated digits it is clear
# that they cannot all be the same: 1111 is divisible by 11, 2222 is
# divisible by 22, and so on. But there are nine 4-digit primes
# containing three ones:
# 
#     1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
# 
# We shall say that M(n, d) represents the maximum number of repeated
# digits for an n-digit prime where d is the repeated digit, N(n, d)
# represents the number of such primes, and S(n, d) represents the sum
# of these primes.
# 
# So M(4, 1) = 3 is the maximum number of repeated digits for a
# 4-digit prime where one is the repeated digit, there are N(4, 1) = 9
# such primes, and the sum of these primes is S(4, 1) = 22275. It
# turns out that for d = 0, it is only possible to have M(4, 0) = 2
# repeated digits, but there are N(4, 0) = 13 such cases.
# 
# In the same way we obtain the following results for 4-digit primes.
#     Digit,d   M(4,d)   N(4,d)    S(4,d)
#       0         2        13      67061
#       1         3        9       22275
#       2         3        1       2221
#       3         3        12      46214
#       4         3        2       8888
#       5         3        1       5557
#       6         3        1       6661
#       7         3        9       57863
#       8         3        1       8887
#       9         3        7       48073
# 
# For d = 0 to 9, the sum of all S(4, d) is 273700.
# 
# Find the sum of all S(10, d).
#
# Solved ??/??/10
# ??? problems solved
# Position #??? on level 3

MAX_PRIME = 10000  # 4 digit primes

prime_table = [True]*(MAX_PRIME)  # prime_table[N] == True means this N is prime
primes = []  # List of prime numbers
def calculate_primes():
    i = 2
    while (i <= (MAX_PRIME/2)):
        if (prime_table[i] == True):
            primes.append(i)
            j = i*2
            while (j < MAX_PRIME):
                prime_table[j] = False
                j += i
        i += 1
    while (i < MAX_PRIME):
        if (prime_table[i] == True):
            primes.append(i)
        i += 1

def is_prime(n):
    if (n > MAX_PRIME*MAX_PRIME):
        print "Error: checking n = {0}, which is larger than MAX_PRIME^2 (MAX_PRIME = {1})".format(n, MAX_PRIME)
        sys.exit()
    elif (n < MAX_PRIME):
        return (prime_table[n])
    else:
        for i in primes:
            if ((n % i) == 0):
                return False
            if (i*i > n):
                return True
        return True

print "Calculating primes up to", (MAX_PRIME-1)
calculate_primes()

candidates = [ 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 
               1121, 1131, 1141, 1151, 1161, 1171, 1181, 1191, 
               1211, 1311, 1411, 1511, 1611, 1711, 1811, 1911,
               2111, 3111, 4111, 5111, 6111, 7111, 8111, 9111 ]

Answer = 0
Count = 0
for i in candidates:
    if is_prime(i):
        Count += 1
        Answer += i

print "Count =", Count
print "Answer =", Answer

