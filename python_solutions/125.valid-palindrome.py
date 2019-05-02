#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.83%)
# Total Accepted:    345.9K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
    	import re
    	s = (re.sub('[^0-9A-Za-z]+', '', s)).lower()
    	return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
