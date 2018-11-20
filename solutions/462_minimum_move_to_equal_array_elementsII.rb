# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
#
# You may assume the array's length is at most 10,000.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 2
#
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
#
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

# @param {Integer[]} nums
# @return {Integer}
def min_moves2(nums)
  return 0 if nums.size == 1
  nums.sort!
  (0..nums.size / 2 - 1).map { |i| nums[nums.size - 1 - i] - nums[i] }.reduce(:+)
end

nums = [1, 3, 5, 7, 12]
# nums = [1, 0, 0, 8, 6]
p min_moves2(nums)
