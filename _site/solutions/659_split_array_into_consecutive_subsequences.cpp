#include "aux.cpp"
/**
You are given an integer array sorted in ascending order (may contain
duplicates), you need to split them into several subsequences, where each
subsequences consist of at least 3 consecutive integers. Return whether you can
make such a split.
Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]

 https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  bool isPossible(vector<int> &nums) {
    if (nums.size() < 3)
      return false;
    unordered_map<int, int> freq, ends;
    for (auto n : nums) {
      freq[n] += 1;
      ends[n] = 0;
    }

    for (auto n : nums) {
      if (freq[n] <= 0)
        continue;
      else if (ends[n - 1] > 0) {
        ends[n] += 1;
        ends[n - 1] -= 1;
      } else if (freq[n + 1] > 0 && freq[n + 2] > 0) {
        freq[n + 2] -= 1;
        freq[n + 1] -= 1;
        ends[n + 2] += 1;
      } else
        return false;
      freq[n] -= 1;
    }
    return true;
  }
};

int main() {
  Solution s;
  vector<int> nums = {1, 2, 3, 4, 4, 5};
  say(s.isPossible(nums));
}
