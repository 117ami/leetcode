/*
 * @lc app=leetcode id=207 lang=cpp
 *
 * [207] Course Schedule
 *
 * https://leetcode.com/problems/course-schedule/description/
 *
 * algorithms
 * Medium (41.64%)
 * Total Accepted:    369K
 * Total Submissions: 884.9K
 * Testcase Example:  '2\n[[1,0]]'
 *
 * There are a total of numCourses courses you have to take, labeled from 0 to
 * numCourses-1.
 *
 * Some courses may have prerequisites, for example to take course 0 you have
 * to first take course 1, which is expressed as a pair: [0,1]
 *
 * Given the total number of courses and a list of prerequisite pairs, is it
 * possible for you to finish all courses?
 *
 *
 * Example 1:
 *
 *
 * Input: numCourses = 2, prerequisites = [[1,0]]
 * Output: true
 * Explanation: There are a total of 2 courses to take.
 * To take course 1 you should have finished course 0. So it is possible.
 *
 *
 * Example 2:
 *
 *
 * Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
 * Output: false
 * Explanation: There are a total of 2 courses to take.
 * To take course 1 you should have finished course 0, and to take course 0 you
 * should
 * also have finished course 1. So it is impossible.
 *
 *
 *
 * Constraints:
 *
 *
 * The input prerequisites is a graph represented by a list of edges, not
 * adjacency matrices. Read more about how a graph is represented.
 * You may assume that there are no duplicate edges in the input
 * prerequisites.
 * 1 <= numCourses <= 10^5
 *
 *
 */
class Solution {
public:
  bool dfs(int n, vector<vector<int>> &depends, vector<int> &visited) {
    if (visited[n] == -1)
      return false;
    if (visited[n] == 1)
      return true;
    visited[n] = -1;
    for (auto k : depends[n]) {
      if (!dfs(k, depends, visited))
        return false;
    }
    visited[n] = 1;
    return true;
  }

  bool canFinish(int n, vector<vector<int>> &p) {
    vector<vector<int>> depends(n, vector<int>());
    for (auto &pair : p) {
      depends[pair[0]].push_back(pair[1]);
    }

    vector<int> visited(n, 0);
    for (int i = 0; i < n; i++) {
      if (!dfs(i, depends, visited))
        return false;
    }
    return true;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
