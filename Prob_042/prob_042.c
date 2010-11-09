// Project Euler.net Problem 42
//
// The nth term of the sequence of triangle numbers is given by, t(n) = n(n+1)/2; so the
// first ten triangle numbers are:
// 
//     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
// 
// By converting each letter in a word to a number corresponding to its alphabetical
// position and adding these values we form a word value. For example, the word value
// for SKY is 19 + 11 + 25 = 55 = t(10). If the word value is a triangle number then
// we shall call the word a triangle word.
// 
// Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
// nearly two-thousand common English words, how many are triangle words?
// 
// $Revision

#include <stdio.h>
#include <string.h>

#define MAX 400

int main()
{
    int i, j;
    char word[32];  // String to store words

    char triang[MAX];  // Table of triangle numbers

    // Create a table of triangle numbers
    for (i = 0; i < MAX; i++)
        triang[i] = 0;
    i = 1;
    do {
        j = i * (i + 1) / 2;
        if (j < MAX)
            triang[j] = i;
        i++;
    } while (j < MAX);

    // Print table of triangle numbers
    for(i = 0; i < MAX; i++) {
        if (triang[i])
            printf("triang[%2d] = %2d\n", triang[i], i);
    }

    // Read in the entries
    int word_count = 0;
    int word_score;
    int word_len;
    int triangle_cnt = 0;
    while (!feof(stdin)) {
        (void)fscanf(stdin, "%s\n", &word);

        // Calculate the word score
        word_count++;
        word_score = 0;
        word_len = strlen(word);
        for (i = 0; i < word_len; i++) {
            word_score += word[i] - 'A' + 1;
        }

        // Check if the word score is a triangle
        if (word_score > MAX)              return(1);
        else if (triang[word_score] != 0)  triangle_cnt++;

        printf("%d %s %d %d\n", word_count, word, word_score, triang[word_score]);
    }

    // Print the answer
    printf("// Print the answer\n");
    printf("The answer is %d\n", triangle_cnt);
}
