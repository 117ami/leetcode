#include "aux.cpp"
/**
Given an m x n matrix of non-negative integers representing the height of each
unit cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to
another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.
Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:
Given the following 5x5 matrix:
  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
parentheses in above matrix).

 https://leetcode.com/problems/pacific-atlantic-water-flow/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  vector<pair<int, int>> pacificAtlantic(vector<vector<int>> &matrix) {
    vector<pair<int, int>> res;
    if (0 == matrix.size())
      return res;

    int k = matrix.size(), z = matrix[0].size();
    map<string, bool> pacific, atlantic;
    infect(matrix, pacific, matrix[0][0], 0, 0, 0, 0);
    infect(matrix, atlantic, matrix[k - 1][z - 1], k - 1, z - 1, k - 1, z - 1);
    for (int i = 0; i < k; i++)
      for (int j = 0; j < z; j++) {
        string pair = to_string(i) + "-" + to_string(j);
        if (pacific[pair] && atlantic[pair])
          res.emplace_back(make_pair(i, j));
      }

    return res;
  }

  void infect(const vector<vector<int>> &m, map<string, bool> &hash, int v,
              int i, int j, int ib, int jb) {
    string pair = to_string(i) + "-" + to_string(j);
    if (hash.find(pair) != hash.end() || i < 0 || j < 0 || i > m.size() - 1 ||
        j > m[0].size() - 1)
      return;
    if (i == ib || j == jb || v <= m[i][j]) {
      hash[pair] = true;
      infect(m, hash, m[i][j], i - 1, j, ib, jb);
      infect(m, hash, m[i][j], i, j - 1, ib, jb);
      infect(m, hash, m[i][j], i + 1, j, ib, jb);
      infect(m, hash, m[i][j], i, j + 1, ib, jb);
    }
  }
};

int main() {
  Solution s;

  std::vector<std::vector<int>> matrix = {{1, 2, 2, 3, 5},
                                          {3, 2, 3, 4, 4},
                                          {2, 4, 5, 3, 1},
                                          {6, 7, 1, 4, 5},
                                          {5, 1, 1, 2, 4}};
  vector<pair<int, int>> res = s.pacificAtlantic(matrix);
  for (auto pair : res)
    cout << pair.first << " " << pair.second << endl;
}
