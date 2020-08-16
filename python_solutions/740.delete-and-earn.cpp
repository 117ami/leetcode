#include <vector>
/*
 * @lc app=leetcode id=740 lang=cpp
 *
 * [740] Delete and Earn
 *
 * https://leetcode.com/problems/delete-and-earn/description/
 *
 * algorithms
 * Medium (48.68%)
 * Total Accepted:    39.5K
 * Total Submissions: 81.1K
 * Testcase Example:  '[3,4,2]'
 *
 * Given an array nums of integers, you can perform operations on the array.
 *
 * In each operation, you pick any nums[i] and delete it to earn nums[i]
 * points. After, you must delete every element equal to nums[i] - 1 or nums[i]
 * + 1.
 *
 * You start with 0 points. Return the maximum number of points you can earn by
 * applying such operations.
 *
 * Example 1:
 *
 *
 * Input: nums = [3, 4, 2]
 * Output: 6
 * Explanation:
 * Delete 4 to earn 4 points, consequently 3 is also deleted.
 * Then, delete 2 to earn 2 points. 6 total points are earned.
 *
 *
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [2, 2, 3, 3, 3, 4]
 * Output: 9
 * Explanation:
 * Delete 3 to earn 3 points, deleting both 2's and the 4.
 * Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
 * 9 total points are earned.
 *
 *
 *
 *
 * Note:
 *
 *
 * The length of nums is at most 20000.
 * Each element nums[i] is an integer in the range [1, 10000].
 *
 *
 *
 *
 */
class Solution {
public:
  int deleteAndEarn(vector<int> &nums) {
      int v[10001];
      memset(v, 0, sizeof(v));
      for(int i = 0; i < nums.size(); i++) v[nums[i]] += nums[i];
      int t = 0, s = 0; 
      for(auto i: v) {
          int copy_t = t; 
          t = s + i, s = max(s, copy_t);
      }
      return max(t, s);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
