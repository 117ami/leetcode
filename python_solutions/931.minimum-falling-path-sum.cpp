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
 * @lc app=leetcode id=931 lang=cpp
 *
 * [931] Minimum Falling Path Sum
 *
 * https://leetcode.com/problems/minimum-falling-path-sum/description/
 *
 * algorithms
 * Medium (62.60%)
 * Total Accepted:    53.7K
 * Total Submissions: 85.8K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given a square array of integers A, we want the minimum sum of a falling
 * path through A.
 * 
 * A falling path starts at any element in the first row, and chooses one
 * element from each row.  The next row's choice must be in a column that is
 * different from the previous row's column by at most one.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [[1,2,3],[4,5,6],[7,8,9]]
 * Output: 12
 * Explanation: 
 * The possible falling paths are:
 * 
 * 
 * 
 * [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
 * [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
 * [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
 * 
 * 
 * The falling path with the smallest sum is [1,4,7], so the answer is 12.
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= A.length == A[0].length <= 100
 * -100 <= A[i][j] <= 100
 * 
 * 
 */
class Solution {
public:
    int dp[101][101];
    int M = 10001; 
    int dfs(int i, int j, vector<vector<int>> &ns) {
      int sz = ns.size(); 
      if (i >= sz || j >= sz || j < 0) return M; 
      if (i == sz - 1) return ns[i][j];
      if (dp[i][j] < M) return dp[i][j];
      int res = ns[i][j] + min(dfs(i + 1, j - 1, ns), min(dfs(i + 1, j, ns), dfs(i + 1, j + 1, ns))); 
      dp[i][j] = res; 
      return res; 
    }

    int minFallingPathSum(vector<vector<int>>& ns) {
      memset(dp, M, sizeof(dp));
      int res = dfs(0, 0, ns);
      for (int j = 1; j < ns.size(); j++) res = min(res, dfs(0, j, ns));
      // say(dp);
      return res;
    }


    // // int dp[101][101];
    // int M = 10001; 
    // int dfs(int i, int j, vector<vector<int>> &ns, vector<vector<int>> &dp) {
    //   int sz = ns.size(); 
    //   if (i >= sz || j >= sz || j < 0) return M; 
    //   if (i == sz - 1) return ns[i][j];
    //   if (dp[i][j] < M) return dp[i][j];
    //   int res = ns[i][j] + min(dfs(i + 1, j - 1, ns, dp), min(dfs(i + 1, j, ns, dp), dfs(i + 1, j + 1, ns, dp))); 
    //   dp[i][j] = res; 
    //   return res; 
    // }

    // int minFallingPathSum(vector<vector<int>>& ns) {
    //   // memset(dp, 10001, sizeof(dp));
    //   vector<vector<int>> dp(101, vector<int>(101, M));
    //   int res = dfs(0, 0, ns, dp);
    //   for (int j = 1; j < ns.size(); j++) res = min(res, dfs(0, j, ns, dp));
    //   // say(dp);
    //   return res;
    // }
};



auto speed_up = [] () {
    ios_base::sync_with_stdio(false);

    return 0;
}(); 
