#
# You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use - as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
#
#  https://leetcode.com/problems/24-game/description/
require './aux.rb'
# @param {Integer[]} nums
# @return {Boolean}
def judge_point24(nums)
  nums.sort
  m1, m2, m3, m4 = nums
  dict = {}
  [[[m1, m2], [m3, m4]], [[m1, m3], [m2, m4]], [[m1, m4], [m2, m3]]].each do |a, b|
    result_two(a).each_key do |i|
      result_two(b).each_key do |j|
        dict.merge!(result_two([i, j]))
        return true if dict.key?(24) || dict.key?(24.0)
      end
    end
  end
  (0..nums.size - 1).each do |idx|
    nums[0], nums[idx] = nums[idx], nums[0]
    result_three(nums[1..-1]).each_key do |k|
      dict.merge!(result_two([nums.first, k]))
      return true if dict.key?(24) || dict.key?(24.0)
    end
    nums[0], nums[idx] = nums[idx], nums[0]
  end
  dict.each_key { |k| return true if (k - 24).abs <= 0.00001 }
  false
end

def result_three(nums)
  a, b, c = nums
  dict = {}
  result_two([b, c]).each_key { |k| dict.merge!(result_two([a, k])) }
  result_two([a, c]).each_key { |k| dict.merge!(result_two([b, k])) }
  result_two([a, b]).each_key { |k| dict.merge!(result_two([c, k])) }
  dict
end

def result_two(nums)
  dict = {}
  a, b = nums
  dict[a + b] = nil
  dict[a - b] = nil
  dict[b - a] = nil
  dict[b * a] = nil
  dict[(b * 1.0) / a] = nil if a != 0
  dict[(a * 1.0) / b] = nil if b != 0
  dict
end

# p result_three([2, 3, 4])
nums = [4, 8, 1, 7]
nums = [1, 3, 4, 6]
nums = [3, 3, 8, 8]
p judge_point24(nums)
