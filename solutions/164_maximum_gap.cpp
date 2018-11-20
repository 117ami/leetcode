#include "aux.cpp"
/**
Given an unsorted array, find the maximum difference between the successive
elements in its sorted form.
Return 0 if the array contains less than 2 elements.
Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
            (3,6) or (6,9) has the maximum difference 3.
Example 2:
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:
        You may assume all elements in the array are non-negative integers and
fit in the 32-bit signed integer range.
        Try to solve it in linear time/space.

 https://leetcode.com/problems/maximum-gap/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int maximumGap(vector<int> &nums) {
    if (nums.size() < 2)
      return 0;
    int maxv = 0, minv = INT_MAX;
    for (auto n : nums) {
      maxv = max(maxv, n);
      minv = min(minv, n);
    }

    int bucket_size = max(1, (maxv - minv) / ((int)nums.size() - 1));
    int bucket_num = (maxv - minv) / bucket_size + 1;

    vector<int> bucket_min(bucket_num, INT_MAX);
    vector<int> bucket_max(bucket_num, -1);
    for (auto n : nums) {
      int idx = (n - minv) / bucket_size;
      bucket_min[idx] = min(bucket_min[idx], n);
      bucket_max[idx] = max(bucket_max[idx], n);
    }

    int res = 0, last_max = bucket_max[0];
    for (int i = 1; i < bucket_num; i++) {
      res = bucket_min[i] == INT_MAX ? res : max(res, bucket_min[i] - last_max);
      last_max = bucket_max[i] == -1 ? last_max : bucket_max[i];
    }
    return res;
  }
};

int main() { Solution s; }
