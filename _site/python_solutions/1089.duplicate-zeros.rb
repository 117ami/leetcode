#
# @lc app=leetcode id=1089 lang=ruby
#
# [1089] Duplicate Zeros
#
# https://leetcode.com/problems/duplicate-zeros/description/
#
# algorithms
# Easy (58.86%)
# Total Accepted:    3.8K
# Total Submissions: 6.4K
# Testcase Example:  '[1,0,2,3,0,4,5,0]'
#
# Given a fixed length array arr of integers, duplicate each occurrence of
# zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return
# anything from your function.
#
#
#
# Example 1:
#
#
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
#
#
# Example 2:
#
#
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
#
#
#
#
# Note:
#
#
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
#
#
# @param {Integer[]} arr
# @return {Void} Do not return anything, modify arr in-place instead.
def duplicate_zeros(arr)
  return if arr.reduce(:*) > 0

  m = arr.size
  i = 0
  while i < m
    if arr[i].zero?
      arr.insert(i, 0)
      arr.pop
      i += 2
    else
      i += 1
    end
  end
end

arr = [1, 0, 2, 3, 0, 4, 5, 0]
p duplicate_zeros(arr)
