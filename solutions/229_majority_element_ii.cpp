#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given an integer array of size n, find all elements that appear more than
&lfloor; n/3 &rfloor; times.
Note: The algorithm should run in linear time and in O(1) space.
Example 1:
Input: [3,2,3]
Output: [3]
Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

**/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<int> majorityElement(vector<int> &nums) {
    vector<int> ans;

    int can1 = 0, cter1 = 0, can2 = 1, cter2 = 0;
    for (int n : nums) {
      if (n == can1)
        cter1++;
      else if (n == can2)
        cter2++;
      else if (cter1 == 0) {
        can1 = n;
        cter1 = 1;
      } else if (cter2 == 0) {
        can2 = n;
        cter2++;
      }

      else {
        cter1--;
        cter2--;
      }
    }

    cter1 = cter2 = 0;
    int bound = nums.size() / 3;

    for (int n : nums) {
      if (n == can1)
        cter1++;

      if (n == can2)
        cter2++;

      if (cter1 > bound) {
        ans.push_back(can1);
        cter1 -= nums.size();
      }
      if (cter2 > bound) {
        ans.push_back(can2);
        cter2 -= nums.size();
      }
    }
    return ans;
  }
};

int main() {
  Solution s;
  vector<int> nums{3, 0, 3, 4}; // 1, 2, 2, 1, 2, 3, 1, 3};
  for (int n : s.majorityElement(nums))
    cout << n << endl;
}
