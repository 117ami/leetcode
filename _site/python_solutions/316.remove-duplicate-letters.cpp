/*
 * @lc app=leetcode id=316 lang=cpp
 *
 * [316] Remove Duplicate Letters
 *
 * https://leetcode.com/problems/remove-duplicate-letters/description/
 *
 * algorithms
 * Hard (32.54%)
 * Total Accepted:    57.2K
 * Total Submissions: 175.6K
 * Testcase Example:  '"bcabc"'
 *
 * Given a string which contains only lowercase letters, remove duplicate
 * letters so that every letter appear once and only once. You must make sure
 * your result is the smallest in lexicographical order among all possible
 * results.
 *
 * Example 1:
 *
 *
 * Input: "bcabc"
 * Output: "abc"
 *
 *
 * Example 2:
 *
 *
 * Input: "cbacdcbc"
 * Output: "acdb"
 *
 */
using namespace std;
using VI = vector<int>;
using LL = long long;

class Solution {
public:
  string removeDuplicateLetters(string s) {
    // int used[26] = {}, cnt[26] = {};
    VI used(26, 0), cnt(used);
    string res;
    for (char &c : s)
      cnt[c - 'a']++;
    for (char &c : s) {
      --cnt[c - 'a'];
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
