// Project Euler.net Problem 14
//
// The following iterative sequence is defined for the set of positive integers:
// 
//     n -> n/2 (n is even)
//     n -> 3n + 1 (n is odd)
// 
// Using the rule above and starting with 13, we generate the following sequence:
//
//     13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
// 
// It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
// Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
// 
// Which starting number, under one million, produces the longest chain?
// 
// NOTE: Once the chain starts the terms are allowed to go above one million.
// 
// $Revision

#include <stdio.h>

#define LIMIT 1000000

int main()
{

    // Set up the number in an array
    long long n;
    int len, max_len = 0, max_n = 0;
    int i;

    // Try every starting value
    for (i=2; i<LIMIT; i++) {
        n = i;
        len = 1;

        //        printf("Trying %d\n", n);
        do {
          //            printf("    term %d is %d\n", len, n);

            if (n & 0x0001)  n = 3 * n + 1;
            else             n = n / 2;

            if (n < 0) {
                printf("Overflow: n = %d, len=%d\n", i, len);
                exit(1);
            }

            len++;

        } while (n != 1);

        if (len > max_len) {
            max_len = len;
            max_n = i;
            printf("Sequence starting with %d has %d terms", i, len);
            printf("(maximum length was %d from starting with %d)\n", max_len, max_n);
        }

    }

}
