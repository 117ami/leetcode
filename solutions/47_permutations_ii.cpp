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
Given a collection of numbers that might contain duplicates, return all possible
unique permutations.
Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<vector<int>> permuteUnique2(vector<int> &nums) {
    vector<vector<int>> res;
    vector<int> xns(nums);
    do {
      res.push_back(xns);
      nextPermutation(xns);
    } while (!equal(nums, xns));
    say(res);
    return res;
  }

  vector<vector<int>> permuteUnique(vector<int> &nums) {
    vector<vector<int>> res;
    sort(nums.begin(), nums.end());
    do {
      res.push_back(nums);
    } while (next_permutation(nums.begin(), nums.end()));
    say(res);
    return res;
  }

  bool equal(std::vector<int> na, vector<int> nb) {
    for (int i = 0; i < na.size(); i++)
      if (na[i] != nb[i])
        return false;
    return true;
  }

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
  vector<int> nums = {1, 2, 1};
  s.permuteUnique(nums);
  nums = {3, 2, 1};
  next_permutation(nums.begin(), nums.end());
  say(nums);
}
