#include <algorithm>
#include <climits>
#include <iostream>
#include <stdio.h>
#include <vector>
/**

You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.
Note:
You can assume that
 0 <= amount <= 5000
 1 <= coin <= 5000
 the number of coins is less than 500
 the answer is guaranteed to fit into signed 32-bit integer
Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
Input: amount = 10, coins = [10]
Output: 1

 **/
using namespace std;

static int speed_up = []() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  return 0;
}();

class Solution {
public:
  int change(int amount, vector<int> &coins) {
    if (amount == 0)
      return 1;
    int dp[amount + 1] = {1};
    for (int c : coins)
      for (int j = c; j <= amount; j++)
        dp[j] += dp[j - c];
    return dp[sizeof(dp) / sizeof(dp[0]) - 1];
  }
};

int main() {
  Solution s;
  int amount = 11;
  vector<int> coins{1, 2, 5};
  cout << s.change(amount, coins) << endl;
}
