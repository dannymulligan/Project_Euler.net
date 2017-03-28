// Project Euler.net Problem 20
//
// n! means n x (n - 1) x ... x 3 x 2 x 1
//
// Find the sum of the digits in the number 100!

#include <stdio.h>

#define PRECISION 30
#define LIMIT 1000000
#define FACTORIAL 100

int main()
{

    // 100! has about 160 decimal digits
    // We're going to store 6 decimal digits per integer
    // We need an array of about 30 integers
    long d[PRECISION];
    int i, j;

    // Initialize the table
    printf("// Initialize the table\n");
    for (i=1; i<PRECISION; i++) {
        d[i] = 0;
    }
    d[0] = 1;

    // Calculate the factorial
    printf("// Calculate the factorial\n");
    for (i=1; i<FACTORIAL; i++) {
         // Do the multiply
        for (j=0; j<PRECISION; j++) {
            d[j] = d[j] * i;
        }

        // Fix up the array of integers
        long temp;
        for (j=0; j<PRECISION; j++) {
            if (d[j] > LIMIT) {
                temp = d[j] / LIMIT;
                d[j] = d[j] - temp * LIMIT;
                d[j+1] = d[j+1] + temp;
            }
        }

    }

    // Calculate the answer
    int answer = 0;
    char ans_str[12];
    printf("// Calculate the result\n");
    for (i=PRECISION-1; i>=0; i--) {
        sprintf(ans_str, "%06d", d[i]);
        for (j=0; j<6; j++) {
            answer += ans_str[j] - '0';
        }
    }
    printf("\n");

    // Print the answer
    printf("// Print the answer\n");
    for (i=PRECISION-1; i>=0; i--) {
        printf("%06d ", d[i]);
    }
    printf("\n");
    printf("The answer is %d\n", answer);


}
