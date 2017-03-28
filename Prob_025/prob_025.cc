// Project Euler.net Problem 25
//
// The Fibonacci sequence is defined by the recurrence relation:
//
//    F_(n) = F_(n-1) + F_(n-2), where F_(1) = 1 and F_(2) = 1.
//
// Hence the first 12 terms will be:
//
//     F_(1) = 1
//     F_(2) = 1
//     F_(3) = 2
//     F_(4) = 3
//     F_(5) = 5
//     F_(6) = 8
//     F_(7) = 13
//     F_(8) = 21
//     F_(9) = 34
//     F_(10) = 55
//     F_(11) = 89
//     F_(12) = 144
//
// The 12th term, F_(12), is the first term to contain three digits.
//
// What is the first term in the Fibonacci sequence to contain 1000 digits?

#include <iostream>

const int PRECISION = 170;
const int LIMIT = 1000000;
const int TARGET = 1000;

int main()
{

  // We're going to store 6 decimal digits per integer
  long a[PRECISION];
  long b[PRECISION];
  long c[PRECISION];
  int i, j;

  // Initialize each array
  std::printf("// Initialize the table\n");
  for (i=1; i<PRECISION; i++) {
    a[i] = 0;
    b[i] = 0;
    c[i] = 0;
  }
  a[0] = 1;
  b[0] = 1;
  c[0] = 1;

  // Calculate the factorial
  std::printf("// Calculate F(n)\n");
  int n = 2;
  int temp, len;
  do {
    // Caculating F(n)
    n++;

    // Calculate c
    for (i=0; i<PRECISION; i++) {
      c[i] = a[i] + b[i];
    }

    // Adjust for any carries
    for (i=0; i<PRECISION-1; i++) {
      if (c[i] > LIMIT) {
        temp = c[i]/LIMIT;
        c[i] = c[i] - LIMIT * temp;
        c[i+1] = c[i+1] + temp;
      }
    }

    // Move b to a
    for (i=0; i<PRECISION; i++) {
      a[i] = b[i];
    }

    // Move c to b
    for (i=0; i<PRECISION; i++) {
      b[i] = c[i];
    }

    // Count the digits
    len = 0;
    for (i=0; i<PRECISION-1; i++) {
      if (c[i] > 0) {
        len = i*6;
        len++;
        if (c[i] >=      10)  len++;
        if (c[i] >=     100)  len++;
        if (c[i] >=    1000)  len++;
        if (c[i] >=   10000)  len++;
        if (c[i] >=  100000)  len++;
        if (c[i] >= 1000000)  len++;
      }
    }

    // Report length
    std::printf("// F(%d) is %d digits long = ", n, len);
//    for (i=PRECISION-1; i>=0; i--) {
//      std::printf("%06d ", c[i]);
//    }
    std::printf("\n");

  } while (len < TARGET);

  // Print the answer
  std::printf("// Print the answer\n");
  for (i=PRECISION-1; i>=0; i--) {
    std::printf("%06ld ", c[i]);
  }
  std::printf("\n");
  std::printf("The answer is %d\n", n);
}
