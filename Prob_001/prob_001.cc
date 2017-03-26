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

