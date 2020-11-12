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
#define MOD 1000000007

#define namespace std;
int dirs[5] = {-1, 0, 1, 0, -1};

// fast IO
static auto __2333__ = []() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  return 0;
}();
// --------------------------------------------------------

class UF {
  // len is the size of a group
  int *id, cnt, *len;

public:
  // Create an empty union find data structure with N isolated sets.
  UF(int N) {
    cnt = N;
    id = new int[N];
    len = new int[N];
    for (int i = 0; i < N; i++) id[i] = i, len[i] = 1;
  }

  ~UF() {
    delete[] id;
    delete[] len;
  }

  // Return the id of component corresponding to object p.
  int find(int p) {
    if (p != id[p]) id[p] = find(id[p]);
    return id[p];
  }

  // Merge to smaller root if greater == false else to larger root.
  // Should use normal merge as possible as you can. This method cause trouble when
  // you try to merge (2, 6), and then (6, 3). The larger number 6 should work as a
  // middleman, however, it's useless if you use this method.
  // void merge_by_value(int x, int y, bool greater) {
  //   int i = find(x), j = find(y);
  //   id[x] = id[y] = greater ? std::max(i, j) : std::min(i, j);
  // }

  // Replace sets containing x and y with their union.
  void merge(int x, int y) {
    int i = find(x), j = find(y);
    if (i == j) return;

    // make smaller root point to larger one
    if (len[i] < len[j])
      id[i] = j, len[j] += len[i];
    else
      id[j] = i, len[i] += len[j];
    cnt--;
  }

  // Are objects x and y in the same set?
  bool connected(int x, int y) { return find(x) == find(y); }

  // Return the number of disjoint sets.
  int count() { return cnt; }
};

class Solution {
public:
  vector<bool> areConnected(int n, int threshold, vector<vector<int>> &queries) {
    int len = queries.size();
    UF uf(n + 1);
    if (threshold > n / 2)
      return vector<bool>(len, false);
    else if (threshold == 0)
      return vector<bool>(len, true);

    for (int i = threshold + 1; i <= n; ++i) {
      int j = i;
      while (j <= n) uf.merge(i, j), j += i;
    }

    vb res;
    for (auto &q : queries) res.push_back(uf.find(q.front()) == uf.find(q.back()));
    return res;
  }
};

int main() { Solution s; }