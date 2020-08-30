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
 * @lc app=leetcode id=1566 lang=cpp
 *
 * [1566] Detect Pattern of Length M Repeated K or More Times
 *
 * https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/description/
 *
 * algorithms
 * Easy (36.78%)
 * Total Accepted:    5K
 * Total Submissions: 13.8K
 * Testcase Example:  '[1,2,4,4,4,4]\n1\n3'
 *
 * Given an array of positive integers arr,  find a pattern of length m that is
 * repeated k or more times.
 *
 * A pattern is a subarray (consecutive sub-sequence) that consists of one or
 * more values, repeated multiple times consecutively without overlapping. A
 * pattern is defined by its length and the number of repetitions.
 *
 * Return true if there exists a pattern of length m that is repeated k or more
 * times, otherwise return false.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [1,2,4,4,4,4], m = 1, k = 3
 * Output: true
 * Explanation: The pattern (4) of length 1 is repeated 4 consecutive times.
 * Notice that pattern can be repeated k or more times but not less.
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
 * Output: true
 * Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times.
 * Another valid pattern (2,1) is also repeated 2 times.
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [1,2,1,2,1,3], m = 2, k = 3
 * Output: false
 * Explanation: The pattern (1,2) is of length 2 but is repeated only 2 times.
 * There is no pattern of length 2 that is repeated 3 or more times.
 *
 *
 * Example 4:
 *
 *
 * Input: arr = [1,2,3,1,2], m = 2, k = 2
 * Output: false
 * Explanation: Notice that the pattern (1,2) exists twice but not
 * consecutively, so it doesn't count.
 *
 *
 * Example 5:
 *
 *
 * Input: arr = [2,2,2,2], m = 2, k = 3
 * Output: false
 * Explanation: The only pattern of length 2 is (2,2) however it's repeated
 * only twice. Notice that we do not count overlapping repetitions.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= arr.length <= 100
 * 1 <= arr[i] <= 100
 * 1 <= m <= 100
 * 2 <= k <= 100
 *
 *
 */
class Solution {
public:
  int64_t quick_pow(int base, int len) {
    // Quick pow method to compute (base ^ len % MOD)
    int64_t res = 1, tmp = base;
    while (len > 0) {
      if ((len & 1) != 0) res = res * tmp % MOD;
      tmp = tmp * tmp % MOD;
      len >>= 1;
    }
    return res;
  }

  bool containsPattern(vector<int> &arr, int m, int k) {
    std::unordered_map<int, vector<int>> cc;
    int p = 233;
    int64_t offset = quick_pow(p, m - 1), hash = 0;
    for (int i = 0; i < arr.size(); i++) {
      if (i >= m) hash += MOD - arr[i - m] * offset % MOD;
      hash = (hash * p + arr[i]) % MOD;
      if (i >= m - 1) {
        // say(vector<int64_t>{i, hash});
        if (cc[hash].empty() || i - cc[hash].back() == m) cc[hash].pb(i);
        else if (i - cc[hash].back() > m) cc[hash] = {i};
        if (cc[hash].size() >= k) return true;
      }
    }

    // for(auto &[k, v]: cc) say(k), say(v);
    return false;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
