#
# @lc app=leetcode id=416 lang=ruby
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (40.57%)
# Total Accepted:    86.4K
# Total Submissions: 212.9K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
# Note:
#
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
#
#
# Example 1:
#
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#
#
# Example 2:
#
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
#
#
# @param {Integer[]} nums
# @return {Boolean}

def can_partition(nums)
  mus = nums.reduce(:+)
  return false if mus.odd?

  target = mus / 2
  seen = {}

  dfs = lambda do |i, acc|
    return true if acc == target
    return false if i >= nums.size || acc > target

    key = "#{acc},#{i}"
    return seen[key] if seen.key?(key)

    res = dfs.call(i + 1, acc + nums[i]) || dfs.call(i + 1, acc)
    seen[key] = res
    res
  end
  dfs.call(0, 0)
end

nums = [1, 2, 5]
p can_partition(nums)
