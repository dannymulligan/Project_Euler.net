// Project Euler.net Problem 16
//
// 2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
// 
// What is the sum of the digits of the number 2^(1000)?
//
// $Revision

#include <stdio.h>

#define PRECISION 60
#define LIMIT 1000000
#define POWER 1000

//#define PRECISION 4
//#define LIMIT 1000000
//#define POWER 16

int main()
{

    // 2^1000 has about 300 decimal digits
    // We're going to store 6 decimal digits per integer
    // We need an array of about 50 integers
    long d[PRECISION];
    int i, j;

    // Initialize the table
    printf("// Initialize the table\n");
    for (i=1; i<PRECISION; i++) {
        d[i] = 0;
    }
    d[0] = 1;

    // Multiply by 2 POWER times
    printf("// Multiply by 2 POWER times\n");
    for (i=0; i<POWER; i++) {
         // Do the multiply
        for (j=0; j<PRECISION; j++) {
            d[j] = d[j] * 2;
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
