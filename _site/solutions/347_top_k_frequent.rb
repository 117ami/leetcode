# coding: utf-8
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
  freq = Hash.new(0).tap { |h| nums.each { |e| h[e] += 1 } }
  freq.sort_by { |_, v| -v }[0..k - 1].map(&:first)
end

nums = 10.times.map { Random.rand(10) }
p nums
top_k_frequent(nums, 3)
