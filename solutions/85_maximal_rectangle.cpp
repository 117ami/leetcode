#include "aux.cpp"
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
   Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
   containing only 1's and return its area.
   Example:
   Input:
   [
   ["1","0","1","0","0"],
   ["1","0","1","1","1"],
   ["1","1","1","1","1"],
   ["1","0","0","1","0"]
   ]
   Output: 6

   https://leetcode.com/problems/maximal-rectangle/description/
**/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int maximalRectangle(vector<vector<char>> &matrix) {
    if (0 == matrix.size())
      return 0;
    int res = 0;
    vector<vector<pair<int, int>>> cache(
        matrix.size(), vector<pair<int, int>>(matrix[0].size()));
    for (int i = matrix.size() - 1; i >= 0; i--) {
      for (int j = matrix[0].size() - 1; j >= 0; j--) {
        if (matrix[i][j] == '0')
          cache[i][j] = make_pair(0, 0);
        else if (i == matrix.size() - 1) {
          cache[i][j] = j == matrix[0].size() - 1
                            ? make_pair(1, 1)
                            : make_pair(cache[i][j + 1].first + 1, 1);
          res = max(res, cache[i][j].first);
        } else if (j == matrix[0].size() - 1) {
          cache[i][j] = i == matrix.size() - 1
                            ? make_pair(1, 1)
                            : make_pair(1, cache[i + 1][j].second + 1);
          res = max(res, cache[i][j].second);
        } else {
          cache[i][j] =
              make_pair(cache[i][j + 1].first + 1, cache[i + 1][j].second + 1);
          // cout << i << " " << j << " / ";
          // say(cache[i][j]);
          int rowlen = cache[i][j].first;
          for (int k = 0; k < cache[i][j].second; k++) {
            rowlen = min(rowlen, cache[i + k][j].first);
            res = max(res, (k + 1) * rowlen);
          }
        }
      }
    }
    return res;
  }
};

int main() {
  Solution s;
  vector<std::vector<char>> matrix = {{'1', '0', '1', '1', '1'},
                                      {'1', '0', '1', '1', '1'},
                                      {'1', '1', '1', '1', '1'},
                                      {'1', '1', '1', '1', '1'}};

  // matrix = {{'1', '1', '1', '1', '1', '1', '1', '1'},
  //           {'1', '1', '1', '1', '1', '1', '1', '0'},
  //           {'1', '1', '1', '1', '1', '1', '1', '0'},
  //           {'1', '1', '1', '1', '1', '0', '0', '0'},
  //           {'0', '1', '1', '1', '1', '0', '0', '0'}};

  say(s.maximalRectangle(matrix));
}
