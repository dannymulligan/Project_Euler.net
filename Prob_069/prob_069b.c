//!/usr/bin/python
//
// Project Euler.net Problem 69
// 
// Euler's Totient function, phi(n) [sometimes called the phi function],
// is used to determine the number of numbers less than n which are
// relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
// less than nine and relatively prime to nine, phi(9)=6.
// 
//     n    Relatively Prime    phi(n)    n/phi(n)
//     2    1                   1         2
//     3    1,2                 2         1.5
//     4    1,3                 2         2
//     5    1,2,3,4             4         1.25
//     6    1,5                 2         3
//     7    1,2,3,4,5,6         6         1.1666...
//     8    1,3,5,7             4         2
//     9    1,2,4,5,7,8         6         1.5
//     10   1,3,7,9             4         2.5
// 
// It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.
// 
// Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
// 
// Answer: 510510
// n = 510510 gives phi(n) = 92160, n/phi(n) = 5.539388
// Total run time for prob_069a to get to 1,000,000
//    real	807m45.314s
//    user	804m20.432s
//    sys	0m2.980s
// Total run time for prob_069b to get to 511000
//    real	180m23.890s
//    user	179m51.406s
//    sys	0m0.736s


#include <stdio.h>
#include <stdlib.h>

#define MAX 511001
#define CMAX 40000
#define CMAX 40

int gcd_cache[CMAX][CMAX];


int gcd(int a, int b)
{
    int t;

    //    if ((a < CMAX) && (b < CMAX) && (gcd_cache[a][b] != 0))
    //        return gcd_cache[a][b];

    while ((a != b) & (b != 0)) {
        t = b;
        b = a % b;
        a = t;
        //        if ((a < CMAX) && (b < CMAX) && (gcd_cache[a][b] != 0))
        //            return gcd_cache[a][b];
    }
    return a;
}

int phi(int n) {
    int i;

    int ans = 0;
    for (i=0; i<n; i++) {
        if (gcd(i,n) == 1)
            ans += 1;
    }
    return ans;
}

//
// // Debug code
// for b in range(1,max):
//     for a in range(b,max+1):
//         if (a,b) not in gcd_cache:
//             gcd_cache[(a,b)] = gcd(a,b)
// 
// for b in range(max,0,-1):
//     for a in range(1,max+1):
//         if (a,b) in gcd_cache:
//             print "{0:2} ".format(gcd_cache[(a,b)]),
//         else:
//             print "{0:2} ".format(0),
//     print
// print
// 
// for n in range(1,max+1):
//     ans = 0
//     for i in range(1,n):
//         if (gcd_cache[(n,i)] == 1):
//             ans += 1
//     print "{0:2} ".format(ans),
// print
// 
// for n in range(1,max+1):
//     print "{0:2} ".format(phi(n)),
// print

main () 
{
    int n;
    int a, b, a1, tmp;

    // Initialize the gcd_cache
    // 1 - everything in the cache is empty
    for (a=0; a<CMAX; a++)
        for (b=0; b<CMAX; b++)
            gcd_cache[a][b] = 0;
    // 2 - everything is coprime to 1
    for (a=0; a<CMAX; a++)
            gcd_cache[a][1] = 1;
    // 3 - calculate everything else
    for (b=2; b<CMAX; b++) {
        if ((b % 1000) == 0)
            printf("Precalculating gcd(x,%d)\n", b);
        for (a=b+1; (a<CMAX) && (a<2*b); a++) {
            tmp = gcd(a,b);
            a1 = a;
            while (a1 < CMAX) {
                gcd_cache[a1][b] = tmp;
                a1 += b;
            }
        }
    }

    // Initialize the phi array
    int p[MAX];
    for (a=0; a<MAX; a++)
        p[a] = 1;  // Everything is co-prime to 1

//    // Testing code
//    for (n=2; n<101; n++)
//        printf("phi(%d) = %d\n", n, phi(n));
//    exit(0);

    float max_n_phi = 0.0;
    float ftmp;

    // Calculate the p[] array
    for (b=2; b<MAX; b++) {
        if ((b % 1000) == 0)
            printf("Calculating contributions due to gcd(x,%d)\n", b);
//        for (a=b+1; (a<MAX) && (a<2*b); a++) {
//            if (gcd(a,b) == 1) {
        for (a=1; (a+b<MAX) && (a<b); a++) {
//            if (gcd(a+b,b) == 1) {
            if (gcd(b,a) == 1) {
                a1 = a+b;
                while (a1 < MAX+1) {
                    p[a1] += 1;
                    a1 += b;
                }
            }
        }

        // Calculate the max N/phi(n)
        ftmp = (float)b/p[b];
        if (ftmp > max_n_phi) {
            max_n_phi = ftmp;
            printf("n = %d gives phi(n) = %d, n/phi(n) = %f\n", b, p[b], ftmp);
        }
    }


}
