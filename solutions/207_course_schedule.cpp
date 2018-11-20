#include "aux.cpp"
/**
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1] Given the total number
of courses and a list of prerequisite pairs, is it possible for you to finish
all courses? Example 1: Input: 2, [[1,0]] Output: true Explanation:There are a
total of 2 courses to take. To take course 1 you should have finished course 0.
So it is possible. Example 2: Input: 2, [[1,0],[0,1]] Output: false
Explanation:There are a total of 2 courses to take.
            To take course 1 you should have finished course 0, and to take
course 0 you should also have finished course 1. So it is impossible. Note: The
input prerequisites is a graph represented by a list of edges, not adjacency
matrices. Read more about how a graph is represented. You may assume that there
are no duplicate edges in the input prerequisites.

 https://leetcode.com/problems/course-schedule/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  bool canFinish(int numCourses, vector<pair<int, int>> &prerequisites) {
    unordered_map<int, int> visit;
    vector<vector<int>> graph(numCourses, vector<int>());
    for (auto pre : prerequisites)
      graph[pre.first].emplace_back(pre.second);
    for (int i = 0; i < numCourses; i++)
      if (!dfs(i, visit, graph))
        return false;
    return true;
  }

  bool dfs(int n, unordered_map<int, int> &visit, vector<vector<int>> &graph) {
    if (visit[n] == -1)
      return false;
    else if (visit[n] == 1)
      return true;
    visit[n] = -1;
    for (int k : graph[n])
      if (!dfs(k, visit, graph))
        return false;
    visit[n] = 1;
    return true;
  }
};

int main() {
  Solution s;
  vector<pair<int, int>> prerequisites = {{1, 2}, {2, 4}, {1, 3}, {3, 4},
                                          {3, 5}, {5, 4}, {7, 3}, {5, 7}};
  int numCourses = 8;
  say(s.canFinish(numCourses, prerequisites));
}
