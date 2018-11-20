# Given an array of integers nums, write a method that returns the "pivot" index of this array.
#
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
#
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
#
# Example 1:
# Input:
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# Example 2:
# Input:
# nums = [1, 2, 3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Note:
#
# The length of nums will be in the range [0, 10000].
#   Each element nums[i] will be an integer in the range [-1000, 1000].
# @param {Integer[]} nums
# @return {Integer}
def pivot_index(nums)
  return -1 if nums.empty?
  r = 0
  sums = nums.map { |n| r += n }
  return 0 if sums[-1] == sums[0]
  (1..nums.size - 1).each do |i|
    return i if sums[-1] - sums[i] == sums[i - 1]
  end
  -1
end

nums = 10.times.map { Random.rand(10) }
nums = [1, 7, 3, 6, 5, 6]
nums = [-1, -1, -1, -1, -1, 0]
p nums
p pivot_index(nums)
