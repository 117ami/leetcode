# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
# Return 0 if the array contains less than 2 elements.
# Example 1:
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#             (3,6) or (6,9) has the maximum difference 3.
# Example 2:
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# Note:
#   You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
#   Try to solve it in linear time/space.
#
#  https://leetcode.com/problems/maximum-gap/description/
require './aux.rb'

# @param {Integer[]} nums
# @return {Integer}
def maximum_gap(nums)
  return 0 if nums.size < 2
  maxv = nums.max
  minv = nums.min
  bucket_size = [(maxv - minv) / (nums.size - 1), 1].max
  bucket_num = (maxv - minv) / bucket_size + 1 # ??
  bucket_max = Array.new(bucket_num, -1)
  bucket_min = Array.new(bucket_num, 2**32 + 1)

  nums.each do |n|
    idx = (n - minv) / bucket_size
    bucket_max[idx] = [bucket_max[idx], n].max
    bucket_min[idx] = [bucket_min[idx], n].min
  end

  res = bucket_size
  last_max = bucket_max[0]
  1.upto(bucket_num - 1).each do |idx|
    res = [res, bucket_min[idx] - last_max].max if bucket_min[idx] != 2**32 + 1
    last_max = bucket_max[idx] if bucket_max[idx] != -1
  end
  res
end

# This is not linear time, sort costs at least O(nlgn) time
def maximum_gap2(nums)
  return 0 if nums.size < 2
  nums.sort!
  maxdiff = 0
  1.upto(nums.size - 1).each do |i|
    maxdiff = [maxdiff, nums[i] - nums[i - 1]].max
  end
  maxdiff
end

nums = [1, 1, 1, 1]
# nums = random_list(4, 100)
p nums.sort
p maximum_gap(nums)
p maximum_gap2(nums)
