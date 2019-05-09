/*
 * @lc app=leetcode id=939 lang=cpp
 *
 * [939] Minimum Area Rectangle
 *
 * https://leetcode.com/problems/minimum-area-rectangle/description/
 *
 * algorithms
 * Medium (50.17%)
 * Total Accepted:    15.7K
 * Total Submissions: 31.3K
 * Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
 *
 * Given a set of points in the xy-plane, determine the minimum area of a
 * rectangle formed from these points, with sides parallel to the x and y
 * axes.
 *
 * If there isn't any rectangle, return 0.
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
 * Output: 4
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
 * Output: 2
 *
 *
 *
 *
 * Note:
 *
 *
 * 1 <= points.length <= 500
 * 0 <= points[i][0] <= 40000
 * 0 <= points[i][1] <= 40000
 * All points are distinct.
 *
 *
 *
 */

// #include "aux.cpp"
// #include <string>

class Solution {
public:
  int minAreaRect(vector<vector<int>> &points) {
    int len = points.size(), lenx = 0, leny = 0;
    set<int> xs, ys;
    for (auto &pair : points) {
      xs.insert(pair[0]);
      ys.insert(pair[1]);
    }

    if (len == xs.size() || len == ys.size())
      return 0;
    if (ys.size() > xs.size()) {
      for (int i = 0; i < len; i++)
        swap(points[i][0], points[i][1]);
    }

    sort(
        points.begin(), points.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[0] < b[0]; });

    map<int, vector<int>> pairs;
    for (auto &p : points)
      pairs[p[0]].push_back(p[1]);

    unordered_map<string, int> visited;
    int res = INT_MAX, prex = points[0][0] - 1, prei = 0;

    for (auto iter = pairs.begin(); iter != pairs.end(); iter++) {
      int x = iter->first;
      vector<int> tmp = iter->second;
      sort(tmp.begin(), tmp.end());
      for (int i = 0; i < tmp.size(); i++) {
        int y1 = tmp[i];
        for (int j = 0; j < i; j++) {
          int y2 = tmp[j];
          string yy = to_string(y1) + "/" + to_string(y2);
          if (visited.find(yy) != visited.end()) {
            res = min(res, (x - visited[yy]) * (y1 - y2));
          }
          visited[yy] = x;
        }
      }
    }
    // say(res);
    return res < INT_MAX ? res : 0;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

// int main(int argc, char const *argv[]) {
//   Solution s;
//   std::vector<std::vector<int>> points = {{1, 3}, {4, 1}, {3, 3},
//                                           {3, 1}, {4, 3}, {1, 1}};
//   // std::vector<std::vector<int>> points = {
//   //     {1, 2}, {3, 2}, {1, 3}, {5, 5}, {2, 0}, {4, 5}, {3, 4}, {1, 4}, {1, 5},
//   //     {0, 0}, {0, 5}, {0, 4}, {4, 2}, {3, 5}, {5, 2}, {2, 4}, {4, 0}};
//   s.minAreaRect(points);
//   return 0;
// }
