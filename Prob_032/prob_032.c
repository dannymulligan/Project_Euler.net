// Project Euler.net Problem 32
//
// We shall say that an n-digit number is pandigital if it makes use of all the digits
// 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
// 
// The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
// multiplier, and product is 1 through 9 pandigital.
// 
// Find the sum of all products whose multiplicand/multiplier/product identity can be
// written as a 1 through 9 pandigital.
//
// HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
// 
//
// $Revision

#include <stdio.h>

// We are looking for A x B = C
// The most digits A or B can have are is 4, because C will then have 4 digits, leading to 9 overall

int main()
{
    int x, y;
    int a[6], b[6], c[6];
    int dig[10];
    int len;
    int t0, i;
    int answer = 0;
    // Test all the possibilities
    for (x = 1; x < 9999; x++) {
        for (y = 1; y < x; y++) {
            len = 0;

            a[0] = x;
            if ((a[0] >= 1       ) && (a[0] < 10       ))  len += 1;
            if ((a[0] >= 10      ) && (a[0] < 100      ))  len += 2;
            if ((a[0] >= 100     ) && (a[0] < 1000     ))  len += 3;
            if ((a[0] >= 1000    ) && (a[0] < 10000    ))  len += 4;
            if ((a[0] >= 10000   ) && (a[0] < 100000   ))  len += 5;

            b[0] = y;
            if ((b[0] >= 1       ) && (b[0] < 10       ))  len += 1;
            if ((b[0] >= 10      ) && (b[0] < 100      ))  len += 2;
            if ((b[0] >= 100     ) && (b[0] < 1000     ))  len += 3;
            if ((b[0] >= 1000    ) && (b[0] < 10000    ))  len += 4;
            if ((b[0] >= 10000   ) && (b[0] < 100000   ))  len += 5;

            c[0] = x * y;
            if ((c[0] >= 1       ) && (c[0] < 10       ))  len += 1;
            if ((c[0] >= 10      ) && (c[0] < 100      ))  len += 2;
            if ((c[0] >= 100     ) && (c[0] < 1000     ))  len += 3;
            if ((c[0] >= 1000    ) && (c[0] < 10000    ))  len += 4;
            if ((c[0] >= 10000   ) && (c[0] < 100000   ))  len += 5;

            if (len == 9) {
                t0 = a[0];
                a[1] = t0 % 10;  t0 -= a[1];  t0 = t0 / 10;
                a[2] = t0 % 10;  t0 -= a[2];  t0 = t0 / 10;
                a[3] = t0 % 10;  t0 -= a[3];  t0 = t0 / 10;
                a[4] = t0 % 10;  t0 -= a[4];  t0 = t0 / 10;
                a[5] = t0 % 10;  t0 -= a[5];  t0 = t0 / 10;

                t0 = b[0];
                b[1] = t0 % 10;  t0 -= b[1];  t0 = t0 / 10;
                b[2] = t0 % 10;  t0 -= b[2];  t0 = t0 / 10;
                b[3] = t0 % 10;  t0 -= b[3];  t0 = t0 / 10;
                b[4] = t0 % 10;  t0 -= b[4];  t0 = t0 / 10;
                b[5] = t0 % 10;  t0 -= b[5];  t0 = t0 / 10;

                t0 = c[0];
                c[1] = t0 % 10;  t0 -= c[1];  t0 = t0 / 10;
                c[2] = t0 % 10;  t0 -= c[2];  t0 = t0 / 10;
                c[3] = t0 % 10;  t0 -= c[3];  t0 = t0 / 10;
                c[4] = t0 % 10;  t0 -= c[4];  t0 = t0 / 10;
                c[5] = t0 % 10;  t0 -= c[5];  t0 = t0 / 10;

                for (i = 0; i < 10; i++) {
                    dig[i] = 0;
                }
                dig[a[1]]++; dig[a[2]]++; dig[a[3]]++; dig[a[4]]++; dig[a[5]]++;
                dig[b[1]]++; dig[b[2]]++; dig[b[3]]++; dig[b[4]]++; dig[b[5]]++;
                dig[c[1]]++; dig[c[2]]++; dig[c[3]]++; dig[c[4]]++; dig[c[5]]++;

                if ((dig[1] == 1) && (dig[2] == 1) && (dig[3] == 1) &&
                    (dig[4] == 1) && (dig[5] == 1) && (dig[6] == 1) &&
                    (dig[7] == 1) && (dig[8] == 1) && (dig[9] == 1)) {
                    answer += x*y;
                    printf("Found x=%d, y=%d, x*y=%d\n", x, y, x*y);
                }
            }
        }
    }


    // Report answer
    printf("// Report answer\n");
    printf("The answer is %d\n", answer);
}
