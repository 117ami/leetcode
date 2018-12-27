#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (42.13%)
# Total Accepted:    34K
# Total Submissions: 80.6K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1.
#
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
#
#
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
#
#
#
# Note:
# The length of the given binary array will not exceed 50,000.
#
#


class Solution:
	def findMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		d = 0
		diff = {0: [-1, -1]}
		res = 0
		for i, e in enumerate(nums):
			d = d + 1 if e else d - 1
			if d not in diff:
				diff[d] = [i, i]
			else:
				diff[d][1] = i
		return max(v[1] - v[0] for v in diff.values())


nums = [0, 1, 0, 0, 1, 0, 1, 1, 1, 1]
# nums = [0, 1]
print(Solution().findMaxLength(nums))
