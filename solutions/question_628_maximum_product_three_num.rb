
# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
#
# Input: [1,2,3]
# Output: 6
#
# Example 2:
#
# Input: [1,2,3,4]
# Output: 24
#
# Note:
#
#     The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
#     Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
#

# @param {Integer[]} nums
# @return {Integer}
def maximum_product(nums)
  nums.sort!
  a = [nums[0], nums[1], nums[-1]].reduce(:*)
  b = [nums[0], nums[-2], nums[-1]].reduce(:*)
  c = [nums[-3], nums[-2], nums[-1]].reduce(:*)
  [a, b, c].max
end

nums = 10.times.map { Random.rand(-10..9) }
p nums.sort
p maximum_product(nums)
