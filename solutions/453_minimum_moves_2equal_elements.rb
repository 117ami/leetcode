# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#

# @param {Integer[]} nums
# @return {Integer}
def min_moves(nums)
  nums.reduce(:+) - nums.size * nums.min
end

def min_moves2(nums)
  nim = 2 << 32
  r = 0
  nums.each {|n| nim = [nim, n].min; r += n}
  r - nim * nums.size
end

nums = [2, 2, 3, 4]
p min_moves(nums)
p min_moves2(nums)
