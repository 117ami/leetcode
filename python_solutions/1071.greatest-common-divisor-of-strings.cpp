/*
 * @lc app=leetcode id=1071 lang=cpp
 *
 * [1071] Greatest Common Divisor of Strings
 *
 * https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
 *
 * algorithms
 * Easy (48.82%)
 * Total Accepted:    3.1K
 * Total Submissions: 6.4K
 * Testcase Example:  '"ABCABC"\n"ABC"'
 *
 * For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T
 * concatenated with itself 1 or more times)
 *
 * Return the largest string X such that X divides str1 and X divides str2.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: str1 = "ABCABC", str2 = "ABC"
 * Output: "ABC"
 *
 *
 * Example 2:
 *
 *
 * Input: str1 = "ABABAB", str2 = "ABAB"
 * Output: "AB"
 *
 *
 * Example 3:
 *
 *
 * Input: str1 = "LEET", str2 = "CODE"
 * Output: ""
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= str1.length <= 1000
 * 1 <= str2.length <= 1000
 * str1[i] and str2[i] are English uppercase letters.
 *
 */
using namespace std;
using LL = long long;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i)
#define EACHV(i, n) for (int i = int(n); i >= 0; --i)

class Solution {
public:
  bool divides(string s, int m) {
    EACH(i, s.size() - 1) if (s[i] != s[i % m]) return false;
    return true;
  }

  string gcdOfStrings(string s1, string s2) {
    int m = __gcd(s1.size(), s2.size());
    if (divides(s1, m) && divides(s2, m) && s1.substr(0, m) == s2.substr(0, m))
      return s1.substr(0, m);
    return "";
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
