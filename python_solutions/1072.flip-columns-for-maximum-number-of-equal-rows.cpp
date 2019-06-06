/*
 * @lc app=leetcode id=1072 lang=cpp
 *
 * [1072] Flip Columns For Maximum Number of Equal Rows
 *
 * https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/
 *
 * algorithms
 * Medium (48.64%)
 * Total Accepted:    2.6K
 * Total Submissions: 5K
 * Testcase Example:  '[[0,1],[1,1]]'
 *
 * Given a matrix consisting of 0s and 1s, we may choose any number of columns
 * in the matrix and flip every cell in that column.  Flipping a cell changes
 * the value of that cell from 0 to 1 or from 1 to 0.
 *
 * Return the maximum number of rows that have all values equal after some
 * number of flips.
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
 * Input: [[0,1],[1,1]]
 * Output: 1
 * Explanation: After flipping no values, 1 row has all values equal.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [[0,1],[1,0]]
 * Output: 2
 * Explanation: After flipping values in the first column, both rows have equal
 * values.
 *
 *
 *
 * Example 3:
 *
 *
 * Input: [[0,0,0],[0,0,1],[1,1,0]]
 * Output: 2
 * Explanation: After flipping values in the first two columns, the last two
 * rows have equal values.
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= matrix.length <= 300
 * 1 <= matrix[i].length <= 300
 * All matrix[i].length's are equal
 * matrix[i][j] is 0 or 1
 *
 *
 *
 *
 */
using namespace std;
using LL = long long;
using uLL = unsigned long long;
using VI = vector<int>;
#define EACH(i, n) for (int i = 0; i <= int(n); ++i)
#define EACHV(i, n) for (int i = int(n); i >= 0; --i)
#define unfold(i, arr) for (auto &i : arr)

class Solution {
public:
  int maxEqualRowsAfterFlips(vector<vector<int>> &matrix) {
    unordered_map<uLL, int> has;
    int res = 0;
    unfold(row, matrix) res = max(res, ++has[toKey(row)]);
    return res;
  }

  uLL toKey(VI &row) {
    bool iv = row[0] == 1;
    uLL key = 0;
    unfold(n, row) {
      if (iv)
        n = !n;
      key = (key << 1) | n;
    }
    return key;
  }

  int maxEqualRowsAfterFlips_2(vector<vector<int>> &matrix) {
    int m = matrix.size(), n = matrix[0].size(), res = 0;
    EACH(i, m - 1) {
      VI flip(matrix[i]);
      int cur = 0;
      EACH(j, n - 1) flip[j] = 1 - flip[j];
      EACH(j, m - 1) if (matrix[j] == matrix[i] || flip == matrix[j]) cur += 1;
      res = max(cur, res);
    }
    return res;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
