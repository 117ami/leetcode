/*
 * @lc app=leetcode id=856 lang=cpp
 *
 * [856] Score of Parentheses
 *
 * https://leetcode.com/problems/score-of-parentheses/description/
 *
 * algorithms
 * Medium (55.72%)
 * Total Accepted:    17.1K
 * Total Submissions: 30.6K
 * Testcase Example:  '"()"'
 *
 * Given a balanced parentheses string S, compute the score of the string based
 * on the following rule:
 *
 *
 * () has score 1
 * AB has score A + B, where A and B are balanced parentheses strings.
 * (A) has score 2 * A, where A is a balanced parentheses string.
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: "()"
 * Output: 1
 *
 *
 *
 * Example 2:
 *
 *
 * Input: "(())"
 * Output: 2
 *
 *
 *
 * Example 3:
 *
 *
 * Input: "()()"
 * Output: 2
 *
 *
 *
 * Example 4:
 *
 *
 * Input: "(()(()))"
 * Output: 6
 *
 *
 *
 *
 * Note:
 *
 *
 * S is a balanced parentheses string, containing only ( and ).
 * 2 <= S.length <= 50
 *
 *
 *
 *
 *
 *
 */
#include "aux.cpp"
#include <stack>
class Solution {
public:
  int scoreOfParentheses(string S) {
  	vector<string> stack; 
    for (auto c : S) {
      if (c == '(')
        st.push_back(string m(1, c));
      else {
        int n = 0;
        while (st.back() != "(") {
          n += int(st.back());
          st.pop();
        }
        n = max(1, 2 * n);
        st.pop();
        st.push((char)n);
      }
    }

    int res = 0;
    while (!st.empty()) {
      say(st.top());
      res += st.top() - '0';
      st.pop();
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

int main(int argc, char const *argv[]) {
  Solution s;
  string S = "()";
  S = "()((((()(()))))((()))()((())((()(())))(())))";
  say(s.scoreOfParentheses(S));
  return 0;
}
