# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
# Example:
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 <= k <= input array's size for non-empty array.
# Follow up:
# Could you solve it in linear time?
#
#  https://leetcode.com/problems/sliding-window-maximum/description/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_sliding_window(nums, k)
  return [] if nums.empty?
  deque = []
  0.upto(k - 1).each do |i|
    deque.pop while !deque.empty? && deque.last < nums[i]
    deque << nums[i]
  end
  res = [deque.first]

  k.upto(nums.size - 1).each do |i|
    deque.shift if deque.first == nums[i - k]
    deque.pop while !deque.empty? && deque.last < nums[i]
    deque << nums[i]
    res << deque.first
  end
  res
end

nums = [1, 3, -1, 4, -3, 5, 3, 6, 7]
k = 3
p max_sliding_window(nums, k)
