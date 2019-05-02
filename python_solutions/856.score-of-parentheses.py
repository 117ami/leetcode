#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (55.72%)
# Total Accepted:    17.1K
# Total Submissions: 30.6K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
#
#
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
#
#
#
#
# Example 1:
#
#
# Input: "()"
# Output: 1
#
#
#
# Example 2:
#
#
# Input: "(())"
# Output: 2
#
#
#
# Example 3:
#
#
# Input: "()()"
# Output: 2
#
#
#
# Example 4:
#
#
# Input: "(()(()))"
# Output: 6
#
#
#
#
# Note:
#
#
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
#
#
#
#
#
#
#


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                n = 0
                while stack[-1] != '(':
                    n += stack.pop()
                stack[-1] = max(1, 2 * n)

        return sum(stack)


S = '(()(()))'
print(Solution().scoreOfParentheses(S))
