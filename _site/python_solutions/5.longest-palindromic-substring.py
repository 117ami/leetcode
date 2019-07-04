#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.16%)
# Total Accepted:    542.5K
# Total Submissions: 2M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#


class Solution:
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        maxlen = 1
        start, i = 0, 0
        while i < len(s):
            j = i - 1
            while i < len(s) and s[i] == s[j + 1]:
                i += 1

            k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                k += 1
                j -= 1

            if k - j - 1 > maxlen:
                maxlen = k - j - 1
                start = j + 1

        return s[start:start + maxlen]


s = Solution()
st = "eabcba"
print(s.longestPalindrome(st))
