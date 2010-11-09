// Project Euler.net Problem 97
//
// The first known prime found to exceed one million digits was
// discovered in 1999, and is a Mersenne prime of the form 2^(6972593)-1;
// it contains exactly 2,098,960 digits. Subsequently other Mersenne
// primes, of the form 2^(p)-1, have been found which contain more
// digits.
// 
// However, in 2004 there was found a massive non-Mersenne prime which
// contains 2,357,207 digits: 28433×2^(7830457)+1.
// 
// Find the last ten digits of this prime number.
// 
// $Revision

#include <stdio.h>

#define PRECISION 10
#define LIMIT 1000

//   28,433 x 2^7,830,457 + 1
// = 28,433 x 2 x 2^7,830,456 + 1
// = 56,866 x 2^7,830,456 + 1
// = 56,866 x (2^8)^978,807 + 1
// = 56,866 x 256^978,807 + 1
// = 56,866 x 256 x 256^978,806 + 1
// = 14,557,696 x 256^978,806 + 1
// = 14,557,696 x (256^2)^489,403 + 1
// = 14,557,696 x 65,536^489,403 + 1

int main()
{

    // Our answer has ~2.3 million digits
    // We're going to store 3 decimal digits per integer
    // We're going to track the bottom 30 digits, so we need an array of 10 integers
    long d[PRECISION];
    int i, p;

    // Initialize the table with 28,433
    printf("// Initialize the table with 28,433\n");
    for (p=0; p<PRECISION; p++) {
        d[p] = 0;
    }
    d[1] =  28;
    d[0] = 433;

    for (p=PRECISION-1; p>=0; p--) {
        printf("%03d ", d[p]);
    }
    printf("\n");

    // Multiply by 2 7,830,457 times
    printf("// Multiply by 2 7,830,457 times\n");
    for (i=0; i<7830457; i++) {
         // Do the multiply
        for (p=0; p<PRECISION; p++) {
            d[p] = d[p] * 2;
        }

        // Fix up the array of integers
        long temp;
        for (p=0; p<PRECISION-1; p++) {
            if (d[p] >= LIMIT) {
                temp = d[p] / LIMIT;
                d[p] = d[p] - temp * LIMIT;
                d[p+1] = d[p+1] + temp;
            }
        }
        d[PRECISION-1] = d[PRECISION-1] % LIMIT;
    }


    // Add 1
    printf("// Add 1\n");
    d[0] = d[0] + 1;
    // Fix up the array of integers
    long temp;
    for (p=0; p<PRECISION; p++) {
        if (d[p] > LIMIT) {
            temp = d[p] / LIMIT;
            d[p] = d[p] - temp * LIMIT;
            d[p+1] = d[p+1] + temp;
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    for (p=PRECISION-1; p>=0; p--) {
        printf("%03d ", d[p]);
    }
    printf("\n");

}
