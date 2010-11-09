// Project Euler.net Problem 9
//
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//     a^(2) + b^(2) = c^(2)
//
// For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
// 
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.
//
// $Revision

#include <stdio.h>

#define MAX 1000

int main()
{

    // Find the answer
    int a, b, c;
    for (a=1; a<MAX/3; a++) {
        for (b=a+1; b<(MAX-a)/2; b++) {
            for (c=b+1; c<MAX; c++) {
                if ((a+b+c) == MAX)
                  if ((a*a) + (b*b) == (c*c))
                        printf("a = %d, b = %d, c = %d, a+b+c = %d, a*b*c = %d\n", a, b, c, (a+b+c), (a*b*c));
            }
        }
    }

}
