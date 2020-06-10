/*
 * @lc app=leetcode id=35 lang=cpp
 *
 * [35] Search Insert Position
 *
 * https://leetcode.com/problems/search-insert-position/description/
 *
 * algorithms
 * Easy (41.73%)
 * Total Accepted:    587.1K
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,3,5,6]\n5'
 *
 * Given a sorted array and a target value, return the index if the target is
 * found. If not, return the index where it would be if it were inserted in
 * order.
 *
 * You may assume no duplicates in the array.
 *
 * Example 1:
 *
 *
 * Input: [1,3,5,6], 5
 * Output: 2
 *
 *
 * Example 2:
 *
 *
 * Input: [1,3,5,6], 2
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: [1,3,5,6], 7
 * Output: 4
 *
 *
 * Example 4:
 *
 *
 * Input: [1,3,5,6], 0
 * Output: 0
 *
 *
 */

int bisect_right(vector<int> &nums, int target) {
  int l = 0, r = nums.size() - 1, m = 0;
  while (l <= r){
    m = l + (r - l) / 2;
    if (nums[m] == target)
      return m;
    else if (nums[m] > target)
      r = m - 1;
    else
      l = m + 1;
  }
  return l;
}


class Solution {
public:
  int searchInsert(vector<int> &nums, int target) {
    return bisect_right(nums, target);
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
