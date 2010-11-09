// Project Euler.net Problem 36
//
// The decimal number, 585 = 1001001001(binary), is palindromic in both bases.
//
// Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
//
// (Please note that the palindromic number, in either base, may not include leading zeros.)
//
// $Revision

#include <stdio.h>



int main()
{
    int i, j;
    int num;
    int b_digits, d_digits;
    int b_palin, d_palin;
    int answer = 0;
    int d[7];
    int b[20];

    // Iterate through all possibilities
    printf("// Iterate through all the possibilities\n");
    for (i = 1; i < 1000000; i++) {
        // Separate out the digits - decimal
        d_digits = 0;
        num = i;
        d[0] = num % 10;  num -= d[0];  num = num / 10;  if (d[0] != 0)  d_digits = 1;
        d[1] = num % 10;  num -= d[1];  num = num / 10;  if (d[1] != 0)  d_digits = 2;
        d[2] = num % 10;  num -= d[2];  num = num / 10;  if (d[2] != 0)  d_digits = 3;
        d[3] = num % 10;  num -= d[3];  num = num / 10;  if (d[3] != 0)  d_digits = 4;
        d[4] = num % 10;  num -= d[4];  num = num / 10;  if (d[4] != 0)  d_digits = 5;
        d[5] = num % 10;  num -= d[5];  num = num / 10;  if (d[5] != 0)  d_digits = 6;
        d[6] = num % 10;  num -= d[6];  num = num / 10;  if (d[6] != 0)  d_digits = 7;
        // printf("i=%4d, digits = %d %d %d %d %d %d %d, d_digits=%d\n", i, d[6], d[5], d[4], d[3], d[2], d[1], d[0], d_digits);

        // Separate out the digits - binary
        b_digits = 0;
        num = i;
        b[ 0] = num % 2;  num -= b[ 0];  num = num / 2;  if (b[ 0] != 0)  b_digits =  1;
        b[ 1] = num % 2;  num -= b[ 1];  num = num / 2;  if (b[ 1] != 0)  b_digits =  2;
        b[ 2] = num % 2;  num -= b[ 2];  num = num / 2;  if (b[ 2] != 0)  b_digits =  3;
        b[ 3] = num % 2;  num -= b[ 3];  num = num / 2;  if (b[ 3] != 0)  b_digits =  4;
        b[ 4] = num % 2;  num -= b[ 4];  num = num / 2;  if (b[ 4] != 0)  b_digits =  5;
        b[ 5] = num % 2;  num -= b[ 5];  num = num / 2;  if (b[ 5] != 0)  b_digits =  6;
        b[ 6] = num % 2;  num -= b[ 6];  num = num / 2;  if (b[ 6] != 0)  b_digits =  7;
        b[ 7] = num % 2;  num -= b[ 7];  num = num / 2;  if (b[ 7] != 0)  b_digits =  8;
        b[ 8] = num % 2;  num -= b[ 8];  num = num / 2;  if (b[ 8] != 0)  b_digits =  9;
        b[ 9] = num % 2;  num -= b[ 9];  num = num / 2;  if (b[ 9] != 0)  b_digits = 10;

        b[10] = num % 2;  num -= b[10];  num = num / 2;  if (b[10] != 0)  b_digits = 11;
        b[11] = num % 2;  num -= b[11];  num = num / 2;  if (b[11] != 0)  b_digits = 12;
        b[12] = num % 2;  num -= b[12];  num = num / 2;  if (b[12] != 0)  b_digits = 13;
        b[13] = num % 2;  num -= b[13];  num = num / 2;  if (b[13] != 0)  b_digits = 14;
        b[14] = num % 2;  num -= b[14];  num = num / 2;  if (b[14] != 0)  b_digits = 15;
        b[15] = num % 2;  num -= b[15];  num = num / 2;  if (b[15] != 0)  b_digits = 16;
        b[16] = num % 2;  num -= b[16];  num = num / 2;  if (b[16] != 0)  b_digits = 17;
        b[17] = num % 2;  num -= b[17];  num = num / 2;  if (b[17] != 0)  b_digits = 18;
        b[18] = num % 2;  num -= b[18];  num = num / 2;  if (b[18] != 0)  b_digits = 19;
        b[19] = num % 2;  num -= b[19];  num = num / 2;  if (b[19] != 0)  b_digits = 20;
        // printf("i=%4d, digits = %d%d%d%d %d%d%d%d %d%d%d%d %d%d%d%d %d%d%d%d, b_digits=%d\n", i,
        //     b[19], b[18], b[17], b[16], b[15], b[14], b[13], b[12], b[11], b[10],
        //     b[ 9], b[ 8], b[ 7], b[ 6], b[ 5], b[ 4], b[ 3], b[ 2], b[ 1], b[ 0], b_digits);

        // Check for palindrome in decimal
        d_palin = 1;
        for (j=0; j < d_digits/2; j++) {
            d_palin = d_palin && (d[j] == d[d_digits-1-j]);
            // printf("    Compare d[%d]=%d & d[%d]=%d\n", j, d[j], d_digits-1-j, d[d_digits-1-j]);
        }

        // Check for palindrome in binary
        b_palin = 1;
        for (j=0; j < b_digits/2; j++) {
            b_palin = b_palin && (b[j] == b[b_digits-1-j]);
            // printf("    Compare b[%d]=%d & b[%d]=%d\n", j, b[j], b_digits-1-j, b[b_digits-1-j]);
        }

        // if ( d_palin && !b_palin)  printf("%d is a decimal palindrome\n", i);
        // if (!d_palin &&  b_palin)  printf("%d is a binary palindrome\n", i);
        if ( d_palin &&  b_palin)  printf("%d is a decimal & binary palindrome!\n", i);

        if ( d_palin &&  b_palin)  answer += i;
    }

    // Report answer
    printf("// Report answer\n");
    printf("The answer is %d\n", answer);
}
