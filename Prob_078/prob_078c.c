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
// Answer 55374
//
// prob_078.c: Searched to 38925 in 2 days 14 hours 10 minutes CPU time
//
//     ways(38925,38925) % 1000000 = 53970
//       C-c C-c
//     
//     real	3778m55.542s
//     user	3716m32.188s
//     sys	14m3.669s
//
// prob_078c.c: Searched to 38925 in 11 hours 33 minutes CPU time
//   = 5.38x faster!

#include <stdio.h>
#include <stdlib.h>

#define CACHE_SIZE 8000
#define OPT_SWITCH 1
#define MOD_SWITCH 1
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int iterations = 0;
int iteration_d = 0;
int prev_iterations = 0;
int debug = 0;
FILE *fp_res;
int ways_cache2[CACHE_SIZE];
int ways_cache[CACHE_SIZE][CACHE_SIZE];

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

    // if (max_n == 2) {
    //     if (debug)  printf("depth=%d ", iteration_d);
    //     if (debug)  printf("ways(%d,%d) = %d (from (max_n == 2) optimization)\n", n, max_n, 1+(n/2));
    //     iteration_d--;
    //     return 1+(n/2);
    // }

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
    int i, x, y;
    for(i = max_n; i > 0; i--) {
        // Iterate as follows
        // i = max_n to 1
        // x = (n-max_n) to (n-1)  ...or... (n-i)
        // y = max_n to 1          ...or... (i)
        // y' = min (x, y)
        // ...then we add ways(x,MIN(x,y)) ...to ans

        x = (n-i);
        y = i;
        y = MIN(x,y);
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("XX    iterating ways(%d,%d)\n", x, y);

        if ((x==y) && (x<CACHE_SIZE) && (ways_cache2[x] != 0)) {
            // Get ways(x,y) from ways_cache2[x]
            if (debug)  printf("depth=%d ", iteration_d);
            if (debug)  printf("XX    ways_cache2[%d] -readB-> %d\n", x, ways_cache2[x]);
            ans = ans + ways_cache2[x];
        } else if (((x+OPT_SWITCH*y)<CACHE_SIZE) && ((y)<CACHE_SIZE) && (ways_cache[x+OPT_SWITCH*y][y] != 0)) {
            // Get ways(x,y) from ways_cache[x+OPT_SWITCH*y][y]
            if (debug)  printf("depth=%d ", iteration_d);
            if (debug)  printf("XX    ways_cache[%d][%d] -readB-> %d\n", x+OPT_SWITCH*y, y, ways_cache[x+OPT_SWITCH*y][y]);
            ans = ans + ways_cache[x+OPT_SWITCH*y][y];
        } else {
            // Get ways(x,y) via recursion
            if (debug)  printf("depth=%d ", iteration_d);
            if (debug)  printf("XX    recursing to ways(%d,%d)\n", x, y);
            ans = ans + ways(x,y);
        }
        if (MOD_SWITCH)  ans = ans % 1000000;
    }

    if ((n==max_n) && (max_n<CACHE_SIZE)) {
        // Save the result in ways_cache2[x]
        ways_cache2[n] = ans;
        fprintf(fp_res, "ways(%d,%d) = %d\n", n, n, ans);
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("XX    ways_cache2[%d] <=write= %d\n", n, ans);
    } else if (((n+OPT_SWITCH*max_n)<CACHE_SIZE) && (max_n<CACHE_SIZE)) {
        // Save the result in ways_cache[x+OPT_SWITCH*y][y]
        ways_cache[n+OPT_SWITCH*max_n][max_n] = ans;
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("XX    ways_cache[%d][%d] <=write= %d\n", n, max_n, ans);
    }
    if (debug)  printf("depth=%d ", iteration_d);
    if (debug)  printf("ways(%d,%d) = %d (from calculation)\n", n, max_n, ans);
    iteration_d--;
    return ans;
}

void init_cache () {
    int n, m;

    // Initialize everything to zero = no present in cache
    for (n=0; n<CACHE_SIZE; n++) {
        ways_cache2[n] = 0;
        for (m=0; m<CACHE_SIZE; m++) {
            ways_cache[n][m] = 0;
        }
    }

    // Optimization: ways(n,0), ways(n,1) are always 1
    for (n=0; n<CACHE_SIZE; n++) {
        ways_cache[n+OPT_SWITCH*0][0] = 1;
        ways_cache[n+OPT_SWITCH*1][1] = 1;
    }

    // Optimization: ways(0,max_n), ways(1,max_n) are always 1
    for (m=0; m<CACHE_SIZE-1; m++) {
        ways_cache[0+OPT_SWITCH*m][m] = 1;
        ways_cache[1+OPT_SWITCH*m][m] = 1;
    }

    // Optimization: ways(n,2) is always 1+(n/2)
    for (n=0; n<CACHE_SIZE-1; n++) {
        ways_cache[n+OPT_SWITCH*2][2] = 1+(n/2);
    }

}

main () {
    int i, j;
    int n;

    fp_res = fopen("./results.txt", "w");
    init_cache();

//    // Use this code to generate test vectors
//    for (i=0; i<121; i=i+1) {
//        n = ways(i,i);
//        printf("ways(%d,%d) = %d\n", i, i, n);
//    }
//    exit(0);

//    for (i=0; i<100; i=i+1) {
//        printf("==== ==== Calculating ways(%d,%d) ==== ====\n", i, i);
//        n = ways(i,i);
//        printf("ways(%d,%d) = %d\n", i, i, n);
//    }
//
//    debug = 1;
//    for (i=100; i<125; i=i+1) {
//        printf("==== ==== Calculating ways(%d,%d) ==== ====\n", i, i);
//        n = ways(i,i);
//        printf("ways(%d,%d) = %d\n", i, i, n);
//    }
//    exit(0);

    debug = 0;
    for (i=0; i<5001; i=i+1) {
        n = ways(i,i);
        if (n == 0) {
            printf("Found!!!   ways(%d,%d) %% 1000000 = %d\n", i, i, n);
            exit(0);
        }
        if ((i % 25) == 0) {
            printf("ways(%d,%d) %% 1000000 = %d\n", i, i, n);
        }
        if ((i % 100) == 0) {
            printf("\ndelta iterations = %d\n\n", iterations-prev_iterations);  prev_iterations = iterations;
        }
    }

    fclose(fp_res);

}
