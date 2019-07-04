# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
# Example:
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
#
#  https://leetcode.com/problems/random-pick-index/description/
require './aux.rb'

class Solution
  #     :type nums: Integer[]
  def initialize(nums)
    # @indexes = {}
    # nums.each_with_index do |n, i|
    #   @indexes[n] = [] if @indexes[n].nil?
    #   @indexes[n] << i
    # end
  end

  #     :type target: Integer
  #     :rtype: Integer
  def pick(target)
    @indexes[target].sample
  end
end

# Your Solution object will be instantiated and called as such:
nums = [3, 2, 3, 1, 3]
obj = Solution.new(nums)
p obj.pick(3)
