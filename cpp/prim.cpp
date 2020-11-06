#include <iostream>
#include <list>
#include <queue>
#include <vector>
using namespace std;
#define INF 0x3f3f3f3f


// This class represents a directed graph using
// adjacency list representation
class Prim {
  std::vector<std::vector<pair<int, int>>> adj;
  // Labels to encode node into 0, 1, 2, ...
  std::unordered_map<int, int> labels;

public:
  int cnt;
  Prim() { cnt = 0; }
  Prim(int N) {cnt=0, adj.reserve(N); }

  int get_label(int u) {
    if (labels.count(u) > 0) return labels[u];
    labels[u] = cnt;
    cnt++;
    return labels[u];
  }

  void add_edge(int u, int v, int w) {
    int lu = get_label(u), lv = get_label(v);
    while (adj.size() <= max(lu, lv) + 1) adj.push_back({});
    adj[lu].push_back(make_pair(lv, w));
    adj[lv].push_back(make_pair(lu, w));
  }

  int cost_of_mst() {
    // Create a priority queue to store std::vector<int>sited vertices.
    priority_queue<std::pair<int, int>, vector<std::pair<int, int>>, greater<std::pair<int, int>>> pq;

    int cost = 0, src = 0; // Taking vertex 0 as source

    // Vector `parent` is used to  print out Tree edges from source 0
    // Vector `key` for storing weights to calculate cost
    vector<int> key(cnt, INT_MAX), parent(cnt, -1);
    vector<bool> visited(cnt, false);

    pq.push(make_pair(0, src));
    key[src] = 0;

    int res = 0;
    /* Looping till priority queue becomes empty */
    while (!pq.empty()) {
      int w = pq.top().first, u = pq.top().second;
      pq.pop();
      if (visited[u]) continue;
      visited[u] = true;
      res += w;

      // 'i' is used to get all adjacent vertices of a vertex
      for (auto &[v, weight] : adj[u]) {
        // Get vertex label and weight of current adjacent of u.
        // If v is not in MST and weight of (u, v) is smaller
        // than current key of v
        if (visited[v] == false && key[v] > weight) {
          // Updating key of v
          key[v] = weight;
          pq.push(make_pair(key[v], v));
          parent[v] = u;
        }
      }
    }

    // If key of some node is still int_max, then this is not a SCC.
    for (int i = 0; i < cnt; ++i)
      if (key[i] == INT_MAX) return -1;
    // cost += key[i], printf("%d - %d\n", key[i], i);
    return res;
  }
};


int main() {
  Graph g(4);
  g.add_edge(0, 1, 2);
  g.add_edge(1, 2, 4);
  g.add_edge(2, 3, 7);
  g.add_edge(0, 3, 3);
  g.add_edge(1, 3, 1);
  int cost = g.cost_of_mst();
  std::cout << cost << endl;

  list<int> *arr = new list<int>(8); 
  arr[0].push_back(1);
  arr[7].push_back(12);
  for(int i=0 ;i < 7; i++) {
    for(auto c: arr[i]) std::cout<< c << std::endl;
  }
}