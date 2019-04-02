#
# @lc app=leetcode id=995 lang=python3
#
# [995] Minimum Number of K Consecutive Bit Flips
#
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/
#
# algorithms
# Hard (50.20%)
# Total Accepted:    3.9K
# Total Submissions: 7.7K
# Testcase Example:  '[0,1,0]\n1'
#
# In an array A containing only 0s and 1s, a K-bit flip consists of choosing a
# (contiguous) subarray of length K and simultaneously changing every 0 in the
# subarray to 1, and every 1 in the subarray to 0.
#
# Return the minimum number of K-bit flips required so that there is no 0 in
# the array.  If it is not possible, return -1.
#
#
#
# Example 1:
#
#
# Input: A = [0,1,0], K = 1
# Output: 2
# Explanation: Flip A[0], then flip A[2].
#
#
#
# Example 2:
#
#
# Input: A = [1,1,0], K = 2
# Output: -1
# Explanation: No matter how we flip subarrays of size 2, we can't make the
# array become [1,1,1].
#
#
#
# Example 3:
#
#
# Input: A = [0,0,0,1,0,1,1,0], K = 3
# Output: 3
# Explanation:
# Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
# Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
# Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
#
#
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 30000
# 1 <= K <= A.length
#
#


class Solution(object):
    def minKBitFlips(self, A, K):
        cur = res = 0
        for i in range(len(A)):
            if i >= K and A[i - K] == 2:
                cur -= 1
            if (cur % 2) == A[i]:
                if i + K > len(A):
                    return -1
                A[i] = 2
                cur, res = cur + 1, res + 1
        return res


A = [0, 0, 1, 1, 1]
K = 3
print(Solution().minKBitFlips(A, K))
