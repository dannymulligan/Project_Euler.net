// Project Euler.net Problem 26
//
// A unit fraction contains 1 in the numerator. The decimal representation of the unit
// fractions with denominators 2 to 10 are given:
// 
//     1/2   =  0.5
//     1/3   =  0.(3)
//     1/4   =  0.25
//     1/5   =  0.2
//     1/6   =  0.1(6)
//     1/7   =  0.(142857)
//     1/8   =  0.125
//     1/9   =  0.(1)
//     1/10  =  0.1
// 
// Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen
// that 1/7 has a 6-digit recurring cycle.
// 
// Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its
// decimal fraction part.
//
// $Revision

#include <stdio.h>

#define MAX 1000002

int main()
{
    char dig[MAX];
    int dig_ptr;
    char a[8];  // Max value we can deal with is 99,999,999 (or MAX = 100,000,000
    int i, j;
    int len, t0;

    // Test all the possibilities
    printf("// Test all the possibilities\n");
    dig_ptr = 1;
    i = 1;
    do {
        t0 = i++;
        if ((t0 >= 1       ) && (t0 < 10       ))  len = 0;
        if ((t0 >= 10      ) && (t0 < 100      ))  len = 1;
        if ((t0 >= 100     ) && (t0 < 1000     ))  len = 2;
        if ((t0 >= 1000    ) && (t0 < 10000    ))  len = 3;
        if ((t0 >= 10000   ) && (t0 < 100000   ))  len = 4;
        if ((t0 >= 100000  ) && (t0 < 1000000  ))  len = 5;
        if ((t0 >= 1000000 ) && (t0 < 10000000 ))  len = 6;
        if ((t0 >= 10000000) && (t0 < 100000000))  len = 7;
        if (t0 >= 100000000)  return(1);  // Error condition

        a[0] = t0 % 10;  t0 -= a[0];  t0 = t0 / 10;
        a[1] = t0 % 10;  t0 -= a[1];  t0 = t0 / 10;
        a[2] = t0 % 10;  t0 -= a[2];  t0 = t0 / 10;
        a[3] = t0 % 10;  t0 -= a[3];  t0 = t0 / 10;
        a[4] = t0 % 10;  t0 -= a[4];  t0 = t0 / 10;
        a[5] = t0 % 10;  t0 -= a[5];  t0 = t0 / 10;
        a[6] = t0 % 10;  t0 -= a[6];  t0 = t0 / 10;
        a[7] = t0 % 10;  t0 -= a[7];  t0 = t0 / 10;

        for (j = len; j >= 0; j--) {
            if (dig_ptr < MAX)
                dig[dig_ptr++] = a[j];
        }
    } while ((i < MAX) && (dig_ptr < MAX));

    // Print dig table
    // printf("// Print dig table (%d entries)\n", dig_ptr);
    // for (i = 1; i < MAX; i++) {
    //     if ((i % 40) == 1)  printf("%4d: ", i);
    //     printf("%1d", dig[i]);
    //     if ((i % 40) == 0)  printf("\n");
    // }
    // printf("\n");


    // Report answer
    printf("// Report answer\n");
    printf(      "d(1) = %d\n", dig[      1]);
    printf(     "d(10) = %d\n", dig[     10]);
    printf(    "d(100) = %d\n", dig[    100]);
    printf(   "d(1000) = %d\n", dig[   1000]);
    printf(  "d(10000) = %d\n", dig[  10000]);
    printf( "d(100000) = %d\n", dig[ 100000]);
    printf("d(1000000) = %d\n", dig[1000000]);
    printf("\n");
    printf("d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000) = %d\n", 
           dig[1] * dig[10] * dig[100] * dig[1000] * dig[10000] * dig[100000] * dig[1000000]);

}
