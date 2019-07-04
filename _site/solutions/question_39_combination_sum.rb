
# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]

# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
  set = candidates.clone.keep_if { |v| v <= target }.sort.reverse
  return [] if set.empty?
  res = []
  set.each do |v|
    if v == target
      res.push([v])
    else
      rest_arr = set.clone.keep_if { |vv| vv <= v }
      tmp = combination_sum(rest_arr, target - v)
      tmp.each do |t|
        res.push([v] + t)
      end
    end
  end
  res
end

def combination_sum_2(candidates, target)
  r = []
  candidates.sort!
  loop = lambda do |i, target, combs|
    if target.zero?
      r << combs
      return
    end
    return if target < 0

    i.upto(candidates.size - 1) do |j|
      c = candidates[j]
      break if target < c
      loop.call(j, target - c, combs + [c])
    end
  end
  loop.call(0, target, [])
  r
end

candidates = [2, 3, 4, 5, 7, 8]
target = 9
res = combination_sum_2(candidates, target)
p res

p [1] + [2, 3]
