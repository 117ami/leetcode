#include <vector>
/*
 * @lc app=leetcode id=1556 lang=cpp
 *
 * [1556] Thousand Separator
 *
 * https://leetcode.com/problems/thousand-separator/description/
 *
 * algorithms
 * Easy (62.02%)
 * Total Accepted:    7.1K
 * Total Submissions: 11.5K
 * Testcase Example:  '987'
 *
 * Given an integer n, add a dot (".") as the thousands separator and return it
 * in string format.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 987
 * Output: "987"
 *
 *
 * Example 2:
 *
 *
 * Input: n = 1234
 * Output: "1.234"
 *
 *
 * Example 3:
 *
 *
 * Input: n = 123456789
 * Output: "123.456.789"
 *
 *
 * Example 4:
 *
 *
 * Input: n = 0
 * Output: "0"
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= n < 2^31
 *
 *
 */

class Solution {
public:
  string thousandSeparator(int n) {
    string s = to_string(n), res;
    for (int i = 0; i < s.size(); i++) {
      if (i > 0 && (s.size() - i) % 3 == 0)
        res.push_back('.');
      res.push_back(s[i]);
    }
    return res;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
