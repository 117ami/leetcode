# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].

# @param {Integer[]} nums
# @return {Boolean}
def check_possibility(nums)
  return true if nums.size < 3
  isnondecreasing = lambda do |seq|
    (0..seq.size - 2).each do |i|
      return false if seq[i] > seq[i + 1]
    end
    true
  end

  (0..nums.size - 2).each do |i|
    next unless nums[i] > nums[i + 1]
    dum = nums.dup
    nums[i] = nums[i + 1]
    dum[i + 1] = dum[i]
    return isnondecreasing.call(nums) || isnondecreasing.call(dum)
  end
  true
end

nums = [2, 3, 3, 4, 4, 1]
p check_possibility(nums)
