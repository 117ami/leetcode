#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given a non-negative integer n, count all numbers with unique digits, x, where 0
<= x < 10n.
    Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of
0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])
Credits:Special thanks to @memoryless for adding this problem and creating all
test cases.
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int countNumbersWithUniqueDigits(int n) {
  	if (0 == n)
  		return 1; 
    if (n > 10)
      return countNumbersWithUniqueDigits(10);
    vector<int> base = {9, 9, 8, 7, 6, 5, 4, 3, 2, 1};

    int res = accumulate(base.begin(), base.begin() + n, 1, multiplies<int>());
    return res + countNumbersWithUniqueDigits(n - 1);
  }
};

bool uniqueNumber(string s) {
  if (1 == s.size())
    return true;
  char pre = 'c';
  sort(s.begin(), s.end());
  for (int i = 0; i < s.size(); i++)
    if (s[i] == pre)
      return false;
    else
      pre = s[i];
  return true;
}

int main() {
  Solution s;
  int cter = 0;
  for (int i = 0; i <= 999999; i++) {
    string si = to_string(i);
    if (uniqueNumber(si))
      cter++;
  }
  cout << cter << endl;
  say(s.countNumbersWithUniqueDigits(6));
}
