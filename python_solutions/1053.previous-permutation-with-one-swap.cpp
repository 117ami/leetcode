#include <vector>
/*
 * @lc app=leetcode id=1053 lang=cpp
 *
 * [1053] Previous Permutation With One Swap
 *
 * https://leetcode.com/problems/previous-permutation-with-one-swap/description/
 *
 * algorithms
 * Medium (48.47%)
 * Total Accepted:    13.2K
 * Total Submissions: 27.3K
 * Testcase Example:  '[3,2,1]'
 *
 * Given an array A of positive integers (not necessarily distinct), return the
 * lexicographically largest permutation that is smaller than A, that can be
 * made with one swap (A swap exchanges the positions of two numbers A[i] and
 * A[j]).  If it cannot be done, then return the same array.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [3,2,1]
 * Output: [3,1,2]
 * Explanation: Swapping 2 and 1.
 *
 *
 * Example 2:
 *
 *
 * Input: [1,1,5]
 * Output: [1,1,5]
 * Explanation: This is already the smallest permutation.
 *
 *
 * Example 3:
 *
 *
 * Input: [1,9,4,6,7]
 * Output: [1,7,4,6,9]
 * Explanation: Swapping 9 and 7.
 *
 *
 * Example 4:
 *
 *
 * Input: [3,1,1,3]
 * Output: [1,3,1,3]
 * Explanation: Swapping 1 and 3.
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= A.length <= 10000
 * 1 <= A[i] <= 10000
 *
 *
 */
class Solution {
public:
  vector<int> prevPermOpt1(vector<int> &ns) {
    if (ns.size() <= 1)
      return ns;
    int idx = ns.size() - 1;
    while (idx > 0 && ns[idx] >= ns[idx - 1])
      idx--;

    say(idx);
    // ns is already smallest.
    if (idx-- == 0)
      return ns;
    int j = ns.size() - 1;
    while (j > idx && (ns[j] >= ns[idx] || ns[j] == ns[j - 1]))
      j--;
    
    say(vector<int>{idx, j});
    swap(ns[idx], ns[j]);
    return ns;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
