#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (40.36%)
# Total Accepted:    134.5K
# Total Submissions: 333.2K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = dict.fromkeys(list("aeiouAEIOU"), True)
        tmp = [i for i in list(s) if i in vowels]
        res = ''.join([tmp.pop() if i in vowels else i for i in list(s)])
        return res


sss = "aA"
print(Solution().reverseVowels(sss))

