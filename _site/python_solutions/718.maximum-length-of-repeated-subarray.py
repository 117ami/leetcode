#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (46.27%)
# Total Accepted:    35.1K
# Total Submissions: 75.8K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
#
# Example 1:
#
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#
#
# Note:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#
#
#
class Solution:
    def findLength(self, A,B):
        def check(i):
            seen = set(A[x:x + i] for x in range(len(A) - i + 1))
            return any(B[x:x + i] in seen for x in range(len(B) - i + 1))
        
        l, r = 0, min(len(A), len(B))
        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + (l == mid)
            else:
                r = mid - 1
        return l if check(l) else l - 1

a, b = [1, 2, 3, 2, 1], [3, 2, 1, 4, 7]
# a, b = [0, 1, 1, 1, 1], [1, 0, 1, 0, 1]
s = Solution()
print(s.findLength(a, b))
