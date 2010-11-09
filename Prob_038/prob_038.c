// Project Euler.net Problem 38
//
// Take the number 192 and multiply it by each of 1, 2, and 3:
// 
//     192 × 1 = 192
//     192 × 2 = 384
//     192 × 3 = 576
// 
// By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call
// 192384576 the concatenated product of 192 and (1,2,3)
// 
// The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving
// the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
// 
// What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
// concatenated product of an integer with (1,2, ... , n) where n > 1?
//
// $Revision

#include <stdio.h>

#define MAX_P      4000000
#define SQRT_MAX_P    2000
#define CNT 1001

// Possible scenarios...
// XXXXXX x (1,2) = 9 digits, provided XXXXX = impossible
// XXXXX x (1,2) = 9 digits, provided XXXX = impossible
// XXXX x (1,2) = 9 digits, provided XXXX > 5000
// XXX x (1,2,3) = 9 digits, provided XXX < 334
// XX x (1,2,3,4) = 9 digits, provided XX > 25 & X < 34
// X x (1,2,3,4,5,6,7,8,9) = 9 digits, provided X = 1
// X x (1,2,3,4,5,6,7,8) = 9 digits, provided X = impossible
// X x (1,2,3,4,5,6,7) = 9 digits, provided X = impossible
// X x (1,2,3,4,5,6) = 9 digits, provided X < 4
// X x (1,2,3,4,5) = 9 digits, provided X > 4
// X x (1,2,3,4) = 9 digits, provided X = impossible
// X x (1,2,3) = 9 digits, provided X = impossible
// X x (1,2) = 9 digits, provided X = impossible
 
