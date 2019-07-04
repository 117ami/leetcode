/*
 * @lc app=leetcode id=448 lang=cpp
 *
 * [448] Find All Numbers Disappeared in an Array
 *
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
 *
 * algorithms
 * Easy (53.24%)
 * Total Accepted:    149.1K
 * Total Submissions: 280K
 * Testcase Example:  '[4,3,2,7,8,2,3,1]'
 *
 * Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
 * elements appear twice and others appear once.
 *
 * Find all the elements of [1, n] inclusive that do not appear in this array.
 *
 * Could you do it without extra space and in O(n) runtime? You may assume the
 * returned list does not count as extra space.
 *
 * Example:
 *
 * Input:
 * [4,3,2,7,8,2,3,1]
 *
 * Output:
 * [5,6]
 *
 *
 */
class Solution {
public:
  vector<int> findDisappearedNumbers(vector<int> &nums) {
    int i = 0;
    while (i < nums.size()) {
      int n = nums[i++];
      while (n > 0) {
        int m = nums[n - 1];
        nums[n - 1] = -1 * n;
        n = m;
      }
    }

    i = 0;
    vector<int> res;
    while (i < nums.size())
      if (nums[i++] > 0)
        res.push_back(i);
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
