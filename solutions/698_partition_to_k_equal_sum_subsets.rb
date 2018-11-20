# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Note:
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
#

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def can_partition_k_subsets(nums, k)
  return true if nums.empty?
  return false if nums.size < k || nums.reduce(:+) % k > 0
  seen = Hash.new(0)
  possible = lambda do |i, cursum, n, target|
    return true if n == 1
    return false if cursum > target
    return possible.call(0, 0, n - 1, target) if cursum == target

    (i..nums.size - 1).each do |j|
      next unless seen[j].zero?
      seen[j] = 1
      return true if possible.call(j, cursum + nums[j], n, target)
      seen[j] = 0
    end
    return false
  end
  possible.call(0, 0, k, nums.reduce(:+) / k)
end

nums = [4, 3, 2, 3, 5, 2, 1]
nums = [2, 2, 2, 2, 3, 4, 5]
k = 4
p can_partition_k_subsets(nums, k)
