#
# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such
# that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
# Note: n will be less than 15,000.
# Example 1:
# Input: [1, 2, 3, 4]
# Output: False
# Explanation: There is no 132 pattern in the sequence.
# Example 2:
# Input: [3, 1, 4, 2]
# Output: True
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:
# Input: [-1, 3, 2, 0]
# Output: True
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
#
#  https://leetcode.com/problems/132-pattern/description/
require './aux.rb'
# @param {Integer[]} nums
# @return {Boolean}
def find132pattern(nums)
  s3 = -Float::INFINITY
  stack = [s3]
  nums.reverse_each do |n|
    return true if n < s3
    s3 = stack.pop while !stack.empty? && stack.last < n
    stack.push(n)
  end
  false
end

nums = [1, 2, 3, 4]
# nums = [3, 1, 4, 2]
# nums = [-1, 3, 2, 0]
# nums = [7, 7, 4, 5, 3, 1, 2, 2, 1, 5]
# nums = 10.times.map { Random.rand(10) }
nums = [3, 5, 0, 3, 4]
nums = [-2, 1, 2, -2, 1, 2]
p nums
p find132pattern(nums)
