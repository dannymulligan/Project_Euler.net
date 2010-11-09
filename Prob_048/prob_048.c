// Project Euler.net Problem 48
//
// The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
//
// Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
//
// $Revision

#include <stdio.h>

#define LIMIT 1000000
#define PRECISION 500
#define POWER 1000
// 1000^1000 has about 3000 decimal digits
// We're going to store 6 decimal digits per integer
// We need a arrays of about 500 integers


int main()
{

    long tot[PRECISION];
    long d[PRECISION];
    int temp;
    int i, j, p;

    // Initialize the total
    printf("// Initialize the total\n");
    for (p = 0; p < PRECISION; p++) {
        tot[p] = 0;
    }

    for (i = 1; i <= POWER; i++) {
        // Initialize d[]
        for (p = 0; p < PRECISION; p++) {
            d[p] = 0;
        }
        d[0] = 1;

        // Calculate i^i
        for (j = 1; j <= i; j++) {
            // Multiply by i
            for (p = 0; p < PRECISION; p++) {
                d[p] = d[p] * i;
            }

            // Adjust for overflows
            for (p = 0; p < PRECISION-1; p++) {
                if (d[p] >= LIMIT) {
                    temp = d[p] / LIMIT;
                    d[p] = d[p] - temp * LIMIT;
                    d[p+1] = d[p+1] + temp;
                }
            }

            // // Print i^j
            // printf("    %d^%d = ", i, j);
            // for (p = PRECISION-1; p >= 0; p--) {
            //     printf("%06d ", d[p]);
            // }
            // printf("\n");

        }

        // // Print i^i
        // printf("%d^%d = ", i, i);
        // for (p = PRECISION-1; p >= 0; p--) {
        //     printf("%06d ", d[p]);
        // }
        // printf("\n");

        // Add to the total
        for (p = 0; p < PRECISION; p++) {
            tot[p] = tot[p] + d[p];
        }

        // Adjust for overflows
        for (p = 0; p < PRECISION-1; p++) {
            if (tot[p] >= LIMIT) {
                temp = tot[p] / LIMIT;
                tot[p] = tot[p] - temp * LIMIT;
                tot[p+1] = tot[p+1] + temp;
            }
        }

        // // Print the total
        // printf("total = ", i, i);
        // for (p = PRECISION-1; p >= 0; p--) {
        //     printf("%06d ", tot[p]);
        // }
        // printf("\n");
    }

    // Print the answer
    printf("// Print the answer\n");
    for (p = PRECISION-1; p >= 0; p--) {
        printf("%06d ", tot[p]);
    }
    printf("\n");
    printf("The last 12 digits of the answer are %06d %06d\n", tot[1], tot[0]);

}
