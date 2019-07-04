
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Credits:
#   Special thanks to @Freezen for adding this problem and creating all test cases.

def maximum_profits(k, prices)
  return 0 if k.zero?
  return all_profits(prices) if prices.size < k * 2 - 1
  m = prices.size

  r = Array.new(k + 1) { Array.new(m, 0) }
  (1..k).each do |i|
    tmax = - prices[0]
    (1..m - 1).each do |j|
      r[i][j] = [r[i][j - 1], tmax + prices[j]].max
      tmax = [tmax, r[i - 1][j - 1] - prices[j]].max
    end
  end
  r[k][m - 1]
end

def all_profits(prices)
  r = 0
  pre = prices[0]
  prices[1..-1].each do |v|
    r += v - pre if v > pre
    pre = v
  end
  r
end

size = 13
prices = size.times.map { |_i| Random.rand(size) }
p prices
p maximum_profits(3, prices)
p all_profits(prices)
