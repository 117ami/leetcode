#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (62.11%)
# Total Accepted:    337K
# Total Submissions: 542.3K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# Example 1:
# 
# 
# 
# Input: "hello"
# Output: "olleh"
# 
# 
# 
# Example 2:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"
# 
# 
# 
# 
#
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


        