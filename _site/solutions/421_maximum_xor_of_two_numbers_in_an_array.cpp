#include "aux.cpp"
/**
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 <= ai < 231.
Find the maximum result of ai XOR aj, where 0 <= i, j < n.
Could you do this in O(n) runtime?
Example:
Input: [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: The maximum result is 5 ^ 25 = 28.

 https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int findMaximumXOR(vector<int> &nums) {
    long res = 0, tmp = 0, mask = 0;
    for (int bit = 31; bit >= 0; bit--) {
      mask = mask | (1 << bit);
      unordered_set<long> dict;
      for (long n : nums)
        dict.insert(n & mask);

      tmp = res | (1 << bit);
      for (auto n : dict)
        if (dict.count(tmp ^ n)) {
          res = tmp;
          break;
        }
    }
    return res;
  }
};

int main() {
  Solution s;
  std::vector<int> nums = {3, 10, 5, 25, 2, 8};
  say(s.findMaximumXOR(nums));
}
