# Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
#   The array is only modifiable by the update function.
#   You may assume the number of calls to update and sumRange function is distributed evenly.
#
#  https://leetcode.com/problems/range-sum-query-mutable/description/

class NumArray
  #     :type nums: Integer[]
  def initialize(nums)
    @arr = nums
  end

  #     :type i: Integer
  #     :type val: Integer
  #     :rtype: Void
  def update(i, val)
    @arr[i] = val
  end

  #     :type i: Integer
  #     :type j: Integer
  #     :rtype: Integer
  def sum_range(i, j)
    @arr[i..j].reduce(:+)
  end
end

# Your NumArray object will be instantiated and called as such:
nums = [0, 9, 5, 7, 3]
obj = NumArray.new(nums)
param_2 = obj.sum_range(3, 3)
p param_2
