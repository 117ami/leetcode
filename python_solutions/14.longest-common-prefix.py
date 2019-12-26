from collections import Counter, defaultdict, OrderedDict
from bisect import bisect_left, bisect_right 
true = True
false = False
#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.47%)
# Total Accepted:    603.9K
# Total Submissions: 1.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        strs.sort()
        res = ''
        for c in strs[0]:
            if strs[-1].startswith(res + c):
                res += c 
            else:
                return res 
        return res 
        
        

s = Solution()
ss = ["flower","flow","flight"]
ss = ["dog","racecar","car"]
ss = ["a", "b"]
print(s.longestCommonPrefix(ss))

