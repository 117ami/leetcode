/*
 * @lc app=leetcode id=336 lang=cpp
 *
 * [336] Palindrome Pairs
 *
 * https://leetcode.com/problems/palindrome-pairs/description/
 *
 * algorithms
 * Hard (31.02%)
 * Total Accepted:    70.1K
 * Total Submissions: 225.9K
 * Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
 *
 * Given a list of unique words, find all pairs of distinct indices (i, j) in
 * the given list, so that the concatenation of the two words, i.e. words[i] +
 * words[j] is a palindrome.
 *
 * Example 1:
 *
 *
 *
 * Input: ["abcd","dcba","lls","s","sssll"]
 * Output: [[0,1],[1,0],[3,2],[2,4]]
 * Explanation: The palindromes are
 * ["dcbaabcd","abcddcba","slls","llssssll"]
 *
 *
 *
 * Example 2:
 *
 *
 * Input: ["bat","tab","cat"]
 * Output: [[0,1],[1,0]]
 * Explanation: The palindromes are ["battab","tabbat"]
 *
 *
 *
 *
 */
using namespace std;
using VI = vector<int>;
using VVI = vector<VI>;
using LL = long long;
using SI = set<int>;
using UMSI = unordered_map<string, int>;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i)       // [0, n)
#define UP(i, a, b) for (int i = int(a); i <= int(b); ++i) // [a, b)
bool isPalindrome(string str) {
  int i = 0, j = str.size() - 1;
  while (i < j)
    if (str[i++] != str[j--])
      return false;
  return true;
}
void reverseStr(string &s) { reverse(s.begin(), s.end()); }

class Solution {
public:
  vector<vector<int>> palindromePairs(vector<string> &words) {
    UMSI m;
    set<VI> sres;
    EACH(i, words.size() - 1) {
      string s(words[i]);
      reverseStr(s);
      m[s] = i;
    }

    EACH(i, words.size() - 1) {
      UP(j, 1, words[i].size()) {
        string left(words[i].substr(0, j)),
            right(words[i].substr(j, words[i].size() - j));

        if (isPalindrome(right) && m.find(left) != m.end() && i != m[left])
          sres.insert({i, m[left]});

        if (isPalindrome(left) && m.find(right) != m.end() && i != m[right])
          sres.insert({m[right], i});

        if (isPalindrome(words[i]) && m.find("") != m.end())
          sres.insert({i, m[""]});
      }
    }

    VVI res(sres.begin(), sres.end());
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
