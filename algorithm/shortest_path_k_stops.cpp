#include <vector> 

int shortest_path_within_k_stops(int n, vector<vector<int>> &flights, int src, int dst, int K) {
  // The smallest price from src to dst by making at most K stops
  // E.g., src -> mid -> dst is called one step.

  // Although this function only returns the minimum distance between src and dst.
  // The byproduct dp actually stores the minimum distances from src to all other
  // nodes by making at K stops. 
  int const MAX = std::numeric_limits<int>::max();
  std::vector<int> dp(n, MAX);
  dp[src] = 0;

  while (K-- >= 0) {
    bool updated = false;
    auto next_dp = dp;
    for (auto const &f : flights) {
      auto new_cost = dp[f[0]] == MAX ? MAX : dp[f[0]] + f[2];
      if (new_cost < next_dp[f[1]]) {
        updated = true;
        next_dp[f[1]] = new_cost;
      }
    }

    if (!updated)
      break;

    dp = std::move(next_dp);
  }

  return dp[dst] == MAX ? -1 : dp[dst];
}

