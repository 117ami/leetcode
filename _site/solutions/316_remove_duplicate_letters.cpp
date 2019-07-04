#include "aux.cpp"
/**
Given a string which contains only lowercase letters, remove duplicate letters
so that every letter appear once and only once. You must make sure your result
is the smallest in lexicographical order among all possible results. Example 1:
Input: "bcabc"
Output: "abc"
Example 2:
Input: "cbacdcbc"
Output: "acdb"

 https://leetcode.com/problems/remove-duplicate-letters/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  string removeDuplicateLetters(string s) {
    if (s.size() <= 1)
      return s;
    vector<int> cnt(256, 0);
    for (int i = 0; i < s.size(); i++)
      cnt[s[i]]++;
    int pos = 0;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] < s[pos])
        pos = i;
      if (--cnt[s[i]] == 0)
        break;
    }
    char ans = s[pos];
    replace(s.begin(), s.end(), ans, '\0');
    return ans + removeDuplicateLetters(s.substr(pos + 1, s.size() - pos));
  }
};

int main() {
  Solution s;
  string xs = "bcabbc";
  xs = "cbacdcbc";
  // xs = "thesqtitxyetpxloeevdeqifkz";
  say(s.removeDuplicateLetters(xs));
}
