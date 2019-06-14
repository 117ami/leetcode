#
# @lc app=leetcode id=5086 lang=python3
#
# [5086] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (33.27%)
# Total Accepted:    1.4K
# Total Submissions: 3.8K
# Testcase Example:  '"cdadabcc"'
#
# Return the lexicographically smallest subsequence of text that contains all
# the distinct characters of text exactly once.
#
#
#
# Example 1:
#
#
# Input: "cdadabcc"
# Output: "adbc"
#
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: "abcd"
#
#
#
# Example 3:
#
#
# Input: "ecbacba"
# Output: "eacb"
#
#
#
# Example 4:
#
#
# Input: "leetcode"
# Output: "letcod"
#
#
#
#
# Note:
#
#
# 1 <= text.length <= 1000
# text consists of lowercase English letters.
#
#
#
#
#
#
#
#
import collections


class Solution:
    def smallestSubsequence(self, text):
        cnt = collections.Counter(text)
        st = []
        seen = {}
        for c in text:
            cnt[c] -= 1
            if c in seen and seen[c] > 0:
                continue
            seen[c] = seen.get(c, 0) + 1
            while len(st) > 0 and st[-1] > c and cnt[st[-1]] > 0:
                z = st.pop()
                seen[z] = 0
            st.append(c)
        return ''.join(st)


s = Solution()
print(s.smallestSubsequence('cdadabcc'))
