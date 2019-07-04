#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Given an unsorted array of integers, find the length of the longest consecutive
elements sequence. Your algorithm should run in O(n) complexity. Example:
Input:[100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int longestConsecutive(vector<int> &nums) {
    unordered_map<int, int> m;
    int ans = 0;
    for (int n : nums)
      if (m[n])
        continue;
      else
        ans = max(ans, m[n] = m[n + m[n + 1]] = m[n - m[n - 1]] =
                           m[n + 1] + m[n - 1] + 1);
    return ans;
  }
};

int main() {
  Solution s;
  vector<int> nums{1, 2, 0, 1};
  cout << s.longestConsecutive(nums) << endl;

  unordered_map<int, int> umap;
  umap[1] = 0;
  if (umap[1])
    cout << "Haha" << endl;
  else
    cout << umap[2] << endl;
}
