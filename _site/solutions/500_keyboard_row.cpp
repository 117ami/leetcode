#include "aux.cpp"
/**
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below. Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

 https://leetcode.com/problems/keyboard-row/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<string> findWords(vector<string> &words) {
    unordered_map<char, int> rows;
    std::vector<string> ss = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
    for (int i = 0; i < ss.size(); i++)
      for (auto c : ss[i])
        rows[c] = i;
    int i = 0;
    for (int j = 0; j < words.size(); j++) {
      int rowlevel = rows[tolower(words[j][0])];
      bool samelevel = true;
      for (auto c : words[j])
        if (rowlevel != rows[tolower(c)]) {
          samelevel = false;
          break;
        }
      if (samelevel) {
        words[i++] = words[j];
      }
    }
    words.resize(i);
    return words;
  }
};

int main() {
  Solution s;
  std::vector<string> words = {"Hello", "Alaska", "Peace", "Dad"};
  say(s.findWords(words));
}
