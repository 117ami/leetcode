# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidateswhere the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
#   All numbers (including target) will be positive integers.
#   The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#  [2,2,2,2],
#  [2,3,3],
#  [3,5]
# ]
#
#  https://leetcode.com/problems/combination-sum/description/
require './aux.rb'

# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
  return [] if candidates.empty?
  recur(candidates.sort, target, 0)
end

def recur(candidates, target, idx)
  res = []
  return res if candidates[0] > target

  idx.upto(candidates.size - 1).each do |i|
    can = candidates[i]
    break if can > target
    if can == target
      res << [can]
    else
      recur(candidates, target - can, i).each do |subarr|
        res << [can] + subarr
      end
    end
  end
  res
end

candidates = [2, 3, 5]
target = 8
candidates = [2,3,6,7]
target = 7
p combination_sum(candidates, target)
