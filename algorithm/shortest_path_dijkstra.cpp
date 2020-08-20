#include <vector> 


vector<int> shortestPath(vector<vector<int>> &graph, int src) {
  // Each vector in graph contains 3 values: (srt, dst, weight)
    //   Return the smallest weight to reach each node from src
  int N = graph.size();
  vector<vector<pair<int, int>>> adj(N); 

//   Graph is usually directed 
  for(auto &v: graph)  
     adj[v[0]].push_back(make_pair(v[1], v[2]));


  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

  vector<int> res(N, INT_MAX);

  pq.push(make_pair(0, src));
  res[src] = 0;

  while (!pq.empty()) {
    int u = pq.top().second;
    pq.pop();

    for (auto &p : adj[u]) {
      int v = p.first, weight = p.second;

      if (res[v] > res[u] + weight) {
        res[v] = res[u] + weight;
        pq.push(make_pair(res[v], v));
      }
    }
  }
  return res; 
}
