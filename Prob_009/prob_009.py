#!/usr/bin/env python3
#
# Project Euler.net Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a^(2) + b^(2) = c^(2)
#
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.



# Since a + b + c are equal to 1000, and a < b < c, the minimum value
# for c must be 335. If c = 334, then at most b = 333, and at most a =
# 332, and a + b + c = 999 which is too small.
#
# The maximum value of c is 997, because if a = 1, and b = 2 and c =
# 998, then a + b + c = 1001 which is too big.
#
# So we're going to search for c values between 335 and 997.

def find_answer(cmin, cmax, target):
    # Loop through all possible values of c
    for c in range(cmin, cmax):

        # Loop through all possible values of b
        for b in range(2, c):

            # Loop through all possible values of a
            for a in range(1, b):

                # Check that these values of a, b, & c are a Pythagorean triplet
                if (a**2 + b**2) == c**2:

                    # Check if this Pythagorean triplet is the one we're looking for
                    if a+b+c == target:

                        # Yay, we've found the answer we're looking for, print it
                        print("{a}^2 + {b}^2 = {c}^2, a + b + c = {s}, abc = {p}".format(a=a, b=b, c=c, s=a+b+c, p=a*b*c))

##find_answer(335, 998, 1000)


# OK, we've found the right answer, but it took ~40 seconds on my
# laptop. That's within the 1 minute goal, so we can stop now, but
# let's play around a bit more to see if we can make it faster.
#
# There is a bunch of fancy mathematics we could use to make this go a
# lot faster, look a the Wikipedia article on Pythagorean triples for
# more details.
#
# But we're trying to learn programming not math, so we're going to
# stick with this simpler approach and see if we can make it faster.
#
# Can you think of any ways to make this code faster?
#
# I can think of one. Since a + b + c = 1000, once we've got b + c
# there is only one possibility for a. Our code currently loops
# through a large number of possibilities, but if there is only one it
# will go a lot faster.

def find_answer_version2(cmin, cmax, target):
    for c in range(cmin, cmax):
        for b in range(2, c):
            a = target - b - c
            if a > b:
                continue
            if (a**2 + b**2) == c**2:
                print("{a}^2 + {b}^2 = {c}^2, a + b + c = {s}, abc = {p}".format(a=a, b=b, c=c, s=a+b+c, p=a*b*c))

##find_answer_version2(335, 998, 1000)


# Almost there...
#
# Our code is MUCH faster, but we're generating 2 answers because
# we've got a negative value of a. This is actually a valid answer
# given the problem statement, but I think we're looking for positive
# values only. Let's enhance our code a little to eliminate negative
# values of a.

def find_answer_version3(cmin, cmax, target):
    for c in range(cmin, cmax):
        for b in range(2, c):
            a = target - b - c
            if a > b or a < 1:
                continue
            if (a**2 + b**2) == c**2:
                print("{a}^2 + {b}^2 = {c}^2, a + b + c = {s}, abc = {p}".format(a=a, b=b, c=c, s=a+b+c, p=a*b*c))

find_answer_version3(335, 998, 1000)
