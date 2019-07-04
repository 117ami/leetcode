/*
 * @lc app=leetcode id=125 lang=cpp
 *
 * [125] Valid Palindrome
 *
 * https://leetcode.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (30.83%)
 * Total Accepted:    345.9K
 * Total Submissions: 1.1M
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * Given a string, determine if it is a palindrome, considering only
 * alphanumeric characters and ignoring cases.
 *
 * Note: For the purpose of this problem, we define empty string as valid
 * palindrome.
 *
 * Example 1:
 *
 *
 * Input: "A man, a plan, a canal: Panama"
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: "race a car"
 * Output: false
 *
 *
 */
// #include "aux.cpp"

class Solution {
public:
  bool isPalindrome(string s) {
    int i = 0, j = s.size() - 1;
    while (i < j) {
      if (!isalphanumber(s[i]))
        i++;
      else if (!isalphanumber(s[j]))
        j--;
      else if (tolower(s[i]) == tolower(s[j])) {
        i++;
        j--;
      } else
        return false;
    }
    return true;
  }

  bool isalphanumber(char c) { return isalpha(c) || isdigit(c); }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
//   Solution s;
//   say(s.isPalindrome("0P"));
//   say(tolower('0'));
//   return 0;
// }
