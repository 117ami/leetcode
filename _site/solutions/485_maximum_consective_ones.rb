# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
  return 0 if nums.empty?
  r = 1
  cter = 0
  nums.each do |n|
    if n == 1
      cter += 1
      r = [r, cter].max
    else
      cter = 0
    end
  end
  r
end

nums = [1, 0, 0, 0, 1, 1]
p find_max_consecutive_ones(nums)
