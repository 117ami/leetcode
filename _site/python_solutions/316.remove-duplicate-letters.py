#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (31.54%)
# Total Accepted:    51.3K
# Total Submissions: 161.8K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example 1:
# 
# 
# Input: "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: "cbacdcbc"
# Output: "acdb"
# 
#

from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s):
    	if not s: return s
    	letters = set(s)
    	for l in sorted(letters):
    		if set(s[s.index(l):]) == letters:
    			return l + self.removeDuplicateLetters(s[s.index(l):].replace(l, ''))

    def removeDuplicateLetters2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        pos = 0
        cache = Counter(s)
        for i in range(len(s)):
        	if s[i] < s[pos]: pos = i
        	cache[s[i]] -= 1
        	if cache[s[i]] == 0: break
        # print(pos, s[pos])
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))



s = 'cbacdcbc'
# s = 'abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba' * 3000
print(Solution().removeDuplicateLetters(s))
