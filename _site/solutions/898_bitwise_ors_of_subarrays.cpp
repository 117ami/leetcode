#include "aux.cpp"
/**
We have an array A of non-negative integers.
For every (contiguous) subarray B =[A[i], A[i+1], ..., A[j]] (with i <= j), we
take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] |
... | A[j]. Return the number of possibleresults. (Results that occur more than
once are only counted once in the final answer.)

Example 1:
Input: [0]
Output: 1
Explanation:
There is only one possible result: 0.
Example 2:
Input: [1,1,2]
Output: 3
Explanation:
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:
Input: [1,2,4]
Output: 6
Explanation:
The possible results are 1, 2, 3, 4, 6, and 7.

Note:
        1 <= A.length <= 50000
        0 <= A[i] <= 10^9

 https://leetcode.com/problems/bitwise-ors-of-subarrays/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int subarrayBitwiseORs(vector<int> &a) {
    std::vector<int> cache;
    for (int i = 0, st = 0, en = 0; i < a.size();
         i++, st = en, en = cache.size()) {
      cache.emplace_back(a[i]);
      for (int j = st; j < en; j++)
        // To avoid possible memory limits error caused by duplicates
        if (cache.back() != (cache[j] | a[i]))
          cache.emplace_back(cache[j] | a[i]);
      say(cache);
    }

    return unordered_set<int>(cache.begin(), cache.end()).size();
  }
  // int subarrayBitwiseORs(vector<int> &a) {
  //   unordered_set<int> res, cache, tmp;
  //   for (auto n : a) {
  //     tmp = {n};
  //     for (int k : cache)
  //       tmp.insert(k | n);
  //     cache = tmp;
  //     for (int k: cache) res.insert(k);
  //   }
  //   return res.size();
  // }
};

int main() {
  Solution s;
  vector<int> a = {1, 2, 2, 2, 2, 4};
  say(s.subarrayBitwiseORs(a));
}
