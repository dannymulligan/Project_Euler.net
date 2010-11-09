// Project Euler.net Problem 46
//
// It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
// 
//      9 =  7 + 2 × 1^2
//     15 =  7 + 2 × 2^2
//     21 =  3 + 2 × 3^2
//     25 =  7 + 2 × 3^2
//     27 = 19 + 2 × 2^2
//     33 = 31 + 2 × 1^2
// 
// It turns out that the conjecture was false.
// 
// What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
//
// 5/18/09 - Searched up to 6.25M and haven't found one.
// 5/21/09 - Searched up to 900M and haven't found one.
// 
// $Revision

#include <stdio.h>

#define MAXP 10000
#define SQRT_MAXP 100
//#define MAXP 7840000  // Biggest I can do when declaring char prime[MAXP] inside main
//#define SQRT_MAXP 2800
//#define MAXP 1024000000
//#define SQRT_MAXP 32000

char prime[MAXP];

int main()
{
    int i, j, k;
    int p_cnt = 0;
    int found;

    // Initialize the array to all prime
    printf("// Initialize the array to all prime\n");
    prime[0] = 0;
    prime[1] = 0;
    for (i = 2; i < MAXP; i++) {
        prime[i] = 1;
    }

    // Calculate the primes
    printf("// Calculate the primes\n");
    for (i = 2; i < SQRT_MAXP; i++) {
        if (prime[i]) {
            p_cnt++;
            for (j = i*i; j < MAXP; j += i) {
                prime[j] = 0;
            }
        }
    }
    printf("%d primes found in the range 1 .. %d\n", p_cnt, SQRT_MAXP-1);
    p_cnt = 0;
    for (i = 1; i < MAXP; i++) {
        if (prime[i])  p_cnt++;
    }
    printf("%d primes found in the range 1 .. %d\n", p_cnt, MAXP-1);

    // Search for the answer
    printf("// Search for the answer\n");
    for (i = 3; i < MAXP; i = i + 2) {
        if (!prime[i]) {
            found = 0;
            for (j = 1; j < SQRT_MAXP; j++) {
                k = i - 2*j*j;
                if ((k > 0) && prime[k]) {
                    found = 1;
                    printf("%d = %d + 2 * %d^2\n", i, k, j);
                    if ((k + 2*j*j) != i)  printf("Error!!!\n");
                    j = SQRT_MAXP;
                }
            }
            if (!found) {
                printf("No solution found for %d\n", i);
                return(0);
            }
        }
    }

    // Report answer
    printf("// Report answer\n");

}
