#
# @lc app=leetcode id=315 lang=ruby
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (36.37%)
# Total Accepted:    65.3K
# Total Submissions: 178.5K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
#
# @param {Integer[]} nums
# @return {Integer[]}
def count_smaller(nums)
  return nums if nums.empty?

  res = [0]
  sorted = [nums.pop]
  nums.reverse_each do |n|
    idx = (0..sorted.size - 1).bsearch { |i| n <= sorted[i] } || sorted.size
    sorted.insert(idx, n)
    res.unshift(idx)
  end
  res
end
