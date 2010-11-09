// Project Euler.net Problem 58
//
// Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
//
//     [37]  36   35   34   33   32  [31]
//      38  [17]  16   15   14  [13]  30
//      39   18   [5]   4   [3]  12   29
//      40   19    6    1    2   11   28
//      41   20   [7]   8    9   10   27
//      42   21   22   23   24   25   26
//     [43]  44   45   46   47   48   49
//
// It is interesting to note that the odd squares lie along the bottom
// right diagonal, but what is more interesting is that 8 out of the 13
// numbers lying along both diagonals are prime; that is, a ratio of 8/13
// ~= 62%.
//
// If one complete new layer is wrapped around the spiral above, a
// square spiral with side length 9 will be formed. If this process is
// continued, what is the side length of the square spiral for which the
// ratio of primes along both diagonals first falls below 10%?
//
// $Revision

#include <stdio.h>

#define MAXP 900000000
#define SQRT_MAXP 30000
#define SIZE 29999

char prime[MAXP];


int main()
{
    int x, y;
    int p_cnt = 0;
    int i, j;
    int answer = 0;

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
    printf("%d primes found in the range 1...%d\n", p_cnt, SQRT_MAXP-1);
    p_cnt = 0;
    for (i = 1; i < MAXP; i++) {
        if (prime[i])  p_cnt++;
    }
    printf("%d primes found in the range 1...%d\n", p_cnt, MAXP-1);

    // Walk the spiral counting primes
    int n = 1;
    int n_cnt = 1;
    int f_cnt = 0;
    // Count primes on the spiral
    printf("// Count primes on the spiral\n");
    for (i=1; i<(SIZE-1)/2; i++) {

        // Right edge
        n += 2*i;  n_cnt++;
        if (prime[n])  f_cnt++;
        // printf("(%d, ", n);

        // Top edge
        n += 2*i;  n_cnt++;
        if (prime[n])  f_cnt++;
        // printf("%d, ", n);

        // Left edge
        n += 2*i;  n_cnt++;
        if (prime[n])  f_cnt++;
        // printf("%d, ", n);

        // Bottom edge
        n += 2*i;  n_cnt++;
        if (prime[n])  f_cnt++;
        // printf("%d) ", n);

        // printf("The spiral that is %d on a side has %d out of %d primes on its diagonals", (1+2*i), f_cnt, n_cnt);
        // if ((f_cnt * 10) > n_cnt)  printf(" >10%%");
        // printf(" (%4.1f%%)\n", (double)100*f_cnt/n_cnt);

        if ((answer == 0) && ((f_cnt * 10) <= n_cnt))  answer = (1+2*i);
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("Then answer is %d\n", answer);

}
