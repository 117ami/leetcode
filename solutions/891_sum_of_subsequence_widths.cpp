#include "aux.cpp"
/**
Given an array of integers A, consider all non-empty subsequences of A.
For any sequence S, let thewidthof S be the difference between the maximum and
minimum element of S. Return the sum of the widths of all subsequences of A. As
the answer may be very large, return the answer modulo 10^9 + 7.

Example 1:
Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.

Note:
        1 <= A.length <= 20000
        1 <= A[i] <= 20000

 https://leetcode.com/problems/sum-of-subsequence-widths/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int sumSubseqWidths(vector<int> &a) {
    sort(a.begin(), a.end());
    long c = 1, res = 0, mod = 1e9 + 7;
    for (int i = 0; i < a.size(); ++i, c = (c << 1) % mod)
      res = (res + a[i] * c - a[a.size() - i - 1] * c) % mod;
    return (res + mod) % mod;

    // sort(a.begin(), a.end());
    // long c = 1, mod = 1e9 + 7, res = 0, d = 2;
    // d <<= a.size() - 1;
    // say(d);
    // for (int i = 0; i < a.size(); i++, c = (c << 1) % mod) {
    //   res = (res + a[i] * (c - d)) % mod;
    //   d >>= 1;
    // }
    // return (res + mod) % mod;
  }
};

int main() {
  Solution s;
  vector<int> a = {
      96, 87,  191, 197, 40,  101, 108, 35,  169, 50,  168, 182, 95,  80,  144,
      43, 18,  60,  174, 13,  77,  173, 38,  46,  80,  117, 13,  19,  11,  6,
      13, 118, 39,  80,  171, 36,  86,  156, 165, 190, 53,  49,  160, 192, 57,
      42, 97,  35,  124, 200, 84,  70,  145, 180, 54,  141, 159, 42,  66,  66,
      25, 95,  24,  136, 140, 159, 71,  131, 5,   140, 115, 76,  151, 137, 63,
      47, 69,  164, 60,  172, 153, 183, 6,   70,  40,  168, 133, 45,  116, 188,
      20, 52,  70,  156, 44,  27,  124, 59,  42,  172};
  say(s.sumSubseqWidths(a));
}
