// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares
// Hard (Difficulty)

// Given a rectangle of size n x m, find the minimum number of integer-sided
// squares that tile the rectangle.   Example 1:
//
// Example 2:
//
// Example 3:
//
//  
// Constraints:
// Input: n = 2, m = 3
// Output: 3
// Explanation: 3 squares are necessary to cover the rectangle.
// 2 (squares of 1x1)
// 1 (square of 2x2)
// Input: n = 5, m = 8
// Output: 5
//
// Input: n = 11, m = 13
// Output: 6
//
// xxxxxxxxxx
// class Solution {
// public:
//     int tilingRectangle(int n, int m) {
//         
//     }
// };

class Solution {

public:
  int ans = 169;
  void dfs(vector<int> &hs, int steps, int n) {
    if (steps >= ans)
      return;
    bool ret = true;

    for (auto &h : hs) {
      if (h != n) {
        ret = false;
        break;
      }
    }
    if (ret) {
      ans = min(ans, steps);
      return;
    }

    int min_h = n, idx = 0, ridx = 0;
    for (size_t i = 0; i < hs.size(); i++)
      if (hs[i] < min_h) {
        min_h = hs[i];
        idx = i;
      }

    ridx = idx;
    while (ridx < hs.size() && hs[ridx++] == min_h)
      ;

    for (size_t i = min(n - min_h, ridx - idx); i > 0; i--) {
      vector<int> tmp(hs);
      for (size_t j = 0; j < i; j++) {
        tmp[idx + j] += i;
      }
      dfs(tmp, steps + 1, n);
    }
  }

  int tilingRectangle(int n, int m) {
    ios_base::sync_with_stdio(false);
    if (n == m)
      return 1;
    vector<int> hs(m, 0);
    dfs(hs, 0, n);
    return ans;
  }
};