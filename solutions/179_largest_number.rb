# Given a list of non negative integers, arrange them such that they form the largest number.
# Example 1:
# Input: [10,2]
# Output: "210"
# Example 2:
# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.
#
#  https://leetcode.com/problems/largest-number/description/
require './aux.rb'

# @param {Integer[]} nums
# @return {String}

# a should be 'larger'
def comp(a, b)
  0.upto([a.size, b.size].min - 1).each do |i|
    return 1 if a[i] > b[i]
    return -1 if a[i] < b[i]
  end
  return 0 if a.size == b.size
  a.size > b.size ? comp(a[b.size..-1], b) : comp(a, b[a.size..-1])
end

def largest_number_2(nums)
  nums.map(&:to_s).sort { |a, b| -comp(a, b) }.join.to_i.to_s
end

def largest_number(nums)
  nums.sort { |a, b| b.to_s + a.to_s <=> a.to_s + b.to_s }.join.to_i.to_s
end

nums = [3, 30, 34, 5, 9]
# nums = [10, 2, 100]
# nums = [0, 0]

p largest_number(nums)
