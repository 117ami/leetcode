#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**
Given a positive integer, return its corresponding column title as appear in an
Excel sheet. For example: 1 -> A 2 -> B 3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:
Input: 1
Output: "A"
Example 2:
Input: 28
Output: "AB"
Example 3:
Input: 701
Output: "ZY"

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  string convertToTitle(int n) {
    return 0 == n ? "" : convertToTitle(n / 26) + (char)(--n % 26 + 'A');
  }
};

int main() {
  cout << (char) (1 + 'A') << endl;
  Solution s;
  for (int i = 1; i < 59; i++)
    cout << i << ", " << s.convertToTitle(i) << endl;
  int j = 701;
  cout << j << ", " << s.convertToTitle(j) << endl;
  j = 24568;
  cout << j << ", " << s.convertToTitle(j) << endl;
}
