// Project Euler.net Problem 27
//
// Euler published the remarkable quadratic formula:
//
//     n^2 + n + 41
//
// It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However,
// when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 +
// 41 + 41 is clearly divisible by 41.
//
// Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes
// for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
//
// Considering quadratics of the form:
//
//     n^2 + an + b, where |a| < 1000 and |b| < 1000
//
//     where |n| is the modulus/absolute value of n
//     e.g. |11| = 11 and |-4| = 4
//
// Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
// number of primes for consecutive values of n, starting with n = 0.
//
//
// $Revision

#include <stdio.h>

#define MAXP 1000000
#define SQRT_MAXP 1000

int main()
{
    int i, j;
    char tab[MAXP];
    int a, b, n;
    int candidate;
    int max_n = 0;

    // Initialize the array to all prime
    printf("// Initialize the array to all prime\n");
    tab[0] = 0;
    tab[1] = 0;
    for (i = 2; i < MAXP; i++) {
        tab[i] = 1;
    }

    // Calculate the primes
    printf("// Calculate the primes\n");
    for (i = 2; i < SQRT_MAXP; i++) {
        if (tab[i]) {
            for (j = i*i; j < MAXP; j += i) {
                tab[j] = 0;
            }
        }
    }

    // Check for each possibility of a & b
    printf("// Check for each possiblity of a & b\n");
    for (a = -999; a < 1000; a++) {
        for (b = -999; b < 1000; b++) {
            n = 0;
            do {
                candidate = n*n + a*n + b;
                n++;
            } while (tab[candidate]);

            if (n > max_n) {
                printf("a = %d, b = %d produces a sequence of %d primes (answer = %d)\n", a, b, n, (a*b));
                max_n = n;
            }
        }
    }

}
