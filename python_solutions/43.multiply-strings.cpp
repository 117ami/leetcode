#include <vector>
/*
 * @lc app=leetcode id=43 lang=cpp
 *
 * [43] Multiply Strings
 *
 * https://leetcode.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (33.92%)
 * Total Accepted:    304.1K
 * Total Submissions: 896.2K
 * Testcase Example:  '"2"\n"3"'
 *
 * Given two non-negative integers num1 and num2 represented as strings, return
 * the product of num1 and num2, also represented as a string.
 *
 * Example 1:
 *
 *
 * Input: num1 = "2", num2 = "3"
 * Output: "6"
 *
 * Example 2:
 *
 *
 * Input: num1 = "123", num2 = "456"
 * Output: "56088"
 *
 *
 * Note:
 *
 *
 * The length of both num1 and num2 is < 110.
 * Both num1 and num2 contain only digits 0-9.
 * Both num1 and num2 do not contain any leading zero, except the number 0
 * itself.
 * You must not use any built-in BigInteger library or convert the inputs to
 * integer directly.
 *
 *
 */

#include <iostream>
#include <sstream>
#include <string>
class Solution {
public:
  string multiply(string_view s, string_view t) {
    int m = s.size(), n = t.size();
    vector<int> res(m + n, 0);
    for (int i = m - 1; i >= 0; i--)
      for (int j = n - 1; j >= 0; j--) {
        int mul = (s[i] - '0') * (t[j] - '0');
        int p1 = i + j, p2 = i + j + 1;
        int sum = res[p2] + mul;
        res[p1] += sum / 10;
        res[p2] = sum % 10;
      }

    stringstream ss;
    std::copy(res.begin(), res.end(), ostream_iterator<int>(ss, ""));

    string rs = ss.str();
    auto it = rs.find_first_not_of("0");
    if (string::npos == it)
      return "0";
    return rs.substr(it);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
