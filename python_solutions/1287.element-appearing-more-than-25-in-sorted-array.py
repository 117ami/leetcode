#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#
# algorithms
# Easy (61.66%)
# Total Accepted:    3.6K
# Total Submissions: 5.9K
# Testcase Example:  '[1,2,2,6,6,6,6,7,10]'
#
# Given an integer array sorted in non-decreasing order, there is exactly one
# integer in the array that occurs more than 25% of the time.
# 
# Return that integer.
# 
# 
# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
# 
#
import collections
class Solution:
    def findSpecialInteger(self, arr):
        return [k for k, v in collections.Counter(arr).items() if v > len(arr) // 4][0]

s = Solution()
arr = [1,2,2,6,6,6,6,7,10]
print(s.findSpecialInteger(arr))

