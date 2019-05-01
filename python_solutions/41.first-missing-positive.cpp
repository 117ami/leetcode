/*
 * @lc app=leetcode id=41 lang=cpp
 *
 * [41] First Missing Positive
 *
 * https://leetcode.com/problems/first-missing-positive/description/
 *
 * algorithms
 * Hard (28.67%)
 * Total Accepted:    206.5K
 * Total Submissions: 719.7K
 * Testcase Example:  '[1,2,0]'
 *
 * Given an unsorted integer array, find the smallest missing positive
 * integer.
 *
 * Example 1:
 *
 *
 * Input: [1,2,0]
 * Output: 3
 *
 *
 * Example 2:
 *
 *
 * Input: [3,4,-1,1]
 * Output: 2
 *
 *
 * Example 3:
 *
 *
 * Input: [7,8,9,11,12]
 * Output: 1
 *
 *
 * Note:
 *
 * Your algorithm should run in O(n) time and uses constant extra space.
 *
 */
class Solution {
public:
  int firstMissingPositive(vector<int> &nums) {
    for (int i = 0; i < nums.size(); i++) {
      while (nums[i] > 0 && nums[i] <= nums.size() && nums[i] != nums[nums[i] - 1]) 
      	swap(nums[i], nums[nums[i] - 1]); 
    }

    for (int i = 0; i < nums.size(); i++)
      if (i + 1 != nums[i])
        return i + 1;
    return nums.size() + 1;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
// 	Solution s;
// 	return 0;
// }
