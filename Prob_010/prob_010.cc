// Project Euler.net Problem 10
//
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// 
// Find the sum of all the primes below two million.

#include <stdio.h>

//const int MAXP = 2000000;
//const int SQRT_MAXP = 1415;
const int MAXP = 2000000;
const int SQRT_MAXP = 1415;

int main()
{
  int i, j;
  char tab[MAXP];

  // Initialize the array to all prime
  printf("// Initialize the array to all prime\n");
  tab[0] = 0;
  tab[1] = 0;
  for (i = 2; i < MAXP; i++)
    tab[i] = 1;

  // Calculate the primes
  printf("// Calculate the primes\n");
  for (i = 2; i < SQRT_MAXP; i++) {
    if (tab[i]) {
      for (j = i*i; j < MAXP; j += i) {
        tab[j] = 0;
      }
    }
  }

  // Calculate the sum of primes
  printf("// Calculate the sum of primes\n");
  int ans_u = 0, ans_l = 0;
  int carry, primes = 0;
  for (i=2; i<MAXP; i++) {
    if (tab[i])  {
      ans_l += i;
      primes++;
    }

    if (ans_l > 1000000) {
      carry = ans_l / 1000000;
      ans_u += carry;
      ans_l -= (carry * 1000000);
    }
  }

  // Report answer
  printf("// Report answer\n");
  printf("Sum of %d primes = %d %d\n", primes, ans_u, ans_l);
}
