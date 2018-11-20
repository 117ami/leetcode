#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Count the number of segments in a string, where a segment is defined to be a
contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.
Example:
Input: "Hello, my name is John"
Output: 5

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int countSegments(string s) {
    int res = 0, i = 0;
    while (i < s.size()) {
      while (' ' == s[i] && i < s.size())
        i++;
      if (i < s.size())
        res++;
      while (' ' != s[i] && i < s.size())
        i++;
    }
    return res;
  }
};

int main() {
  Solution s;
  string str = "  Hello, my name is   pig   ";
  cout << s.countSegments(str) << endl;
}
