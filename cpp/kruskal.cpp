#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <list>
using namespace std;
#define INF 0x3f3f3f3f

class Kruskal {
  priority_queue<pair<int, pair<int, int>>> pq;
  unordered_map<int, int> labels;

public:
  int cnt=0;;
  Kruskal() { }
  Kruskal(int N) {}

  int get_label(int u) {
    if (labels.count(u) > 0) return labels[u];
    return (labels[u] = cnt++);
  }

  void add_edge(int u, int v, int w) {
    int lu = get_label(u), lv = get_label(v);
    pq.push({-1 * w, make_pair(lu, lv)});
  }

  int find(int u, vector<int> &parents) {
    if (u != parents[u]) parents[u] = find(parents[u], parents);
    return parents[u];
  }

  void merge(int u, int v, vector<int> &parents) {
    int pu = find(u, parents), pv = find(v, parents);
    parents[pu] = parents[pv] = min(pu, pv);
  }

  int cost_of_mst() {
    int cost = 0;
    vector<int> parents(cnt, 0);
    std::iota(parents.begin(), parents.end(), 0);
    vector<pair<int, pair<int, int>>> mst;

    while (!pq.empty()) {
      pair<int, pair<int, int>> top = pq.top();
      pq.pop();
      int w = top.first, u = top.second.first, v = top.second.second;

      int pu = find(u, parents), pv = find(v, parents);
      if (pv != pu) {
        cost -= w;
        merge(u, v, parents);
        mst.push_back(top);
      }
    }
    return cost;
  }
};

int main() {
  Kruskal g(4);
  g.add_edge(0, 1, 2);
  g.add_edge(1, 2, 4);
  g.add_edge(2, 3, 7);
  g.add_edge(0, 3, 3);
  g.add_edge(1, 3, 1);
  int cost = g.cost_of_mst();
  std::cout << cost << endl;

  // list<int> *arr = new list<int>(8);
  // arr[0].push_back(1);
  // arr[7].push_back(12);
  // for(int i=0 ;i < 7; i++) {
  //   for(auto c: arr[i]) std::cout<< c << std::endl;
}
