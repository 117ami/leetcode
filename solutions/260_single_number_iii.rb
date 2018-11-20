# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
# Example:
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:
#   The order of the result is not important. So in the above example, [5, 3] is also correct.
#   Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#
#  https://leetcode.com/problems/single-number-iii/description/

# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
  res = [0, 0]
  xor = nums.reduce(:^)
  lastbit = (xor & (xor - 1)) ^ xor
  nums.each do |n|
    res = (lastbit & n).zero? ? [res.first ^ n, res.last] : [res.first, res.last ^ n]
  end
  res
end

nums = [1, 2, 1, 3, 2, 5]
nums = [-1_638_685_546, -2_084_083_624, -307_525_016, -930_251_592, -1_638_685_546, 1_354_460_680, 623_522_045, -1_370_026_032, -307_525_016, -2_084_083_624, -930_251_592, 472_570_145, -1_370_026_032, 1_063_150_409, 160_988_123, 1_122_167_217, 1_145_305_475, 472_570_145, 623_522_045, 1_122_167_217, 1_354_460_680, 1_145_305_475]
p single_number(nums)
