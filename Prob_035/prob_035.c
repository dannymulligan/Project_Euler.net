// Project Euler.net Problem 35
//
// The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
//
// There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
//
// How many circular primes are there below one million?
//
// $Revision

#include <stdio.h>

#define MAXP 1000000
#define SQRT_MAXP 1000

int main()
{
    int i, j;
    char tab[MAXP];
    int count = 0;
    int a, b, c, d, e, f;
    int temp;

    // Initialize the array to all prime
    printf("// Initialize the array to all prime\n");
    tab[0] = 0;
    tab[1] = 0;
    for (i = 2; i < MAXP; i++) {
        tab[i] = 1;
    }

    // Calculate the primes
    printf("// Calculate the primes\n");
    for (i = 2; i < SQRT_MAXP; i++) {
        if (tab[i]) {
            for (j = i*i; j < MAXP; j += i) {
                tab[j] = 0;
            }
        }
    }

    // Calculate the 1 digit circular primes (i.e. < 10)
    printf("// Calculate the 1 digit circulor primes (i.e. < 10)\n");
    for (i = 0; i < 10; i++) {
        a = i;
        if (tab[a])  // is A prime?
        {
            printf("%d is a circular prime.\n", i);
            count++;
        }
    }

    // Calculate the 2 digit circular primes (i.e. < 100)
    printf("// Calculate the 2 digit circulor primes (i.e. < 100)\n");
    for (i = 10; i < 100; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        if (tab[10*b + 1*a])  // is BA prime?
        if (tab[10*a + 1*b])  // is AB prime?
        {
            printf("%d is a circular prime.\n", i);
            count++;
        }
    }

    // Calculate the 3 digit circular primes (i.e. < 1,000)
    printf("// Calculate the 3 digit circulor primes (i.e. < 1,000)\n");
    for (i = 100; i < 1000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        if (tab[100*c + 10*b + 1*a])  // is CBA prime?
        if (tab[100*b + 10*a + 1*c])  // is BAC prime?
        if (tab[100*a + 10*c + 1*b])  // is ACB prime?
        {
            printf("%d is a circular prime.\n", i);
            count++;
        }
    }

    // Calculate the 4 digit circular primes (i.e. < 10,000)
    printf("// Calculate the 4 digit circulor primes (i.e. < 10,000)\n");
    for (i = 1000; i < 10000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        if (tab[1000*d + 100*c + 10*b + 1*a])  // is DCBA prime?
        if (tab[1000*c + 100*b + 10*a + 1*d])  // is CBAD prime?
        if (tab[1000*b + 100*a + 10*d + 1*c])  // is BADC prime?
        if (tab[1000*a + 100*d + 10*c + 1*b])  // is ADCB prime?
        {
            printf("%d is a circular prime.\n", i);
            count++;
        }
    }

    // Calculate the 5 digit circular primes (i.e. < 100,000)
    printf("// Calculate the 5 digit circulor primes (i.e. < 100,000)\n");
    for (i = 10000; i < 100000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        e = temp % 10;  temp -= e;  temp = temp / 10;
        if (tab[10000*e + 1000*d + 100*c + 10*b + 1*a])  // is EDCBA prime?
        if (tab[10000*d + 1000*c + 100*b + 10*a + 1*e])  // is DCBAE prime?
        if (tab[10000*c + 1000*b + 100*a + 10*e + 1*d])  // is CBAED prime?
        if (tab[10000*b + 1000*a + 100*e + 10*d + 1*c])  // is BAEDC prime?
        if (tab[10000*a + 1000*e + 100*d + 10*c + 1*b])  // is AEDCB prime?
        {
            printf("%d is a circular prime.\n", i);
            count++;
        }
    }

    // Calculate the 6 digit circular primes (i.e. < 1,000,000)
    printf("// Calculate the 6 digit circulor primes (i.e. < 1,000,000)\n");
    for (i = 100000; i < 1000000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        e = temp % 10;  temp -= e;  temp = temp / 10;
        f = temp % 10;  temp -= f;  temp = temp / 10;
        if (tab[100000*f + 10000*e + 1000*d + 100*c + 10*b + 1*a])  // is FEDCBA prime?
        if (tab[100000*e + 10000*d + 1000*c + 100*b + 10*a + 1*f])  // is EDCBAF prime?
        if (tab[100000*d + 10000*c + 1000*b + 100*a + 10*f + 1*e])  // is DCBAFE prime?
        if (tab[100000*c + 10000*b + 1000*a + 100*f + 10*e + 1*d])  // is CBAFED prime?
        if (tab[100000*b + 10000*a + 1000*f + 100*e + 10*d + 1*c])  // is BAFEDC prime?
        if (tab[100000*a + 10000*f + 1000*e + 100*d + 10*c + 1*b])  // is AFEDCB prime?
        {
            printf("%d is a circular prime.\n", i);
            count++;
        }
    }

    // Report answer
    printf("// Report answer\n");
    printf("Found %d circular primes\n", count);

}
