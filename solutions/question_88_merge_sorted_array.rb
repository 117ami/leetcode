#!/usr/bin/ruby -w

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
  i = m - 1
  j = n - 1
  pos = m + n - 1
  while i > -1 && j > -1
    if nums1[i] > nums2[j]
      nums1[pos] = nums1[i]
      i -= 1
    else
      nums1[pos] = nums2[j]
      j -= 1
    end
    pos -= 1
  end

  while j > -1
    nums1[pos] = nums2[j]
    j -= 1
    pos -= 1
  end
end

a = Array(1..10)
b = Array(3..12)
p merge(a, 10, b, 10)
p merge([0], 0, [1], 1)
