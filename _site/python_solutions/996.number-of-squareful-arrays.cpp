/*
 * @lc app=leetcode id=996 lang=cpp
 *
 * [996] Number of Squareful Arrays
 *
 * https://leetcode.com/problems/number-of-squareful-arrays/description/
 *
 * algorithms
 * Hard (47.67%)
 * Total Accepted:    4.3K
 * Total Submissions: 8.9K
 * Testcase Example:  '[1,17,8]'
 *
 * Given an array A of non-negative integers, the array is squareful if for
 * every pair of adjacent elements, their sum is a perfect square.
 *
 * Return the number of permutations of A that are squareful.  Two permutations
 * A1 and A2 differ if and only if there is some index i such that A1[i] !=
 * A2[i].
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [1,17,8]
 * Output: 2
 * Explanation:
 * [1,8,17] and [17,8,1] are the valid permutations.
 *
 *
 * Example 2:
 *
 *
 * Input: [2,2,2]
 * Output: 1
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= A.length <= 12
 * 0 <= A[i] <= 1e9
 *
 */
// #include "aux.cpp"

class Solution {
  unordered_map<int, int> count;
  unordered_map<int, unordered_set<int>> cand;
  int res = 0;

public:
  int numSquarefulPerms(vector<int> &A) {
    if (A.size() == 0)
      return 0;
    for (auto &a : A)
      count[a]++;
    for (auto &a : count)
      for (auto &b : count) {
        int x = a.first, y = b.first, s = sqrt(x + y);
        if (s * s == x + y)
          cand[x].insert(y);
      }

    for (auto c : count)
      dfs(c.first, A.size() - 1);
    return res;
  }

  void dfs(int x, int cter) {
    count[x]--;
    if (cter == 0)
      res += 1;
    for (int y : cand[x])
      if (count[y] > 0)
        dfs(y, cter - 1);
    count[x]++;
  }
};


static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();

// int main(int argc, char const *argv[]) {
// 	Solution s;
// 	return 0;
// }

