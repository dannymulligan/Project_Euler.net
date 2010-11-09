// Project Euler.net Problem 82
//
// In the 5 by 5 matrix below, the minimal path sum from the top left to
// the bottom right, by only moving to the right and down, is indicated
// in red and is equal to 2427.
//         
//    >131<    673     234     103      18
//    >201<    >96<   >342<    965     150
//     630     803    >746<   >422<    111
//     537     699     497    >121<    956
//     805     732     524     >37<   >331<
// 
// Find the minimal path sum, in matrix.txt (right click and 'Save
// Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
// from the top left to the bottom right by only moving right and down.
// 
// $Revision

#include <stdio.h>

#define DIM 80

int dat[DIM][DIM];
int best[DIM][DIM];


int main()
{

    int i, j;
    FILE *fin;

    // Read in matrix from std-in
    printf("// Read in matrix from matrix.txt\n");
    fin = fopen("matrix.txt", "r");
 // fin = fopen("mini_matrix.txt", "r");
    for (i=0; i<DIM; i++) {
        for (j=0; j<DIM-1; j++) {
            (void)fscanf(fin, "%d,", &dat[i][j]);
        }
        (void)fscanf(fin, "%d", &dat[i][j]);
    }

    // Print out the matrix
    printf("// Print out the matrix\n");
    for (i=0; i<DIM; i++) {
        for (j=0; j<DIM-1; j++) {
            printf("%d,", dat[i][j]);
        }
        printf("%d\n", dat[i][j]);
    }

    // Fill out the initial guess at the best matrix
    best[0][0] = dat[0][0];
    // Fill out [1..DIM-1][0] assuming D moves
    for (i=1; i<DIM; i++) {
        best[i][0] = best[i-1][0] + dat[i][0];
    }
    // Fill out [0..DIM-1][1..DIM-1] assuming R moves
    for (i=0; i<DIM; i++) {
        for (j=1; j<DIM; j++) {
            best[i][j] = best[i][j-1] + dat[i][j];
        }
    }

    // Look for better alternatives from U and D moves
    int progress;
    do {
        progress = 0;

        // Look for D moves that make progress
        for (i=1; i<DIM; i++) {
            for (j=0; j<DIM; j++) {
                if ((best[i-1][j] + dat[i][j]) < best[i][j]) {
                    progress = 1;
                    best[i][j] = best[i-1][j] + dat[i][j];
                }
            }
        }

        // Look for R moves that make progress
        for (i=0; i<DIM; i++) {
            for (j=1; j<DIM; j++) {
                if ((best[i][j-1] + dat[i][j]) < best[i][j]) {
                    progress = 1;
                    best[i][j] = best[i][j-1] + dat[i][j];
                }
            }
        }
    } while (progress);

    // Print out the solution matrix
    printf("// Print out the solution matrix\n");
    for (i=0; i<DIM; i++) {
        for (j=0; j<DIM-1; j++) {
            printf("%d,", best[i][j]);
        }
        printf("%d\n", best[i][j]);
    }

    // Report answer
    printf("// Report answer\n");
    printf("Answer is %d\n", best[DIM-1][DIM-1]);

}
