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

  //std::cout << "LIMIT_PRIME = " << LIMIT_PRIME << "\n";
  while (i < (LIMIT_PRIME/2)) {
    if (prime_table[i] == 1) {
      j = i*2;
        while (j < LIMIT_PRIME) {
          prime_table[j] = i;
          j += i;
          //std::cout << "prime_table[" << j << "] = " << i << "\n";
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
  i = LIMIT_PRIME - 1;
  while (answer == 0) {
    if (prime_table[i] == 1) {
      if ((TARGET % i) == 0) {
        answer = i;
      }
    }
    i -= 1;
  }
  i += 1;

  std::cout << "The answer is " << answer << ".\n";
}
