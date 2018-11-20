#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <stdio.h>
#include <unordered_map>
#include <vector>
/**
Say you have an array for which the ith element is the price of a given stock on
day i.
Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times) with the following restrictions:
        You may not engage in multiple transactions at the same time (ie, you
must sell the stock before you buy again).
        After you sell your stock, you cannot buy stock on next day. (ie,
cooldown 1 day)
Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

 **/
using namespace std;

static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int profit(0), balence(INT_MIN + 10000), pre_profit(0), pre_balence(0);
    for (auto p : prices) {
      pre_balence = balence;
      balence = max(balence, pre_profit - p);
      pre_profit = profit;
      profit = max(profit, pre_balence + p);
    }
    return profit;
  }
};
int main() {
  Solution s;
  vector<int> prices{1, 2, 3, 0, 2};
  cout << s.maxProfit(prices) << endl;
}
