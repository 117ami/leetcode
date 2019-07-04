#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Best Sightseeing Pair
#
# https://leetcode.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (41.57%)
# Total Accepted:    3.6K
# Total Submissions: 8.3K
# Testcase Example:  '[8,1,5,2,6]'
#
# Given an array A of positive integers, A[i] represents the value of the i-th
# sightseeing spot, and two sightseeing spots i and j have distance j - i
# between them.
#
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) :
# the sum of the values of the sightseeing spots, minus the distance between
# them.
#
# Return the maximum score of a pair of sightseeing spots.
#
#
#
# Example 1:
#
#
# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
#
#
#
#
# Note:
#
#
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
#
#


class Solution:
    def maxScoreSightseeingPair(self, a):
        ans = a[0] + a[1] - 1
        pre = a[1]
        premax = ans
        for n in a[2:]:
            premax = max(premax + n - pre - 1, n + pre - 1)
            ans = max(premax, ans)
            pre = n
        return ans


a = [8, 1, 5, 2, 6]
a = [1, 3, 5]
print(Solution().maxScoreSightseeingPair(a))
