// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix
// Hard (Difficulty)

// Given a m x n binary matrix mat. In one step, you can choose one cell and
// flip it and all the four neighbours of it if they exist (Flip is changing 1
// to 0 and 0 to 1). A pair of cells are called neighboors if they share one
// edge. Return the minimum number of steps required to convert mat to a zero
// matrix or -1 if you cannot. Binary matrix is a matrix with all cells equal to
// 0 or 1 only. Zero matrix is a matrix with all cells equal to 0.   Example 1:
// Example 2:
// Example 3:
// Example 4:
//  
// Constraints:
// Input: mat = [[0,0],[0,1]]
// Output: 3
// Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally
// (1, 1) as shown.
//
// Input: mat = [[0]]
// Output: 0
// Explanation: Given matrix is a zero matrix. We don't need to change it.
//
// Input: mat = [[1,1,1],[1,0,1],[0,0,0]]
// Output: 6
//
// Input: mat = [[1,0,0],[1,0,0]]
// Output: -1
// Explanation: Given matrix can't be a zero matrix
//
// xxxxxxxxxx
// class Solution {
// public:
//     int minFlips(vector<vector<int>>& mat) {
//         
//     }
// };

static vector<int> dirs = {0, 1, 0, -1, 0};
class Solution {
public:
  int m, n;
  int bitVec(vector<vector<int>> &mat) {
    int bit = 0;
    for (auto &row : mat)
      for (auto i : row)
        bit <<= 1, bit |= i;
    return bit;
  }

  int getflip(int i, int j, int bit) {
    int x, y, pos = m * n - 1 - i * n - j;
    bit ^= 1 << pos;
    for (size_t d = 0; d < 4; d++) {
      x = i + dirs[d], y = j + dirs[d + 1];
      if (x >= 0 && y >= 0 && x < m && y < n)
        pos = m * n - 1 - x * n - y, bit ^= 1 << pos;
    }
    return bit;
  }

  int minFlips(vector<vector<int>> &mat) {
    m = mat.size(), n = mat[0].size();
    int bit = bitVec(mat), dist = 0;
    unordered_set<int> memo;

    queue<int> q;
    q.push(bit);

    while (!q.empty()) {
      size_t sz = q.size();
      while (sz--) {
        if (q.front() == 0)
          return dist;
        for (size_t i = 0; i < m; i++)
          for (size_t j = 0; j < n; j++) {
            bit = getflip(i, j, q.front());
            if (!memo.count(bit)) {
              q.push(bit), memo.insert(bit);
            }
          }
        q.pop();
      }
      dist++;
    }
    return -1;
  }
};