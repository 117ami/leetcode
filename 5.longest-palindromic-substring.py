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
    	if s == s[::-1]: return s 
    	maxlen = 1
    	start = 0
    	for i in range(len(s)):
    		if i - maxlen >= 1 and s[i - maxlen - 1:i+1] == s[i - maxlen - 1:i+1][::-1]:
    			start = i - maxlen - 1
    			maxlen += 2
    		elif i - maxlen >= 0 and s[i - maxlen:i+1] == s[i - maxlen:i+1][::-1]:
    			start = i - maxlen
    			maxlen += 1
    	return s[start:start+maxlen]

s = Solution()
st = "babad"    	
print(s.longestPalindrome(st))
    	
        
