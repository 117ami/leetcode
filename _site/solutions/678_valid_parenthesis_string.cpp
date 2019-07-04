#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**

Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity
of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  bool checkValidString(string s) {
    int left = 0, right = 0;
    for (char c : s) {
      left = c == '(' ? left + 1 : left - 1;
      right = c == ')' ? right - 1 : right + 1;
      left = max(left, 0);
      if (right < 0)
        return false;
    }
    return left == 0;
  }
};
int main() { Solution s; }
