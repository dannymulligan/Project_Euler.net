// Project Euler.net Problem 28
//
// Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
// 
//     21 22 23 24 25
//     20  7  8  9 10
//     19  6  1  2 11
//     18  5  4  3 12
//     17 16 15 14 13
// 
// It can be verified that the sum of both diagonals is 101.
// 
// What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?
//
// $Revision

#include <stdio.h>

#define SIZE 1001

int main()
{
    int x, y;
    int d[SIZE][SIZE];
    long long sum_a = 0;
    long long sum_b = 0;

    // Initialize the spiral
    printf("// Initialize the spiral\n");
    for (x = 0; x < SIZE; x++) {
        for (y = 0; y < SIZE; y++) {
            d[x][y] = 0;
        }
    }

    // Set up the spiral
    int i = 1;
    int dir = 0;  // 0 = up, 1 = right; 2 = down; 3 = left
    printf("// Set up the spiral\n");
    x = (SIZE-1)/2;  y = (SIZE-1)/2;
    do{
        // printf("d[%d][%d] = %d, dir = %d\n", x, y, i, dir);
        d[x][y] = i++;

        if (dir == 0)       // direction = up
        {
            if (d[x+1][y] == 0)  { x = x + 1;  y = y + 0;  dir = 1; }
            else                 { x = x + 0;  y = y + 1;  dir = 0; }
        }
        else if (dir == 1)  // direction = right
        {
            if (d[x][y-1] == 0)  { x = x + 0;  y = y - 1;  dir = 2; }
            else                 { x = x + 1;  y = y + 0;  dir = 1; }
        }
        else if (dir == 2)  // direction = down
        {
            if (d[x-1][y] == 0)  { x = x - 1;  y = y + 0;  dir = 3; }
            else                 { x = x + 0;  y = y - 1;  dir = 2; }
        }
        else if (dir == 3)  // direction = left
        {
            if (d[x][y+1] == 0)  { x = x + 0;  y = y + 1;  dir = 0; }
            else                 { x = x - 1;  y = y + 0;  dir = 3; }
        }

    } while (i <= SIZE*SIZE);

    // Print the spiral
//    printf("// Print the spiral\n");
//    for (y = 0; y < SIZE; y++) {
//        for (x = 0; x < SIZE; x++) {
//            printf("%4d, ",d[x][y]);
//        }
//        printf("\n");
//    }

    // Add up the diagonals
    printf("// Add up the diagonals\n");
    for (x = 0; x < SIZE; x++)  sum_a += d[x][x];
    for (x = 0; x < SIZE; x++)  sum_a += d[x][SIZE-1-x];

    // Print the answer
    printf("// Print the answer\n");
    x = (SIZE-1)/2;  y = (SIZE-1)/2;
    printf("The answer is %d\n", (sum_a + sum_b - d[x][y]));

}
