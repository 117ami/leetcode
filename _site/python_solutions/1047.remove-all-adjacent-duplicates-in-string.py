#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (60.39%)
# Total Accepted:    4.9K
# Total Submissions: 8.1K
# Testcase Example:  '"abbaca"'
#
# Given a string S of lowercase letters, a duplicate removal consists of
# choosing two adjacent and equal letters, and removing them.
# 
# We repeatedly make duplicate removals on S until we no longer can.
# 
# Return the final string after all such duplicate removals have been made.  It
# is guaranteed the answer is unique.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.
# 
#
class Solution:
    def removeDuplicates(self, S):
    	stack = []
    	for c in S:
    		if len(stack) > 0 and stack[-1] == c:
    			stack.pop()
    		else:
    			stack.append(c)
    	return ''.join(stack)




s = Solution()
print(s.removeDuplicates('abbaca'))

