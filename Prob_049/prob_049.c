// Project Euler.net Problem 49
//
// The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
// by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii)
// each of the 4-digit numbers are permutations of one another.
//
// There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
// exhibiting this property, but there is one other 4-digit increasing sequence.
//
// What 12-digit number do you form by concatenating the three terms in this sequence?
//
// $Revision

#include <stdio.h>

#define MAXP 10000
#define SQRT_MAXP 100

char prime[MAXP];


int main()
{
    int i, j, k, x;
    int p_cnt = 0;
    int tmp;
    int fnd0, fnd1;
    int perm[24];
    char a, b, c, d;

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

    // Test all the possibilities
    printf("// Test all the possibilities\n");
    for (i = 1000; i < MAXP; i++) {
        if (prime[i])  {
            // Look for the 2nd prime
            for (j=i+1; j<(MAXP+i)/2; j++) {
                if (prime[j]) {
                    if (prime[2*j-i]) {
                        // Extract the digits
                        tmp = i;
                        a = tmp % 10;  tmp -= a;  tmp = tmp / 10;
                        b = tmp % 10;  tmp -= b;  tmp = tmp / 10;
                        c = tmp % 10;  tmp -= c;  tmp = tmp / 10;
                        d = tmp % 10;  tmp -= d;  tmp = tmp / 10;

                        // Generate all the possible combinations
                        perm[ 0] = a*1000 + b*100 + c*10 + d;  // Test ABCD
                        perm[ 1] = a*1000 + b*100 + d*10 + c;  // Test ABDC
                        perm[ 2] = a*1000 + c*100 + b*10 + d;  // Test ACBD
                        perm[ 3] = a*1000 + c*100 + d*10 + b;  // Test ACDB
                        perm[ 4] = a*1000 + d*100 + b*10 + c;  // Test ADBC
                        perm[ 5] = a*1000 + d*100 + c*10 + b;  // Test ADCB

                        perm[ 6] = b*1000 + a*100 + c*10 + d;  // Test BACD
                        perm[ 7] = b*1000 + a*100 + d*10 + c;  // Test BADC
                        perm[ 8] = b*1000 + c*100 + a*10 + d;  // Test BCAD
                        perm[ 9] = b*1000 + c*100 + d*10 + a;  // Test BCDA
                        perm[10] = b*1000 + d*100 + a*10 + c;  // Test BDAC
                        perm[11] = b*1000 + d*100 + c*10 + a;  // Test BDCA

                        perm[12] = c*1000 + a*100 + b*10 + c;  // Test CABC
                        perm[13] = c*1000 + a*100 + c*10 + b;  // Test CACB
                        perm[14] = c*1000 + b*100 + a*10 + d;  // Test CBAD
                        perm[15] = c*1000 + b*100 + d*10 + a;  // Test CBDA
                        perm[16] = c*1000 + d*100 + a*10 + b;  // Test CDAB
                        perm[17] = c*1000 + d*100 + b*10 + a;  // Test CDBA

                        perm[18] = d*1000 + a*100 + b*10 + c;  // Test DABC
                        perm[19] = d*1000 + a*100 + c*10 + b;  // Test DACB
                        perm[20] = d*1000 + b*100 + a*10 + c;  // Test DBAC
                        perm[21] = d*1000 + b*100 + c*10 + a;  // Test DBCA
                        perm[22] = d*1000 + c*100 + a*10 + b;  // Test DCAB
                        perm[23] = d*1000 + c*100 + b*10 + a;  // Test DCBA

                        // Check that the 2nd prime is a combination
                        fnd0 = 0;
                        for (k=1; k<24; k++) {
                            if (j == perm[k])  fnd0 = 1;
                        }

                        // Check that the 2nd prime is a combination
                        fnd1 = 0;
                        for (k=1; k<24; k++) {
                            if (2*j-i == perm[k])  fnd1 = 1;
                        }

                        // If all 3 are combinations, report result
                        if (fnd0 && fnd1)
                            printf("%d %d %d (diff = %d)\n", i, j, 2*j-i, j-i);
                    }
                }
            }
        }
    }

    // Report answer
    printf("// Report answer\n");

}
