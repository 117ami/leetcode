#include "aux.cpp"
/**

Given an unsorted array of integers, find the number of longest increasing
subsequence. Example 1: Input: [1,3,5,4,7] Output: 2 Explanation: The two
longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7]. Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and
there are 5 subsequences' length is 1, so output 5. Note: Length of the given
array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit
signed int.

 https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int findNumberOfLIS(vector<int> &nums) {
    int res = 0, max_len = 0, sz = nums.size();
    vector<int> len(sz, 1);
    vector<int> cnt(sz, 1);
    for (int i = 0; i < sz; i++) {
      for (int j = 0; j < i; j++) {
        if (nums[i] <= nums[j])
          continue;
        if (len[i] == len[j] + 1)
          cnt[i] += cnt[j];
        if (len[i] < len[j] + 1) {
          len[i] = len[j] + 1;
          cnt[i] = cnt[j];
        }
      }
      if (max_len == len[i])
        res += cnt[i];
      if (max_len < len[i]) {
        res = cnt[i];
        max_len = len[i];
      }
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<int> nums = {1, 2, 4, 3, 5, 4, 7, 2};
  say(s.findNumberOfLIS(nums));
}
