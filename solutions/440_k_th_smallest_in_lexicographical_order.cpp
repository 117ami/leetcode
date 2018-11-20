#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
/**
   Given integers n and k, find the lexicographically k-th smallest integer in
the range from 1 to n.
   Note: 1 &le; k &le; n &le; 109.
   Example:
   Input:
   n: 13   k: 2
   Output:
   10
   Explanation:
   The lexi`cographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so
the second smallest number is 10.

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int findKthNumber(int n, int k) {
    long curr = 1;
    k--;
    while (k > 0) {
      int steps = calSteps(n, curr, curr + 1);
      if (steps <= k) {
        curr += 1;
        k -= steps;
      } else {
        curr *= 10;
        k -= 1;
      }
    }
    return static_cast<int>(curr);
  }

  int calSteps(int n, long p, long q) {
    int steps = 0;
    while (p <= n) {
      steps += static_cast<int>(min(n + 1L, q) - p);
      p *= 10;
      q *= 10;
    }
    return steps;
  }
};

int main() {
  Solution s;
  int n = 681692778, k = 351251360;
  cout << s.findKthNumber(n, k) << endl;
}
