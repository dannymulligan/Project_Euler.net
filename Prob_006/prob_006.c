// Project Euler.net Problem 6
//
// The sum of the squares of the first ten natural numbers is,
//
//     1^(2) + 2^(2) + ... + 10^(2) = 385
//
// The square of the sum of the first ten natural numbers is,
// 
//     (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
// 
// Hence the difference between the sum of the squares of the first
// ten natural numbers and the square of the sum is 3025 − 385 = 2640.
// 
// Find the difference between the sum of the squares of the first one
// hundred natural numbers and the square of the sum.
//
//
// $Revision

#include <stdio.h>

#define CNT 100

int main()
{
    int i;

    // Calculate the sum of the squares
    int sum_sq = 0;
    for (i = 1; i <= CNT; i++) {
        sum_sq += i * i;
    }

    // Calculate the square of the sum
    int sq_sum = 0;
    for (i = 1; i <= CNT; i++) {
        sq_sum += i;
    }
    sq_sum = sq_sum * sq_sum;

    // Calculate the difference
    int diff = sq_sum - sum_sq;

    printf("Sum of squares of 1 to %d is %d\n", CNT, sum_sq);
    printf("Square of sum of 1 to %d is %d\n", CNT, sq_sum);
    printf("Difference is %d\n", diff);
}
