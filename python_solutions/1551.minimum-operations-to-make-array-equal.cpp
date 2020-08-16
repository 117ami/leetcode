/*
 * @lc app=leetcode id=1551 lang=cpp
 *
 * [1551] Minimum Operations to Make Array Equal
 *
 * https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/
 *
 * algorithms
 * Medium (78.16%)
 * Total Accepted:    7.4K
 * Total Submissions: 9.4K
 * Testcase Example:  '3'
 *
 * You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid
 * values of i (i.e. 0 <= i < n).
 *
 * In one operation, you can select two indices x and y where 0 <= x, y < n and
 * subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and
 * arr[y] += 1). The goal is to make all the elements of the array equal. It is
 * guaranteed that all the elements of the array can be made equal using some
 * operations.
 *
 * Given an integer n, the length of the array. Return the minimum number of
 * operations needed to make all the elements of arr equal.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 3
 * Output: 2
 * Explanation: arr = [1, 3, 5]
 * First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
 * In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3,
 * 3].
 *
 *
 * Example 2:
 *
 *
 * Input: n = 6
 * Output: 9
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 10^4
 *
 */
class Solution {
public:
  int minOperations(int n) {
    vector<int> res(n / 2);
    std::iota(res.begin(), res.end(), 0);
    return n * n / 2 - n / 2 - 2 * std::accumulate(res.begin(), res.end(), 0);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
