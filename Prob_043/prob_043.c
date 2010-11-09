// Project Euler.net Problem 43
//
// The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits
// 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
//
// Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
//
//     * d2 d3 d4  = 406 is divisible by 2
//     * d3 d4 d5  = 063 is divisible by 3
//     * d4 d5 d6  = 635 is divisible by 5
//     * d5 d6 d7  = 357 is divisible by 7
//     * d6 d7 d8  = 572 is divisible by 11
//     * d7 d8 d9  = 728 is divisible by 13
//     * d8 d9 d10 = 289 is divisible by 17
//
// Find the sum of all 0 to 9 pandigital numbers with this property.
//
// $Revision

#include <stdio.h>

int main()
{
    int d0, d1, d2, d3, d4;
    int d5, d6, d7, d8, d9;
    long answer_u = 0;  // Upper 5 digits
    long answer_l = 0;  // Lower 5 digits

    // Iterate through all possibilities
    printf("// Iterate through all the possibilities\n");
    for (d0 = 0; d0 < 10; d0++) {

        for (d1 = 0; d1 < 10; d1++) {
            if ((d1 != d0))

            for (d2 = 0; d2 < 10; d2++) {
                if ((d2 != d1) && (d2 != d0))

                for (d3 = 0; d3 < 10; d3++) {
                    if ((d3 != d2) && (d3 != d1) && (d3 != d0))
                    if ((d3 % 2) == 0)

                    for (d4 = 0; d4 < 10; d4++) {
                        if ((d4 != d3) && (d4 != d2) && (d4 != d1) && (d4 != d0))
                        if (((d2*100 + d3*10 + d4) % 3) == 0)

                        for (d5 = 0; d5 < 10; d5++) {
                            if ((d5 != d4) && (d5 != d3) && (d5 != d2) && (d5 != d1) && (d5 != d0))
                            if (((d3*100 + d4*10 + d5) % 5) == 0)

                            for (d6 = 0; d6 < 10; d6++) {
                                if ((d6 != d5) && (d6 != d4) && (d6 != d3) && (d6 != d2) && (d6 != d1) && (d6 != d0))
                                if (((d4*100 + d5*10 + d6) % 7) == 0)

                                for (d7 = 0; d7 < 10; d7++) {
                                    if ((d7 != d6) && (d7 != d5) && (d7 != d4) && (d7 != d3) && (d7 != d2) && (d7 != d1) && (d7 != d0))
                                    if (((d5*100 + d6*10 + d7) % 11) == 0)

                                    for (d8 = 0; d8 < 10; d8++) {
                                        if ((d8 != d7) && (d8 != d6) && (d8 != d5) && (d8 != d4) && (d8 != d3) && (d8 != d2) && (d8 != d1) && (d8 != d0))
                                        if (((d6*100 + d7*10 + d8) % 13) == 0)

                                        for (d9 = 0; d9 < 10; d9++) {
                                            if ((d9 != d8) && (d9 != d7) && (d9 != d6) && (d9 != d5) && (d9 != d4) && (d9 != d3) && (d9 != d2) && (d9 != d1) && (d9 != d0))
                                            if (((d7*100 + d8*10 + d9) % 17) == 0) {
                                                printf("%1d%1d%1d%1d%1d%1d%1d%1d%1d%1d\n", d0, d1, d2, d3, d4, d5, d6, d7, d8, d9);
                                                answer_u += d0*10000
                                                          + d1*1000
                                                          + d2*100
                                                          + d3*10
                                                          + d4*1;
                                                answer_l += d5*10000
                                                          + d6*1000
                                                          + d7*100
                                                          + d8*10
                                                          + d9*1;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    if (answer_l > 100000) {
        answer_u += answer_l/100000;
        answer_l = answer_l % 100000;
    }
    printf("answer_u = %05d, answer_l, = %05d\n", answer_u, answer_l);
    printf("answer = %05d%05d\n", answer_u, answer_l);
}
