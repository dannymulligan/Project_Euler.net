#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 407
#
# Idempotents
#
# If we calculate a^2 mod 6 for 0 <= a <= 5 we get: 0,1,4,3,4,1.
#
# The largest value of a such that a^2 ≡ a mod 6 is 4.
#
# Let's call M(n) the largest value of a < n such that a2 === a (mod n).
# So M(6) = 4.
#
# Find sum(M(n)) for 1 <= n <= 10^7.


import sys
import time
start_time = time.clock()

SIZE = int(sys.argv[1])

LIMIT_PRIME = SIZE+1
prime_table = [1]*LIMIT_PRIME  # table of largest factor
primes = []

############################################################
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
    print("There are {} primes less than {}, calculated in {:.3f} seconds".format(len(primes), limit, (time.clock() - start_time)))

    
############################################################
def is_prime(n):
    return prime_table[n] == 1


############################################################
def power(n):
    power_first = 1
    n_factors = factors(n)
    for x in n_factors[1:]:
        if x == n_factors[0]:
            power_first += 1
        else:
            return 0
    return power_first
    

############################################################
def factors(n):
    answer = []
    while (prime_table[n] != 1):
        answer.append(prime_table[n])
        n //= prime_table[n]
        
    answer.append(n)
    answer.sort()
    return answer


############################################################
calculate_primes(LIMIT_PRIME)
powers_of_primes = []
for prime in primes:
    powers_of_primes.append(prime)
    n = 2
    while prime**n < LIMIT_PRIME:
        powers_of_primes.append(prime**n)
        n += 1
#print("powers_of_primes =", powers_of_primes)


########################################
def res(a,n):
    return (a**2) % n


########################################
def M(n):
    for a in range(n, 0, -1):
        r = res(a, n)
        if a == r:
            return a
    return 1


########################################
target_nums = [0] * (SIZE+1) * SIZE
a = 1
target = a * (a - 1)
while target < (SIZE+1) * SIZE:
    target_nums[target] = a
    #print("{} * {} = {} => target_nums[{}] = {}".format(a, a-1, a*(a-1), target, a))
    a += 1
    target = a * (a - 1)

def M(n):
    '''
    a^2 = a mod n
    a^2 = a + x*n, where x is integer
    a^2 - a = x*n
    a(a - 1) = x*n
    '''
    print("Calculating M({})".format(n))
    best_a = 0
    for x in range(n-1, 0, -1):
        if x*n >= (SIZE+1) * SIZE:
            continue
        a = target_nums[x*n]
        print("    x={} n={} x*n={} a={}".format(x, n, x*n, a))
        if (a != 0) and (a < n):
            print("    M({}) = {}".format(n, a))
            if a > best_a:
                best_a = a
            return a
    print("    M({}) = {}".format(n, 1))
    return a


########################################
if False:
#if True:
    for n in range(1,80):
        if M(n) == 1:
            continue
        print("")
        print("="*60)
        print("n = {}, M({}) = {}  factors({}) = {}".format(n, n, M(n), n, factors(n)))
        print("-"*60)
        for a in range(n):
            r = res(a, n)
            if a == r:
                print(" >> a = {:3}, r = {:3} <<  factors(a) = {}".format(a,r, factors(a)))
            else:
                print("    a = {:3}, r = {:3}     factors(a) = {}".format(a,r, factors(a)))
    sys.exit()


########################################
SizeLimit = SIZE
m_table = [-1]*(SizeLimit+1)
m_table[1] = 0
shortcuts = 0
Answer = 0

# All n=prime have M(n) = 1
for prime in primes:
    m_table[prime] = 1
    Answer += 1
    shortcuts += 1

# All n^x have M(n^x) = 1
for prime in primes:
    pow = 2
    while (prime**pow <= SizeLimit+1):
        m_table[prime**pow] = 1
        Answer += 1
        shortcuts += 1
        pow += 1

