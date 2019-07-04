#
# @lc app=leetcode id=41 lang=ruby
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.67%)
# Total Accepted:    206.5K
# Total Submissions: 719.7K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#
#
# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive_2(nums)
  sz = nums.size
  nums.each_with_index do |n, i|
    next if n > sz || n - 1 == i || n <= 0

    loop do
      tmp = nums[n - 1]
      nums[n - 1] = n
      break if tmp <= 0 || tmp > sz || tmp == n

      n = tmp
    end
  end

  nums.each_with_index do |n, i|
    return i + 1 if i + 1 != n
  end
  (nums.last || 0) + 1
end

def first_missing_positive(nums)
  nums.sort!.uniq!
  nums.shift while !nums.empty? && nums.first <= 0
  return 1 if nums.empty?

  nums.each_with_index { |n, i| return i + 1 if n != i + 1 }
  nums.size + 1
end

nums = [1, 2, 0]
# nums = [3, 4, -1, 1]
# nums = [7,8,9,11,12]
# nums = [3, 1]
# nums = []
# nums = [0, 2, 2, 1, 1]
p first_missing_positive(nums)
