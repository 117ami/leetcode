# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.
# Example 1:
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:
# Input: [1,2,4,8]
# Output: [1,2,4,8]
#
#  https://leetcode.com/problems/largest-divisible-subset/description/

# @param {Integer[]} nums
# @return {Integer[]}
def largest_divisible_subset(nums)
  return nums if nums.empty?
  nums.sort!.reverse!
  maxlen = {}
  nexnum = {}
  res = [0, 0]
  nums.each_with_index do |n, idx|
    maxlen[n] = 1
    nexnum[n] = nil
    (idx - 1).downto(0).each do |i|
      next unless nums[i] % n == 0
      if maxlen[nums[i]] + 1 > maxlen[n]
        maxlen[n] = maxlen[nums[i]] + 1
        nexnum[n] = nums[i]
      end
    end
    res = [maxlen[n], n] if maxlen[n] > res[0]
  end
  res.shift
  res << nexnum[res.last] while nexnum[res.last]
  res 
end

nums = [2, 3, 6, 8, 9, 32, 16, 25, 26, 27]
nums = [3]
p largest_divisible_subset(nums)
