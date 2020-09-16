#include <iostream>
#include <list>
#include <numeric>
#include <queue>
#include <vector>

using namespace std;
#define INF 0x3f3f3f3f

typedef pair<int, int> pii;

class Graph {
  int V; // No. of vertices
  std::priority_queue<pair<int, pii>> pq;

public:
  Graph(int V);
  void add_edge(int u, int v, int w);
  int kruskal_mst();
};

Graph::Graph(int V) { this->V = V; }

void Graph::add_edge(int u, int v, int w) { pq.push({-1 * w, {u, v}}); }

int find(int u, vector<int> &parents) {
  if (u != parents[u])
    parents[u] = find(parents[u], parents);
  return parents[u];
}

void merge(int u, int v, vector<int> &parents) {
  int pu = find(u, parents), pv = find(v, parents);
  parents[pu] = parents[pv] = min(pu, pv);
}

int Graph::kruskal_mst() {
  int cost = 0;
  std::vector<int> parents(V);
  std::iota(parents.begin(), parents.end(), 0);
  std::vector<pair<int, pii>> mst; // To store edges of minimum spanning tree

  while (!pq.empty()) {
    pair<int, pii> top = pq.top();
    pq.pop();
    int weight = top.first, u = top.second.first, v = top.second.second;

    int pu = find(u, parents), pv = find(v, parents);
    if (pu != pv) {
      cost -= weight; // Note that weights are stored as negative numbers to
                      // leverage min heap
      merge(u, v, parents);
      mst.push_back(top);
    }
  }

  return cost;
}

int main() {
  // create the graph given in above fugure
  int V = 6;
  Graph g(V);
  vector<vector<int>> ns = {{0, 1, 0}, {1, 3, 10}, {1, 4, 7},
                            {3, 4, 9}, {2, 4, 32}, {4, 5, 23}};
  for (auto &p : ns)
    g.add_edge(p[0], p[1], p[2]);

  int c = g.kruskal_mst();
  std::cout << c << std::endl;

  return 0;
}