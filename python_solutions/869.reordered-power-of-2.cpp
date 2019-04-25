/*
 * @lc app=leetcode id=869 lang=cpp
 *
 * [869] Reordered Power of 2
 *
 * https://leetcode.com/problems/reordered-power-of-2/description/
 *
 * algorithms
 * Medium (50.35%)
 * Total Accepted:    8.7K
 * Total Submissions: 17.3K
 * Testcase Example:  '1'
 *
 * Starting with a positive integer N, we reorder the digits in any order
 * (including the original order) such that the leading digit is not zero.
 *
 * Return true if and only if we can do this in a way such that the resulting
 * number is a power of 2.
 *
 *
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: 1
 * Output: true
 *
 *
 *
 * Example 2:
 *
 *
 * Input: 10
 * Output: false
 *
 *
 *
 * Example 3:
 *
 *
 * Input: 16
 * Output: true
 *
 *
 *
 * Example 4:
 *
 *
 * Input: 24
 * Output: false
 *
 *
 *
 * Example 5:
 *
 *
 * Input: 46
 * Output: true
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= N <= 10^9
 *
 *
 *
 *
 *
 *
 *
 */

// #include "aux.cpp"

class Solution {
public:
  bool reorderedPowerOf2(int N) {
    string arr = to_string(N);
    sort(arr.begin(), arr.end(), greater<int>());
    int bound = stoi(arr), i = 1;
    
    while (i <= bound) {
      string xarr = to_string(i);
      sort(xarr.begin(), xarr.end(), greater<int>());
      if (xarr == arr)
        return true;
      i *= 2;
    }
    return false;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
//   Solution s;
//   bool res = s.reorderedPowerOf2(1);
//   say(res);
//   return 0;
// }
