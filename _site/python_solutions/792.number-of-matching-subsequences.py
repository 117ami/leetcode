#
# @lc app=leetcode id=792 lang=python
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (39.75%)
# Total Accepted:    14.8K
# Total Submissions: 37.2K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
#
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
#
#
# Note:
#
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
#
#
#
from collections import Counter


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        freqs = Counter(words)
        ans = 0
        for w in list(freqs):
            if self.isSubsequence(w, S):
                ans += freqs[w]
        return ans

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        it = iter(t)
        if all(c in it for c in s):
            return True
        return False


S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(Solution().numMatchingSubseq(S, words))
