#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#
# https://leetcode.com/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (58.57%)
# Total Accepted:    2.2K
# Total Submissions: 3.7K
# Testcase Example:  '"!(f)"'
#
# Return the result of evaluating a given boolean expression, represented as a
# string.
#
# An expression can either be:
#
#
# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner
# expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner
# expressions expr1, expr2, ...
#
#
#
# Example 1:
#
#
# Input: expression = "!(f)"
# Output: true
#
#
# Example 2:
#
#
# Input: expression = "|(f,t)"
# Output: true
#
#
# Example 3:
#
#
# Input: expression = "&(t,f)"
# Output: false
#
#
# Example 4:
#
#
# Input: expression = "|(&(t,f,t),!(t))"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= expression.length <= 20000
# expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f',
# ','}.
# expression is a valid expression representing a boolean, as given in the
# description.
#
#
import collections


class Solution:
    def parseBoolExpr(self, e):
        self.e = e
        self.i = 0
        return self.p()

    def p(self):
        c = self.e[self.i]
        if c == 't':
            self.i += 1
            return True
        elif c == 'f':
            self.i += 1
            return False
        elif c == '!':
            return self.p_not()
        elif c == '&':
            return self.p_and()
        else:
            return self.p_or()

    def p_not(self):
        self.i += 2
        r = self.p()
        self.i += 1
        return not r

    def p_and(self):
        self.i += 2
        r = self.p()
        while self.e[self.i] != ')':
            self.i += 1
            r &= self.p()
        self.i += 1
        return r

    def p_or(self):
        self.i += 2
        r = self.p()
        while self.e[self.i] != ')':
            self.i += 1
            r |= self.p()
        self.i += 1
        return r

    def parseBoolExpr2(self, e, t=True, f=False):
        return eval(e.replace('!', 'not |').replace(
            '&(', 'all ([').replace('|(', 'any ([').replace(')', '])'))


s = Solution()
expr = "|(&(t,f,t),!(t))"
# expr = "|(t,f)"
# expr = "!(t)"
expr = "&(&(&(!(&(f)),&(t),|(f,f,t)),|(t),|(f,f,t)),!(&(|(f,f,t),&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))),&(t))),&(!(&(&(!(&(f)),&(t),|(f,f,t)),|(t),|(f,f,t))),!(&(&(&(t,t,f),|(f,f,t),|(f)),!(&(t)),!(&(|(f,f,t),&(&(f),&(!(t),&(f),|(f)),&(!(&(f)),&(t),|(f,f,t))),&(t))))),!(&(f))))"
print(s.parseBoolExpr(expr))
print(s.parseBoolExpr2(expr))
