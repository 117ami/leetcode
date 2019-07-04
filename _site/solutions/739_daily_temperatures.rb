#
# Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put 0 instead.
# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#

# @param {Integer[]} temperatures
# @return {Integer[]}
def daily_temperatures(temperatures)
  return [0] if temperatures.size == 1
  ans = Array.new(temperatures.size, 0)
  (temperatures.size - 2).downto(0).each do |i|
    j = i + 1
    while j < temperatures.size && temperatures[j] <= temperatures[i]
      break if ans[j].zero?
      j += ans[j]
    end
    ans[i] = j < temperatures.size && temperatures[j] > temperatures[i] ? j - i : 0
  end
  ans
end

temperatures = [2, 1, 5, 4, 3, 2, 1] # [73, 74, 75, 71, 69, 72, 76, 73]
p daily_temperatures(temperatures)
