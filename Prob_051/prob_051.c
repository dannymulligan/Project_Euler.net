// Project Euler.net Problem 51
//
// By replacing the 1st digit of *3, it turns out that six of the nine
// possible values: 13, 23, 43, 53, 73, and 83, are all prime.
// 
// By replacing the 3rd and 4th digits of 56**3 with the same digit,
// this 5-digit number is the first example having seven primes among
// the ten generated numbers, yielding the family: 56003, 56113,
// 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being
// the first member of this family, is the smallest prime with this
// property.
// 
// Find the smallest prime which, by replacing part of the number (not
// necessarily adjacent digits) with the same digit, is part of an
// eight prime value family.
//
// The official solution is 121313, which allows the primes...
//     121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393
// but if you allow leading zeros, then 111857 comes earlier, giving...
//     857, 111857, 222857, 333857, 555857,  666857, 777857, 888857
//
// $Revision

#include <stdio.h>

#define MAXP 100000000   // 100 million
#define SQRT_MAXP 10000  // 10 thousand
#define DIGITS 10  // Maximum number of decimal digits in each prime

char prime[MAXP];


int main()
{
    int x, y;
    int p_cnt = 0;
    int i, j, k, l;
    int answer = 0;

    // Initialize the array to all prime
    printf("// Initialize the array to all prime\n");
    prime[0] = 0;
    prime[1] = 0;
    for (i = 2; i < MAXP; i++) {
        prime[i] = 1;
    }

    // Calculate the primes
    printf("// Calculate the primes below %d\n", MAXP);
    for (i = 2; i < SQRT_MAXP; i++) {
        if (prime[i]) {
            p_cnt++;
            for (j = i*i; j < MAXP; j += i) {
                prime[j] = 0;
            }
        }
    }
    printf("%d primes found in the range 1...%d\n", p_cnt, SQRT_MAXP-1);
    p_cnt = 0;
    for (i = 1; i < MAXP; i++) {
        if (prime[i])  p_cnt++;
    }
    printf("%d primes found in the range 1...%d\n", p_cnt, MAXP-1);

    // Test each prime
    int found_count, best_found_count = 0;
    int replacement_found;
    for (i = 100; i < MAXP/100; i++) {
        if (prime[i]) {
            // Convert the prime to digits
            int prime_digits[DIGITS];  // Prime number candidate split into digits
            int prime_temp = i;
            int result_digits[DIGITS];  // Prime number candidate split into digits
            int result;
            int prime_digits_count = 0;
            for (j = 0; j < DIGITS; j++) {
                prime_digits[j] = prime_temp % 10;
                if (prime_digits[j] != 0)  prime_digits_count = j;
                prime_temp = prime_temp / 10;
            }

            // Try replacing 0 to 9 in the number
            for (j = 0; j <= 9; j++) {
                found_count = 0;
                // Try replacing it with 0 to 9
                for (k = 0; k <= 9; k++) {
                    // Copy to result_digits[] while substituting j for k
                    replacement_found = 0;
                    for (l = 0; l <= prime_digits_count; l++) {
                        result_digits[l] = prime_digits[l];
                        if (result_digits[l] == j) {
                            result_digits[l] = k;
                            replacement_found = 1;
                        }
                    }
                
                    // Check the result for primeness
                    if (replacement_found) {
                        result = 0;
                        for (l = prime_digits_count; l >= 0; l--) {
                            result = (result * 10) + result_digits[l];
                        }
                        if (prime[result]) {
                            found_count++;
                            if ((i == 111857) || (i == 121313)) {
                                printf("%d\n", result);
                            }
                        }
                    }
                }

                // See if this is the best result so far
                if (found_count > best_found_count) {
                    best_found_count = found_count;
                    printf("The prime %d, replacing %d is a member of a family of %d\n", i, j, found_count);
                }

                if ((i == 111857) || (i == 121313)) {
                    printf("The prime %d, replacing %d is a member of a family of %d\n", i, j, found_count);
                }
            }
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("Then answer is %d\n", answer);

}
