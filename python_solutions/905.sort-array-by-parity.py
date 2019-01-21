#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (71.54%)
# Total Accepted:    54.7K
# Total Submissions: 76.1K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#
#
#
# Example 1:
#
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
#
#
#


class Solution:
    def sortArrayByParity(self, a):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(a) - 1
        while i <= j:
        	if a[i] & 1:
        		a[i], a[j] = a[j], a[i]
        		j -= 1
        	else:
        		i += 1
        return a


a = [10, 3, 1, 2, 4]
print(Solution().sortArrayByParity(a))
