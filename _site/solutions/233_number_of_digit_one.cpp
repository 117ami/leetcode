#include "aux.cpp"
/**
Given an integer n, count the total number of digit 1 appearing in all
non-negative integers less than or equal to n.
Example:
Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

 https://leetcode.com/problems/number-of-digit-one/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int countDigitOne(int n) {
    if (n <= 0)
      return 0;
    if (n < 10)
      return 1;
    int x = n, y = 1;
    while (x >= 10) {
      x /= 10;
      y *= 10;
    }
    return (x == 1 ? n - y + 1 + countDigitOne(y - 1)
                   : y + x * countDigitOne(y - 1)) +
           countDigitOne(n % y);
  }
};

int main() {
  Solution s;
  int n = 1999;
  say(s.countDigitOne(n));
}
