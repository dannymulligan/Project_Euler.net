// Project Euler.net Problem 19
//
// You are given the following information, but you may prefer to do some research for yourself.
//
//     - 1 Jan 1900 was a Monday.
//     - Thirty days has September,
//       April, June and November.
//       All the rest have thirty-one,
//       Saving February alone,
//       Which has twenty-eight, rain or shine.
//       And on leap years, twenty-nine.
//     - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
//
//  How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#include <iostream>

int main()
{
  int yr, mth;
  int dow;  // day of week, 0 = Monday, 6 = Sunday
  int dim;  // Days in month
  int result = 0;

  // Search through all the months/years
  printf("// Search through all the months/years\n");
  dow = 0;  // 1 January 1900 was a Monday
  dow = 1;  // 1 January 1901 was a Tuesday
  for (yr = 1901; yr <= 2000; yr++) {
    for (mth = 1; mth <= 12; mth++) {
      dim = 0;

      if (mth == 2)  {
        if ((yr %   4) == 0)  dim++;  // Adjust for February in leap year
        if ((yr % 100) == 0)  dim--;  // Unadjust for February in century divisible by 100
        if ((yr % 400) == 0)  dim++;  // Readjust for February in century divisible by 400
      }

      switch (mth) {
        case  1:  printf("1 January ");    dim += 31;  break;
        case  2:  printf("1 February ");   dim += 28;  break;
        case  3:  printf("1 March ");      dim += 31;  break;
        case  4:  printf("1 April ");      dim += 30;  break;
        case  5:  printf("1 May ");        dim += 31;  break;
        case  6:  printf("1 June ");       dim += 30;  break;
        case  7:  printf("1 July ");       dim += 31;  break;
        case  8:  printf("1 August ");     dim += 31;  break;
        case  9:  printf("1 September ");  dim += 30;  break;
        case 10:  printf("1 October ");    dim += 31;  break;
        case 11:  printf("1 November ");   dim += 30;  break;
        case 12:  printf("1 December ");   dim += 31;  break;
      }

      printf("%4d was a ", yr);

      switch (dow % 7) {
        case 0:  printf("Monday");             break;
        case 1:  printf("Tuesday");            break;
        case 2:  printf("Wednesday");          break;
        case 3:  printf("Thursday");           break;
        case 4:  printf("Friday");             break;
        case 5:  printf("Saturday");           break;
        case 6:  printf("Sunday");  result++;  break;
      }
      printf(" (%d days in this month)\n", dim);
      dow += dim;
    }
  }

  // Report answer
  std::printf("// Report answer\n");
  std::printf("There were %d Mondays that fell on the first of the month.\n", result);
}
