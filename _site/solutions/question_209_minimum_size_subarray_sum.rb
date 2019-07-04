# coding: utf-8

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

# @param {Integer} s
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(s, nums)
  return 0 if nums.empty? || nums.sum < s
  sum = i = 0
  rmin = 1 << 32
  (0..nums.size - 1).each do |j|
    sum += nums[j]
    while sum >= s
      rmin = [rmin, j - i + 1].min
      sum -= nums[i]
      i += 1
    end
  end
  rmin
end

nums = [2, 3, 1, 2, 4, 9]
s = 7
p min_sub_array_len(s, nums)
