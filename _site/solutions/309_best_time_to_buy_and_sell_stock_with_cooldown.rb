# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#   You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#   After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75929/7-line-Java:-only-consider-sell-and-cooldown
# check on this explanation on the solution, very clear and concise.
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  pro = cool = 0
  bal = -Float::INFINITY
  prices.each do |pri|
    tmp = pro
    pro = [pro, bal + pri].max
    bal = [bal, cool - pri].max
    cool = [tmp, cool].max
    p [pri, bal, pro, cool]
  end
  pro
end

prices = [1, 2, 3, 0, 3, 4]
p max_profit(prices)
