# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
# You need to return the number of important reverse pairs in the given array.
# Example1:
# Input: [1,3,2,3,1]
# Output: 2
# Example2:
# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
#
#  https://leetcode.com/problems/reverse-pairs/description/
require './aux.rb'

# @param {Integer[]} nums
# @return {Integer}
def reverse_pairs(nums)
  res = 0
  cache = []
  nums.reverse_each do |n|
    halfn = ((n - 1) / 2).round
    cter = (0..cache.size - 1).bsearch { |i| cache[i] > halfn } || cache.size
    res += cter
    idx = (0..cache.size - 1).bsearch { |i| cache[i] >= n } || cache.size
    cache.insert(idx, n)
  end
  res
end

def merge_sort(nums, s, e)
  return 0 if s >= e
  mid = (s + e) / 2
  cnt = merge_sort(nums, s, mid) + merge_sort(nums, mid + 1, e)
  s.upto(mid).each do |i|
    j = mid + 1
    j += 1 while j <= e && nums[i] / 2.0 > nums[j]
    cnt += j - mid - 1
  end
  nums[s..e] = nums[s..e].sort
  p nums
  cnt
end

nums = random_list(10, 10)
# nums = [2, 4, 3, 5, 1]
# nums = [1, 3, 2, 3, 1]
# nums = [-5, -5]
p nums
p reverse_pairs(nums)
p merge_sort(nums, 0, nums.size - 1)
