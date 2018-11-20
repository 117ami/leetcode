# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
  one = two = 0
  nums.each do |i|
    one = (one ^ i) & ~two
    two = (two ^ i) & ~one
  end
  one
end

nums = [1, 1, 2, 2, 1, 2, 3]
nums = [3, 4, 9, 9, 3, 3, 9]

single_number(nums)
