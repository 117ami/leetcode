# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1
#
# Input: [3,0,1]
# Output: 2
# Example 2
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#
# Credits:

# @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
  return 0 if nums.empty?
  n = nums.size
  n * (n + 1) / 2 - nums.sum
end

nums = [5, 4, 1, 2, 0]
p missing_number(nums)
