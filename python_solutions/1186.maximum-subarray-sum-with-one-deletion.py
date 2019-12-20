#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
#
# algorithms
# Medium (34.77%)
# Total Accepted:    8.8K
# Total Submissions: 25.4K
# Testcase Example:  '[1,-2,0,3]'
#
# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion. In other words, you
# want to choose a subarray and optionally delete one element from it so that
# there is still at least one element left and the sum of the remaining
# elements is maximum possible.
#
# Note that the subarray needs to be non-empty after deleting one element.
#
#
# Example 1:
#
#
# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the
# subarray [1, 0, 3] becomes the maximum value.
#
# Example 2:
#
#
# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.
#
#
# Example 3:
#
#
# Input: arr = [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty. You can't choose [-1]
# and delete -1 from it, then get an empty subarray to make the sum equals to
# 0.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i] <= 10^4
#
#


class Solution:
    def maximumSum(self, arr):
        max1 = max0 = res = arr[0] # max sum with at most one deletion, with no deletion, and final result 
        for n in arr[1:]:
            max1 = max(max1 + n, n, max0)
            max0 = max(max0 + n, n)
            res = max(max1, res)
        return res 

s = Solution()
arr = [1, -2, 1, 3, 0, -2, 7]
arr = [1, -2, -2, 3]
arr = [8, -1, 6, -7, -4, 5, -4, 7, -6]
# arr = [-1, -1, -1, -1]
# arr = [1, -2, 0, 3]
print(s.maximumSum(arr))
