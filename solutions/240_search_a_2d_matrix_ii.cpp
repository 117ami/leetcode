#include "aux.cpp"
/**
Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:
        Integers in each row are sorted in ascending from left to right.
        Integers in each column are sorted in ascending from top to bottom.
Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Giventarget=5, returntrue.
Giventarget=20, returnfalse.

 https://leetcode.com/problems/search-a-2d-matrix-ii/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  bool searchMatrix(vector<vector<int>> &matrix, int target) {
    if (matrix.empty() || matrix[0].empty())
      return false;
    int i = 0, j = matrix[0].size() - 1;
    while (i < matrix.size() && j >= 0) {
      if (matrix[i][j] == target)
        return true;
      else if (matrix[i][j] > target)
        j--;
      else
        i++;
    }
    return false;
  }
};

int main() { Solution s; }
