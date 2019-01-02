#
# @lc app=leetcode id=384 lang=ruby
#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (48.91%)
# Total Accepted:    62.7K
# Total Submissions: 128.2K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Shuffle a set of numbers without duplicates.
# 
# 
# Example:
# 
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // Shuffle the array [1,2,3] and return its result. Any permutation of
# [1,2,3] must equally likely to be returned.
# solution.shuffle();
# 
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
# 
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
# 
# 
#
class Solution

=begin
    :type nums: Integer[]
=end
    def initialize(nums)
       @original = nums         
    end


=begin
    Resets the array to its original configuration and return it.
    :rtype: Integer[]
=end
    def reset()
       @original
    end


=begin
    Returns a random shuffling of the array.
    :rtype: Integer[]
=end
    def shuffle()
        @original.shuffle
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# nums = [2, 3, 1]
# p nums.shuffle
# p nums

