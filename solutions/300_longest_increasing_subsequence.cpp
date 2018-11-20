#include "aux.cpp"
/**
Given an unsorted array of integers, find the length of longest increasing
subsequence. Example: Input: [10,9,2,5,3,7,101,18] Output: 4 Explanation: The
longest increasing subsequence is [2,3,7,101], therefore the length is 4. Note:
        There may be more than one LIS combination, it is only necessary for you
to return the length. Your algorithm should run in O(n2) complexity. Follow up:
Could you improve it to O(n log n) time complexity?

 https://leetcode.com/problems/longest-increasing-subsequence/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int lengthOfLIS(vector<int> &nums) {
    vector<int> increase;
    for (auto n : nums) {
      int idx = bsearch_index(increase, n);
      if (idx == increase.size())
        increase.emplace_back(n);
      else
        increase[idx] = n;
    }
    return increase.size();
  }

  int bsearch_index(vector<int> &increase, int n) {
    if (increase.empty())
      return 0;
    else if (increase.back() < n)
      return increase.size();
    int low = 0, high = increase.size() - 1, mid;
    while (low < high) {
      mid = (low + high) / 2;
      if (increase[mid] < n)
        low = mid + 1;
      else
        high = mid;
    }
    return high;
  }
};

int main() {
  Solution s;
  vector<int> nums = {5, 6, 2, 3, 4, 5};
  say(s.lengthOfLIS(nums));
}
