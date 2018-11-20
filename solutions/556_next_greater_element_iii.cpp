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
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
which has exactly the same digits existing in the integer n and is greater in
value than n. If no such positive 32-bit integer exists, you need to return -1.
Example 1:
Input: 12
Output: 21

Example 2:
Input: 21
Output: -1


 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int nextGreaterElement(int n) {
    auto digits = to_string(n);
    next_permutation(digits.begin(), digits.end());
    auto res = stoll(digits);
    return (res > INT_MAX || res <= n) ? -1 : res; // we also check res <= n
                                                   // because in some cases, the
                                                   // next lexicographically
                                                   // greater word might not
    // exist, e.g., 321 has a next permutation 123, which is smaller.
  }
};
int main() {
  Solution s;
  int n = 987;
  say(s.nextGreaterElement(n));
  string sn = "321"; // to_string(n);
  next_permutation(sn.begin(), sn.end());
  say(sn);
}
