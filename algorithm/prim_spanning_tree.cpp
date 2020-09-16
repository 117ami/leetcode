#include <iostream>
#include <list>
#include <queue>
#include <vector>

// STL implementation of Prim's algorithm for MST
using namespace std;
#define INF 0x3f3f3f3f

// pii ==>  Integer Pair
typedef pair<int, int> pii;

// This class represents a directed graph using
// adjacency list representation
class Graph {
  int V; // No. of vertices

  // In a weighted graph, we need to store vertex
  // and weight pair for every edge
  list<pair<int, int>> *adj;

public:
  Graph(int V); // Constructor

  // function to add an edge to graph
  void add_edge(int u, int v, int w);

  // Return the minimum cost using Prim's algorithm.
  int prim_mst();
};

// Allocates memory for adjacency list
Graph::Graph(int V) {
  this->V = V;
  adj = new list<pii>[V];
}

void Graph::add_edge(int u, int v, int w) {
  adj[u].push_back(make_pair(v, w));
  adj[v].push_back(make_pair(u, w));
}

int Graph::prim_mst() {
  // Create a priority queue to store vertices that
  // are being previsited. This is weird syntax in C++.
  // Refer below link for details of this syntax
  // http://geeksquiz.com/implement-min-heap-using-stl/
  priority_queue<pii, vector<pii>, greater<pii>> pq;

  int cost = 0, src = 0; // Taking vertex 0 as source

  vector<int> key(V, INF), parent(V, -1);
  vector<bool> visited(V, false);

  // Insert source itself in priority queue and initialize
  // its key as 0.
  pq.push(make_pair(0, src));
  key[src] = 0;

  /* Looping till priority queue becomes empty */
  while (!pq.empty()) {
    int w = pq.top().first, u = pq.top().second;
    pq.pop();

    visited[u] = true; // Include vertex in MST

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

  // Print edges of MST using parent array
  for (int i = 1; i < V; ++i)
    cost += key[i], printf("%d - %d\n", parent[i], i);
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

  int c = g.prim_mst();
  std::cout << c << std::endl;

  return 0;
}