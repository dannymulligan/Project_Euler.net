// Project Euler.net Problem 21
//
// Let d(n) be defined as the sum of proper divisors of n (numbers less
// than n which divide evenly into n).  If d(a) = b and d(b) = a, where
// a != b, then a and b are an amicable pair and each of a and b are
// called amicable numbers.
//
// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
// 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
// 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
//
// Evaluate the sum of all the amicable numbers under 10000.
//
// $Revision

#include <stdio.h>

#define MAX 10000

int main()
{
    int i, j;
    int tab[MAX];  // Table of number of divisors


    // Initialize the table of divisors
    printf("// Initialize the table of divisors\n");
    for (i = 1; i < MAX; i++) {
        tab[i] = 0;
    }

    // Calculate the table of divisors
    printf("// Calculate the table of divisors\n");
    for (i = 1; i < MAX; i++) {
        for (j = 1; j < (1 + i/2) ; j++) {
            if ((i % j) == 0) {
                tab[i] += j;
                //                if (j == 1)  printf("d(%d) = %d", i, j);
                //                else         printf(" + %d", j);
            }
        }
        //        printf(" = %d\n", tab[i]);
    }

    // Find the amicable numbers
    printf("// Find the anicable numbers\n");
    int answer = 0;
    for (i = 2; i < MAX; i++) {
      if ((tab[i] < MAX) && (tab[i] != i) && (tab[tab[i]] == i)) {
            printf("d(%d) = %d, d(%d) = %d, \n", i, tab[i], tab[i], tab[tab[i]]);
            answer += i;
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("The answer is %d\n", answer);
}
