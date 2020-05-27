/*
 * @lc app=leetcode id=785 lang=cpp
 *
 * [785] Is Graph Bipartite?
 *
 * https://leetcode.com/problems/is-graph-bipartite/description/
 *
 * algorithms
 * Medium (46.56%)
 * Total Accepted:    101.2K
 * Total Submissions: 217.1K
 * Testcase Example:  '[[1,3],[0,2],[1,3],[0,2]]'
 *
 * Given an undirected graph, return true if and only if it is bipartite.
 * 
 * Recall that a graph is bipartite if we can split it's set of nodes into two
 * independent subsets A and B such that every edge in the graph has one node
 * in A and another node in B.
 * 
 * The graph is given in the following form: graph[i] is a list of indexes j
 * for which the edge between nodes i and j exists.  Each node is an integer
 * between 0 and graph.length - 1.  There are no self edges or parallel edges:
 * graph[i] does not contain i, and it doesn't contain any element twice.
 * 
 * 
 * Example 1:
 * Input: [[1,3], [0,2], [1,3], [0,2]]
 * Output: true
 * Explanation: 
 * The graph looks like this:
 * 0----1
 * |    |
 * |    |
 * 3----2
 * We can divide the vertices into two groups: {0, 2} and {1, 3}.
 * 
 * 
 * 
 * Example 2:
 * Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
 * Output: false
 * Explanation: 
 * The graph looks like this:
 * 0----1
 * | \  |
 * |  \ |
 * 3----2
 * We cannot find a way to divide the set of nodes into two independent
 * subsets.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * graph will have length in range [1, 100].
 * graph[i] will contain integers in range [0, graph.length - 1].
 * graph[i] will not contain i or duplicate values.
 * The graph is undirected: if any element j is in graph[i], then i will be in
 * graph[j].
 * 
 * 
 */

int find(int x, vector<int> &p) {
  if (x != p[x])
    p[x] = find(p[x], p);
  return p[x];
}

// Do not use union, since it's a keyword of CPP
void merge(int x, int y, vector<int> &p) { p[find(x, p)] = find(y, p); }

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int> p(101, 0);
        for (int i = 0; i < 101; i++) p[i] = i; 
        for (int i = 0; i < graph.size(); i ++) {
            if (i == 0) {
                for (auto n : graph[i]) {
                    p[graph[i][0]] = 100; 
                    merge(n, graph[i][0], p);
                }
            }  else {
                int x = find(i, p);
                for (auto n: graph[i]) {
                    merge(n, graph[i][0], p); 
                    if (x == find(n, p)) return false ; 
                }
            }
        }
        return true;
    }
};



static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL);return 0; }();
