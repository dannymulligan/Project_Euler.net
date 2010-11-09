// Project Euler.net Problem 56
//
// A googol (10^(100)) is a massive number: one followed by one-hundred zeros; 100^(100) is
// almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum
// of the digits in each number is only 1.
// 
// Considering natural numbers of the form, a^(b), where a, b < 100, what is the maximum digital sum?
// 
// $Revision

#include <stdio.h>

#define LIMIT 10
#define PRECISION 200
#define POWER 100
// 100^100 has about 200 decimal digits
// We're going to store 1 decimal digits per integer
// We need arrays of about 200 integers


int main()
{

    long a, b, r, res[PRECISION];
    long max_a, max_b, max_r = 0;
    int i, j, p;

    for (a = 1; a <= POWER; a++) {
        for (b = 1; b <= POWER; b++) {

            // Initialize res[]
            for (p=0; p<PRECISION; p++)
                res[p] = 0;
            res[0] = 1;

            // Calculate a^b
            for (i=0; i<b; i++) {
                // Multiply by a
                for (p=0; p<PRECISION; p++)
                    res[p] = res[p] * a;

                // Adjust array
                for (p=0; p<PRECISION-1; p++)
                    if (res[p] >= LIMIT) {
                        res[p+1] += res[p] / LIMIT;
                        res[p] = res[p] % LIMIT;
                    }
            }

            // Calculate result
            r = 0;
            for (p=0; p<PRECISION-1; p++)
                r += res[p];

            // New max?
            if (r > max_r) {
                max_r = r;
                max_a = a;
                max_b = b;
                printf("New maximum, %d^%d, result = %d\n", a, b, r);
            }
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("Result = %d^%d with a digital sum of %d\n", max_a, max_b, max_r);
}