print("Shortcuts for {:,} out of {:,} numbers = {:.2f}%".format(shortcuts, SizeLimit, (100.0*shortcuts/SizeLimit)))

for n in range(1, SIZE+1):
    if (m_table[n] == -1):
        mm = M(n)
        m_table[n] = mm
        #if n > 980:
        if False:
            n_factors = factors(n)
            if True:
                print("M({:3}) = {:3},  factors({:3}) = {}".format(n, mm, n, n_factors))
                print("               (a-1)*a = {} = {} * {} + {}".format((mm-1)*mm,  (mm-1)*mm // n, n, (mm-1)*mm % n))
                if ((mm-1)*mm % n) != 0:
                    sys.exit("Error")
                if is_prime(n):
                    print("  prime  ", end='')
                elif power(n) == 2:
                    print("  square ", end='')
                elif power(n) == 3:
                    print("  cube   ", end='')
                elif power(n) >= 3:
                    print("  ^{}    ".format(power(n)), end='')
                else:
                    print("         ", end='')
                print("      factors({:3}) = {}".format(mm, factors(mm)))
                print("         ", end='')
                print("      factors({:3}) = {}".format(((mm-1)*mm // n), factors((mm-1)*mm // n)))
                print("")
        Answer += mm

if True:
    for n in range(1, SIZE+1):
        m = m_table[n]
        print("M({n:2}) = {m:2}".format(n=n, m=m))
        x = m*(m-1)//n
        if False:
            print("    {m}^2 = {mm} = {m} + {n} * {x}".format(n=n, m=m, mm=m*m, x=x))
            for z in [m, n, x]:
                print("    factors({}) = {}".format(z, factors(z)))
            print()
        
print("When SizeLimit = {:,}, answer is {:,} (calculated in {:.2f} seconds)".format(SizeLimit, Answer, time.clock() - start_time))
#print("Time taken = {:.2f} seconds".format(time.clock() - start_time))

# When SizeLimit = 10, answer is 18 (calculated in 0.00 seconds)
# When SizeLimit = 100, answer is 2,550 (calculated in 0.00 seconds)
# When SizeLimit = 1,000, answer is 314,035 (calculated in 0.22 seconds)
# When SizeLimit = 10,000, answer is 34,981,570 (calculated in 21.69 seconds)


# When SizeLimit = 10, answer is 18 (calculated in 0.00 seconds)
# When SizeLimit = 100, answer is 2,550 (calculated in 0.01 seconds)
# When SizeLimit = 1,000, answer is 314,035 (calculated in 0.14 seconds)
# When SizeLimit = 10,000, answer is 34,981,570 (calculated in 5.16 seconds)
# When SizeLimit = 20,000, answer is 142,893,767 (calculated in 18.25 seconds)

# When SizeLimit = 10, answer is 18 (calculated in 0.00 seconds)
# When SizeLimit = 100, answer is 2,550 (calculated in 0.01 seconds)
# When SizeLimit = 1,000, answer is 314,035 (calculated in 0.14 seconds)
# When SizeLimit = 10,000, answer is 34,981,570 (calculated in 5.07 seconds)
# When SizeLimit = 20,000, answer is 142,893,767 (calculated in 17.91 seconds)
# When SizeLimit = 100,000, answer is 3,717,852,516 (calculated in 385.23 seconds)

# Was calculating M(1) incorrectly, was 1 should be 0, so the following differ from the
# above by 1, but the following are correct

# When SizeLimit = 10, answer is 17 (calculated in 0.00 seconds)
# When SizeLimit = 100, answer is 2,549 (calculated in 0.00 seconds)
# When SizeLimit = 1,000, answer is 314,034 (calculated in 0.05 seconds)
# When SizeLimit = 10,000, answer is 34,981,569 (calculated in 4.21 seconds)
# When SizeLimit = 20,000, answer is 142,893,766 (calculated in 15.33 seconds)
# When SizeLimit = 100,000, answer is 3,717,852,515 (calculated in 389.52 seconds)
