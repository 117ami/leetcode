#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.
Examples:
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in
the window. Each time the sliding window moves right by one position. Your job
is to output the median array for each window in the original array.
For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].
Note:
You may assume k is always valid, ie: k is always smaller than input array's
size for non-empty array.
 https://leetcode.com/problems/sliding-window-median/description/
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<double> medianSlidingWindow(vector<int> &nums, int k) {
    std::vector<double> res;
    multiset<int> window(nums.begin(), nums.begin() + k);
    auto mid = next(window.begin(), k / 2);
    for (int i = k;; i++) {
      res.push_back((double(*mid) + *prev(mid, 1 - k % 2)) / 2);
      if (i == nums.size())
        return res;

      window.insert(nums[i]);
      if (nums[i] < *mid)
        mid--;
      if (nums[i - k] <= *mid)
        mid++;
      window.erase(window.lower_bound(nums[i - k]));
    }
  }
};

int main() {
  Solution s;
  multiset<int> window = {1, 5, 2, 3};
  auto it = next(window.begin(), 0);
  auto nit = next(it);
  say(*it);
  say(*nit);
  say(*prev(nit));
}
