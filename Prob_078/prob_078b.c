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

#define CACHE_SIZE 10000
#define OPT_SWITCH 1
#define MOD_SWITCH 1
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int ways_cache[CACHE_SIZE][CACHE_SIZE];
int iterations = 0;
int iteration_d = 0;
int prev_iterations = 0;
int debug = 0;

long ways(int n, int max_n)
{
    int temp;

    iterations++;
    iteration_d++;
    // if (debug)  printf("depth=%d ", iteration_d);
    // if (debug)  printf("Calling ways(%d,%d)\n", n, max_n);

    if ((n <= 1) || (max_n <= 1)) {
        if (debug)  printf("ways(%d,%d) = %d (from ((n <= 1) || (max_n <= 1)) optimization)\n", n, max_n, 1);
        iteration_d--;
        return 1;
    }

    if (max_n == 2) {
        if (debug)  printf("ways(%d,%d) = %d (from (max_n == 2) optimization)\n", n, max_n, 1+(n/2));
        return 1+(n/2);
    }

    if (((n+OPT_SWITCH*max_n)<CACHE_SIZE) && (max_n<CACHE_SIZE) && (ways_cache[n+OPT_SWITCH*max_n][max_n] != 0)) {
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("ways(%d,%d) = %d (from ways_cache[%d][%d])\n", n, max_n, ways_cache[n+OPT_SWITCH*max_n][max_n], n+OPT_SWITCH*max_n, max_n);
        temp = ways_cache[n+OPT_SWITCH*max_n][max_n];
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("XX    ways_cache[%d][%d] -readA-> %d\n", n+OPT_SWITCH*max_n, max_n, temp);
        iteration_d--;
        return temp;
    }

    int ans = 0;
    int i;
    int nn = (n<max_n) ? n : max_n;  // nn = min(n, max_n)
    for(i = nn; i > 0; i--) {
        int ii = (nn<i) ? nn : i;  // ii = min(nn, i)
        if (debug)  printf("XX> iterating i=%d, n=%d, max_n=%d, ii=%d, nn=%d\n", i, n, max_n, ii, nn);
        if (((n-i+OPT_SWITCH*ii)<CACHE_SIZE) && (ii<CACHE_SIZE) && (ways_cache[n-i+OPT_SWITCH*ii][ii] != 0)) {
            temp = ways_cache[n-i+OPT_SWITCH*ii][ii];  // i coins, followed by all possible combinations of n-i
            if (debug)  printf("XX    ways_cache[%d][%d] -readB-> %d\n", n-i+OPT_SWITCH*ii, ii, temp);
            ans = (ans + temp);
            if (MOD_SWITCH)  ans = ans % 1000000;
        } else {
            if (debug)  printf("XX> recursing ways(%d,%d)\n", n-i, ii);
            temp = ways(n-i,ii);  // i coins, followed by all possible combinations of n-i
            ans = (ans + temp);
            if (MOD_SWITCH)  ans = ans % 1000000;
        }
    }

    if (((n+OPT_SWITCH*max_n)<CACHE_SIZE) && (max_n<CACHE_SIZE)) {
        ways_cache[n+OPT_SWITCH*max_n][max_n] = ans;
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("XX    ways_cache[%d][%d] <=write= %d\n", n+OPT_SWITCH*max_n, max_n, ans);
    }
    if (debug)  printf("depth=%d ", iteration_d);
    if (debug)  printf("ways(%d,%d) = %d (from calculation)\n", n, max_n, ans);
    iteration_d--;
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

//    // Use this code to generate test vectors
//    for (i=0; i<121; i=i+1) {
//        n = ways(i,i);
//        printf("ways(%d,%d) = %d\n", i, i, n);
//    }
//    exit(0);

    debug = 0;
    for (i=0; i<4001; i=i+1) {
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
