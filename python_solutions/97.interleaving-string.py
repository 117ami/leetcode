#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (28.01%)
# Total Accepted:    111.8K
# Total Submissions: 398.7K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
#


def twoDArray(m, n, v=0):
    return [[v] * n for _ in range(m)]


class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n, k = len(s1), len(s2), len(s3)
        if m + n != k:
            return False
        dp = twoDArray(m + 1, n + 1, False)

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                                ) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[m][n]


s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
s1, s2, s3 = "a", "b", "ab"
print(s.isInterleave(s1, s2, s3))
