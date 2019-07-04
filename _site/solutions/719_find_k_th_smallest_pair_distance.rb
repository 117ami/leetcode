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

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_distance_pair(nums, k)
  nums.sort!
  lo = 0
  hi = nums.last - nums.first
  sz = nums.size
  while lo < hi
    cter = 0
    mid = (lo + hi) / 2
    i = j = 0
    while i < sz
      j += 1 while j < sz && nums[j] - nums[i] <= mid
      cter += j - 1 - i
      i += 1
    end

    if cter < k
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

# require './aux.rb'
# nums = random_list(10, 100)
# nums.sort!
# p nums
# p smallest_distance_pair(nums, 9)
