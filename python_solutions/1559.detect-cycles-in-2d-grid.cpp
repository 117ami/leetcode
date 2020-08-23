// C libraries
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

// Containers
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// Input/Output
#include <fstream>
#include <iomanip>
#include <ios>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>

// Other
#include <algorithm>
#include <bitset>
#include <chrono>
#include <iterator>
#include <limits>
#include <random>
#include <stdexcept>
#include <string>
#include <tuple>
#include <type_traits>
#include <utility>

// ==================================================

using namespace std;

// constants
const double EPS = 1e-9;
const int MOD = 1000000007;

// type alias
using pii = pair<int, int>;
using ll = long long;
using ull = unsigned long long;
using vi = vector<int>;
using vb = vector<bool>;
using vc = vector<char>;
using vs = vector<string>;
using vvb = vector<vector<bool>>;
using vvc = vector<vector<char>>;
using vvi = vector<vector<int>>;
using vvs = vector<vector<string>>;
using mii = map<int, int>;
using mci = map<char, int>;
using si = set<int>;
using spii = set<pair<int, int>>;
using umii = unordered_map<int, int>;
using umci = unordered_map<char, int>;
using umsi = unordered_map<string, int>;
using usi = unordered_set<int>;
using usc = unordered_set<char>;
using uss = unordered_set<string>;
using vpii = vector<pair<int, int>>;

typedef struct TreeNode TreeNode;
using ptn = TreeNode *;
using tn = TreeNode;

// ==================================================

// fast IO
static auto __speedup__ = []() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  return 0;
}();

// ==================================================

// some macro for less typing
#define forloop(i, n) for (int i = 0; i < n; i++)             //[0, n)
#define forloopr(i, n) for (int i = n - 1; i >= 0; --i)       // reverse [0, n)
#define forloopup(i, a, b) for (int i = a; i < b; ++i)        // [a, b)
#define forloopdown(i, a, b) for (int i = b - 1; i >= a; --i) // reverse [a, b)
#define forunfold(i, arr) for (auto &i : arr)

#define INF 0x3f3f3f3f
#define MAX(a, b) a = max(a, b)
#define MIN(a, b) a = min(a, b)

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define ef emplace_front
#define eb emplace_back
#define qall(v) v.begin(), v.end()
#define qsize(v) (int)v.size()
#define qsort(v) sort(v.begin(), v.end())
#define rqsort(v) sort(v.rbegin(), v.rend())
#define qreverse(v) reverse(v.begin(), v.end())

// int to string
string itos(int n) { return to_string(n); }
// char to string
string ctos(char c) { return string(1, c); };

inline string upper(string s) {
  string t(s);
  transform(t.begin(), t.end(), t.begin(), ::toupper);
  return t;
}
inline string lower(string s) {
  string t(s);
  transform(t.begin(), t.end(), t.begin(), ::tolower);
  return t;
}

int dirs[5] = {-1, 0, 1, 0, -1};
// ==================================================
/*
 * @lc app=leetcode id=1559 lang=cpp
 *
 * [1559] Detect Cycles in 2D Grid
 *
 * https://leetcode.com/problems/detect-cycles-in-2d-grid/description/
 *
 * algorithms
 * Hard (41.58%)
 * Total Accepted:    3.7K
 * Total Submissions: 8.8K
 * Testcase Example:
 * '[["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]'
 *
 * Given a 2D array of characters grid of size m x n, you need to find if there
 * exists any cycle consisting of the same value in grid.
 *
 * A cycle is a path of length 4 or more in the grid that starts and ends at
 * the same cell. From a given cell, you can move to one of the cells adjacent
 * to it - in one of the four directions (up, down, left, or right), if it has
 * the same value of the current cell.
 *
 * Also, you cannot move to the cell that you visited in your last move. For
 * example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2)
 * we visited (1, 1) which was the last visited cell.
 *
 * Return true if any cycle of the same value exists in grid, otherwise, return
 * false.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: grid =
 * [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
 * Output: true
 * Explanation: There are two valid cycles shown in different colors in the
 * image below:
 *
 *
 *
 * Example 2:
 *
 *
 *
 *
 * Input: grid =
 * [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
 * Output: true
 * Explanation: There is only one valid cycle highlighted in the image
 * below:
 *
 *
 *
 * Example 3:
 *
 *
 *
 *
 * Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m <= 500
 * 1 <= n <= 500
 * grid consists only of lowercase English letters.
 *
 *
 */
class Solution {
public:
  vector<int> dir = {0, 1, 0, -1, 0};

  bool isCyclic(vector<vector<char>> &grid, vector<vector<bool>> &visited,
                int i, int j, int x, int y) {
    visited[i][j] = true;
    forloop(d, 4) {
      int a = i + dir[d];
      int b = j + dir[d + 1];
      if (a >= 0 && a < grid.size() && b >= 0 && b < grid[0].size() &&
          grid[a][b] == grid[i][j] && !(x == a && y == b))
        if (visited[a][b] || isCyclic(grid, visited, a, b, i, j))
          return true;
    }
    return false;
  }
  bool containsCycle(vector<vector<char>> &grid) {
    int n = qsize(grid), m = qsize(grid[0]);
    vvb visited(n, vb(m, false));
    forloop(i, n)
        forloop(j, m) if (!visited[i][j] &&
                          isCyclic(grid, visited, i, j, -1, -1)) return true;
    return false;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
