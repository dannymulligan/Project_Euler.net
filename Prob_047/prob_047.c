// Project Euler.net Problem 47
//
// The first two consecutive numbers to have two distinct prime factors are:
// 
//     14 = 2 × 7
//     15 = 3 × 5
// 
// The first three consecutive numbers to have three distinct prime factors are:
// 
//     644 = 2^2 × 7 × 23
//     645 = 3 × 5 × 43
//     646 = 2 × 17 × 19.
// 
// Find the first four consecutive integers to have four distinct primes factors.
// What is the first of these numbers?
// 
// $Revision

#include <stdio.h>

#define MAX 1000000
#define SQRT_MAX 32

int main()
{
    int i, j;

    // // Initialize the array to all prime
    // char prime[MAX];
    // printf("// Initialize the array to all prime\n");
    // prime[0] = 0;
    // prime[1] = 0;
    // for (i = 2; i < MAX; i++) {
    //     prime[i] = 1;
    // }
    // 
    // // Calculate the primes
    // printf("// Calculate the primes\n");
    // for (i = 2; i < SQRT_MAX; i++) {
    //     if (prime[i]) {
    //         for (j = i*i; j < MAX; j += i) {
    //             prime[j] = 0;
    //         }
    //     }
    // }

    // Count factors
    int temp;
    int factor_cnt;
    int factor_fnd = 0;
    for (i = 2; i < MAX; i++) {
        factor_cnt = 0;
        temp = i;
        j = 2;
        do {
            if ((temp % j) == 0) {
                factor_cnt++;
                do {
                    temp = temp / j;
                } while ((temp % j) == 0);
            }
            j++;
        } while (temp != 1);

        if (factor_cnt == 4)  factor_fnd++;
        else                  factor_fnd = 0;

        //printf("%d has %d factors (%d found with 4 factors)\n", i, factor_cnt, factor_fnd);

        if (factor_fnd == 4) {
            printf("%d has %d factors (%d found with 4 factors)\n", i, factor_cnt, factor_fnd);
            return (0);
        }
    }

    // Report answer
    printf("// Report answer\n");

}
