#include "aux.cpp"
/**
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] <
nums[3].... Example 1: Input: nums = [1, 5, 1, 1, 6, 4] Output: One possible
answer is [1, 4, 1, 5, 1, 6]. Example 2: Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.
Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

 https://leetcode.com/problems/wiggle-sort-ii/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
	// in-place but not O(n)
  void wiggleSort(vector<int> &nums) {
    vector<int> sorted(nums);
    sort(sorted.begin(), sorted.end());
    for (int i = nums.size() - 1, j = 0, k = i / 2 + 1; i >= 0; i--) {
      nums[i] = sorted[i & 1 ? k++ : j++];
    }
    // say(nums);
  }
};

int main() {
  Solution s;
  std::vector<int> nums = {1, 5, 1, 1, 6, 4};
  nums = {2, 3, 1, 3, 1, 2};
  s.wiggleSort(nums);
}
