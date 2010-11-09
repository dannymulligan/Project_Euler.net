// Project Euler.net Problem 37
//
// Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
//
//     1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
//     8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
//     9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)
//
// As 1 = 1^(4) is not a sum it is not included.
//
// The sum of these numbers is 1634 + 8208 + 9474 = 19316.
//
// Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
//
// $Revision

#include <stdio.h>

#define MAXP 1000000
#define SQRT_MAXP 1000

int main()
{
    int i;
    int count = 0;
    int sum = 0;
    int a, b, c, d, e, f;
    int temp;

    // Test all the numbers up to 1,000,000
    printf("// Test all the unumbers up to 1,000,000\n");
    for (i = 2; i < 1000000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        e = temp % 10;  temp -= e;  temp = temp / 10;
        f = temp % 10;  temp -= f;  temp = temp / 10;
        if ((a*a*a*a + b*b*b*b + c*c*c*c + d*d*d*d + e*e*e*e + f*f*f*f) == i)
        {
          printf("%d = %d^4 + %d^4 + %d^4 + %d^4 + %d^4 + %d^4\n", i, f, e, d, c, b, a);
            count++;  sum += i;
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("Found %d numbers with a sum of %d\n", count, sum);

    // Reset the statistics
    count = 0;
    sum = 0;

    // Test all the numbers up to 1,000,000
    printf("// Test all the unumbers up to 1,000,000\n");
    for (i = 2; i < 1000000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        e = temp % 10;  temp -= e;  temp = temp / 10;
        f = temp % 10;  temp -= f;  temp = temp / 10;
        if ((a*a*a*a*a + b*b*b*b*b + c*c*c*c*c + d*d*d*d*d + e*e*e*e*e + f*f*f*f*f) == i)
        {
          printf("%d = %d^5 + %d^5 + %d^5 + %d^5 + %d^5 + %d^5\n", i, f, e, d, c, b, a);
            count++;  sum += i;
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("Found %d numbers with a sum of %d\n", count, sum);

}
