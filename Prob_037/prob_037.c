// Project Euler.net Problem 37
//
// The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
// from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
// left: 3797, 379, 37, and 3.
//
// Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
//
// NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
    int sum = 0;
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

    // Check for 2 digit truncatable primes (i.e. < 100)
    printf("// Check for 2 digit truncatable primes (i.e. < 100)\n");
    for (i = 10; i < 100; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        if (tab[10*b + 1*a])  // is BA prime?
        if (tab[a])           // is  A prime?
        if (tab[b])           // is B  prime?
        {
            printf("%d is a 2 digit truncatable prime.\n", i);
            count++;  sum += i;
        }
    }

    // Check for 3 digit truncatable primes (i.e. < 1,000)
    printf("// Check for 3 digit truncatable primes (i.e. < 1,000)\n");
    for (i = 100; i < 1000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        if (tab[               1*c])  // is C   prime?
        if (tab[        10*c + 1*b])  // is CB  prime?
        if (tab[100*c + 10*b + 1*a])  // is CBA prime?
        if (tab[        10*b + 1*a])  // is  BA prime?
        if (tab[               1*a])  // is   A prime?
        {
            printf("%d is a 3 digit truncatable prime.\n", i);
            count++;  sum += i;
        }
    }

    // Check for 4 digit truncatable primes (i.e. < 10,000)
    printf("// Check for 4 digit truncatable primes (i.e. < 10,000)\n");
    for (i = 1000; i < 10000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        if (tab[                        1*d])  // is D    prime?
        if (tab[                 10*d + 1*c])  // is DC   prime?
        if (tab[         100*d + 10*c + 1*b])  // is DCB  prime?
        if (tab[1000*d + 100*c + 10*b + 1*a])  // is DCBA prime?
        if (tab[         100*c + 10*b + 1*a])  // is  CBA prime?
        if (tab[                 10*b + 1*a])  // is   BA prime?
        if (tab[                        1*a])  // is    A prime?
        {
            printf("%d is a 4 digit truncatable prime.\n", i);
            count++;  sum += i;
        }
    }

    // Check for 5 digit truncatable primes (i.e. < 100,000)
    printf("// Check for 5 digit truncatable primes (i.e. < 100,000)\n");
    for (i = 10000; i < 100000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        e = temp % 10;  temp -= e;  temp = temp / 10;
        if (tab[                                  1*e])  // is E     prime?
        if (tab[                           10*e + 1*d])  // is ED    prime?
        if (tab[                   100*e + 10*d + 1*c])  // is EDC   prime?
        if (tab[          1000*e + 100*d + 10*c + 1*b])  // is EDCB  prime?
        if (tab[10000*e + 1000*d + 100*c + 10*b + 1*a])  // is EDCBA prime?
        if (tab[          1000*d + 100*c + 10*b + 1*a])  // is  DCBA prime?
        if (tab[                   100*c + 10*b + 1*a])  // is   CBA prime?
        if (tab[                           10*b + 1*a])  // is    BA prime?
        if (tab[                                  1*a])  // is     A prime?
        {
            printf("%d is a 5 digit truncatable prime.\n", i);
            count++;  sum += i;
        }
    }

    // Check for 6 digit truncatable primes (i.e. < 1,000,000)
    printf("// Check for 5 digit truncatable primes (i.e. < 1,000,000)\n");
    for (i = 100000; i < 1000000; i++) {
        temp = i;
        a = temp % 10;  temp -= a;  temp = temp / 10;
        b = temp % 10;  temp -= b;  temp = temp / 10;
        c = temp % 10;  temp -= c;  temp = temp / 10;
        d = temp % 10;  temp -= d;  temp = temp / 10;
        e = temp % 10;  temp -= e;  temp = temp / 10;
        f = temp % 10;  temp -= f;  temp = temp / 10;
        if (tab[                                             1*f])  // is F      prime?
        if (tab[                                      10*f + 1*e])  // is FE     prime?
        if (tab[                              100*f + 10*e + 1*d])  // is FED    prime?
        if (tab[                     1000*f + 100*e + 10*d + 1*c])  // is FEDC   prime?
        if (tab[           10000*f + 1000*e + 100*d + 10*c + 1*b])  // is FEDCB  prime?
        if (tab[100000*f + 10000*e + 1000*d + 100*c + 10*b + 1*a])  // is FEDCBA prime?
        if (tab[           10000*e + 1000*d + 100*c + 10*b + 1*a])  // is  EDCBA prime?
        if (tab[                     1000*d + 100*c + 10*b + 1*a])  // is   DCBA prime?
        if (tab[                              100*c + 10*b + 1*a])  // is    CBA prime?
        if (tab[                                      10*b + 1*a])  // is     BA prime?
        if (tab[                                             1*a])  // is      A prime?
        {
            printf("%d is a 5 digit truncatable prime.\n", i);
            count++;  sum += i;
        }
    }



    // Report answer
    printf("// Report answer\n");
    printf("Found %d truncatable primes with a sum of %d\n", count, sum);

}
