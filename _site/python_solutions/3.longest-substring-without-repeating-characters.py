#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.12%)
# Total Accepted:    862.5K
# Total Submissions: 3.1M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#


class Solution:
    def lengthOfLongestSubstring(self, s):
        res = 0
        char2index = {}
        leftmost = -1
        for i, c in enumerate(s):
            cur = char2index.get(c, -1)
            if cur > leftmost:
                leftmost = cur
            char2index[c] = i
            res = max(res, i - leftmost)
        return res


s = 'bbbbb'
# s = 'tmmzuxt'
print(Solution().lengthOfLongestSubstring(s))