int main()
{
    int x, y;
    int a[6], b[6], c[6], d[6], e[6], f[6], g[6], h[6], i[6];
    int dig[10];
    int len;
    int t1, t0;

    // Test all the possibilities
    for (x = 1; x < 9999; x++) {
        len = 0;

        a[0] = x;
        if ((a[0] >= 1    ) && (a[0] < 10    ))  len += 1;
        if ((a[0] >= 10   ) && (a[0] < 100   ))  len += 2;
        if ((a[0] >= 100  ) && (a[0] < 1000  ))  len += 3;
        if ((a[0] >= 1000 ) && (a[0] < 10000 ))  len += 4;
        if ((a[0] >= 10000) && (a[0] < 100000))  len += 5;
        t0 = a[0];
        a[1] = t0 % 10;  t0 -= a[1];  t0 = t0 / 10;
        a[2] = t0 % 10;  t0 -= a[2];  t0 = t0 / 10;
        a[3] = t0 % 10;  t0 -= a[3];  t0 = t0 / 10;
        a[4] = t0 % 10;  t0 -= a[4];  t0 = t0 / 10;
        a[5] = t0 % 10;  t0 -= a[5];  t0 = t0 / 10;

        if (len < 9)  b[0] = x * 2;  else  b[0] = 0;
        if ((b[0] >= 1    ) && (b[0] < 10    ))  len += 1;
        if ((b[0] >= 10   ) && (b[0] < 100   ))  len += 2;
        if ((b[0] >= 100  ) && (b[0] < 1000  ))  len += 3;
        if ((b[0] >= 1000 ) && (b[0] < 10000 ))  len += 4;
        if ((b[0] >= 10000) && (b[0] < 100000))  len += 5;
        t0 = b[0];
        b[1] = t0 % 10;  t0 -= b[1];  t0 = t0 / 10;
        b[2] = t0 % 10;  t0 -= b[2];  t0 = t0 / 10;
        b[3] = t0 % 10;  t0 -= b[3];  t0 = t0 / 10;
        b[4] = t0 % 10;  t0 -= b[4];  t0 = t0 / 10;
        b[5] = t0 % 10;  t0 -= b[5];  t0 = t0 / 10;

        if (len < 9)  c[0] = x * 3;  else  c[0] = 0;
        if ((c[0] >= 1    ) && (c[0] < 10    ))  len += 1;
        if ((c[0] >= 10   ) && (c[0] < 100   ))  len += 2;
        if ((c[0] >= 100  ) && (c[0] < 1000  ))  len += 3;
        if ((c[0] >= 1000 ) && (c[0] < 10000 ))  len += 4;
        if ((c[0] >= 10000) && (c[0] < 100000))  len += 5;
        t0 = c[0];
        c[1] = t0 % 10;  t0 -= c[1];  t0 = t0 / 10;
        c[2] = t0 % 10;  t0 -= c[2];  t0 = t0 / 10;
        c[3] = t0 % 10;  t0 -= c[3];  t0 = t0 / 10;
        c[4] = t0 % 10;  t0 -= c[4];  t0 = t0 / 10;
        c[5] = t0 % 10;  t0 -= c[5];  t0 = t0 / 10;

        if (len < 9)  d[0] = x * 4;  else  d[0] = 0;
        if ((d[0] >= 1    ) && (d[0] < 10    ))  len += 1;
        if ((d[0] >= 10   ) && (d[0] < 100   ))  len += 2;
        if ((d[0] >= 100  ) && (d[0] < 1000  ))  len += 3;
        if ((d[0] >= 1000 ) && (d[0] < 10000 ))  len += 4;
        if ((d[0] >= 10000) && (d[0] < 100000))  len += 5;
        t0 = d[0];
        d[1] = t0 % 10;  t0 -= d[1];  t0 = t0 / 10;
        d[2] = t0 % 10;  t0 -= d[2];  t0 = t0 / 10;
        d[3] = t0 % 10;  t0 -= d[3];  t0 = t0 / 10;
        d[4] = t0 % 10;  t0 -= d[4];  t0 = t0 / 10;
        d[5] = t0 % 10;  t0 -= d[5];  t0 = t0 / 10;

        if (len < 9)  e[0] = x * 5;  else  e[0] = 0;
        if ((e[0] >= 1    ) && (e[0] < 10    ))  len += 1;
        if ((e[0] >= 10   ) && (e[0] < 100   ))  len += 2;
        if ((e[0] >= 100  ) && (e[0] < 1000  ))  len += 3;
        if ((e[0] >= 1000 ) && (e[0] < 10000 ))  len += 4;
        if ((e[0] >= 10000) && (e[0] < 100000))  len += 5;
        t0 = e[0];
        e[1] = t0 % 10;  t0 -= e[1];  t0 = t0 / 10;
        e[2] = t0 % 10;  t0 -= e[2];  t0 = t0 / 10;
        e[3] = t0 % 10;  t0 -= e[3];  t0 = t0 / 10;
        e[4] = t0 % 10;  t0 -= e[4];  t0 = t0 / 10;
        e[5] = t0 % 10;  t0 -= e[5];  t0 = t0 / 10;

        if (len < 9)  f[0] = x * 6;  else  f[0] = 0;
        if ((f[0] >= 1    ) && (f[0] < 10    ))  len += 1;
        if ((f[0] >= 10   ) && (f[0] < 100   ))  len += 2;
        if ((f[0] >= 100  ) && (f[0] < 1000  ))  len += 3;
        if ((f[0] >= 1000 ) && (f[0] < 10000 ))  len += 4;
        if ((f[0] >= 10000) && (f[0] < 100000))  len += 5;
        t0 = f[0];
        f[1] = t0 % 10;  t0 -= f[1];  t0 = t0 / 10;
        f[2] = t0 % 10;  t0 -= f[2];  t0 = t0 / 10;
        f[3] = t0 % 10;  t0 -= f[3];  t0 = t0 / 10;
        f[4] = t0 % 10;  t0 -= f[4];  t0 = t0 / 10;
        f[5] = t0 % 10;  t0 -= f[5];  t0 = t0 / 10;

        if (len < 9)  g[0] = x * 7;  else  g[0] = 0;
        if ((g[0] >= 1    ) && (g[0] < 10    ))  len += 1;
        if ((g[0] >= 10   ) && (g[0] < 100   ))  len += 2;
        if ((g[0] >= 100  ) && (g[0] < 1000  ))  len += 3;
        if ((g[0] >= 1000 ) && (g[0] < 10000 ))  len += 4;
        if ((g[0] >= 10000) && (g[0] < 100000))  len += 5;
        t0 = g[0];
        g[1] = t0 % 10;  t0 -= g[1];  t0 = t0 / 10;
        g[2] = t0 % 10;  t0 -= g[2];  t0 = t0 / 10;
        g[3] = t0 % 10;  t0 -= g[3];  t0 = t0 / 10;
        g[4] = t0 % 10;  t0 -= g[4];  t0 = t0 / 10;
        g[5] = t0 % 10;  t0 -= g[5];  t0 = t0 / 10;

        if (len < 9)  h[0] = x * 8;  else  h[0] = 0;
        if ((h[0] >= 1    ) && (h[0] < 10    ))  len += 1;
        if ((h[0] >= 10   ) && (h[0] < 100   ))  len += 2;
        if ((h[0] >= 100  ) && (h[0] < 1000  ))  len += 3;
        if ((h[0] >= 1000 ) && (h[0] < 10000 ))  len += 4;
        if ((h[0] >= 10000) && (h[0] < 100000))  len += 5;
        t0 = h[0];
        h[1] = t0 % 10;  t0 -= h[1];  t0 = t0 / 10;
        h[2] = t0 % 10;  t0 -= h[2];  t0 = t0 / 10;
        h[3] = t0 % 10;  t0 -= h[3];  t0 = t0 / 10;
        h[4] = t0 % 10;  t0 -= h[4];  t0 = t0 / 10;
        h[5] = t0 % 10;  t0 -= h[5];  t0 = t0 / 10;

        if (len < 9)  i[0] = x * 9;  else  i[0] = 0;
        if ((i[0] >= 1    ) && (i[0] < 10    ))  len += 1;
        if ((i[0] >= 10   ) && (i[0] < 100   ))  len += 2;
        if ((i[0] >= 100  ) && (i[0] < 1000  ))  len += 3;
        if ((i[0] >= 1000 ) && (i[0] < 10000 ))  len += 4;
        if ((i[0] >= 10000) && (i[0] < 100000))  len += 5;
        t0 = i[0];
        i[1] = t0 % 10;  t0 -= i[1];  t0 = t0 / 10;
        i[2] = t0 % 10;  t0 -= i[2];  t0 = t0 / 10;
        i[3] = t0 % 10;  t0 -= i[3];  t0 = t0 / 10;
        i[4] = t0 % 10;  t0 -= i[4];  t0 = t0 / 10;
        i[5] = t0 % 10;  t0 -= i[5];  t0 = t0 / 10;


        for (y = 0; y < 10; y++) {
            dig[y] = 0;
        }
        dig[a[1]]++; dig[a[2]]++; dig[a[3]]++; dig[a[4]]++; dig[a[5]]++;
        dig[b[1]]++; dig[b[2]]++; dig[b[3]]++; dig[b[4]]++; dig[b[5]]++;
        dig[c[1]]++; dig[c[2]]++; dig[c[3]]++; dig[c[4]]++; dig[c[5]]++;
        dig[d[1]]++; dig[d[2]]++; dig[d[3]]++; dig[d[4]]++; dig[d[5]]++;
        dig[e[1]]++; dig[e[2]]++; dig[e[3]]++; dig[e[4]]++; dig[e[5]]++;
        dig[f[1]]++; dig[f[2]]++; dig[f[3]]++; dig[f[4]]++; dig[f[5]]++;
        dig[g[1]]++; dig[g[2]]++; dig[g[3]]++; dig[g[4]]++; dig[g[5]]++;
        dig[h[1]]++; dig[h[2]]++; dig[h[3]]++; dig[h[4]]++; dig[h[5]]++;
        dig[i[1]]++; dig[i[2]]++; dig[i[3]]++; dig[i[4]]++; dig[i[5]]++;

        if (len == 9)
        if ((dig[1] == 1) && (dig[2] == 1) && (dig[3] == 1) &&
            (dig[4] == 1) && (dig[5] == 1) && (dig[6] == 1) &&
            (dig[7] == 1) && (dig[8] == 1) && (dig[9] == 1))
            printf("Found x=%d, a=%d, b=%d, c=%d, d=%d, e=%d, f=%d, g=%d, h=%d, i=%d\n", x, a[0], b[0], c[0], d[0], e[0], f[0], g[0], h[0], i[0]);
    }


    // Report answer
    printf("// Report answer\n");
}
