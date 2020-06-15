/*
 * @lc app=leetcode id=188 lang=cpp
 *
 * [188] Best Time to Buy and Sell Stock IV
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
 *
 * algorithms
 * Hard (27.74%)
 * Total Accepted:    124.3K
 * Total Submissions: 447.8K
 * Testcase Example:  '2\n[2,4,1]'
 *
 * Say you have an array for which the i-th element is the price of a given
 * stock on day i.
 *
 * Design an algorithm to find the maximum profit. You may complete at most k
 * transactions.
 *
 * Note:
 * You may not engage in multiple transactions at the same time (ie, you must
 * sell the stock before you buy again).
 *
 * Example 1:
 *
 *
 * Input: [2,4,1], k = 2
 * Output: 2
 * Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit
 * = 4-2 = 2.
 *
 *
 * Example 2:
 *
 *
 * Input: [3,2,6,5,0,3], k = 2
 * Output: 7
 * Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit
 * = 6-2 = 4.
 * Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 =
 * 3.
 *
 *
 */
class Solution {
public:
  int maxProfit(int k, vector<int> &prices) {
    int n = prices.size();
    if (k >= n / 2)
      return _quick_solve(prices);

    // dp[i][j] the maximum prefit gained at day j with at most i transcations
    vector<vector<int>> dp(k + 1, vector<int>(n, 0));

    for (int i = 1; i <= k; i++) {
        // pre_max is the maximum profit we gain if conduct transaction at last day
      int pre_max = -prices[0];
      for (int j = 1; j <= n; j++) {
        dp[i][j] = max(dp[i][j - 1], pre_max + prices[j]);
        pre_max = max(pre_max, dp[i - 1][j - 1] - prices[j]);
      }
    }
    return dp.back().back();
  }

  int _quick_solve(vector<int> &prices) {
    int ans = 0;
    for (int i = 1; i < prices.size(); i++) {
      ans += max(0, prices[i] - prices[i - 1]);
    }
    return ans;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
