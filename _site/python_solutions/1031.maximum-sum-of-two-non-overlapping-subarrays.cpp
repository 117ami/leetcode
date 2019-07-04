/*
 * @lc app=leetcode id=1031 lang=cpp
 *
 * [1031] Maximum Sum of Two Non-Overlapping Subarrays
 *
 * https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
 *
 * algorithms
 * Medium (52.51%)
 * Total Accepted:    2.8K
 * Total Submissions: 5.2K
 * Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
 *
 * Given an array A of non-negative integers, return the maximum sum of
 * elements in two non-overlapping (contiguous) subarrays, which have lengths L
 * and M.  (For clarification, the L-length subarray could occur before or
 * after the M-length subarray.)
 *
 * Formally, return the largest V for which V = (A[i] + A[i+1] + ... +
 * A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
 *
 *
 * 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
 * 0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 *
 *
 *
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
 * Output: 20
 * Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
 * length 2.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
 * Output: 29
 * Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9]
 * with length 2.
 *
 *
 *
 * Example 3:
 *
 *
 * Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
 * Output: 31
 * Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8]
 * with length 3.
 *
 *
 *
 *
 * Note:
 *
 *
 * L >= 1
 * M >= 1
 * L + M <= A.length <= 1000
 * 0 <= A[i] <= 1000
 *
 *
 *
 *
 *
 */

// #include "aux.cpp"

class Solution {
public:
  int maxSumTwoNoOverlap(vector<int> &A, int L, int M) {
    for (int i = 1; i < A.size(); i++)
      A[i] += A[i - 1];
    int res = A[L + M - 1], maxL = A[L - 1], maxM = A[M - 1];
    for (int i = L + M; i < A.size(); i++) {
      maxL = max(maxL, A[i - M] - A[i - L - M]);
      maxM = max(maxM, A[i - L] - A[i - L - M]);
      res = max(res, max(A[i] - A[i - L] + maxM, A[i] - A[i - M] + maxL));
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
//   Solution s;
//   std::vector<int> A = {3, 8, 1, 3, 2, 1, 8, 9, 0};
//   say(s.maxSumTwoNoOverlap(A, 3, 2));
//   return 0;
// }
