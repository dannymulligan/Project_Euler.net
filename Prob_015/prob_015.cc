// Project Euler.net Problem 015
//
// Lattice paths
//
// Starting in the top left corner of a 2×2 grid, and only being able
// to move to the right and down, there are exactly 6 routes to the
// bottom right corner.
//
// How many such routes are there through a 20×20 grid?

#include <chrono>
#include <iostream>
#include <vector>

// From: https://stackoverflow.com/questions/728068/how-to-calculate-a-time-difference-in-c
class Timer
{
public:
  Timer() : beg_(clock_::now()) {}
  void reset() { beg_ = clock_::now(); }
  double elapsed() const { 
    return std::chrono::duration_cast<second_>
      (clock_::now() - beg_).count(); }

private:
  typedef std::chrono::high_resolution_clock clock_;
  typedef std::chrono::duration<double, std::ratio<1> > second_;
  std::chrono::time_point<clock_> beg_;
};


const int SIZE = 20;

int main () {
  // Start a timer
  Timer tmr;

  // Create an empty array of node values, initialized with 0
  std::vector<std::vector<int> > nodes(SIZE+1, std::vector<int>(SIZE+1, 0));

  // Next we step through the array and calculate the number of paths to that node
  // We have to remember to initialize nodes[0][0] to 1
  int value_above;
  int value_left;
  for(int x = 0; x < SIZE+1; x++) {
    for(int y = 0; y < SIZE+1; y++) {
      if ((x-1) < 0)
        value_above = 0;
      else
        value_above = nodes[x-1][y];

      if ((y-1) < 0)
        value_left = 0;
      else
        value_left = nodes[x][y-1];

      if ((x == 0) & (y == 0))
        nodes[x][y] = 1;
      else
        nodes[x][y] = value_above + value_left;
    }
  }

  // Print out the resulting array for debugging
  if (false) {
    for(int x = 0; x < SIZE+1; x++) {
      for(int y = 0; y < SIZE+1; y++) {
        std::cout << nodes[x][y];
        if (y < SIZE)
          std::cout << ", ";
      }
      std::cout << std::endl;
    }
  }


  // And our answer is in the lower right node, which is nodes[SIZE][SIZE]
  std::printf("For a %dx%d grid...\n", SIZE, SIZE);
  std::printf("Answer = %d\n", nodes[SIZE][SIZE]);

  double t = tmr.elapsed();
  std::printf("Time taken = %f seconds\n", t);

}

