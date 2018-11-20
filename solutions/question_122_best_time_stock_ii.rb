
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  r = 0
  low = 1 << 32
  sz = prices.size
  prices.each_with_index do |v, i|
    low = [low, v].min
    r += v - low if i < sz - 1 && v >= prices[i + 1] ||
                    i == sz - 1 && v >= prices[i - 1]
  end
  r
end

prices = [7, 1, 5, 3, 6, 1, 3]
prices = [1, 4, 2]
p max_profit(prices)
