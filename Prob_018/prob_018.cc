// Project Euler.net Problem 18
//
// Maximum path sum I
//
// By starting at the top of the triangle below and moving to adjacent
// numbers on the row below, the maximum total from top to bottom is
// 23.
//
//        3
//       7 4
//      2 4 6
//     8 5 9 3
//
// That is, 3 + 7 + 4 + 9 = 23.
//
// Find the maximum total from top to bottom of the triangle below:
//
//                   75
//                  95 64
//                 17 47 82
//                18 35 87 10
//               20 04 82 47 65
//              19 01 23 75 03 34
//             88 02 77 73 07 63 67
//            99 65 04 28 06 16 70 92
//           41 41 26 56 83 40 80 70 33
//          41 48 72 33 47 32 37 16 94 29
//         53 71 44 65 25 43 91 52 97 51 14
//        70 11 33 28 77 73 17 78 39 68 17 57
//       91 71 52 38 17 14 91 43 58 50 27 29 48
//      63 66 04 68 89 53 67 30 73 16 69 87 40 31
//     04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
//
// NOTE: As there are only 16384 routes, it is possible to solve this
// problem by trying every route. However, Problem 67, is the same
// challenge with a triangle containing one-hundred rows; it cannot be
// solved by brute force, and requires a clever method! ;o)
//
// Need to compile this on my mac with...
//   g++ -std=c++11 prob_018.cc
//
// My g++ compiler is as follows...
//    bash-3.2$ g++ --version
//    g++ --version
//    Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
//    Apple LLVM version 8.0.0 (clang-800.0.42.1)
//    Target: x86_64-apple-darwin16.4.0
//    Thread model: posix
//    InstalledDir: /Library/Developer/CommandLineTools/usr/bin


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

////////////////////////////////////////
std::vector<std::vector<int>> triangle = {
                {75},
               {95, 64},
              {17, 47, 82},
             {18, 35, 87, 10},
            {20,  4, 82, 47, 65},
           {19,  1, 23, 75,  3, 34},
          {88,  2, 77, 73,  7, 63, 67},
         {99, 65,  4, 28,  6, 16, 70, 92},
        {41, 41, 26, 56, 83, 40, 80, 70, 33},
       {41, 48, 72, 33, 47, 32, 37, 16, 94, 29},
      {53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14},
     {70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57},
    {91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48},
   {63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31},
  { 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23} };


////////////////////////////////////////
int find_max(int x, int y) {
  if (x == (triangle.size() - 1))
      return triangle[x][y];

  int l = triangle[x][y] + find_max(x+1, y);
  int r = triangle[x][y] + find_max(x+1, y+1);
  return std::max(l, r);
}


////////////////////////////////////////
int main() {
  Timer tmr;  // Start a timer

  int Answer = find_max(0, 0);
  std::printf("Answer = %d\n", Answer);

  double t = tmr.elapsed();
  std::printf("Time taken = %f seconds\n", t);
}
