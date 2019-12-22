#
# @lc app=leetcode id=5293 lang=python3
#
# [5293] Maximum Number of Occurrences of a Substring
#
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/
#
# algorithms
# Medium (31.39%)
# Total Accepted:    1.2K
# Total Submissions: 3.8K
# Testcase Example:  '"aababcaab"\n2\n3\n4'
#
# Given a string s, return the maximum number of ocurrences of any substring
# under the following rules:
#
#
# The number of unique characters in the substring must be less than or equal
# to maxLetters.
# The substring size must be between minSize and maxSize inclusive.
#
#
#
# Example 1:
#
#
# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# Explanation: Substring "aab" has 2 ocurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and
# maxSize).
#
#
# Example 2:
#
#
# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
#
#
# Example 3:
#
#
# Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# Output: 3
#
#
# Example 4:
#
#
# Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)
# s only contains lowercase English letters.
#
#
from collections import defaultdict


class Solution:
    def maxFreq(
            self,
            s: str,
            maxLetters: int,
            minSize: int,
            maxSize: int) -> int:
        memo = defaultdict(int)
        uniq = defaultdict(int)
        start = 0

        for i, c in enumerate(s):
            uniq[c] += 1
            # print(i, uniq, memo)
            if i - start + 1 == minSize:
                if len(uniq) <= maxLetters:
                    memo[s[start:i + 1]] += 1

                uniq[s[start]] -= 1
                if uniq[s[start]] == 0:
                    del uniq[s[start]]
                start += 1

        return max(memo.values()) if memo else 0


s = Solution()
ss, l, m, x = "aababcaab", 2, 3, 4
# ss, l, m, x = "aaaa", 1, 3, 3
# ss, l, m, x = 'abcde', 2, 3, 3
print(s.maxFreq(ss, l, m, x))
