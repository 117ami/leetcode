#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.
Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
number of 0 and 1.
Note:
The length of the given binary array will not exceed 50,000.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int findMaxLength(vector<int> &nums) {
    int res = 0, sum = 0;
    unordered_map<int, int> um;
    um[0] = -1;
    for (int i = 0; i < nums.size(); i++) {
      sum += 1 == nums[i] ? 1 : -1;
      if (um.find(sum) != um.end())
        res = max(res, i - um[sum]);
      else
        um[sum] = i;
    }
    return res;
  }
};

int main() {
  Solution s;
  std::vector<int> nums = {0, 0, 1}; //, 1, 0, 0, 0, 1, 0, 1, 1};
  cout << s.findMaxLength(nums) << endl;
}
