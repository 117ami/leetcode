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
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).
The replacement must be in-place and use only constantextra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  void nextPermutation(vector<int> &nums) {
    int i = 0, j;
    for (i = nums.size() - 1; i > 0; i--)
      if (nums[i] > nums[i - 1])
        break;
    if (i == 0) {
      sort(nums.begin(), nums.end());
      return;
    }

    int rlargest = nums[i];
    for (j = nums.size() - 1; j > i; j--)
      if (nums[j] > nums[i - 1]) {
        rlargest = nums[j];
        break;
      }

    nums[j] = nums[i - 1];
    nums[i - 1] = rlargest;
    sort(nums.begin() + i, nums.end());
  }
};
int main() {
  Solution s;
  std::vector<int> nums = {5, 3, 4, 9, 7, 4, 3, 2};
  nums = {3, 2, 1};
  s.nextPermutation(nums);
  say(nums);
}
