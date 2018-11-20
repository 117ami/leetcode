#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**

You are given two integer arrays nums1 and nums2 sorted in ascending order and
an integer k.
Define a pair (u,v) which consists of one element from the first array and one
element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
Return: [1,2],[1,4],[1,6]
The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
Return: [1,1],[1,1]
The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3
Return: [1,3],[2,3]
All possible pairs are returned from the sequence:
[1,3],[2,3]
Credits:Special thanks to @elmirap and @StefanPochmann for adding this problem
and creating all test cases.
 https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<pair<int, int>> kSmallestPairs(vector<int> &nums1, vector<int> &nums2,
                                        int k) {
    vector<pair<int, int>> res;
    if (0 == nums2.size() || 0 == nums1.size() || 0 == k)
      return res;
    auto comp = [&nums1, &nums2](pair<int, int> a, pair<int, int> b) {
      return nums1[a.first] + nums2[a.second] >
             nums1[b.first] + nums2[b.second];
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)>
        min_heap(comp);
    min_heap.emplace(0, 0);
    while (k-- > 0 && min_heap.size()) {
      auto idx = min_heap.top();
      min_heap.pop();
      res.emplace_back(nums1[idx.first], nums2[idx.second]);
      if (idx.first < nums1.size() - 1)
        min_heap.emplace(idx.first + 1, idx.second);
      if (0 == idx.first && idx.second < nums2.size() - 1)
        min_heap.emplace(idx.first, idx.second + 1);
    }

    return res;
  }
};

int main() {
  Solution s;
  std::vector<int> a = {1, 5, 7};
  std::vector<int> b = {2, 3, 8};
  for (auto p : s.kSmallestPairs(a, b, 3))
    cout << p.first << ", " << p.second << endl;
}
