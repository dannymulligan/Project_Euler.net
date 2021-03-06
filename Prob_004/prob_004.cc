// Project Euler.net Problem 4
//
// A palindromic number reads the same both ways.
//
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 � 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

#include <iostream>
#include <cstring>

int palindrome(int candidate_int)
{
  char candidate_str[12];
  int candidate_len;
  int i;

  // Convert the candidate number to a string
  sprintf(candidate_str, "%d", candidate_int);
  candidate_len = (int)strlen(candidate_str);
  //printf("Testing %s for palindrome (len=%d)\n", candidate_str, candidate_len);

  // Try to eliminate it as a palindrome
  for(i=0; i<(candidate_len/2); i++) {
    if (candidate_str[i] != candidate_str[candidate_len-i-1])
      return (0);  // Not a palindrome
  }

  // It is a palindrome!
  return (1);
}

int main()
{
  int candidate;
  int max_ij = 0, max_i = 0, max_j = 0;

  for (int i=999; i>99; i--) {
    for (int j=999; j>99; j--) {
      candidate = i * j;
      if ((candidate > max_ij) && palindrome(candidate)) {
        max_ij = candidate;
        max_i = i; max_j = j;
        printf("i = %d, j = %d, candidate = %d\n", i, j, candidate);
      }
    }
  }

  printf("Largest palindrome is %d from multiplying %d by %d.\n", max_ij, max_i, max_j);
  printf("Answer = %d.\n", max_ij);
}
