// Project Euler.net Problem 39
//
// If p is the perimeter of a right angle triangle with integral length
// sides, {a,b,c}, there are exactly three solutions for p = 120.
// 
// {20,48,52}, {24,45,51}, {30,40,50}
// 
// For which value of p <= 1000, is the number of solutions maximised?
//
// $Revision

#include <stdio.h>

#define MAX_SIDE  502

// The a or b maximum size length is calculated as follows
// p = a + b + c and is <= 1000
// c^2 = a^2 + b^2
// we will insure that a >=b at all times
// if b = 1 (minimum value), then c ~= a <= 500
// So MAX_SIDE is 500


int main()
{
    int a, b;
    int p[MAX_SIDE][MAX_SIDE];
    int sqrt[2*MAX_SIDE*MAX_SIDE];
    int p_cnt[2*MAX_SIDE];
    int max_cnt, max_p;

    // Generate a table of squares
    for (a = 0; a < 2*MAX_SIDE*MAX_SIDE; a++) {
        sqrt[a] = 0;
    }
    a = 1;
    do {
        if (a*a < 2*MAX_SIDE*MAX_SIDE)
            sqrt[a*a] = a;
        a++;
    } while (a*a < 2*MAX_SIDE*MAX_SIDE);
    // for (a = 0; a < 2*MAX_SIDE*MAX_SIDE; a++) {
    //     printf("sqrt[%d] = %d\n", a, sqrt[a]);
    // }


    // Generate a table that lists the possible C values, given A & B
    for (a = 1; a < MAX_SIDE; a++) {
        for (b = 1; b <= a; b++) {
            if ((a*a + b*b) >= 2*MAX_SIDE*MAX_SIDE) return (1);

            p[a][b] = sqrt[a*a + b*b];
            if (sqrt[a*a + b*b])
                p[a][b] += a + b;

            // printf("p[%d][%d] = %d (using sqrt[%d] = %d)\n", a, b, p[a][b], (a*a + b*b), sqrt[a*a + b*b]);
            printf("p[%d][%d] = %d\n", a, b, p[a][b]);
        }
    }

    // Find how many solutions for each p value
    for (a = 1; a < 2*MAX_SIDE; a++)
        p_cnt[a] = 0;

    for (a = 1; a < MAX_SIDE; a++) {
        for (b = 1; b <= a; b++) {
            p_cnt[(p[a][b])]++;
        }
    }

    // Find the p with the maximum number of solutions
    max_cnt = 0;
    max_p = 0;
    for (a = 1; a < 2*MAX_SIDE; a++) {
        if (p_cnt[a] > max_cnt) {
            max_cnt = p_cnt[a];
            max_p = a;
        }
    }

    // Report answer
    printf("// Report answer\n");
    printf("Maximum number of solutions (%d) with p = %d\n", max_cnt, max_p);
}
