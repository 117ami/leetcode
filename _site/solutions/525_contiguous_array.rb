# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note:
# The length of the given binary array will not exceed 50,000.
#

# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums)
  hash = { 0 => -1 }
  res = sum = 0
  0.upto(nums.size - 1).each do |i|
    sum += nums[i] == 1 ? 1 : -1
    if hash.key?(sum)
      res = [res, i - hash[sum]].max
    else
      hash[sum] = i
    end
  end
  res
end


for i in 0..10 
	p i
end
p i