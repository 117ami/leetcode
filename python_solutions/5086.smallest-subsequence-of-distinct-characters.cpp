/*
 * @lc app=leetcode id=5086 lang=cpp
 *
 * [5086] Smallest Subsequence of Distinct Characters
 *
 * https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
 *
 * algorithms
 * Medium (33.27%)
 * Total Accepted:    1.4K
 * Total Submissions: 3.8K
 * Testcase Example:  '"cdadabcc"'
 *
 * Return the lexicographically smallest subsequence of text that contains all
 * the distinct characters of text exactly once.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: "cdadabcc"
 * Output: "adbc"
 *
 *
 *
 * Example 2:
 *
 *
 * Input: "abcd"
 * Output: "abcd"
 *
 *
 *
 * Example 3:
 *
 *
 * Input: "ecbacba"
 * Output: "eacb"
 *
 *
 *
 * Example 4:
 *
 *
 * Input: "leetcode"
 * Output: "letcod"
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= text.length <= 1000
 * text consists of lowercase English letters.
 *
 *
 *
 *
 *
 *
 *
 */
using namespace std;
using VI = vector<int>;
using LL = long long;

class Solution {
public:
  string smallestSubsequence(string text) {
    // VI cnt(26, 0), used(cnt);
    int cnt[26]={}, used[26]={};
    for (auto &c : text)
      ++cnt[c - 'a'];
    string res = "";
    for (auto &c : text) {
      cnt[c - 'a']--;
      if (used[c - 'a']++ > 0)
        continue;
      while (!res.empty() && res.back() > c && cnt[res.back() - 'a'] > 0) {
        used[res.back() - 'a'] = 0;
        res.pop_back();
      }
      res.push_back(c);
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
