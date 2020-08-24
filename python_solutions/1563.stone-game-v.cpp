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
 * @lc app=leetcode id=1563 lang=cpp
 *
 * [1563] Stone Game V
 *
 * https://leetcode.com/problems/stone-game-v/description/
 *
 * algorithms
 * Hard (27.84%)
 * Total Accepted:    3.5K
 * Total Submissions: 8.8K
 * Testcase Example:  '[6,2,3,4,5,5]'
 *
 * There are several stones arranged in a row, and each stone has an associated
 * value which is an integer given in the array stoneValue.
 *
 * In each round of the game, Alice divides the row into two non-empty rows
 * (i.e. left row and right row), then Bob calculates the value of each row
 * which is the sum of the values of all the stones in this row. Bob throws
 * away the row which has the maximum value, and Alice's score increases by the
 * value of the remaining row. If the value of the two rows are equal, Bob lets
 * Alice decide which row will be thrown away. The next round starts with the
 * remaining row.
 *
 * The game ends when there is only one stone remaining. Alice's is initially
 * zero.
 *
 * Return the maximum score that Alice can obtain.
 *
 *
 * Example 1:
 *
 *
 * Input: stoneValue = [6,2,3,4,5,5]
 * Output: 18
 * Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5].
 * The left row has the value 11 and the right row has value 14. Bob throws
 * away the right row and Alice's score is now 11.
 * In the second round Alice divides the row to [6], [2,3]. This time Bob
 * throws away the left row and Alice's score becomes 16 (11 + 5).
 * The last round Alice has only one choice to divide the row which is [2],
 * [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The
 * game ends because only one stone is remaining in the row.
 *
 *
 * Example 2:
 *
 *
 * Input: stoneValue = [7,7,7,7,7,7,7]
 * Output: 28
 *
 *
 * Example 3:
 *
 *
 * Input: stoneValue = [4]
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= stoneValue.length <= 500
 * 1 <= stoneValue[i] <= 10^6
 *
 *
 */
class Solution {
public:
  vector<int> v;
  int dp[501][501];
  int sum[501];
  int solve(int l, int r) {
    if (l == r)
      return 0;
    int &ret = dp[l][r];
    if (~ret)
      return ret;
    for (int j = l; j < r; j++) {
      int x = sum[j] - sum[l] + v[l];
      int y = sum[r] - sum[j];
      if (x <= y)
        ret = max(ret, solve(l, j) + x);
      if (y <= x)
        ret = max(ret, solve(j + 1, r) + y);
    }
    return ret;
  }
  int stoneGameV(vector<int> &stoneValue) {
    v = stoneValue;
    sum[0] = v[0];
    for (int i = 1; i < v.size(); i++) {
      sum[i] = sum[i - 1] + v[i];
    }
    memset(dp, -1, sizeof dp);
    return solve(0, v.size() - 1);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
