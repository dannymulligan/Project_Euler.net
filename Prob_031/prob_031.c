// Project Euler.net Problem 31
//
// In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
//
//     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
//
// It is possible to make £2 in the following way:
//
//     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
//
// How many different ways can £2 be made using any number of coins?
//
// $Revision

#include <stdio.h>

int main()
{
    int i, j;

    int p1, p2, p5, p10, p20, p50, p100, p200;
    int total, count = 0;

    // Iterate through all possibilities of 8 different coins
    printf("// Iterate through all the possibilities of 8 different coins\n");
    for (p200 = 0; p200 <= 200/200; p200++) {
        if ((200*p200) <= 200)

        for (p100 = 0; p100 <= 200/100; p100++) {
            if ((200*p200 + 100*p100) <= 200)

            for (p50 = 0; p50 <= 200/50; p50++) {
                if ((200*p200 + 100*p100 + 50*p50) <= 200)

                for (p20 = 0; p20 <= 200/20; p20++) {
                    if ((200*p200 + 100*p100 + 50*p50 + 20*p20) <= 200)

                    for (p10 = 0; p10 <= 200/10; p10++) {
                        if ((200*p200 + 100*p100 + 50*p50 + 20*p20 + 10*p10) <= 200)

                        for (p5 = 0; p5 <= 200/5; p5++) {
                            if ((200*p200 + 100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5) <= 200)

                            for (p2 = 0; p2 <= 200/2; p2++) {
                                if ((200*p200 + 100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2) <= 200)

                                for (p1 = 0; p1 <= 200/1; p1++) {
                                    if ((200*p200 + 100*p100 + 50*p50 + 20*p20 + 10*p10 + 5*p5 + 2*p2 + 1*p1) <= 200)
                                    {
                                        total = 200*p200
                                              + 100*p100
                                              +  50*p50
                                              +  20*p20
                                              +  10*p10
                                              +   5*p5
                                              +   2*p2
                                              +   1*p1;

                                        if (total == 200) {
                                            //printf("%dx£2 + %dx£1 + %dx50p + %dx20p + %dx10p + %dx5p + %dx2p + %dx1p = %d\n", p200, p100, p50, p20, p10, p5, p2, p1, total);
                                            count++;
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

    // Report answer
    printf("// Report answer\n");
    printf("There are %d different ways to make £2 using any number of coins.\n", count);
}
