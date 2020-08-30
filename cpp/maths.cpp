#include <iostream>
#include <vector>

int64_t comb(int n, int k) {
  // Similiar to Python math.comb(n, k) but modulate a number mod
  // to avoid stack overflow
  const int mod = 1e9 + 7;
  if (k * 2 > n) return comb(n, n - k);

  int dp[k + 1], pre[k + 1];
  memset(dp, 0, sizeof(dp)), memset(pre, 0, sizeof(pre));
  pre[0] = dp[0] = 1;
  
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= std::min(i, k); j++) dp[j] = (pre[j - 1] + pre[j]) % mod;

    // Copy dp to pre 
    for (int j = 1; j <= k; j++) pre[j] = dp[j];
  }
  return dp[k];
}
