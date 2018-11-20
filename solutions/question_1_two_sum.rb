
# Given an array of integers, return indices of the two numbers
#  such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
#  and you may not use the same element twice.

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  hash = Hash.new(0).tap { |h| nums.each_with_index { |v, i| h[v] = i } }
  size = nums.size - 1

  (0..size).each do |i|
    diff = target - nums[i]
    return i, hash[diff] if hash.key?(diff) && hash[diff] != i
  end
end

def two_sum_2(nums, target)
  h = {}
  nums.each_with_index do |v, i|
    return i, h[target - v] if h.key?(target - v)
    h[v] = i
  end
end

p two_sum_2([3, 3], 6)
