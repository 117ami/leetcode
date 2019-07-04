# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
  r = 0
  nums.each { |i| r ^= i }
  r
end

nums = [2, 3, 1, 2, 3, 5, 1]
single_number(nums)
