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
//     real	3778m55.542s = 226,735.542s
//     user	3716m32.188s
//     sys	14m3.669s
//
// prob_078c.c: Searched to 38925 in 11 hours 33 minutes CPU time
//   = 5.38x faster then prob_078.c!
//
// prob_078d.c: Searched to 39000 in 39.678 seconds
//   = 5,714x faster than prob_078.c!
//   = 1,048x faster than prob_078c.c!
//
// prob_078e.c: Searched to 55374 in 161.290 seconds
//   = 4,047x faster than prob_078.c!  (assuming prob_078.c needed 8x CPU time to search 2x deeper)
//   Solution found!
//
// Note: compile with...
//    gcc -g -o prob_078e -mcmodel=medium prob_078e.c && time ./prob_078e

#include <stdio.h>
#include <stdlib.h>

#define CACHE_SIZE 28000
#define MOD_SWITCH 1
#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int iterations = 0;
int iteration_d = 0;
int prev_iterations = 0;
int debug = 0;
FILE *fp_res;
int ways_cache[CACHE_SIZE*2][CACHE_SIZE];

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

    if ((n<CACHE_SIZE*2) && (max_n<CACHE_SIZE) && (ways_cache[n][max_n] != 0)) {
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("ways(%d,%d) = %d (from ways_cache[%d][%d])\n", n, max_n, ways_cache[n][max_n], n, max_n);
        temp = ways_cache[n][max_n];
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("XX    ways_cache[%d][%d] -readA-> %d\n", n, max_n, temp);
        iteration_d--;
        return temp;
    }

    int ans = 0;
    int i, x, y;
    for(i = 1; i <= max_n; i++) {
        // Iterate as follows
        // i = 1 to max_n
        // x = (n-1) to (n-max_n)  ...or... (n-i)
        // y = 1 to max_n          ...or... (i)
        // y' = min (x, y)
        // ...then we add ways(x,MIN(x,y)) ...to ans

        x = (n-i);
        y = i;
        y = MIN(x,y);
        if (debug)  printf("depth=%d ", iteration_d);
        if (debug)  printf("XX    iterating ways(%d,%d)\n", x, y);

        if ((x<CACHE_SIZE*2) && (y<CACHE_SIZE) && (ways_cache[x][y] != 0)) {
            // Get ways(x,y) from ways_cache[x][y]
            if (debug)  printf("depth=%d ", iteration_d);
            if (debug)  printf("XX    ways_cache[%d][%d] -readC-> %d\n", x, y, ways_cache[x][y]);
            ans = ans + ways_cache[x][y];
        } else {
            // Get ways(x,y) via recursion
            if (debug)  printf("depth=%d ", iteration_d);
            if (debug)  printf("XX    recursing to ways(%d,%d)\n", x, y);
            ans = ans + ways(x,y);
        }
        if (MOD_SWITCH)  ans = ans % 1000000;

        // each intermediate step calculates a different ways value
        //   when i = 1, we have calculated ways(n,0)
        //   when i = 2, we have calculated ways(n,2)
        // so we store these values in ways_cache[n][i]
        if ((n<CACHE_SIZE*2) && (i<CACHE_SIZE)) {
            // Save the result in ways_cache[n][i]
            ways_cache[n][i] = ans;
            if (debug)  printf("depth=%d ", iteration_d);
            if (debug)  printf("XX    ways_cache[%d][%d] <=write= %d\n", n, i, ans);
        }
    }

    if (debug)  printf("depth=%d ", iteration_d);
    if (debug)  printf("ways(%d,%d) = %d (from calculation)\n", n, max_n, ans);
    iteration_d--;
    return ans;
}

void init_cache () {
    int n, m;

    // Initialize everything to zero = not present in cache
    for (n=0; n<CACHE_SIZE*2; n++) {
        for (m=0; m<CACHE_SIZE; m++) {
            ways_cache[n][m] = 0;
        }
    }

    // Optimization: ways(n,0), ways(n,1) are always 1
    for (n=0; n<CACHE_SIZE*2; n++) {
        ways_cache[n][0] = 1;
        ways_cache[n][1] = 1;
    }

    // Optimization: ways(0,max_n), ways(1,max_n) are always 1
    for (m=0; m<CACHE_SIZE; m++) {
        ways_cache[0][m] = 1;
        ways_cache[1][m] = 1;
    }

    // Optimization: ways(n,2) is always 1+(n/2)
    for (n=0; n<CACHE_SIZE*2; n++) {
        ways_cache[n][2] = 1+(n/2);
    }

}

main () {
    int i, j;
    int n;

    fp_res = fopen("./results.txt", "w");
    init_cache();

//    // Use this code to generate test vectors
//    for (i=0; i<121; i=i+1) {
//        //        if (i==102)  debug = 1;
//        prev_iterations = iterations;
//        n = ways(i,i);
//        //printf("ways(%d,%d) = %d calculated in %d iterations\n", i, i, n, iterations-prev_iterations);
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
    for (i=0; i<56001; i=i+1) {
        n = ways(i,i);
        fprintf(fp_res, "ways(%d,%d) = %d\n", i, i, n);
        if (n == 0) {
            printf("Found!!!   ways(%d,%d) %% 1000000 = %d\n", i, i, n);
            exit(0);
        }
        if ((i % 25) == 0) {
            printf("ways(%d,%d) %% 1000000 = %d\n", i, i, n);
        }
        if ((i % 1000) == 0) {
            printf("\ndelta iterations = %d\n\n", iterations-prev_iterations);
            prev_iterations = iterations;
        }
    }

    fclose(fp_res);

}
