#include "aux.cpp"
/**
Implement function ToLowerCase() that has a string parameter str, and returns
the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"
Example 2:
Input: "here"
Output: "here"
Example 3:
Input: "LOVELY"
Output: "lovely"

 https://leetcode.com/problems/to-lower-case/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  string toLowerCase(string str) {
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    return str;
  }
};

int main() {
  Solution s;
  string str = "aHKKKldkjf";
  say(s.toLowerCase(str));
}
