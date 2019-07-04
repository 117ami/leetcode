/*
 * @lc app=leetcode id=867 lang=cpp
 *
 * [867] Transpose Matrix
 *
 * https://leetcode.com/problems/transpose-matrix/description/
 *
 * algorithms
 * Easy (63.82%)
 * Total Accepted:    41.2K
 * Total Submissions: 64.5K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given a matrix A, return the transpose of A.
 *
 * The transpose of a matrix is the matrix flipped over it's main diagonal,
 * switching the row and column indices of the matrix.
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [[1,4,7],[2,5,8],[3,6,9]]
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [[1,2,3],[4,5,6]]
 * Output: [[1,4],[2,5],[3,6]]
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= A.length <= 1000
 * 1 <= A[0].length <= 1000
 *
 *
 *
 *
 */

// #include "aux.cpp"

class Solution {
public:
  vector<vector<int>> transpose(vector<vector<int>> &A) {
    vector<vector<int>> B(A[0].size(), vector<int>(A.size()));
    for (int i = 0; i < A.size(); i++)
      for (int j = 0; j < A[0].size(); j++)
        B[j][i] = A[i][j];
    return B;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
//   Solution s;
//   std::vector<std::vector<int>> A = {{1, 2, 3}, {5, 6, 7}};
//   vector<std::vector<int>> B = s.transpose(A);
//   say(B);
//   return 0;
// }
