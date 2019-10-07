#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
# https://leetcode.com/problems/unique-number-of-occurrences/description/
#
# algorithms
# Easy (74.36%)
# Total Accepted:    12.1K
# Total Submissions: 16.3K
# Testcase Example:  '[1,2,2,1,1,3]'
#
# Given an array of integers arr, write a function that returns true if and
# only if the number of occurrences of each value in the array is unique.
#
#
# Example 1:
#
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
# values have the same number of occurrences.
#
# Example 2:
#
#
# Input: arr = [1,2]
# Output: false
#
#
# Example 3:
#
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
#
#
#
import collections


class Solution:
    def uniqueOccurrences(self, arr):
        vs = collections.Counter(arr)
        return len(vs.values()) == len(set(vs.values()))


s = Solution()
arr = [1, 2, 3, 2, 1, 1, 3]
print(s.uniqueOccurrences(arr))
