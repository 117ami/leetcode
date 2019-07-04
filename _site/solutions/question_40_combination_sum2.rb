
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

def combination_sum(candidates, target)
  r = []
  candidates.sort!
  #candidates = candidates.reverse
  loop = lambda do |i, target, combs|
    if target.zero?
      r << combs
      return
    end
    return if target < 0

    i.upto(candidates.size - 1) do |j|
      c = candidates[j]
      next if j > i && candidates[j-1] == c
      break if target < c
      loop.call(j + 1, target - c, combs + [c])
    end
  end
  loop.call(0, target, [])
  r
end

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = combination_sum(candidates, target)
p res
