from collections import Counter, defaultdict
from bisect import bisect_left, bisect_right
true = True
false = False
#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (26.92%)
# Total Accepted:    236.1K
# Total Submissions: 876.6K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#
#


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        longest = 0
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                if len(st):
                    if s[st[-1]] == '(':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)

        # print(st)
        if not st:
            return len(s)
        a, b = len(s), 0
        while len(st):
            b = st.pop()
            longest = max(longest, a - b - 1)
            a = b
        longest = max(longest, a)
        return longest


s = Solution()
ss = "(()"
ss = ")()())"
# ss = "()(()"
ss = "())"
print(s.longestValidParentheses(ss))
