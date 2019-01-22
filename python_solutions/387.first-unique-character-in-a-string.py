#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (48.34%)
# Total Accepted:    211.6K
# Total Submissions: 435.5K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
from collections import Counter
class Solution:
    def firstUniqChar(self, s):
    	seen = set()
    	for c in s:
    		if c in seen: continue
    		l, r = s.find(c), s.rfind(c)
    		if l == r: return l 
    		seen.add(c)
    	return -1


    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        return min([idx for idx, char in enumerate(s) if c[char] == 1] or [-1])
        # for i in range(len(s)):
        # 	if c[s[i]] == 1:
        # 		return i
        # return -1 



# s = 'loveleetcode'      
# print(Solution().firstUniqChar(s))

# print(ord('a'))
# print(chr(98))

