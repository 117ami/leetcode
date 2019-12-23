import re
from collections import Counter, defaultdict
true = True
false = False
#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (52.60%)
# Total Accepted:    87.5K
# Total Submissions: 166.4K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#


class Solution:
    def diffWaysToCompute(self, input):
        if input.isnumeric():
            return [int(input)]
        res = []
        i = 0
        while i < len(input):
            if input[i] == '*':
                res += [a * b for a in self.diffWaysToCompute(
                    input[:i]) for b in self.diffWaysToCompute(input[i + 1:])]
                print(input, res)
            elif input[i] == '-':
                res += [a - b for a in self.diffWaysToCompute(
                    input[:i]) for b in self.diffWaysToCompute(input[i + 1:])]
            elif input[i] == '+':
                res += [a + b for a in self.diffWaysToCompute(
                    input[:i]) for b in self.diffWaysToCompute(input[i + 1:])]
            i += 1
        # print(input,res)
        return res


s = Solution()
ss = "2*3-4*5"
# ss = "3-4*5"
print(s.diffWaysToCompute(ss))

print("-9".isnumeric())
