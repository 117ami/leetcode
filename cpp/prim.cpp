#include <iostream>
#include <list>
#include <queue>
#include <vector>
using namespace std;
#define INF 0x3f3f3f3f

typedef pair<int, int> pii;

// This class represents a directed graph using
// adjacency list representation
class Graph {
  int V; // No. of vertices
  list<pair<int, int>> *adj;

public:
  Graph(int V); // Constructor
  void add_edge(int u, int v, int w);
  int cost_of_mst();
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

// Prints shortest paths from src to all other vertices
int Graph::cost_of_mst() {
  // Create a priority queue to store visited vertices.
  priority_queue<pii, vector<pii>, greater<pii>> pq;

  int cost = 0, src = 0; // Taking vertex 0 as source

  // Vector `parent` is used to  print out Tree edges from source 0
  // Vector `key` for storing weights to calculate cost
  vector<int> key(V, INF), parent(V, -1);
  vector<bool> visited(V, false);

  pq.push(make_pair(0, src));
  key[src] = 0;

    int res=0;
  /* Looping till priority queue becomes empty */
  while (!pq.empty()) {
    int w = pq.top().first, u = pq.top().second;
    res += w;
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
  return res;
}



int main() {
    Graph g(4); 
    g.add_edge(0, 1, 2);
    g.add_edge(1, 2, 4);
    g.add_edge(2, 3, 7);
    g.add_edge(0, 3, 3);
    g.add_edge(1, 3, 1);
    int cost = g.cost_of_mst(); 
    std::cout << cost << endl;
}