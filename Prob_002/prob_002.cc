#include <iostream>

int main ()
{
  const int LIMIT = 4000000;

  int f0 = 1;
  int f1 = 2;
  int n = 2;
  int answer = f1;

  //std::cout << "The first few Fibonacci numbers are";
  //std::cout << f0 << f1;

  while ((f0 + f1) < LIMIT) {
    n += 1;
    int temp = f0 + f1;
    f0 = f1;
    f1 = temp;
    //std::cout << ", " << f1;

    if ((f1 % 2) == 0) {
      // f1 is even
      answer += f1;
    }
  }
  //std::cout << "\n";

  std::cout << "The answer is " << answer << ".\n";
}
