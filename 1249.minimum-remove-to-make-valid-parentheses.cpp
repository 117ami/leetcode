/*
 * @lc app=leetcode id=1249 lang=cpp
 *
 * [1249] Minimum Remove to Make Valid Parentheses
 *
 * https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
 *
 * algorithms
 * Medium (55.66%)
 * Total Accepted:    3.5K
 * Total Submissions: 6.2K
 * Testcase Example:  '"lee(t(c)o)de)"'
 *
 * Given a string s of '(' , ')' and lowercase English characters. 
 *
 * Your task is to remove the minimum number of parentheses ( '(' or ')', in
 * any positions ) so that the resulting parentheses string is valid and return
 * any valid string.
 *
 * Formally, a parentheses string is valid if and only if:
 *
 *
 * It is the empty string, contains only lowercase characters, or
 * It can be written as AB (A concatenated with B), where A and B are valid
 * strings, or
 * It can be written as (A), where A is a valid string.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: s = "lee(t(c)o)de)"
 * Output: "lee(t(c)o)de"
 * Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "a)b(c)d"
 * Output: "ab(c)d"
 *
 *
 * Example 3:
 *
 *
 * Input: s = "))(("
 * Output: ""
 * Explanation: An empty string is also valid.
 *
 *
 * Example 4:
 *
 *
 * Input: s = "(a(b(c)d)"
 * Output: "a(b(c)d)"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s[i] is one of  '(' , ')' and lowercase English letters.
 *
 */

class Solution {
public:
  string minRemoveToMakeValid(string s) {
    stack<int> left;
    vector<int> removed;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '(') {
        left.push(i);
      } else if (s[i] == ')') {
        if (!left.empty()) {
          left.pop();
        } else {
          removed.emplace_back(i);
        }
      }
    }

    while (!left.empty()) {
      removed.emplace_back(left.top());
      left.pop();
    }

    sort(removed.begin(), removed.end());
    string res;
    for (int i = 0, j = 0; i < s.size(); i++) {
      if (j < removed.size() && i == removed[j]) {
        j++;
      } else {
        res.push_back(s[i]);
      }
    }

    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
