#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (44.33%)
# Total Accepted:    4.3K
# Total Submissions: 9.5K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
#
#
#
# Example 1:
#
#
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#
#
#
#
# Note:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
#
#
#
#
#
#


class Solution:
    def longestStrChain(self, words):
        res = {}
        for w in sorted(words, key=len):
            res[w] = max(res.get(w[:i] + w[i + 1:], 0) +
                         1 for i in range(len(w)))
        return max(res.values())


# s = Solution()
# words = ["a","b","ba","bca","bda","bdca"]
# print(s.longestStrChain(words))
