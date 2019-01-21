#
# @lc app=leetcode id=40 lang=ruby
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (39.19%)
# Total Accepted:    191.5K
# Total Submissions: 486.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum2(candidates, target)
  ans = []
  candidates.sort!
  # p candidates
  helper = lambda do |i, target, combs|
    return if target < 0 || (target.zero? && ans << combs)

    i.upto(candidates.size - 1).each do |j|
      c = candidates[j]
      next if j > i && candidates[j - 1] == c
      break if target < c

      helper.call(j + 1, target - c, combs + [c])
    end
  end
  helper.call(0, target, [])
  ans
end

target = 8
candidates = [10, 1, 2, 7, 6, 1, 5]

p combination_sum2(candidates, target)
