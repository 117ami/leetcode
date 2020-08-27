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
 * @lc app=leetcode id=436 lang=cpp
 *
 * [436] Find Right Interval
 *
 * https://leetcode.com/problems/find-right-interval/description/
 *
 * algorithms
 * Medium (45.52%)
 * Total Accepted:    39.2K
 * Total Submissions: 85.3K
 * Testcase Example:  '[[1,2]]'
 *
 * Given a set of intervals, for each of the interval i, check if there exists
 * an interval j whose start point is bigger than or equal to the end point of
 * the interval i, which can be called that j is on the "right" of i.
 *
 * For any interval i, you need to store the minimum interval j's index, which
 * means that the interval j has the minimum start point to build the "right"
 * relationship for interval i. If the interval j doesn't exist, store -1 for
 * the interval i. Finally, you need output the stored value of each interval
 * as an array.
 *
 * Note:
 *
 *
 * You may assume the interval's end point is always bigger than its start
 * point.
 * You may assume none of these intervals have the same start point.
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [ [1,2] ]
 *
 * Output: [-1]
 *
 * Explanation: There is only one interval in the collection, so it outputs
 * -1.
 *
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [ [3,4], [2,3], [1,2] ]
 *
 * Output: [-1, 0, 1]
 *
 * Explanation: There is no satisfied "right" interval for [3,4].
 * For [2,3], the interval [3,4] has minimum-"right" start point;
 * For [1,2], the interval [2,3] has minimum-"right" start point.
 *
 *
 *
 *
 * Example 3:
 *
 *
 * Input: [ [1,4], [2,3], [3,4] ]
 *
 * Output: [-1, 2, -1]
 *
 * Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
 * For [2,3], the interval [3,4] has minimum-"right" start point.
 *
 *
 * NOTE: input types have been changed on April 15, 2019. Please reset to
 * default code definition to get new method signature.
 *
 */
class Solution {
public:
  vector<int> findRightInterval(vector<vector<int>> &it) {
    vector<pair<int, int>> helper;
    int n = it.size();
    forloop(i, n) helper.push_back(mp(it[i][0], i));
    sort(helper.begin(), helper.end(), [](const pii &a, const pii &b) {
      return a.first < b.first || (a.first == b.first && a.second < b.second);
    });

    // for (auto &p : helper)
    //   say(p);

    vi res;
    for (auto &c : it) {
      int end = c[1];
      auto pos = lower_bound(helper.begin(), helper.end(), mp(end, 0));
      if (pos == helper.end()) {
        if (helper.back().first >= end)
          res.pb(n - 1);
        else
          res.pb(-1);
      } else {
        int idx = pos - helper.begin();
        if (helper[idx].first >= end)
          res.pb(helper[idx].second);
        else
          res.pb(-1);
      }
    }
    return res;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
