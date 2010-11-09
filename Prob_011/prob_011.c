// Project Euler.net Problem 11
//
// In the 20�20 grid below, four numbers along a diagonal line have been marked in red.
// 
//     08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
//     49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
//     81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
//     52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
//     22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
//     24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
//     32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
//     67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
//     24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
//     21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
//     78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
//     16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
//     86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
//     19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
//     04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
//     88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
//     04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
//     20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
//     20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
//     01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
// 
// The product of these numbers is 26 � 63 � 78 � 14 = 1788696.
// 
// What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20�20 grid?
//
// $Revision

#include <stdio.h>


int main()
{

    // Set up the number in an array
    int d[20][20];
    int x, y = 0;
    x = 0;  d[x++][y] =  8; d[x++][y] =  2; d[x++][y] = 22; d[x++][y] = 97; d[x++][y] = 38; d[x++][y] = 15; d[x++][y] =  0; d[x++][y] = 40; d[x++][y] =  0; d[x++][y] = 75; d[x++][y] =  4; d[x++][y] =  5; d[x++][y] =  7; d[x++][y] = 78; d[x++][y] = 52; d[x++][y] = 12; d[x++][y] = 50; d[x++][y] = 77; d[x++][y] = 91; d[x++][y++] =  8;
    x = 0;  d[x++][y] = 49; d[x++][y] = 49; d[x++][y] = 99; d[x++][y] = 40; d[x++][y] = 17; d[x++][y] = 81; d[x++][y] = 18; d[x++][y] = 57; d[x++][y] = 60; d[x++][y] = 87; d[x++][y] = 17; d[x++][y] = 40; d[x++][y] = 98; d[x++][y] = 43; d[x++][y] = 69; d[x++][y] = 48; d[x++][y] =  4; d[x++][y] = 56; d[x++][y] = 62; d[x++][y++] =  0;
    x = 0;  d[x++][y] = 81; d[x++][y] = 49; d[x++][y] = 31; d[x++][y] = 73; d[x++][y] = 55; d[x++][y] = 79; d[x++][y] = 14; d[x++][y] = 29; d[x++][y] = 93; d[x++][y] = 71; d[x++][y] = 40; d[x++][y] = 67; d[x++][y] = 53; d[x++][y] = 88; d[x++][y] = 30; d[x++][y] =  3; d[x++][y] = 49; d[x++][y] = 13; d[x++][y] = 36; d[x++][y++] = 65;
    x = 0;  d[x++][y] = 52; d[x++][y] = 70; d[x++][y] = 95; d[x++][y] = 23; d[x++][y] =  4; d[x++][y] = 60; d[x++][y] = 11; d[x++][y] = 42; d[x++][y] = 69; d[x++][y] = 24; d[x++][y] = 68; d[x++][y] = 56; d[x++][y] =  1; d[x++][y] = 32; d[x++][y] = 56; d[x++][y] = 71; d[x++][y] = 37; d[x++][y] =  2; d[x++][y] = 36; d[x++][y++] = 91;
    x = 0;  d[x++][y] = 22; d[x++][y] = 31; d[x++][y] = 16; d[x++][y] = 71; d[x++][y] = 51; d[x++][y] = 67; d[x++][y] = 63; d[x++][y] = 89; d[x++][y] = 41; d[x++][y] = 92; d[x++][y] = 36; d[x++][y] = 54; d[x++][y] = 22; d[x++][y] = 40; d[x++][y] = 40; d[x++][y] = 28; d[x++][y] = 66; d[x++][y] = 33; d[x++][y] = 13; d[x++][y++] = 80;
    x = 0;  d[x++][y] = 24; d[x++][y] = 47; d[x++][y] = 32; d[x++][y] = 60; d[x++][y] = 99; d[x++][y] =  3; d[x++][y] = 45; d[x++][y] =  2; d[x++][y] = 44; d[x++][y] = 75; d[x++][y] = 33; d[x++][y] = 53; d[x++][y] = 78; d[x++][y] = 36; d[x++][y] = 84; d[x++][y] = 20; d[x++][y] = 35; d[x++][y] = 17; d[x++][y] = 12; d[x++][y++] = 50;
    x = 0;  d[x++][y] = 32; d[x++][y] = 98; d[x++][y] = 81; d[x++][y] = 28; d[x++][y] = 64; d[x++][y] = 23; d[x++][y] = 67; d[x++][y] = 10; d[x++][y] = 26; d[x++][y] = 38; d[x++][y] = 40; d[x++][y] = 67; d[x++][y] = 59; d[x++][y] = 54; d[x++][y] = 70; d[x++][y] = 66; d[x++][y] = 18; d[x++][y] = 38; d[x++][y] = 64; d[x++][y++] = 70;
    x = 0;  d[x++][y] = 67; d[x++][y] = 26; d[x++][y] = 20; d[x++][y] = 68; d[x++][y] =  2; d[x++][y] = 62; d[x++][y] = 12; d[x++][y] = 20; d[x++][y] = 95; d[x++][y] = 63; d[x++][y] = 94; d[x++][y] = 39; d[x++][y] = 63; d[x++][y] =  8; d[x++][y] = 40; d[x++][y] = 91; d[x++][y] = 66; d[x++][y] = 49; d[x++][y] = 94; d[x++][y++] = 21;
    x = 0;  d[x++][y] = 24; d[x++][y] = 55; d[x++][y] = 58; d[x++][y] =  5; d[x++][y] = 66; d[x++][y] = 73; d[x++][y] = 99; d[x++][y] = 26; d[x++][y] = 97; d[x++][y] = 17; d[x++][y] = 78; d[x++][y] = 78; d[x++][y] = 96; d[x++][y] = 83; d[x++][y] = 14; d[x++][y] = 88; d[x++][y] = 34; d[x++][y] = 89; d[x++][y] = 63; d[x++][y++] = 72;
    x = 0;  d[x++][y] = 21; d[x++][y] = 36; d[x++][y] = 23; d[x++][y] =  9; d[x++][y] = 75; d[x++][y] =  0; d[x++][y] = 76; d[x++][y] = 44; d[x++][y] = 20; d[x++][y] = 45; d[x++][y] = 35; d[x++][y] = 14; d[x++][y] =  0; d[x++][y] = 61; d[x++][y] = 33; d[x++][y] = 97; d[x++][y] = 34; d[x++][y] = 31; d[x++][y] = 33; d[x++][y++] = 95;
    x = 0;  d[x++][y] = 78; d[x++][y] = 17; d[x++][y] = 53; d[x++][y] = 28; d[x++][y] = 22; d[x++][y] = 75; d[x++][y] = 31; d[x++][y] = 67; d[x++][y] = 15; d[x++][y] = 94; d[x++][y] =  3; d[x++][y] = 80; d[x++][y] =  4; d[x++][y] = 62; d[x++][y] = 16; d[x++][y] = 14; d[x++][y] =  9; d[x++][y] = 53; d[x++][y] = 56; d[x++][y++] = 92;
    x = 0;  d[x++][y] = 16; d[x++][y] = 39; d[x++][y] =  5; d[x++][y] = 42; d[x++][y] = 96; d[x++][y] = 35; d[x++][y] = 31; d[x++][y] = 47; d[x++][y] = 55; d[x++][y] = 58; d[x++][y] = 88; d[x++][y] = 24; d[x++][y] =  0; d[x++][y] = 17; d[x++][y] = 54; d[x++][y] = 24; d[x++][y] = 36; d[x++][y] = 29; d[x++][y] = 85; d[x++][y++] = 57;
    x = 0;  d[x++][y] = 86; d[x++][y] = 56; d[x++][y] =  0; d[x++][y] = 48; d[x++][y] = 35; d[x++][y] = 71; d[x++][y] = 89; d[x++][y] =  7; d[x++][y] =  5; d[x++][y] = 44; d[x++][y] = 44; d[x++][y] = 37; d[x++][y] = 44; d[x++][y] = 60; d[x++][y] = 21; d[x++][y] = 58; d[x++][y] = 51; d[x++][y] = 54; d[x++][y] = 17; d[x++][y++] = 58;
    x = 0;  d[x++][y] = 19; d[x++][y] = 80; d[x++][y] = 81; d[x++][y] = 68; d[x++][y] =  5; d[x++][y] = 94; d[x++][y] = 47; d[x++][y] = 69; d[x++][y] = 28; d[x++][y] = 73; d[x++][y] = 92; d[x++][y] = 13; d[x++][y] = 86; d[x++][y] = 52; d[x++][y] = 17; d[x++][y] = 77; d[x++][y] =  4; d[x++][y] = 89; d[x++][y] = 55; d[x++][y++] = 40;
    x = 0;  d[x++][y] =  4; d[x++][y] = 52; d[x++][y] =  8; d[x++][y] = 83; d[x++][y] = 97; d[x++][y] = 35; d[x++][y] = 99; d[x++][y] = 16; d[x++][y] =  7; d[x++][y] = 97; d[x++][y] = 57; d[x++][y] = 32; d[x++][y] = 16; d[x++][y] = 26; d[x++][y] = 26; d[x++][y] = 79; d[x++][y] = 33; d[x++][y] = 27; d[x++][y] = 98; d[x++][y++] = 66;
    x = 0;  d[x++][y] = 88; d[x++][y] = 36; d[x++][y] = 68; d[x++][y] = 87; d[x++][y] = 57; d[x++][y] = 62; d[x++][y] = 20; d[x++][y] = 72; d[x++][y] =  3; d[x++][y] = 46; d[x++][y] = 33; d[x++][y] = 67; d[x++][y] = 46; d[x++][y] = 55; d[x++][y] = 12; d[x++][y] = 32; d[x++][y] = 63; d[x++][y] = 93; d[x++][y] = 53; d[x++][y++] = 69;
    x = 0;  d[x++][y] =  4; d[x++][y] = 42; d[x++][y] = 16; d[x++][y] = 73; d[x++][y] = 38; d[x++][y] = 25; d[x++][y] = 39; d[x++][y] = 11; d[x++][y] = 24; d[x++][y] = 94; d[x++][y] = 72; d[x++][y] = 18; d[x++][y] =  8; d[x++][y] = 46; d[x++][y] = 29; d[x++][y] = 32; d[x++][y] = 40; d[x++][y] = 62; d[x++][y] = 76; d[x++][y++] = 36;
    x = 0;  d[x++][y] = 20; d[x++][y] = 69; d[x++][y] = 36; d[x++][y] = 41; d[x++][y] = 72; d[x++][y] = 30; d[x++][y] = 23; d[x++][y] = 88; d[x++][y] = 34; d[x++][y] = 62; d[x++][y] = 99; d[x++][y] = 69; d[x++][y] = 82; d[x++][y] = 67; d[x++][y] = 59; d[x++][y] = 85; d[x++][y] = 74; d[x++][y] =  4; d[x++][y] = 36; d[x++][y++] = 16;
    x = 0;  d[x++][y] = 20; d[x++][y] = 73; d[x++][y] = 35; d[x++][y] = 29; d[x++][y] = 78; d[x++][y] = 31; d[x++][y] = 90; d[x++][y] =  1; d[x++][y] = 74; d[x++][y] = 31; d[x++][y] = 49; d[x++][y] = 71; d[x++][y] = 48; d[x++][y] = 86; d[x++][y] = 81; d[x++][y] = 16; d[x++][y] = 23; d[x++][y] = 57; d[x++][y] =  5; d[x++][y++] = 54;
    x = 0;  d[x++][y] =  1; d[x++][y] = 70; d[x++][y] = 54; d[x++][y] = 71; d[x++][y] = 83; d[x++][y] = 51; d[x++][y] = 54; d[x++][y] = 69; d[x++][y] = 16; d[x++][y] = 92; d[x++][y] = 33; d[x++][y] = 48; d[x++][y] = 61; d[x++][y] = 43; d[x++][y] = 52; d[x++][y] =  1; d[x++][y] = 89; d[x++][y] = 19; d[x++][y] = 67; d[x++][y++] = 48;

    // Print back the table
    printf("Print back the table\n");
    for (y=0; y<20; y++) {
        for (x=0; x<20; x++) {
            printf("%02d ", d[x][y]);
        }
        printf("\n");
    }

    // Search for horizontal results
    int max_h = 0;
    printf("// Search for horizontal results\n");
    for (x = 0; x < 17; x++) {
        for (y = 0; y < 20; y++) {
          if ((d[x][y] * d[x+1][y] * d[x+2][y] * d[x+3][y]) > max_h)
                max_h = (d[x][y] * d[x+1][y] * d[x+2][y] * d[x+3][y]);
        }
    }

    // Search for vertical results
    int max_v = 0;
    printf("// Search for vertical results\n");
    for (x = 0; x < 20; x++) {
        for (y = 0; y < 17; y++) {
          if ((d[x][y] * d[x][y+1] * d[x][y+2] * d[x][y+3]) > max_v)
                max_v = (d[x][y] * d[x][y+1] * d[x][y+2] * d[x][y+3]);
        }
    }

    // Search for diagonal NW/SE results
    printf("// Search for diagonal NW/SE results\n");
    int max_nw = 0;
    printf("// Search for vertical results\n");
    for (x = 0; x < 17; x++) {
        for (y = 0; y < 17; y++) {
          if ((d[x][y] * d[x+1][y+1] * d[x+2][y+2] * d[x+3][y+3]) > max_nw)
                max_nw = (d[x][y] * d[x+1][y+1] * d[x+2][y+2] * d[x+3][y+3]);
        }
    }

    // Search for diagonal NE/SW results
    printf("// Search for diagonal NE/SW results\n");
    int max_ne = 0;
    printf("// Search for vertical results\n");
    for (x = 0; x < 17; x++) {
        for (y = 3; y < 20; y++) {
          if ((d[x][y] * d[x+1][y-1] * d[x+2][y-2] * d[x+3][y-3]) > max_ne)
                max_ne = (d[x][y] * d[x+1][y-1] * d[x+2][y-2] * d[x+3][y-3]);
        }
    }

    // Print the answer
    printf("// Print the answer\n");
    int max = max_h;
    if (max_v > max_h)   max = max_v;
    if (max_nw > max_h)  max = max_nw;
    if (max_ne > max_h)  max = max_ne;
    printf("max = %d\n", max);
    printf("max_h  = %d\n", max_h);
    printf("max_v  = %d\n", max_v);
    printf("max_nw = %d\n", max_nw);
    printf("max_ne = %d\n", max_ne);
}