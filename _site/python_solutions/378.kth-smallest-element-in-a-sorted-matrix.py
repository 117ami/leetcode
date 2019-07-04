#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (49.69%)
# Total Accepted:    113K
# Total Submissions: 227.4K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
#
#
# Example:
#
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
#


class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo <= hi:
            mid = (lo + hi) // 2
            ct = self.lessEqualNumber(matrix, mid)
            if ct < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def lessEqualNumber(self, matrix, val):
        res = 0
        n = len(matrix)
        i, j = n - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] > val:
                i -= 1
            else:
                res += i + 1
                j += 1
        return res


s = Solution()
matrix = [[1, 5, 9],
          [10, 11, 13],
          [12, 13, 15]]
print(s.lessEqualNumber(matrix, 12))
print(s.kthSmallest(matrix, 7))
