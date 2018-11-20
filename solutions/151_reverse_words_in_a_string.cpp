#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given an input string, reverse the string word by word.
Example:
Input: "the sky is blue",
Output:"blue is sky the".
Note:
        A word is defined as a sequence of non-space characters.
        Input string may contain leading or trailing spaces. However, your
reversed string should not contain leading or trailing spaces.
        You need to reduce multiple spaces between two words to a single space
in the reversed string.
Follow up:For C programmers, try to solve it in-place in O(1) space.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  void reverseWords(string &s) {
    const int n = s.size();
    reverse_string(s, 0, n - 1);
    // cout << "1. reverse all " << s << endl;
    reverse_each_word(s, n - 1);
    // cout << "2. reverse each " << s << endl;
    remove_dup_spaces(s, n);
    // cout << "3. remove space " << s << endl;
  }

  void reverse_each_word(string &s, int n) {
    int i = 0, j = 0;
    while (j < n) {
      while (i++ < n && s[i] == ' ')
        ;
      if (s[i - 1] != ' ')
        i--;
      j = i;
      while (j++ < n && s[j] != ' ')
        ;
      j -= 1;
      reverse_string(s, i, j);
      i = j;
    }
  }

  void remove_dup_spaces(string &s, int n) {
    int i = 0, j = 0;
    while (j < n) {
      while (j < n && s[j] == ' ')
        j++; // removing duplicate spaces

      if (j > 0 && s[j - 1] != ' ')
        j--;
      if (j < n && 0 != i)
        s[i++] = ' '; // add one space between words
      while (j < n && s[j] != ' ') {
        s[i++] = s[j++];
      }
    }
    s = s.substr(0, i);
  }

  void reverse_string(string &s, int i, int j) {
    while (i < j) {
      char c = s[i];
      s[i++] = s[j];
      s[j--] = c;
    }
  }
};

int main() {
  Solution s;
  string as = "i     love blue    sky   and Coca Cola ";
  as = "the sky is blue";
  as = " o";
  s.reverseWords(as);
  cout << "The size is : " << as.size() << endl;
  // s.reverse_string(as, 0, as.size() - 1);
  // cout << as << endl;
  // s.reverse_each_word(as, as.size()-1);
  // cout << as << endl;
  // s.remove_dup_spaces(as, as.size());
  cout << as << endl;
}
