#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <deque>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in
the window. Each time the sliding window moves right by one position. Return the
max sliding window.
Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 <= k <= input array's size for non-empty
array.
Follow up:
Could you solve it in linear time?

 https://leetcode.com/problems/sliding-window-maximum/description/
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  vector<int> maxSlidingWindow(vector<int> &nums, int k) {
    deque<int> dq;
    vector<int> res;
    for (int i = 0; i < nums.size(); i++) {
      while (!dq.empty() && nums[i] > dq.back())
        dq.pop_back();
      dq.push_back(nums[i]);

      if (i >= k && nums[i - k] == dq.front())
        dq.pop_front();
      if (i >= k - 1)
        res.push_back(dq.front());
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
  int k = 3;
  vector<int> exp = s.maxSlidingWindow(nums, k);
  say(exp);
}
