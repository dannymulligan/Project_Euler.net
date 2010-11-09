// Project Euler.net Problem 33
//
// The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
// attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
// correct, is obtained by cancelling the 9s.
// 
// We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
// 
// There are exactly four non-trivial examples of this type of fraction, less than
// one in value, and containing two digits in the numerator and denominator.
// 
// If the product of these four fractions is given in its lowest common terms,
// find the value of the denominator.
// 
//
// $Revision

#include <stdio.h>

#define MAX 1000002

int main()
{
    int x, x0, x1;
    int y, y0, y1;
    int a, b;
    int c = 1, d = 1;
    int tmp;
    int found;

    for (y = 10; y < 100; y++) {
        for (x = 10; x < y; x++) {
            tmp = x;
            x0 = tmp % 10;  tmp -= x0;  tmp = tmp / 10;
            x1 = tmp % 10;  tmp -= x1;  tmp = tmp / 10;

            tmp = y;
            y0 = tmp % 10;  tmp -= y0;  tmp = tmp / 10;
            y1 = tmp % 10;  tmp -= y1;  tmp = tmp / 10;

            // if x = CD (i.e. x1 = C, x0 = D)
            // if y = EF (i.e. x1 = E, x0 = F)
            // printf("x=%d y=%d ", x, y);
            found = 0;
            if (x0 == y0) {
                // Is CD/EF == C/E?
                // Or is (CD * E) == (C * EF)?
                found = ((x * y1) == (x1 * y));
                if ((x0 == 0) && (y0 == 0))
                    found = 0;
                a = x1;  b = y1;
                // printf("Found x0 == y0\n");
            }
            else
            if (x0 == y1) {
                // Is CD/EF == C/F?
                // Or is (CD * F) == (C * EF)?
                found = ((x * y0) == (x1 * y));
                a = x1;  b = y0;
                // printf("Found x0 == y1\n");
            }
            else
            if (x1 == y0) {
                // Is CD/EF == D/E?
                // Or is (CD * E) == (D * EF)?
                found = ((x * y1) == (x0 * y));
                a = x0;  b = y1;
                // printf("Found x1 == y0\n");
            }
            else
            if (x1 == y1) {
                // Is CD/EF == D/F?
                // Or is (CD * F) == (D * EF)?
                found = ((x * y0) == (x0 * y));
                a = x0;  b = y0;
                // printf("Found x1 == y1\n");
            }

            if (found) {
                printf("Found %d/%d == %d/%d (x1=%d x0=%d y1=%d y0=%d)\n", x, y, a, b, x1, x0, y1, y0);
                c = c * a;
                d = d * b;
            }
        }
    }

    printf("Answer is %d/%d\n", c, d);
}
