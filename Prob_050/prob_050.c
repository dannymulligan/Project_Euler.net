// Project Euler.net Problem 50
//
// The prime 41, can be written as the sum of six consecutive primes:
//     41 = 2 + 3 + 5 + 7 + 11 + 13
//
// This is the longest sum of consecutive primes that adds to a prime below one-hundred.
//
// The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
//
// Which prime, below one-million, can be written as the sum of the most consecutive primes?
//
// $Revision

#include <stdio.h>

#define MAXP 1000000    // Maximum number we check up to looking for primes
#define SQRT_MAXP 1000  // Square root of MAXP
//#define MAXP 1000
//#define SQRT_MAXP 35
//#define MAXP 100
//#define SQRT_MAXP 10

#define MAXL 550

int main()
{
    int i, j, k;
    char primes_tab[MAXP];

    // Initialize the array to all prime
    printf("// Initialize the array to all prime\n");
    primes_tab[0] = 0;
    primes_tab[1] = 0;
    for (i = 2; i < MAXP; i++) {
        primes_tab[i] = 1;
    }

    // Calculate the primes
    printf("// Calculate the primes\n");
    for (i = 2; i < SQRT_MAXP; i++) {
        if (primes_tab[i]) {
            for (j = i*i; j < MAXP; j += i) {
                primes_tab[j] = 0;
            }
        }
    }

    // Move the primes to a different format table
    printf("// Move the primes to a different format table\n");
    int primes_list[MAXP/4];  // Just by accounting for multiples of 2, 3, & 5, at most 8 out of 30 numbers are prime < 25%
    int prime_cnt = 0;
    for (i = 0; i < MAXP; i++) {
        if (primes_tab[i]) {
            primes_list[prime_cnt++] = i;
        }
    }

/*     // Print out the primes */
/*     printf("%d primes found: ", prime_cnt); */
/*     for (i = 0; i < prime_cnt; i++) */
/*         printf("%d ", primes_list[i]); */
/*     printf("\n"); */

    // Test different length sequences of primes
    int len;
    int candidates[MAXL];
    printf("// Test different length sequences of primes\n");
    for (len = 500; len < MAXL; len++) {  // len = length of consecutive primes we're looking for

        printf("Looking for a sequence of length %d\n", len);

        // Initialize the candidate array
        j = 0;
        for (i = (len-1); i >= 0; i--) {
            j = j + primes_list[i];
            candidates[i] = j;
        }

        // Test sequences
        for (i = len; i < prime_cnt; i++) {
            // Test the current candidate
          if ((candidates[0] < MAXP) && (primes_tab[candidates[0]]))
                printf("%d is prime and the sum of %d primes ending in %d\n", candidates[0], len, primes_list[(i-1)]);

            // Shift the candidates down
            for (j=0; j<len; j++)
                candidates[j] = candidates[j+1];
            candidates[(len-1)] = 0;

            // Add the latest prime
            for (j=0; j<len; j++)
                candidates[j] += primes_list[i];

/*             // Print the table */
/*             printf("Candidates: "); */
/*             for (j=0; j<len; j++) */
/*                 printf("%d ", candidates[j]); */
/*             printf("\n"); */
        }

    }


}
