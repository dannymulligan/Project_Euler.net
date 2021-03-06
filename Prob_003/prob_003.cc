// Project Euler.net Problem 3
//
// Find the largest prime factor of a composite number.
//
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

#include <iostream>

//const int TARGET = 13195;
//const int LIMIT_PRIME = 115;
const long TARGET = 600851475143;
const int LIMIT_PRIME = 775147;  // smallest int so that square is greater than target
int prime_table[LIMIT_PRIME];


void calculate_primes() {
  std::cout << "Starting calculate_primes()\n";
  int i = 2;
  int j;

  while (i < (LIMIT_PRIME/2)) {
    if (prime_table[i] == 1) {
      j = i*2;
        while (j < LIMIT_PRIME) {
          prime_table[j] = i;
          j += i;
        }
    }
    i += 1;
  }
  std::cout << "Finishing calculate_primes()\n";
}


int main ()
{
  int i;
  for (i = 0; i < LIMIT_PRIME; i++)
    prime_table[i] = 1;

  calculate_primes();

  int answer = 0;
  i = LIMIT_PRIME;
  do {
    i--;
    if (prime_table[i] == 1)
      if ((TARGET % i) == 0)
        answer = i;
  } while (answer == 0);

  std::cout << "The answer is " << answer << ".\n";
}
