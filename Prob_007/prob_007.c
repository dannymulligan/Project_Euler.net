// Project Euler.net Problem 7
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//
// What is the 10,001st prime number?
//
// $Revision

#include <stdio.h>

#define MAX 200000
#define SQRT_MAX 500
#define CNT 10001

int main()
{
    int i, j;
    char tab[MAX];
    printf("sizeof(tab[MAX]) = %d\n", sizeof(tab[MAX]));
    printf("sizeof(tab) = %d\n", sizeof(tab));


    // Initialize the array to all prime
    printf("// Initialize the array to all prime\n");
    for (i = 1; i < MAX; i++) {
        tab[i] = 1;
    }
    tab[0] = 0;
    tab[1] = 0;

    // Calculate the primes
    printf("// Calculate the primes\n");
    for (i = 2; i < SQRT_MAX; i++) {
        if (tab[i]) {
            printf("%d is a prime.\n", i);
            for (j = i*i; j < MAX; j += i) {
                  tab[j] = 0;
            }
        }
    }

    // Count up to the answer
    printf("// Count up to the answer\n");
    int answer;
    i = 2;
    j = 0;
    do {
        j += tab[i];
        i++;
    } while ((j < CNT) && (i < MAX));
    i--;

    // Report answer
    printf("// Report answer\n");
    if (j == CNT)
        printf("The %dth prime is %d.\n", j, i);
    else 
      printf("The %dth prime was not found (only got up to the %dth).\n", CNT, j);
}
