#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Your are given an array of integers prices, for which the i-th element is the
price of a given stock on day i; and a non-negative integer fee representing a
transaction fee.
You may complete as many transactions as you like, but you need to pay the
transaction fee for each transaction.  You may not buy more than 1 share of a
stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.
Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling at
prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int maxProfit(vector<int> &prices, int fee) {
    if (prices.size() <= 1)
      return 0;
    // note that without +50000, the computation in profit = max(..., ...) may
    // cause underflow when p- fee < 0.
    int profit = 0, balence = INT_MIN + 50000;
    for (auto p : prices) {
      int tmp = profit;
      profit = max(profit, balence + p - fee);
      balence = max(balence, tmp - p);
      cout << profit << " " << balence << endl;
    }
    return profit;
  }
};

int main() {
  Solution s;
  std::vector<int> prices = {1, 1, 1, 3, 5, 2, 5, 4, 3, 2};
  cout << s.maxProfit(prices, 4) << endl;
}
