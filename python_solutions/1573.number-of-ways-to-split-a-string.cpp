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
 * @lc app=leetcode id=1573 lang=cpp
 *
 * [1573] Number of Ways to Split a String
 *
 * https://leetcode.com/problems/number-of-ways-to-split-a-string/description/
 *
 * algorithms
 * Medium (27.87%)
 * Total Accepted:    3.9K
 * Total Submissions: 14K
 * Testcase Example:  '"10101"'
 *
 * Given a binary string s (a string consisting only of '0's and '1's), we can
 * split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).
 *
 * Return the number of ways s can be split such that the number of characters
 * '1' is the same in s1, s2, and s3.
 *
 * Since the answer may be too large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "10101"
 * Output: 4
 * Explanation: There are four ways to split s in 3 parts where each part
 * contain the same number of letters '1'.
 * "1|010|1"
 * "1|01|01"
 * "10|10|1"
 * "10|1|01"
 *
 *
 * Example 2:
 *
 *
 * Input: s = "1001"
 * Output: 0
 *
 *
 * Example 3:
 *
 *
 * Input: s = "0000"
 * Output: 3
 * Explanation: There are three ways to split s in 3 parts.
 * "0|0|00"
 * "0|00|0"
 * "00|0|0"
 *
 *
 * Example 4:
 *
 *
 * Input: s = "100100010100110"
 * Output: 12
 *
 *
 *
 * Constraints:
 *
 *
 * s[i] == '0' or s[i] == '1'
 * 3 <= s.length <= 10^5
 *
 *
 */
const int M = 1e9 + 7;
class Solution {
public:
  int numWays(string s) {
    long cnt = 0, n = s.size();
    for (char &c : s) cnt += c == '1' ? 1 : 0;
    if (cnt % 3 > 0) return 0;

    if (cnt == 0)
      return (n - 1) * (n - 2) / 2 % M;

    long a = 0, b = 0, i = 0, k = 0;
    while (k < cnt / 3) if (s[i++] == '1') k++; 
    while (s[i] != '1') a++, i++;

    while (k < cnt * 2 / 3) if (s[i ++] == '1') k++;
    while (s[i] != '1') b++, i++;
    
    return (a + 1) * (b + 1) % M;

  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
