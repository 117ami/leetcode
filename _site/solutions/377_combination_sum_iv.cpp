#include "aux.cpp"
/**
 Given an integer array with all positive numbers and no duplicates, find the
number of possible combinations that add up to a positive integer target.
Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
Credits:Special thanks to @pbrother for adding this problem and creating all
test cases. https://leetcode.com/problems/combination-sum-iv/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int combinationSum4(vector<int> &nums, int target) {
    vector<int> res(target + 1, 0);
    res[0] = 1;
    for (int i = 1; i <= target; i++)
      for (auto n : nums)
        if (i >= n)
          res[i] += res[i - n];
    return res.back();
  }
};

int main() {
  Solution s;
  std::vector<int> nums = {1, 2, 3};
  int target = 4;
  say(s.combinationSum4(nums, target));
}
