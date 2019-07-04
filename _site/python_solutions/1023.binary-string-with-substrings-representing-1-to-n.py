#
# @lc app=leetcode id=1023 lang=python3
#
# [1023] Binary String With Substrings Representing 1 To N
#
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (65.52%)
# Total Accepted:    2.7K
# Total Submissions: 4.2K
# Testcase Example:  '"0110"\n3'
#
# Given a binary string S (a string consisting only of '0' and '1's) and a
# positive integer N, return true if and only if for every integer X from 1 to
# N, the binary representation of X is a substring of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "0110", N = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: S = "0110", N = 4
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 1000
# 1 <= N <= 10^9
# 
#
class Solution:
    def queryString(self, s, n):
    	return all(bin(i)[2:] in s for i in range(n, n // 2, -1))
        


s = '0110'        
n = 4
Solution().queryString(s, n)
