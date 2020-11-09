// Containers
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "conf.d/say.h"

#define vi vector<int>
#define vb vector<bool>
#define vc vector<char>
#define vs vector<string>
#define vvi vector<vi>
#define vvb vector<vb>
#define mii map<int, int>
#define mci map<char, int>
#define si set<int>
#define spii set<pair<int, int>>
#define umii unordered_map<int, int>
#define umci unordered_map<char, int>
#define umsi unordered_map<string, int>
#define usi unordered_set<int>
#define vpii vector<pair<int, int>>
#define ll long long
#define pb push_back
#define mp make_pair
#define INF 0x3F3F3F3F
#define all(v) v.begin(), v.end()
#define f first
#define s second
#define mod 1000000007
#define MOD 998244353
#define fori(i, n) for (int i = 0; i < n; i++)            //[0, n)
#define forir(i, n) for (int i = n - 1; i >= 0; --i)      // reverse [0, n)
#define forup(i, a, b) for (int i = a; i < b; ++i)        // [a, b)
#define fordown(i, a, b) for (int i = b - 1; i >= a; --i) // reverse [a, b)

#define namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

// fast IO
static auto __2333__ = []() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  return 0;
}();
// --------------------------------------------------------
class Solution {
public:
  int me;
  int query(int x, vi &bit) {
    int ans = 0;
    while (x > 0) {
      ans += bit[x];
      x -= (x & -x);
    }
    return ans;
  }

  void update(int x, vi &bit) {
    while (x <= me) {
      bit[x]++;
      x += (x & -x);
    }
  }
  int createSortedArray(vector<int> &ns) {
    me = *max_element(all(ns));
    vi bit(me + 1, 0);
    int cost = 0;
    for (int i = 0; i < ns.size(); i++) {
      int n = ns[i];
      int l = query(n - 1, bit), r = i - query(n, bit);
      cost += min(l, r);
      cost %= mod;
      update(n, bit);
    }
    return cost;
  }
};

int main() {
  Solution s;
  vi ns = {1, 3, 3, 3, 2, 4, 2, 1, 2};
  say(s.createSortedArray(ns));
}