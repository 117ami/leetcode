#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**
Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing only 1's and return its area.
Example:
Input:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int maximalSquare(vector<vector<char>> &matrix) {
    int rsize = matrix.size(), csize = matrix[0].size(), ans = 0;
    for (int i = 0; i < rsize; i++) {
      for (int j = 0; j < csize; j++) {
        ans = max(ans, squareSize(i, j, matrix));
      }
    }
    return ans * ans;
  }

  int squareSize(int a, int b, vector<vector<char>> &matrix) {
    if ('0' == matrix[a][b])
      return 0;
    int ans = 1;
    while (a + ans <= matrix.size() && b + ans <= matrix[0].size()) {
      for (int i = a; i < a + ans; i++) {
        for (int j = b; j < b + ans; j++)
          if ('0' == matrix[i][j])
            return ans - 1;
      }
      ans += 1;
    }
    return ans - 1;
  }
};
int main() {
  Solution s;
  vector<vector<char>> matrix = {
      {'1', '0', '1', '0', '0'},
      {'1', '0', '1', '1', '1'},
      {'1', '1', '1', '1', '1'},
      {'1', '0', '0', '1', '0'},
  };
  cout << s.maximalSquare(matrix) << endl;
}
