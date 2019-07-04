# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)
  sums = Hash.new(0)
  tmp = 0
  r = 0
  nums.each do |n|
    tmp += n
    r += 1 if tmp == k
    r += sums[tmp - k]
    sums[tmp] += 1
  end
  r
end

nums = 10.times.map { Random.rand(-10..10) }
# nums = [1, 1, 1]
# nums = [1, 1]
p nums
p subarray_sum(nums, 5)
