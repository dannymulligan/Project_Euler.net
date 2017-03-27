// Project Euler.net Problem 1
//
// Add all the natural numbers below one thousand that are multiples of 3 or 5.
//
// If we list all the natural numbers below 10 that are multiples of 3
// or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Find the sum of all the multiples of 3 or 5 below 1000.

#include <iostream>

int main()
{
  int answer = 0;
  const int LIMIT = 1000;
  int i;
  for(i=0; i<LIMIT; i++)
    if (((i % 3) == 0) || ((i % 5) == 0)) {
      answer += i;
    }

  std::cout << "The answer is "
            << answer
            << ".\n";
}

