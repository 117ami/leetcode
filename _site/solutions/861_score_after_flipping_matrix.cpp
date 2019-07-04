#include "aux.cpp"
/**
We have a two dimensional matrixA where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that
row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a
binary number, and the score of the matrix is the sum of these numbers.
Return the highest possiblescore.

Example 1:
Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:
        1 <= A.length <= 20
        1 <= A[0].length <= 20
        A[i][j]is 0 or 1.

 https://leetcode.com/problems/score-after-flipping-matrix/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int matrixScore(vector<vector<int>> &a) {
    int res = 0, col = a[0].size(), row = a.size();
    for (int j = 0; j < col; j++) {
      int cter = 0;
      for (int i = 0; i < row; i++) {
        cter += a[i][0] ^ a[i][j];
      }
      res += (1 << (col - 1 - j)) * max(cter, row - cter);
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<vector<int>> a = {{0, 0, 1, 1}, {1, 0, 1, 0}, {1, 1, 0, 0}};
  say(s.matrixScore(a));
  say("hello world");
  int m = 23, n = 398249;
  say(__gcd(m, n));
}
