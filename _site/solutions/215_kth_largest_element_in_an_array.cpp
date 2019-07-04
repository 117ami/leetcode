#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element. Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 <= k <= array's length.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int findKthLargest(vector<int> &nums, int k) {
    sort(nums.begin(), nums.end());
    return nums[nums.size() - k];
  }
};

int main() {
  Solution s;
  vector<int> nums = {3, 2, 3, 1, 2, 4, 5, 5, 6};
  //vector<int> nums ={3,2,1,5,6,4};
  cout << s.findKthLargest(nums, 6) << endl;
}
