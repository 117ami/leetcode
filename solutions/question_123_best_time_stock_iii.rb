

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# @param {Integer[]} prices
# @return {Integer}

def extreme(nums) # Keep only maximum and minimum points for array with size larger than 10
  return nums if nums[10].nil?
  r = []
  (1..nums.size - 2).each do |i|
    next if nums[i] == nums[i + 1]
    r << nums[i] unless nums[i - 1] < nums[i] && nums[i] < nums[i + 1] ||
                        nums[i - 1] > nums[i] && nums[i] > nums[i + 1]
  end
  r.unshift(nums[0]) if nums[0] < r[0]
  r.push(nums[-1]) if nums[-1] > r[-1]
  r
end

def max_profit(prices)
  dp = lambda do |i, j|
    r = 0
    low = Float::INFINITY
    prices[i..j].each do |v|
      low = [v, low].min
      r = [v - low, r].max
    end
    return r
  end

  r = 0
  prices = extreme(prices)
  (1..prices.size - 1).each do |i|
    r = [r, dp.call(0, i) + dp.call(i + 1, prices.size - 1)].max
  end
  r
end

def mp2(prices)
  pay1 = pay2 = - Float::INFINITY
  prof1 = prof2 = 0
  prices.each do |price|
    pay1 = [- price, pay1].max
    prof1 = [price + pay1, prof1].max
    pay2 = [prof1 - price, pay2].max
    prof2 = [price + pay2, prof2].max
  end
  prof2
end


def mp3(prices)
  low = Float::INFINITY
  maxpro = 0
  profits = []
  prices.each_with_index do |v, i|
    low = [low, v].min
    maxpro = [maxpro, v - low].max
    profits[i] = maxpro
  end

  r = maxpro = 0
  high = - Float::INFINITY
  (prices.size - 1).downto(1) do |i|
    high = [high, prices[i]].max
    maxpro = [maxpro, high - prices[i]].max
    r = [r, maxpro + profits[i]].max
  end
  r
end

prices = 20.times.map { Random.rand(1..20) }
p [prices, prices.size]
p max_profit(prices)
p mp2(prices)
p mp3(prices)
