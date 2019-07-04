# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].

# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def find_max_average(nums, k)
  maxsum = sum = nums[0..k - 1].reduce(:+)

  k.upto(nums.size - 1).each do |i|
    sum += nums[i] - nums[i - k]
    maxsum = [maxsum, sum].max
  end
  maxsum / (k * 1.0)
end

nums = [1, 12, -5, -6, 50, 3]
k = 4
# nums = [1, 2]
# k = 1
p find_max_average(nums, k)
