#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#
# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
#
# algorithms
# Hard (53.47%)
# Total Accepted:    2K
# Total Submissions: 3.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square grid of integers arr, a falling path with non-zero shifts is a
# choice of exactly one element from each row of arr, such that no two elements
# chosen in adjacent rows are in the same column.
#
# Return the minimum sum of a falling path with non-zero shifts.
#
#
# Example 1:
#
#
# Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.
#
#
#
# Constraints:
#
#
# 1 <= arr.length == arr[i].length <= 200
# -99 <= arr[i][j] <= 99
#
#
#

import heapq 
class Solution:
    def minFallingPathSum(self, arr):
        for i in range(1, len(arr)):
            r = heapq.nsmallest(2, arr[i-1])
            for j in range(len(arr[0])):
                arr[i][j] += r[1] if arr[i-1][j] == r[0] else r[0]

        return min(arr[-1])


s = Solution()
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [[-2, -18, 31, -10, -71, 82, 47, 56, -14, 42], [-95, 3, 65, -7, 64, 75, -51, 97, -66, -28], [36, 3, -62, 38, 15, 51, -58, -90, -23, -63], [58, -26, -42, -66, 21, 99, -94, -95, -90, 89], [83, -66, -42, -45, 43, 85, 51, -86, 65, -39], [56, 9, 9, 95, -56, -77, -2, 20, 78, 17], [78, -13, -55, 55, -7, 43, -98, -89, 38, 90], [32, 44, -47, 81, -1, -55, -5, 16, -81, 17], [-87, 82, 2, 86, -88, -58, -91, -79, 44, -9], [-96, -14, -52, -8, 12, 38, 84, 77, -51, 52]]
# arr = [[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2]]
# arr = [[2,2,1,2,2], [2,2,1,2,2], [2,2,1,2,2]]
print(s.minFallingPathSum(arr))
