#include "aux.cpp"
#include <algorithm>
#include <bitset>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>

/**

Starting with a positive integer N, we reorder the digits in any order
(including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting
number is a power of 2.



Example 1:

Input: 1
Output: true

Example 2:

Input: 10
Output: false

Example 3:

Input: 16
Output: true

Example 4:

Input: 24
Output: false

Example 5:

Input: 46
Output: true

Note:

    1 <= N <= 10^9
**/
using namespace std;

class Solution {
public:
  bool reorderedPowerOf2(int N) {
    string sn = to_string(N);
    sort(sn.begin(), sn.end());

    int xtm = 1;
    while (to_string(xtm).size() < sn.size())
      xtm *= 2;

    while (to_string(xtm).size() == sn.size()) {
      string sx = to_string(xtm);
      sort(sx.begin(), sx.end());
      if (sx == sn)
        return true;
      xtm *= 2;
    }
    return false;
  }
};

int main() {
  Solution s;
  for (int i = 1; i < 100; i++) {
    vector<int> x{i, s.reorderedPowerOf2(i)};
    if (1 == x.back())
      say(x);
  }
}