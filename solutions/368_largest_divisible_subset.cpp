#include "aux.cpp"
/**
Given a set of distinct positive integers, find the largest subset such that
every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si
= 0. If there are multiple solutions, return any subset is fine. Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]

 https://leetcode.com/problems/largest-divisible-subset/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<int> largestDivisibleSubset(vector<int> &nums) {
    if (nums.size() == 0)
      return nums;
    sort(nums.begin(), nums.end(),
         [](const int a, const int b) { return a > b; });
    unordered_map<int, int> maxlen;
    unordered_map<int, int> nexnum;
    vector<int> res = {0, 0}, tmp;
    for (int i = 0; i < nums.size(); i++) {
      int cn = nums[i];
      maxlen[cn] = 1;
      nexnum[cn] = -1;
      for (int j = i - 1; j >= 0; j--) {
        if (nums[j] % cn != 0)
          continue;
        if (maxlen[nums[j]] + 1 > maxlen[cn]) {
          maxlen[cn] = maxlen[nums[j]] + 1;
          nexnum[cn] = nums[j];
        }
      }
      if (maxlen[cn] > res[0]) {
        res[0] = maxlen[cn];
        res[1] = cn;
      }
    }
    tmp.emplace_back(res[1]);
    while (nexnum[tmp.back()] != -1)
      tmp.emplace_back(nexnum[tmp.back()]);
    return tmp;
  }
};

int main() {
  Solution s;
  vector<int> nums = {3, 2, 9, 6, 8, 16, 25, 26, 28, 27, 32};
  say(s.largestDivisibleSubset(nums));
}
