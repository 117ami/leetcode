// https://leetcode.com/problems/count-square-submatrices-with-all-ones
// Medium
//
// Given a m * n matrix of ones and zeros, return how many square submatrices
// have all ones.   Example 1: Example 2:   Constraints: Input: matrix =
// [
//   [0,1,1,1],
//   [1,1,1,1],
//   [0,1,1,1]
// ]
// Output: 15
// Explanation:
// There are 10 squares of side 1.
// There are 4 squares of side 2.
// There is  1 square of side 3.
// Total number of squares = 10 + 4 + 1 = 15.
//
// Input: matrix =
// [
//   [1,0,1],
//   [1,1,0],
//   [1,1,0]
// ]
// Output: 7
// Explanation:
// There are 6 squares of side 1.
// There is 1 square of side 2.
// Total number of squares = 6 + 1 = 7.
//
// xxxxxxxxxx
class Solution {
public:
  int countSquares(vector<vector<int>> &matrix) {
    int ans = accumulate(matrix[0].begin(), matrix[0].end(), 0);

    for (int i = 1; i < matrix.size(); i++) {
      for (int j = 0; j < matrix[0].size(); ans += matrix[i][j++]) {
        if (matrix[i][j] && j)
          matrix[i][j] += min(min(matrix[i - 1][j - 1], matrix[i][j - 1]),
                              matrix[i - 1][j]);
      }
    }
    return ans;
  }
};
