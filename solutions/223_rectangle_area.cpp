#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as
shown in the figure.
Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:
Assume that the total area is never beyond the maximum possible value of int.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int computeArea(int a, int b, int c, int d, int e, int f, int g, int h) {
    int totalArea = area(a, b, c, d) + area(e, f, g, h);
    if (e >= c || a >= g || f >= d || b >= h) // intersection area is zero
      return totalArea;
    int x = max(a, e);
    int y = max(b, f);
    int u = min(c, g);
    int v = min(d, h);
    return totalArea - area(x, y, u, v);
  }
  int area(int a, int b, int c, int d) { return (c - a) * (d - b); }
};

int main() {
  Solution s;
  cout << s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) << endl;
}
