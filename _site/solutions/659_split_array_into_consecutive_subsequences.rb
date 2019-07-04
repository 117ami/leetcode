# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.
# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False
# Note:
# The length of the input is in range of [1, 10000]
#
#  https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
require './aux.rb'

# @param {Integer[]} nums
# @return {Boolean}
def is_possible(nums)
  freq = Hash.new(0).tap { |h| nums.each { |n| h[n] += 1 } }
  terminates = Hash.new(0)
  nums.each do |n|
    next if freq[n].zero?
    freq[n] -= 1
    if terminates[n - 1] > 0
      terminates[n - 1] -= 1
      terminates[n] += 1
    elsif freq[n + 1] > 0 && freq[n + 2] > 0
      freq[n + 1] -= 1
      freq[n + 2] -= 1
      terminates[n + 2] += 1
    else
      return false
    end
  end
  true
end

nums = [1, 2, 3, 3, 4, 4, 5, 5]
p is_possible(nums)
