# Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.
# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Note:
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.
#
#  https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
require './aux.rb'

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_distance_pair(nums, k)
  nums.sort!
  low = -1
  high = nums.last - nums.first
  while low < high
    mi = (low + high) / 2
    if coutpairs(nums, mi) < k
      low = mi + 1
    else
      high = mi
    end
  end
  low
end

def coutpairs(nums, mi)
  res = 0
  0.upto(nums.size - 2).each do |i|
    next if nums[i + 1] - nums[i] > mi
    j = i + 1
    j = (i + 1..nums.size - 1).bsearch { |k| nums[k] - nums[i] > mi } || nums.size
    res += j - i - 1
  end
  res
end

nums = random_list(10, 100)
nums.sort!
p nums
p smallest_distance_pair(nums, 9)
