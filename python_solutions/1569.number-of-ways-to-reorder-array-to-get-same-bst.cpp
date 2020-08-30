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
 * @lc app=leetcode id=1569 lang=cpp
 *
 * [1569] Number of Ways to Reorder Array to Get Same BST
 *
 * https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/
 *
 * algorithms
 * Hard (40.03%)
 * Total Accepted:    1.3K
 * Total Submissions: 3.1K
 * Testcase Example:  '[2,1,3]'
 *
 * Given an array nums that represents a permutation of integers from 1 to n.
 * We are going to construct a binary search tree (BST) by inserting the
 * elements of nums in order into an initially empty BST. Find the number of
 * different ways to reorder nums so that the constructed BST is identical to
 * that formed from the original array nums.
 *
 * For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left
 * child, and 3 as a right child. The array [2,3,1] also yields the same BST
 * but [3,2,1] yields a different BST.
 *
 * Return the number of ways to reorder nums such that the BST formed is
 * identical to the original BST formed from nums.
 *
 * Since the answer may be very large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: nums = [2,1,3]
 * Output: 1
 * Explanation: We can reorder nums to be [2,3,1] which will yield the same
 * BST. There are no other ways to reorder nums which will yield the same
 * BST.
 *
 *
 * Example 2:
 *
 *
 *
 *
 * Input: nums = [3,4,5,1,2]
 * Output: 5
 * Explanation: The following 5 arrays will yield the same BST:
 * [3,1,2,4,5]
 * [3,1,4,2,5]
 * [3,1,4,5,2]
 * [3,4,1,2,5]
 * [3,4,1,5,2]
 *
 *
 * Example 3:
 *
 *
 *
 *
 * Input: nums = [1,2,3]
 * Output: 0
 * Explanation: There are no other orderings of nums that will yield the same
 * BST.
 *
 *
 * Example 4:
 *
 *
 *
 *
 * Input: nums = [3,1,2,5,4,6]
 * Output: 19
 *
 *
 * Example 5:
 *
 *
 * Input: nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
 * Output: 216212978
 * Explanation: The number of ways to reorder nums to get the same BST is
 * 3216212999. Taking this number modulo 10^9 + 7 gives 216212978.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= nums.length
 * All integers in nums are distinct.
 *
 *
 */
class Solution {
public:
  int rec(vector<int> &ns) {
    int sz = ns.size();
    if (sz <= 2)
      return 1;

    vi left, right;
    for (auto n : ns)
      if (n > ns[0])
        right.pb(n);
      else if (n < ns[0])
        left.pb(n);

    int64_t res = comb(sz - 1, left.size()) % MOD;
    res = res * rec(left) % MOD;
    res = res * rec(right) % MOD;
    return res % MOD;
  }

  int numOfWays(vector<int> &nums) { return rec(nums) - 1; }

  int64_t comb(int n, int k) {
    // Similiar to Python math.comb(n, k) but modulate a number mod
    // to avoid stack overflow
    const int mod = 1e9 + 7;
    if (k * 2 > n)
      return comb(n, n - k);
    int dp[k + 1], pre[k + 1];
    memset(dp, 0, sizeof(dp)), memset(pre, 0, sizeof(pre));
    pre[0] = dp[0] = 1;
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= min(i, k); j++)
        dp[j] = (pre[j - 1] + pre[j]) % mod;

      for (int j = 0; j <= k; j++)
        pre[j] = dp[j];
    }
    return dp[k];
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
