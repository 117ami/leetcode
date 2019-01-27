#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#
# https://leetcode.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (33.13%)
# Total Accepted:    13.3K
# Total Submissions: 39.5K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# Let's call any (contiguous) subarray B (of A) a mountain if the following
# properties hold:
#
#
# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] <
# B[i] > B[i+1] > ... > B[B.length - 1]
#
#
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain. 
#
# Return 0 if there is no mountain.
#
# Example 1:
#
#
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
#
# Example 2:
#
#
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
#
# Note:
#
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
#
#
# Follow up:
#
#
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
#
#
#


class Solution:
    def longestMountain(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = up = down = 0
        for i in range(1, len(a)):
            if down and a[i - 1] < a[i] or a[i - 1] == a[i]:
                up = down = 0
            up += a[i - 1] < a[i]
            down += a[i - 1] > a[i]
            if up and down:
                ans = max(ans, up + down + 1)

        return ans if ans > 2 else 0


a = [2, 1, 4, 7, 3, 2, 5]
a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a = [2, 2, 2, 2, 2, 3, 2]
# a = [0]
# a = [0,2,2]
# a = [2,3,3,2,0,2]
print(Solution().longestMountain(a))
