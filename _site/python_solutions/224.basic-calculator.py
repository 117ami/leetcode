#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (32.49%)
# Total Accepted:    105.1K
# Total Submissions: 323K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
#
# Example 1:
#
#
# Input: "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: " 2-1 + 2 "
# Output: 3
#
# Example 3:
#
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
#
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
#
#
#


class Solution:
    def calculate(self, s):
        res = num = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + ord(c) - ord('0')
            elif c == '+':
                res += num * sign
                num = 0
                sign = 1
            elif c == '-':
                res += num * sign
                num = 0
                sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return num * sign + res


s = Solution()
ss = '(1-(3-4))'
# ss = '(5-(1+(5)))'
# ss = '1-(2+3-(4+(5-(1-(2+4-(5+6))))))'
print(s.calculate(ss))
