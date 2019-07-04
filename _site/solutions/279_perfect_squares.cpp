#include "aux.cpp"
/**
Given a positive integer n, find the least number of perfect square numbers (for
example, 1, 4, 9, 16, ...) which sum to n. Example 1: Input: n = 12 Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

 https://leetcode.com/problems/perfect-squares/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int numSquares(int n) {
    if (perfectSquares(n))
      return 1;
    while ((n & 3) == 0)
      n >>= 2;
    if ((n & 7) == 7)
      return 4;

    int sn = floor(sqrt(n));
    for (int k = 1; k <= sn; k++) {
      if (k * k > n)
        break;
      if (perfectSquares(n - k * k))
        return 2;
    }
    return 3;
  }

  bool perfectSquares(int n) {
    if (n <= 1)
      return true;
    int sn = floor(sqrt(n));
    return sn * sn == n;
  }
};

int main() {
  Solution s;
  int n = 40901;
  say(s.numSquares(n));
}
