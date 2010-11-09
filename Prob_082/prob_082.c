// Project Euler.net Problem 82
//
// NOTE: This problem is a more challenging version of Problem 81.
// 
// The minimal path sum in the 5 by 5 matrix below, by starting in any
// cell in the left column and finishing in any cell in the right column,
// and only moving up, down, and right, is indicated in red; the sum is
// equal to 994.
// 
//     131     673    >234<   >103<    >18<
//    >201<    >96<   >342<    965     150
//     630     803     746     422     111
//     537     699     497     121     956
//     805     732     524      37     331
// 
// Find the minimal path sum, in matrix.txt (right click and 'Save
// Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
// from the left column to the right column.
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

    // Fill out the first column
    for (i=0; i<DIM; i++) {
        best[i][0] = dat[i][0];
    }

    // Fill out 2nd and subsequent columns
    for (j=1; j<DIM; j++) {
        // Start by assuming a R move
        for (i=0; i<DIM; i++) {
            best[i][j] = best[i][j-1] + dat[i][j];
        }

        // The look for better alternatives from U and D moves
        int progress;
        do {
            progress = 0;

            // Look for a better U move
            for (i=0; i<DIM-1; i++) {
                if ((best[i+1][j] + dat[i][j]) < best[i][j]) {
                    progress = 1;
                    best[i][j] = best[i+1][j] + dat[i][j];
                }
            }

            // Look for a better D move
            for (i=DIM-1; i>0; i--) {
                if ((best[i-1][j] + dat[i][j]) < best[i][j]) {
                    progress = 1;
                    best[i][j] = best[i-1][j] + dat[i][j];
                }
            }
        } while (progress);

    }

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
    int min = best[0][DIM-1];
    for (i=0; i<DIM; i++) {
        if (best[i][DIM-1] < min)
            min = best[i][DIM-1];
    }
    printf("Answer is %d\n", min);

}
