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
 * @lc app=leetcode id=952 lang=cpp
 *
 * [952] Largest Component Size by Common Factor
 *
 * https://leetcode.com/problems/largest-component-size-by-common-factor/description/
 *
 * algorithms
 * Hard (30.37%)
 * Total Accepted:    18.1K
 * Total Submissions: 53.6K
 * Testcase Example:  '[4,6,15,35]'
 *
 * Given a non-empty array of unique positive integers A, consider the
 * following graph:
 *
 *
 * There are A.length nodes, labelled A[0] to A[A.length - 1];
 * There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a
 * common factor greater than 1.
 *
 *
 * Return the size of the largest connected component in the graph.
 *
 *
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: [4,6,15,35]
 * Output: 4
 *
 *
 *
 *
 * Example 2:
 *
 *
 * Input: [20,50,9,63]
 * Output: 2
 *
 *
 *
 *
 * Example 3:
 *
 *
 * Input: [2,3,6,7,4,12,21,39]
 * Output: 8
 *
 *
 *
 * Note:
 *
 *
 * 1 <= A.length <= 20000
 * 1 <= A[i] <= 100000
 *
 *
 *
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

  // Merge to smaller root if greater == false else to larger root
  void merge_by_value(int x, int y, bool greater) {
    int i = find(x), j = find(y);
    id[x] = id[y] = greater ? std::max(i, j) : std::min(i, j);
  }

  // Replace sets containing x and y with their union.
  void merge(int x, int y) {
    int i = find(x), j = find(y);
    if (i == j)
      return;

    // make smaller root point to larger one
    if (sz[i] < sz[j]) {
      id[i] = j, sz[j] += sz[i];
    } else {
      id[j] = i, sz[i] += sz[j];
    }

    cnt--;
  }

  // Are objects x and y in the same set?
  bool connected(int x, int y) { return find(x) == find(y); }

  // Return the number of disjoint sets.
  int count() { return cnt; }
};

class Solution {
private:
public:
  int largestComponentSize(vector<int> &A) {
    int bound = 0;
    for (int x : A)
      bound = max(bound, x);
    // qsort(A);
    UF uf(bound + 1);
    for (int n : A) {
      if (n % 2 == 0)
        uf.merge(n, 2), uf.merge(n, max(n / 2, 2)); // Get rid of merge (n, 1)
      for (int i = 3; i <= std::sqrt(n); i++) {
        if (n % i == 0)
          uf.merge(n, i), uf.merge(n, n / i);
      }
    }
    int res = 1;
    unordered_map<int, int> cc;
    for (auto n : A) {
      int p = uf.find(n);
      say(vi{n, p});
      cc[p]++;
      res = max(res, cc[p]);
    }
    return res;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
