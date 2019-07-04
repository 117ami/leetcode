# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Note:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
#
# @param {Integer[]} prices
# @param {Integer} fee
# @return {Integer}
def max_profit(prices, fee)
  profit = 0                    # holding zero stocks
  hold = - Float::INFINITY      # holding one stocks
  prices.each do |pri|
    tmp = profit
    profit = [profit, hold + pri].max     # sell the one stock in hand
    hold = [hold, profit - pri - fee].max # buy one stock
    p [pri, profit, hold]
  end
  profit
end

prices = [1, 3, 2, 8, 4, 9]
# prices = [1, 3, 7, 5, 10, 3]
# prices = [4, 5, 2, 4, 3, 3, 1, 2, 5, 4]
# prices = [2, 2, 1, 1, 5, 5, 3, 1, 5, 4]
fee = 0

p max_profit(prices, fee)
