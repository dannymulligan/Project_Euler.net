// Project Euler.net Problem 24
//
// What is the millionth lexicographic permutation of the digits 0, 1,
// 2, 3, 4, 5, 6, 7, 8 and 9?
//
// A permutation is an ordered arrangement of objects. For example,
// 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all
// of the permutations are listed numerically or alphabetically, we
// call it lexicographic order. The lexicographic permutations of 0, 1
// and 2 are:
// 
//     012   021   102   120   201   210
//
// What is the millionth lexicographic permutation of the digits 0, 1,
// 2, 3, 4, 5, 6, 7, 8 and 9?
//
// Compile with...
//    g++ -std=c++11 prob_024.cc


#include <algorithm>
#include <iostream>
#include <vector>

const int N = 1000000;

int main () {
  std::vector<int> nums = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };


  int count = 0;
  do {
    if (false) {
      // Print the current permutation
      std::cout << count << ": ";
      for (int i = 0; i < nums.size(); i++) {
        std::cout << nums[i] << ", ";
      }
      std::cout << std::endl;
    }

    count += 1;
    if (count == N) {
      break;
    }
  } while (std::next_permutation(nums.begin(), nums.end()));

  std::printf("Answer = ");
  for (int i = 0; i < 10; i++)
    std::printf("%1d", nums[i]);
  std::printf("\n");

}
