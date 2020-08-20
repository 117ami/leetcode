#include <vector>
/*
 * @lc app=leetcode id=815 lang=cpp
 *
 * [815] Bus Routes
 *
 * https://leetcode.com/problems/bus-routes/description/
 *
 * algorithms
 * Hard (42.57%)
 * Total Accepted:    38.7K
 * Total Submissions: 90.8K
 * Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
 *
 * We have a list of bus routes. Each routes[i] is a bus route that the i-th
 * bus repeats forever. For example if routes[0] = [1, 5, 7], this means that
 * the first bus (0-th indexed) travels in the sequence
 * 1->5->7->1->5->7->1->... forever.
 *
 * We start at bus stop S (initially not on a bus), and we want to go to bus
 * stop T. Travelling by buses only, what is the least number of buses we must
 * take to reach our destination? Return -1 if it is not possible.
 *
 *
 * Example:
 * Input:
 * routes = [[1, 2, 7], [3, 6, 7]]
 * S = 1
 * T = 6
 * Output: 2
 * Explanation:
 * The best strategy is take the first bus to the bus stop 7, then take the
 * second bus to the bus stop 6.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= routes.length <= 500.
 * 1 <= routes[i].length <= 10^5.
 * 0 <= routes[i][j] < 10 ^ 6.
 *
 *
 */
class Solution {
public:
  int numBusesToDestination(vector<vector<int>> &routes, int S, int T) {
    int n = routes.size();
    if (S == T)
      return 0;
    unordered_map<int, unordered_set<int>> stop2bus;
    for (int i = 0; i < n; i++) {
      for (auto s : routes[i])
        stop2bus[s].insert(i);
    }

    unordered_set<int> starts = stop2bus[S];
    say(starts);
    std::deque<int> d(starts.begin(), starts.end());
    bool visited[n];
    memset(visited, false, sizeof(visited));
    int step = 1;

    while (!d.empty()) {
      int len = d.size();
      while (len-- > 0) {
        int bus = d.front();
        d.pop_front();

        if (visited[bus])
          continue;
        visited[bus] = true;

        say(bus);
        for (auto stop : routes[bus]) {
          if (stop == T)
            return step;
          for (auto b : stop2bus[stop])
            d.push_back(b);
        }
      }
      step++;
    }
    return -1;
  }
};

auto speed_up = []() {
  ios_base::sync_with_stdio(false);
  return 0;
}();
