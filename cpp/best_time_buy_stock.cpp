
int maxProfit(vector<int> &prices) {
  /* General solution for conducting at most K transactions

  dp[i][j] is the max profit up until prices[j] using at most i
  transactions. dp[i][j] = for m in [0, j - 1]: max(dp[i][j-1], prices[j] -
  prices[m] + dp[i-1][m]) = max(dp[i][j-1], prices[j] + max(dp[i-1][m] -
  prices[m]))


  dp[0][j] = 0, no transcation no profit
  dp[i][0] = 0, no price data, no profit
  */
  int n = prices.size();
  if (n <= 1)
    return 0;
  int k = 2;
  int dp[k + 1][n];
  memset(dp, 0, sizeof(dp));

  for (int i = 1; i <= k; i++) {
    int tmp_max = -prices[0];
    for (int j = 1; j < n; j++) {
      dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max);
      tmp_max = max(tmp_max, dp[i - 1][j] - prices[j]);
    }
  }

  return dp[k][n - 1];
}
