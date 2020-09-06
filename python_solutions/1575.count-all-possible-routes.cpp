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
 * @lc app=leetcode id=1575 lang=cpp
 *
 * [1575] Count All Possible Routes
 *
 * https://leetcode.com/problems/count-all-possible-routes/description/
 *
 * algorithms
 * Hard (59.30%)
 * Total Accepted:    1.7K
 * Total Submissions: 2.8K
 * Testcase Example:  '[2,3,6,8,4]\n1\n3\n5'
 *
 * You are given an array of distinct positive integers locations where
 * locations[i] represents the position of city i. You are also given integers
 * start, finish and fuel representing the starting city, ending city, and the
 * initial amount of fuel you have, respectively.
 *
 * At each step, if you are at city i, you can pick any city j such that j != i
 * and 0 <= j < locations.length and move to city j. Moving from city i to city
 * j reduces the amount of fuel you have by |locations[i] - locations[j]|.
 * Please notice that |x| denotes the absolute value of x.
 *
 * Notice that fuel cannot become negative at any point in time, and that you
 * are allowed to visit any city more than once (including start and finish).
 *
 * Return the count of all possible routes from start to finish.
 *
 * Since the answer may be too large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
 * Output: 4
 * Explanation: The following are all possible routes, each uses 5 units of
 * fuel:
 * 1 -> 3
 * 1 -> 2 -> 3
 * 1 -> 4 -> 3
 * 1 -> 4 -> 2 -> 3
 *
 *
 * Example 2:
 *
 *
 * Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
 * Output: 5
 * Explanation: The following are all possible routes:
 * 1 -> 0, used fuel = 1
 * 1 -> 2 -> 0, used fuel = 5
 * 1 -> 2 -> 1 -> 0, used fuel = 5
 * 1 -> 0 -> 1 -> 0, used fuel = 3
 * 1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5
 *
 *
 * Example 3:
 *
 *
 * Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
 * Output: 0
 * Explanation: It's impossible to get from 0 to 2 using only 3 units of fuel
 * since the shortest route needs 4 units of fuel.
 *
 * Example 4:
 *
 *
 * Input: locations = [2,1,5], start = 0, finish = 0, fuel = 3
 * Output: 2
 * Explanation: There are two possible routes, 0 and 0 -> 1 -> 0.
 *
 * Example 5:
 *
 *
 * Input: locations = [1,2,3], start = 0, finish = 2, fuel = 40
 * Output: 615088286
 * Explanation: The total number of possible routes is 2615088300. Taking this
 * number modulo 10^9 + 7 gives us 615088286.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= locations.length <= 100
 * 1 <= locations[i] <= 10^9
 * All integers in locations are distinct.
 * 0 <= start, finish < locations.length
 * 1 <= fuel <= 200
 *
 *
 */
const int M = 1e9 + 7;

class Solution {
public:
  int dp[101][201];
  long solve(int i, int j, int f, vector<int> &locs) {
    if (f < 0) return 0;
    if (f == 0) return i == j ? 1 : 0;
    
    if (dp[i][f] >= 0)
      return dp[i][f];


    // Essential, if fuel > 0 but i = j already, then this should counts as 
    // 1 possible route
    long res = 0;
    if (i == j) res++;

    for (int k = 0; k < locs.size(); k++) {
      int abs_diff = abs(locs[i] - locs[k]);
      if (k != i && f >= abs_diff) {
        res += solve(k, j, f - abs_diff, locs) % M;
      }
    }
    res %= M;
    dp[i][f] = res;
    return res;
  }

  int countRoutes(vector<int> &locations, int start, int finish, int fuel) {
    int n = locations.size();
    std::memset(dp, -1, sizeof(dp));
    // std::vector<std::vector<int>>dp (n, std::vector<int>(n, -1));
    return solve(start, finish, fuel, locations);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
