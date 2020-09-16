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
#include <array>
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
 * @lc app=leetcode id=1584 lang=cpp
 *
 * [1584] Min Cost to Connect All Points
 *
 * https://leetcode.com/problems/min-cost-to-connect-all-points/description/
 *
 * algorithms
 * Medium (31.62%)
 * Total Accepted:    1.7K
 * Total Submissions: 5.4K
 * Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
 *
 * You are given an array points representing integer coordinates of some
 * points on a 2D-plane, where points[i] = [xi, yi].
 *
 * The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
 * distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
 * absolute value of val.
 *
 * Return the minimum cost to make all points connected. All points are
 * connected if there is exactly one simple path between any two points.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
 * Output: 20
 * Explanation:
 *
 * We can connect the points as shown above to get the minimum cost of 20.
 * Notice that there is a unique path between every pair of points.
 *
 *
 * Example 2:
 *
 *
 * Input: points = [[3,12],[-2,5],[-4,1]]
 * Output: 18
 *
 *
 * Example 3:
 *
 *
 * Input: points = [[0,0],[1,1],[1,0],[-1,1]]
 * Output: 4
 *
 *
 * Example 4:
 *
 *
 * Input: points = [[-1000000,-1000000],[1000000,1000000]]
 * Output: 4000000
 *
 *
 * Example 5:
 *
 *
 * Input: points = [[0,0]]
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= points.length <= 1000
 * -10^6 <= xi, yi <= 10^6
 * All pairs (xi, yi) are distinct.
 *
 *
 */
class Solution {
public:
  int minCostConnectPoints(vector<vector<int>> &ps) {
    int n = ps.size();
    if (n < 2)
      return 0;
    int keys[1001];
    bool visited[1001];
    memset(keys, INF, sizeof(keys)), memset(visited, false, sizeof(visited));
    keys[0] = 0;

    // std::vector<int> keys(n, INF);
    // std::vector<bool> visited(n, false);
    // std::priority_queue<pii, vector<pii>, greater<pii>> pq;
    // pq.push({0, 0});
    
    int cost = 0;
    for (int i = 0; i < n; i++) {
      int idx = 0, n_min = INF;
      for (int j = 0; j < n; j++) {
        if (false == visited[j] && keys[j] < n_min)
          idx = j, n_min = keys[j];
      }
    
      visited[idx] = true, cost += n_min;
      for (int j = 0; j < n; j++) {
        if (visited[j])
          continue;
        int len = abs(ps[j][0] - ps[idx][0]) + abs(ps[j][1] - ps[idx][1]);
        if (len < keys[j])
          keys[j] = len;
      }
    }
    
    return cost;

    // while (!pq.empty()) {
    //   int w = pq.top().first, u = pq.top().second;
    //   // say(vi{u, w});
    //   pq.pop();
    //   visited[u] = true;
    //   for (int i = 0; i < n; i++) {
    //     if (i == u || visited[i])
    //       continue;
    //     int weight = abs(ps[i][0] - ps[u][0]) + abs(ps[i][1] - ps[u][1]);

    //     if (keys[i] > weight) {
    //       keys[i] = weight;
    //       pq.push({weight, i});
    //     }
    //   }
    // }
    // say(keys);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
