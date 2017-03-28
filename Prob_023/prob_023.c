// Project Euler.net Problem 22
//
// A perfect number is a number for which the sum of its proper divisors is exactly
// equal to the number. For example, the sum of the proper divisors of 28 would be
// 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
//
// A number whose proper divisors are less than the number is called deficient and
// a number whose proper divisors exceed the number is called abundant.
//
// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
// number that can be written as the sum of two abundant numbers is 24. By
// mathematical analysis, it can be shown that all integers greater than 28123 can
// be written as the sum of two abundant numbers. However, this upper limit cannot
// be reduced any further by analysis even though it is known that the greatest
// number that cannot be expressed as the sum of two abundant numbers is less than
// this limit.
//
// Find the sum of all the positive integers which cannot be written as the sum of
// two abundant numbers.

#include <stdio.h>

#define MAX 28500
//#define MAX 30

int main()
{
    int i, j;
    int tab[MAX];   // Table of sum of divisors
    int abun[MAX];  // Table of abundant numbers


    // Initialize the table of divisors
    printf("// Initialize the table of divisors\n");
    for (i = 1; i < MAX; i++) {
        tab[i] = 0;
    }

    // Calculate the table of sum of divisors
    printf("// Calculate the table of sum of divisors\n");
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

    // Find the abundant numbers
    printf("// Find the abundant numbers\n");
    for (i = 1; i < MAX; i++) {
        if (tab[i] > i)  abun[i] = 1;
        else             abun[i] = 0;
    }

    // Print the abundant numbers
    printf("// Print the abundant numbers\n");
    for (i = 1; i < MAX; i++) {
        if (abun[i])
          printf("%d is an abundant number, d(%d) = %d, \n", i, i, tab[i]);
    }

    // Find numbers that can't be written as the sum of abundant numbers
    printf("// Find numbers that can't be written as the sum of abundant numbers\n");
    int found;
    int answer = 0;
    for (i = 1; i < MAX; i++) {
        found = 0;
        for (j = 2; j < i; j++) {
            if (abun[j] && abun[i-j])  found = 1;
        }
        if (found == 0) {
            answer += i;
            printf("%d is not a sum of two abundant numbers.\n", i);
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("Answer = %d\n", answer);
}
