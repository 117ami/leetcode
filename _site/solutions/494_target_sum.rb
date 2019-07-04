#
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
#
# @param {Integer[]} nums
# @param {Integer} s
# @return {Integer}
def find_target_sum_ways(nums, s)
  return 0 if nums.empty?
  if nums.size == 1
    i = 0
    i += 1 if nums.first == s
    i += 1 if nums.first == -1 * s
    return i
  end
  find_target_sum_ways(nums[1..-1], s + nums[0]) +
    find_target_sum_ways(nums[1..-1], s - nums[0])
end

def find_target_sum_ways2(nums, s)
  cache = Hash.new(0)
  [nums[0], nums[0] * -1].each { |i| cache[i] += 1 }
  (1..nums.size - 1).each do |i|
    dummy = Hash.new(0)
    cache.each_pair do |k, v|
      dummy[k + nums[i]] += v
      dummy[k - nums[i]] += v
    end
    cache = dummy
  end
  cache[s]
end

def find_target_sum_ways3(nums, _s)
  cache = [nums[0], nums[0] * -1]
  (1..nums.size - 1).each do |i|
    cache = cache.map { |n| [n + nums[i], n - nums[i]] }.flatten
  end
  cache.size
end

nums = [1, 0, 1, 1] # , 1, 1]
# nums = 21.times.map { Random.rand(10) }
# nums = [1, 0]
nums = [7, 46, 36, 49, 5, 34, 25, 39, 41, 38, 49, 47, 17, 11, 1, 41, 7, 16, 23, 13]
p nums
s = 3
# p find_target_sum_ways(nums, s)
p find_target_sum_ways2(nums, s)
p find_target_sum_ways3(nums, s)
