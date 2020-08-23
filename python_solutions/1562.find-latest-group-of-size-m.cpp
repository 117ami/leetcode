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

int direction[8][2] = {{-1, 0},  {1, 0},  {0, -1}, {0, 1},
                       {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

vector<int> dirs = {-1, 0, 1, 0, -1};
// ==================================================

/*
 * @lc app=leetcode id=1562 lang=cpp
 *
 * [1562] Find Latest Group of Size M
 *
 * https://leetcode.com/problems/find-latest-group-of-size-m/description/
 *
 * algorithms
 * Medium (21.84%)
 * Total Accepted:    1.4K
 * Total Submissions: 6.5K
 * Testcase Example:  '[3,5,1,2,4]\n1'
 *
 * Given an array arr that represents a permutation of numbers from 1 to n. You
 * have a binary string of size n that initially has all its bits set to zero.
 *
 * At each step i (assuming both the binary string and arr are 1-indexed) from
 * 1 to n, the bit at position arr[i] is set to 1. You are given an integer m
 * and you need to find the latest step at which there exists a group of ones
 * of length m. A group of ones is a contiguous substring of 1s such that it
 * cannot be extended in either direction.
 *
 * Return the latest step at which there exists a group of ones of length
 * exactly m. If no such group exists, return -1.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [3,5,1,2,4], m = 1
 * Output: 4
 * Explanation:
 * Step 1: "00100", groups: ["1"]
 * Step 2: "00101", groups: ["1", "1"]
 * Step 3: "10101", groups: ["1", "1", "1"]
 * Step 4: "11101", groups: ["111", "1"]
 * Step 5: "11111", groups: ["11111"]
 * The latest step at which there exists a group of size 1 is step 4.
 *
 * Example 2:
 *
 *
 * Input: arr = [3,1,5,4,2], m = 2
 * Output: -1
 * Explanation:
 * Step 1: "00100", groups: ["1"]
 * Step 2: "10100", groups: ["1", "1"]
 * Step 3: "10101", groups: ["1", "1", "1"]
 * Step 4: "10111", groups: ["1", "111"]
 * Step 5: "11111", groups: ["11111"]
 * No group of size 2 exists during any step.
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [1], m = 1
 * Output: 1
 *
 *
 * Example 4:
 *
 *
 * Input: arr = [2,1], m = 2
 * Output: 2
 *
 *
 *
 * Constraints:
 *
 *
 * n == arr.length
 * 1 <= n <= 10^5
 * 1 <= arr[i] <= n
 * All integers in arr are distinct.
 * 1 <= m <= arr.length
 *
 *
 */

class UF {
  // sz is the size of a group
  int *id, cnt, *sz;

public:
  // Create an empty union find data structure with N isolated sets.
  UF(int N) {
    cnt = N;
    id = new int[N];
    sz = new int[N];
    for (int i = 0; i < N; i++)
      id[i] = i, sz[i] = 1;
  }

  ~UF() {
    delete[] id;
    delete[] sz;
  }

  // Return the id of component corresponding to object p.
  int find(int p) {
    if (p != id[p])
      id[p] = find(id[p]);
    return id[p];
  }

  void merge(int x, int y, bool greater) {
    int i = find(x), j = find(y);
    id[x] = id[y] = greater ? std::max(i, j) : std::min(i, j);
  }

  // Are objects x and y in the same set?
  bool connected(int x, int y) { return find(x) == find(y); }

  // Return the number of disjoint sets.
  int count() { return cnt; }
};

class Solution {
public:
  int findLatestStep(vector<int> &arr, int m) {
    int n = qsize(arr);
    UF left(n + 1), right(n + 1);
    bool p[n + 1];
    memset(p, false, sizeof(p));
    int cache[n + 1];
    memset(cache, 0, sizeof(cache));
    int res = -1;

    forloop(i, n) {
      int a = arr[i];
      p[a] = true;

      if (p[a - 1]) {
        left.merge(a, a - 1, false);
        right.merge(a - 1, a, true);
      }

      if (a <= n - 1 && p[a + 1]) {
        right.merge(a + 1, a, true);
        left.merge(a, a + 1, false);
      }

      int la = left.find(a), ra = right.find(a);
      cache[a - la]--, cache[ra - a]--;
      cache[ra - la + 1]++;
      if (cache[m] > 0)
        res = i + 1;
    }
    return res;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
