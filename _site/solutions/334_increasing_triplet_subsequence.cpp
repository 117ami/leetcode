#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**

Given an unsorted array return whether an increasing subsequence of length 3
exists or not in the array.
Formally the function should:
Return true if there exists i, j, k
such that arr[i] &lt; arr[j] &lt; arr[k] given 0 &le; i &lt; j &lt; k &le; n-1
else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.
Examples:
Given [1, 2, 3, 4, 5],
return true.
Given [5, 4, 3, 2, 1],
return false.
Credits:Special thanks to @DjangoUnchained for adding this problem and creating
all test cases.
 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  bool increasingTriplet(vector<int> &nums) {
    int a = INT_MAX, b = INT_MAX;
    for (int n : nums) {
      a = min(a, n);
      if (n > a)
        b = min(b, n);
      if (n > b)
        return true;
    }
    return false;
  }
};

int main() {
  Solution s;
  vector<int> nums {1, 2, 3, 9};
  cout << s.increasingTriplet(nums) << endl;
}
