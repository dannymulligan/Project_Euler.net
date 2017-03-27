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

#include <iostream>

const int CNT = 100;

int main()
{
  int sum_sq = 0;
  int sq_sum = 0;
  for (int i = 1; i <= CNT; i++) {
    sum_sq += i * i;  // sum(i^2)
    sq_sum += i;      // sum(i)
  }
  sq_sum = sq_sum * sq_sum;
  int diff = sq_sum - sum_sq;

  printf("Sum of squares of 1 to %d is %d\n", CNT, sum_sq);
  printf("Square of sum of 1 to %d is %d\n", CNT, sq_sum);
  printf("Difference is %d\n", diff);
}
