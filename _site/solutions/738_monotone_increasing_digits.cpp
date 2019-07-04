#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**

Given a non-negative integer N, find the largest number that is less than or
equal to N with monotone increasing digits. (Recall that an integer has monotone
increasing digits if and only if each pair of adjacent digits x and y satisfy x
<= y.) Example 1: Input: N = 10 Output: 9 Example 2: Input: N = 1234 Output:
1234 Example 3: Input: N = 332 Output: 299 Note: N is an integer in the range
[0, 10^9].

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int monotoneIncreasingDigits(int N) {
    string n_str = to_string(N);
    int loc = n_str.size(), res = 0;
    for (int i = n_str.size() - 1; i > 0; i--)
      if (n_str[i] < n_str[i - 1]) {
        loc = i;
        n_str[i - 1] -= 1;
      }
    for (int i = loc; i < n_str.size(); i++)
      n_str[i] = '9';

    return stoi(n_str);
  }
};

int main() {
  Solution s;
  int n = 1234;
  say(s.monotoneIncreasingDigits(n));

  srand(time(NULL));
  n = rand() % 100000;
  say(n);
}
