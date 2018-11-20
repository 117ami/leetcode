#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Say you have an array for which the ith element is the price of a given stock on
day i. Design an algorithm to find the maximum profit. You may complete at most
k transactions. Note: You may not engage in multiple transactions at the same
time (ie, you must sell the stock before you buy again). Example 1: Input:
[2,4,1], k = 2 Output: 2 Explanation: Buy on day 1 (price = 2) and sell on day 2
(price = 4), profit = 4-2 = 2. Example 2: Input: [3,2,6,5,0,3], k = 2 Output: 7
        Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6),
profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3),
profit = 3-0 = 3.

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int maxProfit(int k, vector<int> &prices) {
    vector<int> balance(prices.size(), INT_MIN + 50000),
        profit(prices.size(), 0);

    if (k > prices.size() / 2)
      k = prices.size() / 2;

    for (auto pri : prices) {
      int tmp = profit[0];
      profit[0] = max(profit[0], balance[0] + pri);
      balance[0] = max(balance[0], -pri);
      for (int i = 1; i < k; i++) {
        profit[i] = max(profit[i], balance[i] + pri);
        balance[i] = max(balance[i], tmp - pri);
        tmp = profit[i];
      }
      // cout << pri << " " << balance[0] << " " << profit[0] << " "
      //      << balance[k - 1] << " " << profit[k - 1] << endl;
    }
    return profit[k - 1];
  }
};

int main() {
  Solution s;
  std::vector<int> prices = {1, 2, 6, 2, 5, 3, 7, 4, 6};
  cout << s.maxProfit(100, prices) << endl;
}
