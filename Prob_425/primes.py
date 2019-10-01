#!/usr/bin/env python


SELF_TEST = __name__ == "__main__"

###############################################################################
def calculate_primes_list(limit, make_prime_list=True, silent=False):
    """Calculates a table of primes less than limit using a list
    The resulting datastructure can also be used to find the factors of non-primes
    Optionally generates a list of prime numbers
    """

    if not silent:
        import time
        start_time = time.clock()

    prime_table = [1]*limit
    prime_table[0] = 0  # Not a prime
    prime_table[1] = 0  # Not a prime
    prime_count = 0

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    i = 2
    prime_count += 1
    if make_prime_list:
        prime_list = [2]
    j = i**2
    while (j < limit):
        prime_table[j] = i
        j += i

    i = 3
    while (i < (limit/2)):
        if (prime_table[i] == 1):
            prime_count += 1
            if make_prime_list:
                prime_list.append(i)
            j = i**2
            while (j < limit):
                prime_table[j] = i
                j += i
        i += 2
    while (i < limit):
        if (prime_table[i] == 1):
            prime_count += 1
            if make_prime_list:
                prime_list.append(i)
        i += 2

    if not silent:
        print("There are {:,} primes less than {:,}, calculated in {:.2f} seconds".format(prime_count, limit, (time.clock() - start_time)))

    if make_prime_list:
        return prime_table, prime_list
    else:
        return prime_table


###############################################################################
def calculate_primes_bitarray(limit, make_prime_list=True, silent=False):
    """Calculates a table of primes/factors for integers less than limit
    Optionally generates a list of prime numbers
    """

    if not silent:
        import time
        start_time = time.clock()

    import bitarray
    prime_table = bitarray.bitarray(limit+1)
    prime_table.setall(1)

    # Optimization to allow us to increment i by 2 for the rest of the algoritm
    prime_table[:2] = prime_table[2*2::2] = 0
    prime_count = 1
    if make_prime_list:
        prime_list = [2]

    i = 3
    while (i < (limit/2)):
        if prime_table[i]:
            prime_count += 1
            if make_prime_list:
                prime_list.append(i)
            prime_table[i*i::i*2] = 0
        i += 2

    while (i < limit):
        if prime_table[i]:
            prime_count += 1
            if make_prime_list:
                prime_list.append(i)
        i += 2

    if not silent:
        print("There are {:,} primes less than {:,}, calculated in {:.2f} seconds".format(prime_count, limit, (time.clock() - start_time)))

    if make_prime_list:
        return prime_table, prime_list
    else:
        return prime_table


###############################################################################
def calculate_primes(limit, make_prime_list=True, silent=False):
    return calculate_primes_list(limit, make_prime_list, silent)
# Example call:
#     import primes
#     prime_table, prime_list = primes.calculate_primes(SIZE)
# or
#     prime_table = primes.calculate_primes(SIZE, make_prime_list=False)

if SELF_TEST:
    print("Running self test on calculate_primes()")
    primes_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                  61, 67, 71, 73, 79, 83, 89, 97]
    primes_500 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                  61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                  131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                  193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
                  263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
                  337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
                  409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
                  479, 487, 491, 499]
    prime_table, prime_list = calculate_primes(500, make_prime_list=True, silent=True)
    assert prime_list == primes_500
    print("Test passed")


###############################################################################
def exp_by_sq(x,y,z):
    '''Calculate (x**y % z) efficiently, using recursion'''
    if (y == 1):
        ans = x
    elif ((y % 2) == 0):
        # y is even
        ans = exp_by_sq(x, y/2, z)
        ans = (ans * ans) % z
    else:
        # l is odd
        ans = exp_by_sq(x, (y-1)/2, z)
        ans = (ans * ans) % z
        ans = (x * ans) % z
    return ans


###############################################################################
import random
def miller_rabin_primality_test(n,s,d,k):
    # True  = n might be prime
    # False = n not prime
    #
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    for kk in range(k):
        a = random.randint(2,n-2)
        x = exp_by_sq(a,d,n)
        if ((x == 1) or (x == n-1)):
            continue
        for r in range(1,s):
            x = ((x*x) % n)
            if (x == 1):  return False
            if (x == n-1):  break
        if (x != n-1):  return False
    return True

# From: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# There is a deterministic version of the Miller-Rabin primality test that provides an authorative answer
# after testing a smallish number of possible witnesses a
#
#    if n < 2,047, it is enough to test a = 2;
#    if n < 1,373,653, it is enough to test a = 2 and 3;
#    if n < 9,080,191, it is enough to test a = 31 and 73;
#    if n < 25,326,001, it is enough to test a = 2, 3, and 5;
#    if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
#    if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
#    if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
#    if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
#    if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17;
#    if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23.
#
# 3,825,123,056,546,413,051 > 2^61


