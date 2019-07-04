#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (46.30%)
# Total Accepted:    58.1K
# Total Submissions: 125.5K
# Testcase Example:  '"bbbab"'
#
# 
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# 
# Example 1:
# Input: 
# 
# "bbbab"
# 
# Output: 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# Input:
# 
# "cbbd"
# 
# Output:
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
#
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        if s == s[::-1]: return n         
        cur = [0] * n

        for i in range(len(s))[::-1]:
            pre = cur[:]
            cur[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    cur[j] = 2 + pre[j-1]
                else:
                    cur[j] = max(cur[j-1], pre[j])
        return cur[-1]
        



s = Solution()
st = 'bbbab'
print(s.longestPalindromeSubseq(st))


