#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given an array of integers nums and a positive integer k, find whether it's
possible to divide this array into k non-empty subsets whose sums are all equal.
Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3)
with equal sums.
Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  bool canPartitionKSubsets(vector<int> &nums, int k) {
    if (nums.empty())
      return false;
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (nums.size() < k || sum % k != 0)
      return false;
    vector<int> seen(nums.size(), 0);
    return possible(nums, seen, 0, k, 0, sum / k);
  }

  bool possible(std::vector<int> &nums, std::vector<int> &seen, int i, int k,
                int cursum, int target) {
  	cout << i << ", " << k << ", " << cursum << endl; 
    if (k == 1)
      return true;
    if (cursum == target)
      return possible(nums, seen, 0, k - 1, 0, target);
  	if (cursum > target)
  		return false; 
    for (int j = i; j < nums.size(); j++) {
      if (!seen[j]) {
        seen[j] = 1;
        if (possible(nums, seen, j + 1, k, cursum + nums[j], target))
          return true;
        seen[j] = 0;
      }
    }
    return false;
  }
};

int main() {
  Solution s;
  vector<int> nums = {1, 4, 3, 5, 7};
  sort(nums.begin(), nums.end(), greater<int>());
  for (int n : nums)
    cout << n << " ";
  cout << endl;
  nums = {4, 3, 2, 3, 5, 2, 1};
  cout << s.canPartitionKSubsets(nums, 4) << endl;
}
