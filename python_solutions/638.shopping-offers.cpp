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
 * @lc app=leetcode id=638 lang=cpp
 *
 * [638] Shopping Offers
 *
 * https://leetcode.com/problems/shopping-offers/description/
 *
 * algorithms
 * Medium (51.65%)
 * Total Accepted:    31.5K
 * Total Submissions: 60.9K
 * Testcase Example:  '[2,5]\n[[3,0,5],[1,2,10]]\n[3,2]'
 *
 *
 * In LeetCode Store, there are some kinds of items to sell. Each item has a
 * price.
 *
 *
 *
 * However, there are some special offers, and a special offer consists of one
 * or more different kinds of items with a sale price.
 *
 *
 *
 * You are given the each item's price, a set of special offers, and the number
 * we need to buy for each item.
 * The job is to output the lowest price you have to pay for exactly certain
 * items as given, where you could make optimal use of the special offers.
 *
 *
 *
 * Each special offer is represented in the form of an array, the last number
 * represents the price you need to pay for this special offer, other numbers
 * represents how many specific items you could get if you buy this offer.
 *
 *
 * You could use any of special offers as many times as you want.
 *
 * Example 1:
 *
 * Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
 * Output: 14
 * Explanation:
 * There are two kinds of items, A and B. Their prices are $2 and $5
 * respectively.
 * In special offer 1, you can pay $5 for 3A and 0B
 * In special offer 2, you can pay $10 for 1A and 2B.
 * You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer
 * #2), and $4 for 2A.
 *
 *
 *
 * Example 2:
 *
 * Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
 * Output: 11
 * Explanation:
 * The price of A is $2, and $3 for B, $4 for C.
 * You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
 * You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special
 * offer #1), and $3 for 1B, $4 for 1C.
 * You cannot add more items, though only $9 for 2A ,2B and 1C.
 *
 *
 *
 * Note:
 *
 * There are at most 6 kinds of items, 100 special offers.
 * For each item, you need to buy at most 6 of them.
 * You are not allowed to buy more items than you want, even if that would
 * lower the overall price.
 *
 *
 */
#include <vector>

const int M = 0x3f3f3f3f;
class Solution {
public:
  // std::vector<int> memo = std::vector<int>(46658, -1);
  std::unordered_map<int, int> memo;

  int get_key(vector<int> &needs) {
    int ans = 0;
    for (int i = 0; i < needs.size(); i++) {
      // Be careful some item is already less than 0 in needs
      if (needs[i] < 0)
        return -1;
      ans = ans * 6 + needs[i];
    }

    return ans;
  }

  int dp(vector<int> &price, vector<vector<int>> &special, vector<int> &needs) {
    int key = get_key(needs);
    if (key <= 0)
      return key == 0 ? 0 : M;

    if (memo.count(key) > 0)
      return memo[key];

    int ans = 0;
    for (int i = 0; i < price.size(); i++)
      ans += price[i] * needs[i];

    for (auto &s : special) {
      int cur = s.back();
      for (int i = 0; i < needs.size(); i++)
        needs[i] -= s[i];

      ans = min(ans, cur + dp(price, special, needs));
      for (int i = 0; i < needs.size(); i++)
        needs[i] += s[i];
    }

    memo[key] = ans;
    return ans;
  }

  int shoppingOffers(vector<int> &price, vector<vector<int>> &special,
                     vector<int> &needs) {
    return dp(price, special, needs);
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
