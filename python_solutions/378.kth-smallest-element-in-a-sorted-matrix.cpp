/*
 * @lc app=leetcode id=378 lang=cpp
 *
 * [378] Kth Smallest Element in a Sorted Matrix
 *
 * https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
 *
 * algorithms
 * Medium (49.69%)
 * Total Accepted:    113K
 * Total Submissions: 227.4K
 * Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
 *
 * Given a n x n matrix where each of the rows and columns are sorted in
 * ascending order, find the kth smallest element in the matrix.
 *
 *
 * Note that it is the kth smallest element in the sorted order, not the kth
 * distinct element.
 *
 *
 * Example:
 *
 * matrix = [
 * ⁠  [ 1,  5,  9],
 * ⁠  [10, 11, 13],
 * ⁠  [12, 13, 15]
 * ],
 * k = 8,
 *
 * return 13.
 *
 *
 *
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ n2.
 */
using namespace std;
using vi = vector<int>;
using vvi = vector<vi>;
using ll = long long;
#define each(i, n) for (int i = 0; i <= int(n); ++i) // [0, n)
#define fori(n) for (int i = 0; i <= int(n); ++i)    // [0, n)
#include <cassert>
#define mp make_pair

class Solution {
public:
  int kthSmallest(vector<vector<int>> &matrix, int k) {
    ll n = matrix.size(), lo = matrix[0][0], hi = matrix[n - 1][n - 1];
    while (lo <= hi) {
      ll mid = (lo + hi) / 2;
      ll ct = lessEqualNumber(matrix, mid);
      if (ct < k)
        lo = mid + 1;
      else
        hi = mid - 1;
    }
    return lo;
  }
  int lessEqualNumber(vvi &matrix, int val) {
    int res = 0, i = matrix.size() - 1, j = 0;
    while (i >= 0 && j < matrix.size()) {
      if (matrix[i][j] > val)
        i--;
      else {
        res += i + 1;
        j++;
      }
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
