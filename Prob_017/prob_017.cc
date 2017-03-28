// Project Euler.net Problem 17
//
// If the numbers 1 to 5 are written out in words: one, two, three, four, five,
// then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
//
// If all the numbers from 1 to 1000 (one thousand) inclusive were written out
// in words, how many letters would be used?
//
// NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
// forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
// 20 letters. The use of "and" when writing out numbers is in compliance with
// British usage.

#include <iostream>

const int LIMIT = 1000;

int main()
{
  int n;
  int len, total_len = 0;
  int temp;

  for (int i=1; i<=LIMIT; i++) {
    len = 0;
    n = i;

    // Thousands
    if (n == 1000) {
      printf("one thousand ");
      len += 11;
      n -= 1000;
    }

    // Hundreds
    if (n >= 100) {
      temp = n / 100;
      if (temp == 9)  { printf("nine hundred ");   len += 11;  n -= 900; }
      if (temp == 8)  { printf("eight hundred ");  len += 12;  n -= 800; }
      if (temp == 7)  { printf("seven hundred ");  len += 12;  n -= 700; }
      if (temp == 6)  { printf("six hundred ");    len += 10;  n -= 600; }
      if (temp == 5)  { printf("five hundred ");   len += 11;  n -= 500; }
      if (temp == 4)  { printf("four hundred ");   len += 11;  n -= 400; }
      if (temp == 3)  { printf("three hundred ");  len += 12;  n -= 300; }
      if (temp == 2)  { printf("two hundred ");    len += 10;  n -= 200; }
      if (temp == 1)  { printf("one hundred ");    len += 10;  n -= 100; }
    }

    // And
    if ((i > 100) && (n > 0))  { printf("and ");  len += 3; }

    // Tens
    if (n >= 20) {
      temp = n / 10;
      if (temp == 9)  { printf("ninety ");   len += 6;  n -= 90; }
      if (temp == 8)  { printf("eighty ");   len += 6;  n -= 80; }
      if (temp == 7)  { printf("seventy ");  len += 7;  n -= 70; }
      if (temp == 6)  { printf("sixty ");    len += 5;  n -= 60; }
      if (temp == 5)  { printf("fifty ");    len += 5;  n -= 50; }
      if (temp == 4)  { printf("forty ");    len += 5;  n -= 40; }
      if (temp == 3)  { printf("thirty ");   len += 6;  n -= 30; }
      if (temp == 2)  { printf("twenty ");   len += 6;  n -= 20; }
    }

    // Tens
    if (n > 0) {
      if (n == 19)  { printf("nineteen ");   len += 8; }
      if (n == 18)  { printf("eighteen ");   len += 8; }
      if (n == 17)  { printf("seventeen ");  len += 9; }
      if (n == 16)  { printf("sixteen ");    len += 7; }
      if (n == 15)  { printf("fifteen ");    len += 7; }
      if (n == 14)  { printf("fourteen ");   len += 8; }
      if (n == 13)  { printf("thirteen ");   len += 8; }
      if (n == 12)  { printf("twelve ");     len += 6; }
      if (n == 11)  { printf("eleven ");     len += 6; }
      if (n == 10)  { printf("ten ");        len += 3; }
      if (n ==  9)  { printf("nine ");       len += 4; }
      if (n ==  8)  { printf("eight ");      len += 5; }
      if (n ==  7)  { printf("seven ");      len += 5; }
      if (n ==  6)  { printf("six ");        len += 3; }
      if (n ==  5)  { printf("five ");       len += 4; }
      if (n ==  4)  { printf("four ");       len += 4; }
      if (n ==  3)  { printf("three ");      len += 5; }
      if (n ==  2)  { printf("two ");        len += 3; }
      if (n ==  1)  { printf("one ");        len += 3; }
    }

    printf("(length = %d)\n", len);
    total_len += len;
  }

  // Print the answer
  printf("// Print the answer\n");
  printf("The answer is %d\n", total_len);
}
