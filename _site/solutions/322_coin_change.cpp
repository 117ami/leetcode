#include "aux.cpp"
/**
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1. Example 1: Input: coins = [1, 2, 5], amount
= 11 Output: 3 Explanation: 11 = 5 + 5 + 1 Example 2: Input: coins = [2], amount
= 3 Output: -1 Note: You may assume that you have an infinite number of each
kind of coin.

 https://leetcode.com/problems/coin-change/description/
 **/
static const int _ = []() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();
class Solution {
public:
  int coinChange(vector<int> &coins, int amount) {
    std::vector<int> res(amount + 1, INT_MAX);
    res[0] = 0;
    for (int n = 1; n <= amount; n++)
      for (int i = 0; i < coins.size(); i++)
        if (n >= coins[i])
          res[n] = min(res[n], res[n - coins[i]] + 1);
    return res[amount] > amount ? -1 : res[amount];
  }
};
int main() { Solution s; }
