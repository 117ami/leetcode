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
 * @lc app=leetcode id=1591 lang=cpp
 *
 * [1591] Strange Printer II
 *
 * https://leetcode.com/problems/strange-printer-ii/description/
 *
 * algorithms
 * Hard (47.98%)
 * Total Accepted:    1.3K
 * Total Submissions: 2.5K
 * Testcase Example:  '[[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]'
 *
 * There is a strange printer with the following two special
 * requirements:
 *
 *
 * On each turn, the printer will print a solid rectangular pattern of a single
 * color on the grid. This will cover up the existing colors in the
 * rectangle.
 * Once the printer has used a color for the above operation, the same color
 * cannot be used again.
 *
 *
 * You are given a m x n matrix targetGrid, where targetGrid[row][col] is the
 * color in the position (row, col) of the grid.
 *
 * Return true if it is possible to print the matrix targetGrid, otherwise,
 * return false.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
 * Output: true
 *
 *
 * Example 2:
 *
 *
 *
 *
 * Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
 * Output: true
 *
 *
 * Example 3:
 *
 *
 * Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
 * Output: false
 * Explanation: It is impossible to form targetGrid because it is not allowed
 * to print the same color in different turns.
 *
 * Example 4:
 *
 *
 * Input: targetGrid = [[1,1,1],[3,1,3]]
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * m == targetGrid.length
 * n == targetGrid[i].length
 * 1 <= m, n <= 60
 * 1 <= targetGrid[row][col] <= 60
 *
 *
 */
class Solution {
public:
  int memo[61]; // -1 for invalid sub-rectangles, 0 for uncertain, 1 for valid
                // sub-rectangles
  int m, n;
  bool dfs(int color, vector<vector<int>> &targetGrid) {
    if (memo[color] == -1)
      return false;
    if (memo[color] == 1)
      return true;
    int &res = memo[color];
    res = -1; //

    int l = INT_MAX, r = INT_MIN, u = INT_MAX, d = INT_MIN;
    for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
        if (targetGrid[i][j] == color)
          l = min(l, i), r = max(r, i), u = min(u, j), d = max(d, j);

    if (l == INT_MAX)
      return true;

    for (int i = l; i <= r; i++)
      for (int j = u; j <= d; j++)
        if (targetGrid[i][j] != color && !dfs(targetGrid[i][j], targetGrid))
          return false;

    res = 1;
    return true;
  }

  bool isPrintable(vector<vector<int>> &targetGrid) {
    memset(memo, 0, sizeof(memo));
    m = targetGrid.size(), n = targetGrid[0].size();
    for (int i = 1; i <= 60; i++)
      if (!dfs(i, targetGrid))
        return false;
    return true;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
