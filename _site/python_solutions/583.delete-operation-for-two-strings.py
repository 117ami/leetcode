#
# @lc app=leetcode id=583 lang=python
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (43.87%)
# Total Accepted:    25.1K
# Total Submissions: 57.3K
# Testcase Example:  '"sea"\n"eat"'
#
#
# Given two words word1 and word2, find the minimum number of steps required to
# make word1 and word2 the same, where in each step you can delete one
# character in either string.
#
#
# Example 1:
#
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
#
#
#
# Note:
#
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
#
#
#


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return len(word2) + len(word1) - \
            self.longestCommonSubstr(word1, word2) * 2

    def longestCommonSubstr(self, word1, word2):
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for j in range(len(word2) + 1):
            dp[0][j] = 0

        dp[len(word1)][0] = 0
        for i in range(len(word1)):
            dp[i][0] = 0
            for j in range(len(word2)):
                dp[i + 1][j + 1] = dp[i][j] + 1 if word1[i] == word2[j] else max(
                    dp[i + 1][j], dp[i][j + 1])
        # print(dp)
        return dp[-1][-1]


word1 = "sea"
word2 = "eat"
word1 = "sea"
word2 = "ate"
# print(Solution().minDistance(word1, word2))
print(Solution().longestCommonSubstr(word1, word2))
