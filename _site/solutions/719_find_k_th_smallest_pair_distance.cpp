#include "aux.cpp"
/**
Given an integer array, return the k-th smallest distance among all the pairs.
The distance of a pair (A, B) is defined as the absolute difference between A
and B.
Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.

 https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int smallestDistancePair(vector<int> &nums, int k) {
    sort(nums.begin(), nums.end());
    int low = 0, high = nums[nums.size() - 1] - nums[0], mid;
    while (low < high) {
      mid = (low + high) / 2;
      if (countPairs(nums, mid) < k)
        low = mid + 1;
      else
        high = mid;
    }
    return low;
  }

  int countPairs(const vector<int> &nums, int mid) {
    int res = 0;
    for (int i = 0; i < nums.size(); i++)
      res += bsearch(nums, i, mid) - i - 1;
    return res;
  }

  int bsearch(const vector<int> &nums, const int i, int mid) {
    if (i == nums.size() - 1 || nums.back() - nums[i] <= mid)
      return nums.size();
    int low = i, high = nums.size(), xmi;
    while (low < high) {
      // say(vector<int>{i, mid, xmi});
      xmi = (low + high) / 2;
      if (nums[xmi] - nums[i] <= mid)
        low = xmi + 1;
      else
        high = xmi;
    }
    return low;
  }
};

int main() {
  Solution s;
  vector<int> nums = {0, 0, 1, 0, 1, 1, 2, 1, 0};
  say(s.smallestDistancePair(nums, 8));
}
