// Project Euler.net Problem 41
//
// We shall say that an n-digit number is pandigital if it makes use of all the digits
// 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
//
// What is the largest n-digit pandigital prime that exists?
//
// $Revision

#include <stdio.h>

#define MAX_P      4000000
#define SQRT_MAX_P    2000
#define CNT 1001

int main()
{
    int i, j;
    char tab[MAX_P];
    int limit;

    // Initialize the array to all prime
    printf("// Initialize the array to all prime\n");
    for (i = 1; i < MAX_P; i++) {
        tab[i] = 1;
    }
    tab[0] = 0;
    tab[1] = 0;

    // Calculate the primes
    printf("// Calculate the primes\n");
    for (i = 2; i < SQRT_MAX_P; i++) {
        if (tab[i]) {
            for (j = i*i; j < MAX_P; j += i) {
                  tab[j] = 0;
            }
        }
    }


    int d1, d2, d3, d4, d5, d6, d7, d8, d9;
    int answer, sqrt_answer, prime;

    // Iterate through all possibilities for 4 digits
    printf("// Iterate through all the possibilities for 4 digits\n");
    limit = 4; d1 = 0; d2 = 0; d3 = 0; d4 = 0; d5 = 0;
    for (d6 = 1; d6 <= limit; d6++) {
        if ((d6 != d5) && (d6 != d4) && (d6 != d3) && (d6 != d2) && (d6 != d1))

        for (d7 = 1; d7 <= limit; d7++) {
            if ((d7 != d6) && (d7 != d5) && (d7 != d4) && (d7 != d3) && (d7 != d2) && (d7 != d1))

            for (d8 = 1; d8 <= limit; d8++) {
                if ((d8 != d7) && (d8 != d6) && (d8 != d5) && (d8 != d4) && (d8 != d3) && (d8 != d2) && (d8 != d1))

                for (d9 = 1; d9 <= limit; d9++) {
                    if ((d9 != d8) && (d9 != d7) && (d9 != d6) && (d9 != d5) && (d9 != d4) && (d9 != d3) && (d9 != d2) && (d9 != d1))
                    {
                        answer = d1*100000000
                               + d2*10000000
                               + d3*1000000
                               + d4*100000
                               + d5*10000
                               + d6*1000
                               + d7*100
                               + d8*10
                               + d9*1;

                        sqrt_answer = (int) sqrt(answer);
                        prime = 1;
                        for (i = 2; i <= sqrt_answer; i++)
                            if (tab[i] && ((answer % i) == 0))
                                prime = 0;

                        if (prime)
                            printf("%1d%1d%1d%1d%1d%1d%1d%1d%1d is a prime\n", d1, d2, d3, d4, d5, d6, d7, d8, d9);
                    }
                }
            }
        }
    }

    // Iterate through all possibilities for 5 digits
    printf("// Iterate through all the possibilities for 5 digits\n");
    limit = 5; d1 = 0; d2 = 0; d3 = 0; d4 = 0;
    for (d5 = 1; d5 <= limit; d5++) {
        if ((d5 != d4) && (d5 != d3) && (d5 != d2) && (d5 != d1))

        for (d6 = 1; d6 <= limit; d6++) {
            if ((d6 != d5) && (d6 != d4) && (d6 != d3) && (d6 != d2) && (d6 != d1))

            for (d7 = 1; d7 <= limit; d7++) {
                if ((d7 != d6) && (d7 != d5) && (d7 != d4) && (d7 != d3) && (d7 != d2) && (d7 != d1))

                for (d8 = 1; d8 <= limit; d8++) {
                    if ((d8 != d7) && (d8 != d6) && (d8 != d5) && (d8 != d4) && (d8 != d3) && (d8 != d2) && (d8 != d1))

                    for (d9 = 1; d9 <= limit; d9++) {
                        if ((d9 != d8) && (d9 != d7) && (d9 != d6) && (d9 != d5) && (d9 != d4) && (d9 != d3) && (d9 != d2) && (d9 != d1))
                        {
                            answer = d1*100000000
                                   + d2*10000000
                                   + d3*1000000
                                   + d4*100000
                                   + d5*10000
                                   + d6*1000
                                   + d7*100
                                   + d8*10
                                   + d9*1;

                            sqrt_answer = (int) sqrt(answer);
                            prime = 1;
                            for (i = 2; i <= sqrt_answer; i++)
                                if (tab[i] && ((answer % i) == 0))
                                    prime = 0;

                            if (prime)
                                printf("%1d%1d%1d%1d%1d%1d%1d%1d%1d is a prime\n", d1, d2, d3, d4, d5, d6, d7, d8, d9);
                            }
                    }
                }
            }
        }
    }

    // Iterate through all possibilities for 6 digits
    printf("// Iterate through all the possibilities for 6 digits\n");
    limit = 6; d1 = 0; d2 = 0; d3 = 0;
    for (d4 = 1; d4 <= limit; d4++) {
        if ((d4 != d3) && (d4 != d2) && (d4 != d1))

        for (d5 = 1; d5 <= limit; d5++) {
            if ((d5 != d4) && (d5 != d3) && (d5 != d2) && (d5 != d1))

            for (d6 = 1; d6 <= limit; d6++) {
                if ((d6 != d5) && (d6 != d4) && (d6 != d3) && (d6 != d2) && (d6 != d1))

                for (d7 = 1; d7 <= limit; d7++) {
                    if ((d7 != d6) && (d7 != d5) && (d7 != d4) && (d7 != d3) && (d7 != d2) && (d7 != d1))

                    for (d8 = 1; d8 <= limit; d8++) {
                        if ((d8 != d7) && (d8 != d6) && (d8 != d5) && (d8 != d4) && (d8 != d3) && (d8 != d2) && (d8 != d1))

                        for (d9 = 1; d9 <= limit; d9++) {
                            if ((d9 != d8) && (d9 != d7) && (d9 != d6) && (d9 != d5) && (d9 != d4) && (d9 != d3) && (d9 != d2) && (d9 != d1))
                            {
                                answer = d1*100000000
                                       + d2*10000000
                                       + d3*1000000
                                       + d4*100000
                                       + d5*10000
                                       + d6*1000
                                       + d7*100
                                       + d8*10
                                       + d9*1;

                                sqrt_answer = (int) sqrt(answer);
                                prime = 1;
                                for (i = 2; i <= sqrt_answer; i++)
                                    if (tab[i] && ((answer % i) == 0))
                                        prime = 0;

                                if (prime)
                                    printf("%1d%1d%1d%1d%1d%1d%1d%1d%1d is a prime\n", d1, d2, d3, d4, d5, d6, d7, d8, d9);
                            }
                        }
                    }
                }
            }
        }
    }

    // Iterate through all possibilities for 7 digits
    printf("// Iterate through all the possibilities for 7 digits\n");
    limit = 7; d1 = 0; d2 = 0;
    for (d3 = 1; d3 <= limit; d3++) {
        if ((d3 != d2) && (d3 != d1))

        for (d4 = 1; d4 <= limit; d4++) {
            if ((d4 != d3) && (d4 != d2) && (d4 != d1))

            for (d5 = 1; d5 <= limit; d5++) {
                if ((d5 != d4) && (d5 != d3) && (d5 != d2) && (d5 != d1))

                for (d6 = 1; d6 <= limit; d6++) {
                    if ((d6 != d5) && (d6 != d4) && (d6 != d3) && (d6 != d2) && (d6 != d1))

                    for (d7 = 1; d7 <= limit; d7++) {
                        if ((d7 != d6) && (d7 != d5) && (d7 != d4) && (d7 != d3) && (d7 != d2) && (d7 != d1))

                        for (d8 = 1; d8 <= limit; d8++) {
                            if ((d8 != d7) && (d8 != d6) && (d8 != d5) && (d8 != d4) && (d8 != d3) && (d8 != d2) && (d8 != d1))

                            for (d9 = 1; d9 <= limit; d9++) {
                                if ((d9 != d8) && (d9 != d7) && (d9 != d6) && (d9 != d5) && (d9 != d4) && (d9 != d3) && (d9 != d2) && (d9 != d1))
                                {
                                    answer = d1*100000000
                                           + d2*10000000
                                           + d3*1000000
                                           + d4*100000
                                           + d5*10000
                                           + d6*1000
                                           + d7*100
                                           + d8*10
                                           + d9*1;
                                    sqrt_answer = (int) sqrt(answer);
                                    prime = 1;
                                    for (i = 2; i <= sqrt_answer; i++)
                                        if (tab[i] && ((answer % i) == 0))
                                            prime = 0;

                                    if (prime)
                                        printf("%1d%1d%1d%1d%1d%1d%1d%1d%1d is a prime\n", d1, d2, d3, d4, d5, d6, d7, d8, d9);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    // Iterate through all possibilities for 8 digits
    printf("// Iterate through all the possibilities for 8 digits\n");
    limit = 8; d1 = 0;
    for (d2 = 1; d2 <= limit; d2++) {
        if ((d2 != d1))

        for (d3 = 1; d3 <= limit; d3++) {
            if ((d3 != d2) && (d3 != d1))

            for (d4 = 1; d4 <= limit; d4++) {
                if ((d4 != d3) && (d4 != d2) && (d4 != d1))

                for (d5 = 1; d5 <= limit; d5++) {
                    if ((d5 != d4) && (d5 != d3) && (d5 != d2) && (d5 != d1))

                    for (d6 = 1; d6 <= limit; d6++) {
                        if ((d6 != d5) && (d6 != d4) && (d6 != d3) && (d6 != d2) && (d6 != d1))

                        for (d7 = 1; d7 <= limit; d7++) {
                            if ((d7 != d6) && (d7 != d5) && (d7 != d4) && (d7 != d3) && (d7 != d2) && (d7 != d1))

                            for (d8 = 1; d8 <= limit; d8++) {
                                if ((d8 != d7) && (d8 != d6) && (d8 != d5) && (d8 != d4) && (d8 != d3) && (d8 != d2) && (d8 != d1))

                                for (d9 = 1; d9 <= limit; d9++) {
                                    if ((d9 != d8) && (d9 != d7) && (d9 != d6) && (d9 != d5) && (d9 != d4) && (d9 != d3) && (d9 != d2) && (d9 != d1))
                                    {
                                        answer = d1*100000000
                                               + d2*10000000
                                               + d3*1000000
                                               + d4*100000
                                               + d5*10000
                                               + d6*1000
                                               + d7*100
                                               + d8*10
                                               + d9*1;

                                        sqrt_answer = (int) sqrt(answer);
                                        prime = 1;
                                        for (i = 2; i <= sqrt_answer; i++)
                                            if (tab[i] && ((answer % i) == 0))
                                                prime = 0;

                                        if (prime)
                                            printf("%1d%1d%1d%1d%1d%1d%1d%1d%1d is a prime\n", d1, d2, d3, d4, d5, d6, d7, d8, d9);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    // Iterate through all possibilities for 9 digits
    printf("// Iterate through all the possibilities for 9 digits\n");
    limit = 9;
    for (d1 = 1; d1 <= limit; d1++) {

        for (d2 = 1; d2 <= limit; d2++) {
            if ((d2 != d1))

            for (d3 = 1; d3 <= limit; d3++) {
                if ((d3 != d2) && (d3 != d1))

                for (d4 = 1; d4 <= limit; d4++) {
                    if ((d4 != d3) && (d4 != d2) && (d4 != d1))

                    for (d5 = 1; d5 <= limit; d5++) {
                        if ((d5 != d4) && (d5 != d3) && (d5 != d2) && (d5 != d1))

                        for (d6 = 1; d6 <= limit; d6++) {
                            if ((d6 != d5) && (d6 != d4) && (d6 != d3) && (d6 != d2) && (d6 != d1))

                            for (d7 = 1; d7 <= limit; d7++) {
                                if ((d7 != d6) && (d7 != d5) && (d7 != d4) && (d7 != d3) && (d7 != d2) && (d7 != d1))

                                for (d8 = 1; d8 <= limit; d8++) {
                                    if ((d8 != d7) && (d8 != d6) && (d8 != d5) && (d8 != d4) && (d8 != d3) && (d8 != d2) && (d8 != d1))

                                    for (d9 = 1; d9 <= limit; d9++) {
                                        if ((d9 != d8) && (d9 != d7) && (d9 != d6) && (d9 != d5) && (d9 != d4) && (d9 != d3) && (d9 != d2) && (d9 != d1))
                                        {
                                            answer = d1*100000000
                                                   + d2*10000000
                                                   + d3*1000000
                                                   + d4*100000
                                                   + d5*10000
                                                   + d6*1000
                                                   + d7*100
                                                   + d8*10
                                                   + d9*1;

                                            sqrt_answer = (int) sqrt(answer);
                                            prime = 1;
                                            for (i = 2; i <= sqrt_answer; i++)
                                                if (tab[i] && ((answer % i) == 0))
                                                    prime = 0;

                                            if (prime)
                                                printf("%1d%1d%1d%1d%1d%1d%1d%1d%1d is a prime\n", d1, d2, d3, d4, d5, d6, d7, d8, d9);
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
}
