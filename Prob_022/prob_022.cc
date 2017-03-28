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

#include <iostream>
#include <fstream>
#include <string>

int main()
{
  std::ifstream FileIn;
  FileIn.open("names_1.txt");

  std::string name;
  int name_count = 0;
  int name_score;
  int name_len;
  int tot_score = 0;

  // Read in the entries
  while(FileIn >> name) {
    name_count++;
    name_score = 0;

    for (int i = 0; i < name.length(); i++) {
      name_score += name[i] - 'A' + 1;
    }
    name_score = name_score * name_count;
    tot_score += name_score;
    std::printf("%d %s %d %d\n", name_count, name.c_str(), name_score, tot_score);
  }

  FileIn.close();

  // Print the answer
  std::printf("// Print the answer\n");
  std::printf("The answer is %d\n", tot_score);
}
 
