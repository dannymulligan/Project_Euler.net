// Project Euler.net Problem 52
//
// It can be seen that the number, 125874, and its double, 251748,
// contain exactly the same digits, but in a different order.
// 
// Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
// and 6x, contain the same digits.
//
// $Revision

#include <stdio.h>

int main()
{
    int x, y;
    int p_cnt = 0;
    int i, j, k, l;
    int answer = 0;

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
