#include<vector>
/*
 * @lc app=leetcode id=315 lang=cpp
 *
 * [315] Count of Smaller Numbers After Self
 *
 * https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
 *
 * algorithms
 * Hard (41.46%)
 * Total Accepted:    134.3K
 * Total Submissions: 323.4K
 * Testcase Example:  '[5,2,6,1]'
 *
 * You are given an integer array nums and you have to return a new counts
 * array. The counts array has the property where counts[i] is the number of
 * smaller elements to the right of nums[i].
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [5,2,6,1]
 * Output: [2,1,1,0]
 * Explanation:
 * To the right of 5 there are 2 smaller elements (2 and 1).
 * To the right of 2 there is only 1 smaller element (1).
 * To the right of 6 there is 1 smaller element (1).
 * To the right of 1 there is 0 smaller element.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 *
 *
 */

class Solution {
public:
  void mergesort(int left, int right, vector<int> &indices, vector<int> &nums,
                 vector<int> &res) {
    if (right - left <= 1)
      return;
    int mid = left + (right - left) / 2;
    mergesort(left, mid, indices, nums, res),
        mergesort(mid, right, indices, nums, res);
    int i = left, j = mid;
    vector<int> tmp;
    tmp.reserve(right - left);

    while (i < mid || j < right) {
      if (j == right || (i < mid && nums[indices[i]] <= nums[indices[j]])) {
        // All number from nums[mid] to nums[j-1] are smaller than nums[i]
        res[indices[i]] += j - mid;
        tmp.emplace_back(indices[i++]);
      } else {
        tmp.emplace_back(indices[j++]);
      }
    }

    std::move(tmp.begin(), tmp.end(), indices.begin() + left); 
  }

  vector<int> countSmaller(vector<int> &nums) {
    int n = nums.size();
    vector<int> res(n, 0), indices(n);
    std::iota(indices.begin(), indices.end(), 0);
    mergesort(0, n, indices, nums, res);
    return res;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
