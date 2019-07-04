#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (55.98%)
# Total Accepted:    22.7K
# Total Submissions: 40.7K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#
class Solution:
    def reverseOnlyLetters(self, s):
    	i = 0 
    	j = len(s) - 1
    	s = list(s)
    	while i < j:
    		while i < j and not s[i].isalpha(): i += 1
    		while i < j and not s[j].isalpha(): j -= 1
    		s[i], s[j] = s[j], s[i]
    		i += 1
    		j -= 1
    		print(i, j)
    	return ''.join(s)


print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!")    	)

        
