# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.

# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
  return 0 if nums.empty?
  ret = 1
  lt = 0
  (1..nums.size - 1).each do |i|
    next if nums[i] > nums[i - 1]
    ret = [ret, i - lt].max
    lt = i
  end
  [ret, nums.size - lt].max
end

nums = [1, 3, 5, 7]
p find_length_of_lcis(nums)
