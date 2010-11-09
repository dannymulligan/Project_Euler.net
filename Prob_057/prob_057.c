// Project Euler.net Problem 57
//
// It is possible to show that the square root of two can be expressed
// as an infinite continued fraction.
// 
// sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
// 
// By expanding this for the first four iterations, we get:
// 
// 1 + 1/2 = 3/2 = 1.5
// 1 + 1/(2 + 1/2) = 7/5 = 1.4
// 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
// 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
// 
// The next three expansions are 99/70, 239/169, and 577/408, but the
// eighth expansion, 1393/985, is the first example where the number of
// digits in the numerator exceeds the number of digits in the
// denominator.
// 
// In the first one-thousand expansions, how many fractions contain a
// numerator with more digits than denominator?
// 
// 
// $Revision

#include <stdio.h>

#define MAX 1000
#define PRECISION 130
#define LIMIT 1000

int main()
{
    int num[PRECISION], den[PRECISION];
    int j[PRECISION], k[PRECISION];
    int num_dig, den_dig;
    int n;
    int p, temp;
    int answer = 0;

    // Initialize the numerator & denominator
    for (p=0; p<PRECISION; p++) {
        num[p] = 0;
        den[p] = 0;
    }

    // Calculate expansion #1
    num[0] = 3;
    den[0] = 2;
    n = 1;
    printf("Expansion #%03d = ", n);
    for(p=PRECISION-1; p>=1; p--)  printf("%03d,", num[p]);
    printf("%03d", num[0]);
    printf(" / ");
    for(p=PRECISION-1; p>=1; p--)  printf("%03d,", den[p]);
    printf("%03d", den[0]);
    printf("\n");

    // Calculate the next expansions
    for (n = 2; n <= MAX; n++) {
        // k = num + den;
        for (p=0; p<PRECISION; p++) {
            k[p] = num[p] + den[p];
        }
        for (p=0; p<PRECISION-1; p++) {
            if (k[p] >= LIMIT) {
                temp = k[p] / LIMIT;
                k[p] = k[p] - temp * LIMIT;
                k[p+1] = k[p+1] + temp;
            }
        }

        // j = den + k;
        for (p=0; p<PRECISION; p++) {
            j[p] = den[p] + k[p];
        }
        for (p=0; p<PRECISION-1; p++) {
            if (j[p] >= LIMIT) {
                temp = j[p] / LIMIT;
                j[p] = j[p] - temp * LIMIT;
                j[p+1] = j[p+1] + temp;
            }
        }

        // num = j; den = k;
        for (p=0; p<PRECISION; p++) {
            num[p] = j[p];
            den[p] = k[p];
        }

        // Count the digits
        num_dig = 0;
        den_dig = 0;
        for(p=PRECISION-1; p>=0; p--) {
            if ((num_dig == 0) && (num[p] != 0)) {
                num_dig = p * 3;
                if (num[p] >=   1)  num_dig++;
                if (num[p] >=  10)  num_dig++;
                if (num[p] >= 100)  num_dig++;
            }

            if ((den_dig == 0) && (den[p] != 0)) {
                den_dig = p * 3;
                if (den[p] >=   1)  den_dig++;
                if (den[p] >=  10)  den_dig++;
                if (den[p] >= 100)  den_dig++;
            }
        }

        // Calculate the answer
        if (num_dig > den_dig)  answer++;

        // Print the expansion
        printf("Expansion #%03d = %d digits / %d digits = ", n, num_dig, den_dig);
        for(p=PRECISION-1; p>=1; p--)  printf("%03d,", num[p]);
        printf("%03d", num[0]);
        printf(" / ");
        for(p=PRECISION-1; p>=1; p--)  printf("%03d,", den[p]);
        printf("%03d", den[0]);
        printf("\n");

    }

    // Report answer
    printf("// Report answer\n");
    printf("The answer is %d\n", answer);

}
