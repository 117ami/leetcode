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
If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.
Note that you cannot sell a stock before you buy one.
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
6-1 = 5.
            Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int maxProfit(vector<int> &prices) {
    if (prices.size() <= 1)
      return 0;
    int profits = 0, min_prince = prices[0];
    for (int p : prices) {
      min_prince = min(p, min_prince);
      profits = max(profits, p - min_prince);
    }
    return profits;
  }
};
int main() {
  Solution s;
  vector<int> prices = {7, 1, 5, 3, 6, 4, 9};
  cout << s.maxProfit(prices) << endl;
}
