# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#  https://leetcode.com/problems/coin-change/description/

# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def coin_change(coins, amount)
  dp = Array.new(amount + 1, Float::INFINITY)
  dp[0] = 0
  1.upto(amount).each do |n|
    0.upto(coins.size - 1).each do |i|
      dp[n] = [dp[n], dp[n - coins[i]] + 1].min if n >= coins[i]
    end
  end
  dp[amount] > amount ? -1 : dp[amount]
end

coins = [2, 5]
amount = 3
# coins = [186, 419, 83, 408]
# amount = 6249
p coin_change(coins, amount)
