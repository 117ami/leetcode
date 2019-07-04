# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets_with_dup(nums)
  return [[]] if nums.empty?
  nums.sort!
  cache = {}
  r = [[]]
  loop = lambda do |i|
    r.dup.each do |a|
      ns = a + [nums[i]]
      s = ns.join('.')
      next if cache.key?(s)
      cache[s] = nil
      r << ns
    end
  end
  (0..nums.size - 1).each { |j| loop.call(j) }
  r
end

nums = [1, 2, 2, 2, 2]
p subsets_with_dup(nums)
