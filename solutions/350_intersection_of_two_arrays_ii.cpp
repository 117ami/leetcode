#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**

Given two arrays, write a function to compute their intersection.
Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
Note:
Each element in the result should appear as many times as it shows in both
arrays. The result can be in any order. Follow up: What if the given array is
already sorted? How would you optimize your algorithm? What if nums1's size is
small compared to nums2's size? Which algorithm is better? What if elements of
nums2 are stored on disk, and the memory is limited such that you cannot load
all elements into the memory at once?

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<int> intersect(vector<int> &nums1, vector<int> &nums2) {
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    int i = 0, j = 0;
    vector<int> ans;
    while (i < nums1.size() && j < nums2.size()) {
      if (nums1[i] == nums2[j]) {
        ans.push_back(nums2[j]);
        i++;
        j++;
      } else if (nums1[i] < nums2[j]) {
        i++;
      } else {
        j++;
      }
    }
    return ans;
  }
};

int main() {
  Solution s;
  vector<int> n1 = {1, 2, 3, 2}, n2 = {2, 3}, ans = s.intersect(n1, n2);
  for (int n : ans)
    cout << n << " ";
  cout << endl;
}
