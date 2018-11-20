#include "aux.cpp"
/**
Given a list of words, we may encode it by writing a reference string S and a
list of indexes A.
For example, if the list of words is ["time", "me", "bell"], we can write it as
S = "time#bell#"and indexes = [0, 2, 5].
Then for each index, we will recover the word by reading from the reference
string from that index until we reach a "#" character.
What is the length of the shortest reference string S possible that encodes the
given words?
Example:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
Note:
        1 <= words.length<= 2000.
        1 <=words[i].length<= 7.
        Each wordhas onlylowercase letters.

 https://leetcode.com/problems/short-encoding-of-words/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int minimumLengthEncoding(vector<string> &words) {
    unordered_set<string> uniq(words.begin(), words.end());
    for (auto w : uniq)
      for (int i = 1; i < w.length(); i++)
        uniq.erase(w.substr(i));
    int res = 0;
    for (auto w : uniq)
      res += w.length() + 1;
    return res;
  }
};

int main() {
  Solution s;
  vector<string> words = {"me", "time", "bell"};
  say(s.minimumLengthEncoding(words));
  string ppp = "abcedf";
  say(ppp.substr(6));
}
