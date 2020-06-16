/*
 * @lc app=leetcode id=123 lang=cpp
 *
 * [123] Best Time to Buy and Sell Stock III
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
 *
 * algorithms
 * Hard (36.88%)
 * Total Accepted:    206.6K
 * Total Submissions: 560.1K
 * Testcase Example:  '[3,3,5,0,0,3,1,4]'
 *
 * Say you have an array for which the i^th element is the price of a given
 * stock on day i.
 *
 * Design an algorithm to find the maximum profit. You may complete at most two
 * transactions.
 *
 * Note: You may not engage in multiple transactions at the same time (i.e.,
 * you must sell the stock before you buy again).
 *
 * Example 1:
 *
 *
 * Input: [3,3,5,0,0,3,1,4]
 * Output: 6
 * Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit
 * = 3-0 = 3.
 * Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
 * 3.
 *
 * Example 2:
 *
 *
 * Input: [1,2,3,4,5]
 * Output: 4
 * Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit
 * = 5-1 = 4.
 * Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
 * are
 * engaging multiple transactions at the same time. You must sell before buying
 * again.
 *
 *
 * Example 3:
 *
 *
 * Input: [7,6,4,3,1]
 * Output: 0
 * Explanation: In this case, no transaction is done, i.e. max profit = 0.
 *
 */
class Solution {
public:
  int maxProfit(vector<int> &ps) {
    int n = ps.size();
    if (n < 2)
      return 0;
    // balance and profit 1, 2
    int b1 = INT_MIN, b2 = INT_MIN;
    int p1 = 0, p2 = 0;
    for (int p : ps) {
      b1 = max(b1, -p);
      p1 = max(p1, p + b1);
      b2 = max(b2, p1 - p);
      p2 = max(p2, p + b2);
      // say(vector<int>{b1,p1,b2,p2});
    }
    return p2;
  }
};

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
