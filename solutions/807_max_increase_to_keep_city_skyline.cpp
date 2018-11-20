#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <vector>
/**
In a 2 dimensional array grid, each value grid[i][j] represents the height of a
building located there. We are allowed to increase the height of any number of
buildings, by any amount (the amountscan be different for different buildings).
Height0 is considered to be abuildingas well. At the end, the "skyline" when
viewed from all four directionsof the grid, i.e.top, bottom, left, and
right,must be the same as theskyline of the original grid. A city's skyline is
the outer contour of the rectangles formed by all the buildings when viewed from
a distance. Seethe following example. What is the maximum total sum that the
height of the buildings can be increased? Example: Input: grid =
[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]] Output: 35 Explanation: The grid is:
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
Notes:
        1 &lt; grid.length = grid[0].length &lt;= 50.
        All heights grid[i][j] are in the range [0, 100].
        All buildings in grid[i][j] occupy the entire grid cell: that is, they
are a 1 x 1 x grid[i][j] rectangular prism.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int maxIncreaseKeepingSkyline(vector<vector<int>> &grid) {
    int rowmax[grid.size()] = {-1}, colmax[grid.size()] = {-1};
    for (int i = 0; i < grid.size(); i++)
      for (int j = 0; j < grid.size(); j++) {
        rowmax[i] = max(rowmax[i], grid[i][j]);
        colmax[j] = max(colmax[j], grid[i][j]);
      }
    int ans = 0;
    for (int i = 0; i < grid.size(); i++)
      for (int j = 0; j < grid.size(); j++)
        ans += min(rowmax[i], colmax[j]) - grid[i][j];
    return ans;
  }
};
int main() {
  Solution s;
  vector<vector<int>> grid = {
      {3, 0, 8, 4},
      {2, 4, 5, 7},
      {9, 2, 6, 3},
      {0, 3, 1, 0},
  };
  cout << s.maxIncreaseKeepingSkyline(grid) << endl;
}