###############################################################################
def is_prime(n, prime_table):
    if ((n % 2) == 0) or ((n % 3) == 0) or ((n % 5) == 0):
        # Quick test - is n divisible by 2, 3, or 5
        # This eliminates 22 out of 30 numbers
        return False
    elif n < len(prime_table):
        # If n is in our table of primes, look up the answer
        return prime_table[n] == 1
    elif n < (len(prime_table)-1)**2:
        # If n is less than the square of our table of primes,
        # then we can check it against every prime in that table
        x = 5
        while (x**2 <= n) and (x <= len(prime_table)):
            if prime_table[x] == 1:
                if (n % x) == 0:
                    return False
            x += 2
        return True
    else:
        # If all other options are exhausted, we use the probabilistic
        # Miller Rabin primality test
        s = 0
        d = n - 1
        while ((d % 2) == 0):
            d /= 2
            s += 1
        return miller_rabin_primality_test(n,s,d,4)

if SELF_TEST:
    print("Running self test on is_prime()")
    prime_table, prime_list = calculate_primes(10*3)
    print(prime_table)
    print(len(prime_table))
    assert is_prime(51, prime_table) == False
    assert is_prime(53, prime_table) == True
    assert is_prime(5678027, prime_table) == False
    assert is_prime(5678039, prime_table) == True
    print("Test passed")

# Example call:
#     import primes
#     prime_table, prime_list = primes.calculate_primes(SIZE)
#     answer = primes.is_prime(n, prime_table)


###############################################################################
def factors(n, prime_table):
    """Returns a list of the factors of an integer
    Relies on a table of prime values/factors calculated by calculate_primes()
    """
    answer = []
    while (prime_table[n] != 1):
        answer.append(prime_table[n])
        n //= prime_table[n]

    answer.append(n)
    answer.sort()
    return answer


###############################################################################
import itertools
import operator
import functools
def divisors(n, prime_table):
    """Generates divisors of an integer
    Relies on a table of prime values/factors calculated by calculate_primes()
    """
    n_factors = factors(n, prime_table)
    for l in range(1, len(n_factors)):
        for c in itertools.combinations(n_factors, l):
            yield functools.reduce(operator.mul, c)


###############################################################################
def gcd(a,b):
    """Greatest Common Denominator
    Takes two integers, returns an integer
    """
    while ((a != b) & (b != 0)):
        t = b
        b = a % b
        a = t
    return a


###############################################################################
def lcm(nums):
    """Lowest Common Multiplier
    Takes a list of integers
    Returns an integer
    """
    lcm = nums[0]
    for num in nums[1:]:
        #print("lcm = {} * {} // {}".format(lcm, num, gcd(lcm, num)))
        lcm = lcm * num // gcd(lcm, num)
    return lcm

if False:
    print("testing lcm()")
    testcases = [
        ([30], 30),
        ([20, 30], 60),
        ([2, 3, 5, 7, 11, 13], 2*3*5*7*11*13),
        ([2, 3, 9], 2*9),
        ([2, 3, 5, 7, 9, 11, 13], 2*3*5*7*3*11*13),
    ]
    for (nums, ans) in testcases:
        res = lcm(nums)
        print("lcm({}) = {}".format(nums, res))
        assert ans == res, "lcm({}) = {} but expecting {}".format(nums, res, ans)


###############################################################################
def calculate_phi(prime_table, silent=False):
    """Calculates a table of Euler's Totient function values
    Relies on a table of prime values/factors calculated by calculate_primes()
    """
    import time
    start_time = time.clock()
    length = len(prime_table)
    phi_table = [0]*length
    for n in range(1, length):
        if prime_table[n] == 1:
            # n is a prime number
            phi = n-1
        else:
            # n is a composite number
            divisor = prime_table[n]
            phi = divisor - 1
            num = n // divisor
            while (num % divisor) == 0:
                phi *= divisor
                num = num // divisor
            if num > 1:
                phi *= phi_table[num]
        phi_table[n] = phi

    if not silent:
        print("Calculated Eulers totient up to {:,} in {:.2f} seconds".format(length, (time.clock() - start_time)))
    return phi_table


###############################################################################
# Speed testing

if __name__ == "__main__":

    SIZE = 100*(10**6)
    print("Running calculate_primes_list({})".format(SIZE))
    prime_table, prime_list = calculate_primes_list(SIZE, make_prime_list=True)

    SIZE = 100*(10**6)
    print("Running calculate_primes_bitarray({})".format(SIZE))
    prime_table, prime_list = calculate_primes_bitarray(SIZE, make_prime_list=True)

    if len(prime_list) < 100:
        print(prime_list)
        for i in range(2, SIZE):
            if prime_table[i] == 1:
                print("{}, ".format(i))
    # Running in Sept 2019...
    #
    # I can calculate primes up to 100M using the bitarray approach in approx.
    # the same time as I can calculate primes up to 36M using lists, or about
    # 2.7x more in the same amount of run time.
    #
    # I calcalculate primes up to 100M in 35 seconds using the list approach
    # versus 12.5 seconds using the bitarray approach, or the same in about
    # 1/2.8x less time.
