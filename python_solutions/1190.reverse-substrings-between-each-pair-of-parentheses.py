#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (58.36%)
# Total Accepted:    9.6K
# Total Submissions: 16.5K
# Testcase Example:  '"(abcd)"'
#
# You are given a string s that consists of lower case English letters and
# brackets. 
#
# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.
#
# Your result should not contain any brackets.
#
#
# Example 1:
#
#
# Input: s = "(abcd)"
# Output: "dcba"
#
#
# Example 2:
#
#
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is
# reversed.
#
#
# Example 3:
#
#
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally,
# the whole string.
#
#
# Example 4:
#
#
# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It's guaranteed that all parentheses are balanced.
#
#
#


class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for c in s:
            if len(st) == 0 or c != ')':
                st.append(c)
            elif c == ')':
                tmp = ""
                while len(st) > 0 and st[-1] != '(':
                    tmp = st[-1] + tmp
                    st.pop()
                st[-1] = tmp[::-1]  # replace '(' by reversed string
        return ''.join(st)


s = Solution()
ss = "(ed(et(oc))el)"
# ss = "a(bcdefghijkl(mno)p)q"
# ss = "(u(love)i)"
# ss = "vdgzyj()"
# ss = "ta()usw((((a))))"
print(s.reverseParentheses(ss))
