# Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.
#

class NumArray
  #     :type nums: Integer[]

  def initialize(nums)
    @accum = [0]
    nums.each do |n|
      @accum << @accum[-1] + n
    end
  end

  #     :type i: Integer
  #     :type j: Integer
  #     :rtype: Integer
  def sum_range(i, j)
    @accum[j + 1] - @accum[i]
  end
end

# Your NumArray object will be instantiated and called as such:
# obj = NumArray.new(nums)
# param_1 = obj.sum_range(i, j)
