#include "aux.cpp"
/**
Given a positive integer n, break it into the sum of at least two positive
integers and maximize the product of those integers. Return the maximum product
you can get. Example 1: Input: 2 Output: 1 Explanation: 2 = 1 + 1, 1 &times; 1
= 1. Example 2: Input: 10 Output: 36 Explanation: 10 = 3 + 3 + 4, 3 &times;3
&times;4 = 36. Note: You may assume that n is not less than 2 and not larger
than 58.

 https://leetcode.com/problems/integer-break/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int integerBreak(int n) {
    if (n <= 3)
      return n - 1;
    int res = 1;
    while (n > 4) {
      res *= 3;
      n -= 3;
    }
    return res * n;
  }
};

int main() {
  Solution s;
  int n = 11;
  say(s.integerBreak(n));
}
