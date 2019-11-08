#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (45.89%)
# Total Accepted:    13.5K
# Total Submissions: 29.3K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an array A of positive integers, call a (contiguous, not necessarily
# distinct) subarray of A good if the number of different integers in that
# subarray is exactly K.
#
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
#
# Return the number of good subarrays of A.
#
#
#
# Example 1:
#
#
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#
#
# Example 2:
#
#
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
#
#
#
#
# Note:
#
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
#
#
import collections


class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atmostk(A, K) - self.atmostk(A, K - 1)

    def atmostk(self, A, K):
        c = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if c[A[j]] == 0:
                K -= 1
            c[A[j]] += 1

            while K < 0:
                c[A[i]] -= 1
                if c[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res


s = Solution()
A = [1, 2, 1, 3, 4]
K = 3
print(s.subarraysWithKDistinct2(A, K))
