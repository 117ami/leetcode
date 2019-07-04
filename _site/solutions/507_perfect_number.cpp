#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**
   We define the Perfect Number is a positive integer that is equal to the
sum of all its positive divisors except itself.
   Now, given an integer n, write a function that returns true when it is a
perfect number and false when it is not.
   Example:
   Input: 28
   Output: True
   Explanation: 28 = 1 + 2 + 4 + 7 + 14
   Note:
   The input number n will not exceed 100,000,000. (1e8)

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  bool checkPerfectNumber(int num) {
    if (num <= 1)
      return false;
    int xsum = 1;
    for (int i = 2; i <= sqrt(num); i++)
      if (num % i == 0)
        xsum += i + num / i;
    return xsum == num;
  }
};

int main() {
  Solution s;
  for (int i = 1; i < 2000; i++)
    if (s.checkPerfectNumber(i))
      cout << i << " ";
  cout << endl;
}
