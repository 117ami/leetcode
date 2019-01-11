#
# @lc app=leetcode id=420 lang=python3
#
# [420] Strong Password Checker
#
# https://leetcode.com/problems/strong-password-checker/description/
#
# algorithms
# Hard (18.36%)
# Total Accepted:    5.6K
# Total Submissions: 30.8K
# Testcase Example:  '""'
#
# A password is considered strong if below conditions are all met:
# 
# 
# ⁠It has at least 6 characters and at most 20 characters. 
# ⁠It must contain at least one lowercase letter, at least one uppercase
# letter, and at least one digit. 
# ⁠It must NOT contain three repeating characters in a row ("...aaa..." is
# weak, but "...aa...a..." is strong, assuming other conditions are met). 
# 
# 
# Write a function strongPasswordChecker(s), that takes a string s as input,
# and return the MINIMUM change required to make s a strong password. If s is
# already strong, return 0.
# 
# Insertion, deletion or replace of any one character are all considered as one
# change.
#
class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        if self.already_strong(s): return 0
        if len(s) <= 4: return 6 - len(s)
        


    def already_strong(self, s):
    	slen = len(s)
    	if slen < 6 or slen > 20: return False
    	lowercase = uppercase = digit = False
    	for i, c in enumerate(s):
    		if i >= 2 and c == s[i-1] and c == s[i-2]:
    			return False
    		if c.islower(): lowercase = True
    		if c.isupper(): uppercase = True
    		if c.isdigit(): digit = True

    	return all([lowercase, uppercase, digit])

s = 'aeiouuBu23'
print(Solution().already_strong(s))




