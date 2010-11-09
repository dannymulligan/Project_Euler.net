// Project Euler.net Problem 22
//
// Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it
// into alphabetical order. Then working out the alphabetical value for each name, multiply this
// value by its alphabetical position in the list to obtain a name score.
//
// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12
// + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
//
// What is the total of all the name scores in the file?
//
// $Revision

#include <stdio.h>
#include <string.h>

#define MAX 10000

int main()
{
    int i, j;
    char name[32];  // String to store names

    // Read in the entries
    int name_count;
    int name_score;
    int name_len;
    int tot_score = 0;
    while (!feof(stdin)) {
        (void)fscanf(stdin, "%s\n", &name);

        name_count++;
        name_score = 0;
        name_len = strlen(name);
        for (i = 0; i < name_len; i++) {
            name_score += name[i] - 'A' + 1;
        }
        name_score = name_score * name_count;
        tot_score += name_score;
        printf("%d %s %d %d\n", name_count, name, name_score, tot_score);
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("The answer is %d\n", tot_score);
}
