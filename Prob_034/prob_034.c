// Project Euler.net Problem 34
//
// 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
//
// Find the sum of all numbers which are equal to the sum of the factorial of their digits.
//
// Note: as 1! = 1 and 2! = 2 are not sums they are not included.
//
// $Revision

#include <stdio.h>


// The biggest value of a single digit is 9, and 9! = 362,880.
// So an N digit number can must have a value less than or equal to (362,880 x N).
// This means that the maximum number of digits in a number that satisifies the above
// requirement is 7, with a maximum value of 2,540,160

int main()
{
    int i, j;
    int num, sum;
    int answer = 0;
    int d0, d1, d2, d3, d4, d5, d6, d7;
    int f0, f1, f2, f3, f4, f5, f6, f7;

    // Iterate through all possibilities
    printf("// Iterate through all the possibilities\n");
    for (i = 10; i <= 2540160; i++) {
        // Separate out the digits
        num = i;
        d0 = num % 10;  num -= d0;  num = num / 10;
        d1 = num % 10;  num -= d1;  num = num / 10;
        d2 = num % 10;  num -= d2;  num = num / 10;
        d3 = num % 10;  num -= d3;  num = num / 10;
        d4 = num % 10;  num -= d4;  num = num / 10;
        d5 = num % 10;  num -= d5;  num = num / 10;
        d6 = num % 10;  num -= d6;  num = num / 10;
        d7 = num % 10;  num -= d7;  num = num / 10;

        // Calculate factorials
        f0 = 1;  for (j = 1; j <= d0; j++)  f0 = f0 * j;  if ((d0+d1+d2+d3+d4+d5+d6+d7) == 0)  f0 = 0;
        f1 = 1;  for (j = 1; j <= d1; j++)  f1 = f1 * j;  if ((   d1+d2+d3+d4+d5+d6+d7) == 0)  f1 = 0;
        f2 = 1;  for (j = 1; j <= d2; j++)  f2 = f2 * j;  if ((      d2+d3+d4+d5+d6+d7) == 0)  f2 = 0;
        f3 = 1;  for (j = 1; j <= d3; j++)  f3 = f3 * j;  if ((         d3+d4+d5+d6+d7) == 0)  f3 = 0;
        f4 = 1;  for (j = 1; j <= d4; j++)  f4 = f4 * j;  if ((            d4+d5+d6+d7) == 0)  f4 = 0;
        f5 = 1;  for (j = 1; j <= d5; j++)  f5 = f5 * j;  if ((               d5+d6+d7) == 0)  f5 = 0;
        f6 = 1;  for (j = 1; j <= d6; j++)  f6 = f6 * j;  if ((                  d6+d7) == 0)  f6 = 0;
        f7 = 1;  for (j = 1; j <= d7; j++)  f7 = f7 * j;  if ((                     d7) == 0)  f7 = 0;

        // Check for a match
        sum = f0 + f1 + f2 + f3 + f4 + f5 + f6 + f7;
        if (sum == i) {
            printf("%d works\n", i);
            answer += i;
        }

        float diff;
        if (sum > i)  diff = 1.0* (sum - i)/i;
        else          diff = 1.0* (i - sum)/sum;


        if (diff < 0.0001) {
            printf("almost %10.8f ", diff);
            printf("d7=%d d6=%d d5=%d d4=%d d3=%d d2=%d d1=%d d0=%d  num=%d sum=%-6d  ", d7, d6, d5, d4, d3, d2, d1, d0, i, sum);
            printf("f7=%d f6=%d f5=%d f4=%d f3=%d f2=%d f1=%d f0=%d sum=%d\n", f7, f6, f5, f4, f3, f2, f1, f0, sum);
        }
    }

    // Report answer
    printf("// Report answer\n");
    printf("The answer is %d\n", answer);
}
