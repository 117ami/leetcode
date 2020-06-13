/*
 * @lc app=leetcode id=368 lang=cpp
 *
 * [368] Largest Divisible Subset
 *
 * https://leetcode.com/problems/largest-divisible-subset/description/
 *
 * algorithms
 * Medium (36.32%)
 * Total Accepted:    61.6K
 * Total Submissions: 169.7K
 * Testcase Example:  '[1,2,3]'
 *
 * Given a set of distinct positive integers, find the largest subset such that
 * every pair (Si, Sj) of elements in this subset satisfies:
 *
 * Si % Sj = 0 or Sj % Si = 0.
 *
 * If there are multiple solutions, return any subset is fine.
 *
 * Example 1:
 *
 *
 *
 * Input: [1,2,3]
 * Output: [1,2] (of course, [1,3] will also be ok)
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [1,2,4,8]
 * Output: [1,2,4,8]
 *
 *
 *
 */
class Solution {
public:
  vector<int> largestDivisibleSubset(vector<int> &ns) {
    sort(ns.begin(), ns.end());
    int n = ns.size();
    vector<int> cnt(n, 0);
    vector<int> pre(n, 0);
    vector<int> res;
    int maxlen = 0, maxkey = -1;
    for (int i = 0; i < n; i++) {
      cnt[i] = 1, pre[i] = -1;
      for (int j = 0; j < i; j++)
        if (ns[i] % ns[j] == 0 && 1 + cnt[j] > cnt[i]) {
          cnt[i] = 1 + cnt[j];
          pre[i] = j;
        }
      if (cnt[i] > maxlen) {
        maxlen = cnt[i];
        maxkey = i;
      }
    }
    while (maxkey != -1) {
      res.push_back(ns[maxkey]);
      maxkey = pre[maxkey];
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
