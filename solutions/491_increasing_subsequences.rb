# Given an integer array, your task is to find all the different possible
# increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .
#
# Example:
#
# Input: [4, 6, 7, 7, 8, 9, 10, 11, 13]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
#
# Note:
#
#     The length of the given array will not exceed 15.
#     The range of integer in the given array is [-100,100].
#     The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

# @param {Integer[]} nums
# @return {Integer[][]}
def find_subsequences(nums)
  return [] if nums.size < 2
  res = { [nums[-1]] => nil }
  recur = lambda do |n, arr|
    res.keys.each do |k|
      res[[n]] = nil
      next if n > k[0]
      res[[n].concat(k)] = nil
      arr.each { |m| res[[n, m]] = nil if n <= m }
    end
  end
  (0..nums.size - 2).reverse_each { |i| recur.call(nums[i], nums[i + 1..-1]) }
  res.keys.select { |k| k.size >= 2 }
end

def find_subsequences2(nums)
  res = {}
  nums.each_with_index do |cur, i|
    res.keys.each do |k|
      next if k.last > cur
      res[k.dup.concat([cur])] = nil
    end
    (0..i - 1).each { |j| res[[nums[j], cur]] = nil if cur >= nums[j] } if i > 0
    res[[cur]] = nil
  end
  res.keys.select { |k| k.size >= 2 }
end

nums = [4, 6, 7, 7]
# nums = [4, 6, 7, 7, 8, 9, 10, 11, 11, 12, 13, 14]
nums = [4, 3, 2, 1]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
nums = [2, 1]
p find_subsequences(nums)
p find_subsequences2(nums)
