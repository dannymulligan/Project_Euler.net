// Project Euler.net Problem 78
//
// Let p(n) represent the number of different ways in which n coins can
// be separated into piles. For example, five coins can separated into
// piles in exactly seven different ways, so p(5)=7.
// 
//     OOOOO
//     OOOO O
//     OOO OO
//     OOO O O
//     OO OO O
//     OO O O O
//     O O O O O
// 
// Find the least value of n for which p(n) is divisible by one million.
//
// Searched to 38925 in 2 days 14 hours 10 minutes CPU time
//
//     ways(38925,38925) % 1000000 = 53970
//       C-c C-c
//     
//     real	3778m55.542s
//     user	3716m32.188s
//     sys	14m3.669s
// 
// Answer 55374

#include <stdio.h>
#include <stdlib.h>

#define CACHE_SIZE 40000

int ways_cache[CACHE_SIZE][CACHE_SIZE];
int iterations = 0;
int prev_iterations = 0;
int debug = 0;

long ways(int n, int max_n)
{
    iterations++;

    if ((n <= 1) || (max_n <= 1)) {
        if (debug)  printf(">  ways(%d,%d) = %d\n", n, max_n, 1);
        if ((n<CACHE_SIZE) && (max_n<CACHE_SIZE))
            ways_cache[n][max_n] = 1;
        return 1;
    }

//    if (max_n == 2) {
//        if (debug)  printf(">  ways(%d,%d) = %d\n", n, max_n, 1);
//        if ((n<CACHE_SIZE) && (max_n<CACHE_SIZE))
//            ways_cache[n][max_n] = 1+(n/2);
//        return 1+(n/2);
//    }

    if ((n<CACHE_SIZE) && (max_n<CACHE_SIZE) && (ways_cache[n][max_n] != 0)) {
        if (debug)  printf("+  ways(%d,%d) = %d\n", n, max_n, ways_cache[n][max_n]);
        return ways_cache[n][max_n];
    }

    int ans = 0;
    int i;
    int temp;
    int nn = (n<max_n) ? n : max_n;  // nn = max(n, max_n)
    for(i = nn; i > 0; i--) {
        int ii = (nn<i) ? nn : i;  // ii = max(nn, i)
        if (((n-i)<CACHE_SIZE) && (ii<CACHE_SIZE) && (ways_cache[n-i][ii] != 0)) {
            temp = ways_cache[n-i][ii];  // i coins, followed by all possible combinations of n-i
            ans = (ans + temp) % 1000000;
        } else {
            temp = ways(n-i,ii);  // i coins, followed by all possible combinations of n-i
            ans = (ans + temp) % 1000000;
        }
    }
    if ((n<CACHE_SIZE) && (max_n<CACHE_SIZE))
        ways_cache[n][max_n] = ans;
    if (debug)  printf(">> ways(%d,%d) = %d\n", n, max_n, ans);
    return ans;
}

main () {
    int i, j;
    int n;

    for (i=0; i<CACHE_SIZE; i++) {
        for (j=0; j<CACHE_SIZE; j++) {
            ways_cache[i][j] = 0;
        }
    }

    for (i=0; i<60001; i=i+1) {
        n = ways(i,i);
        if (n == 0) {
            printf("Found!!!   ways(%d,%d) %% 1000000 = %d\n", i, i, n);
            exit(0);
        }
        if ((i % 25) == 0) {
            printf("ways(%d,%d) %% 1000000 = %d\n", i, i, n);
        }
        if ((i % 1000) == 0) {
            printf("\ndelta iterations = %d\n\n", iterations-prev_iterations);  prev_iterations = iterations;
        }
    }

}

//    printf("\niterations = %d\n\n", iterations);  prev_iterations = iterations;
//    for (i=1000; i<2001; i++) {
//        n = ways(i,i);
//        if (n == 0) {
//            printf("Found!!!   ways(%d,%d) %% 1000000 = %d\n", i, i, n);
//            exit(0);
//        }
//        if ((i % 25) == 0) {
//            printf("ways(%d,%d) %% 1000000 = %d\n", i, i, n);
//        }
//    }
//    printf("\ndelta iterations = %d\n\n", iterations-prev_iterations);  prev_iterations = iterations;

//    printf("\niterations = %d\n\n", iterations);  prev_iterations = iterations;
//
//    debug = 1;
//    i = 101;  n = ways(i,i);
//    printf("ways_cache[%d][%d] = %d\n", i, i, ways_cache[i][i]);
//    printf("ways(%d,%d) = %d\n", i, i, n);
//    printf("\ndelta iterations = %d\n\n", iterations-prev_iterations);  prev_iterations = iterations;
//
//    i = 1002;  n = ways(i,i);
//    printf("ways_cache[%d][%d] = %d\n", i, i, ways_cache[i][i]);
//    printf("ways(%d,%d) = %d\n", i, i, n);
//    printf("\ndelta iterations = %d\n\n", iterations-prev_iterations);  prev_iterations = iterations;
//
//    i = 1003;  n = ways(i,i);
//    printf("ways_cache[%d][%d] = %d\n", i, i, ways_cache[i][i]);
//    printf("ways(%d,%d) = %d\n", i, i, n);
//    printf("\ndelta iterations = %d\n\n", iterations-prev_iterations);  prev_iterations = iterations;

