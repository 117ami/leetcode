# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 <= ai < 231.
# Find the maximum result of ai XOR aj, where 0 <= i, j < n.
# Could you do this in O(n) runtime?
# Example:
# Input: [3, 10, 5, 25, 2, 8]
# Output: 28
# Explanation: The maximum result is 5 ^ 25 = 28.
#
#  https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
require './aux.rb'

# @param {Integer[]} nums
# @return {Integer}
def find_maximum_xor(nums)
  mask = res = tmp = 0
  31.downto(0).each do |bit|
    mask |= (1 << bit)
    dict = {}
    nums.each { |n| dict[n & mask] = nil }

    tmp = res | (1 << bit)
    dict.each_key do |k|
      if dict.key?(tmp ^ k)
        res = tmp
        break
      end
    end
    p [dict, tmp, res]
  end
  res
end

nums = [3, 10, 5, 25, 2, 8]
nums = [1] * 1000
p find_maximum_xor(nums)


