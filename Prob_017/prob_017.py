#!/usr/bin/python
#
# Project Euler.net Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.


LIMIT = 1000

total_len = 0

for i in range(1, LIMIT+1):
    len = 0
    n = i

    # Thousands
    if (n >= 1000):
        print("one thousand"),
        len += 11
        n -= 1000

    # Hundreds
    if (n >= 100):
        temp = n / 100
        if (temp == 9):  print("nine hundred" ),;  len += 11;  n -= 900;
        if (temp == 8):  print("eight hundred"),;  len += 12;  n -= 800;
        if (temp == 7):  print("seven hundred"),;  len += 12;  n -= 700;
        if (temp == 6):  print("six hundred"  ),;  len += 10;  n -= 600;
        if (temp == 5):  print("five hundred" ),;  len += 11;  n -= 500;
        if (temp == 4):  print("four hundred" ),;  len += 11;  n -= 400;
        if (temp == 3):  print("three hundred"),;  len += 12;  n -= 300;
        if (temp == 2):  print("two hundred"  ),;  len += 10;  n -= 200;
        if (temp == 1):  print("one hundred"  ),;  len += 10;  n -= 100;

    # And
    if ((i > 100) and (n > 0)):  print("and"),;  len += 3;

    # Tens
    if (n >= 20):
        temp = n / 10
        if (temp == 9):  print("ninety" ),;  len += 6;  n -= 90;
        if (temp == 8):  print("eighty" ),;  len += 6;  n -= 80;
        if (temp == 7):  print("seventy"),;  len += 7;  n -= 70;
        if (temp == 6):  print("sixty"  ),;  len += 5;  n -= 60;
        if (temp == 5):  print("fifty"  ),;  len += 5;  n -= 50;
        if (temp == 4):  print("forty"  ),;  len += 5;  n -= 40;
        if (temp == 3):  print("thirty" ),;  len += 6;  n -= 30;
        if (temp == 2):  print("twenty" ),;  len += 6;  n -= 20;

    # Tens
    if (n > 0):
        if (n == 19):  print("nineteen" ),;  len += 8;
        if (n == 18):  print("eighteen" ),;  len += 8;
        if (n == 17):  print("seventeen"),;  len += 9;
        if (n == 16):  print("sixteen"  ),;  len += 7;
        if (n == 15):  print("fifteen"  ),;  len += 7;
        if (n == 14):  print("fourteen" ),;  len += 8;
        if (n == 13):  print("thirteen" ),;  len += 8;
        if (n == 12):  print("twelve"   ),;  len += 6;
        if (n == 11):  print("eleven"   ),;  len += 6;
        if (n == 10):  print("ten"      ),;  len += 3;
        if (n ==  9):  print("nine"     ),;  len += 4;
        if (n ==  8):  print("eight"    ),;  len += 5;
        if (n ==  7):  print("seven"    ),;  len += 5;
        if (n ==  6):  print("six"      ),;  len += 3;
        if (n ==  5):  print("five"     ),;  len += 4;
        if (n ==  4):  print("four"     ),;  len += 4;
        if (n ==  3):  print("three"    ),;  len += 5;
        if (n ==  2):  print("two"      ),;  len += 3;
        if (n ==  1):  print("one"      ),;  len += 3;

    print("(length = {})".format(len))
    total_len += len

# Print the answer
print("The answer is {}".format(total_len))
