#
# @lc app=leetcode id=856 lang=ruby
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
# @param {String} s
# @return {Integer}
def score_of_parentheses(s)
  stack = []
  s.each_char do |c|
    if c == '('
      stack << c
    else
    	n = 0
        n += stack.pop while stack.last != '('
        stack[-1] = [2 * n, 1].max
    end
  end
  stack.reduce(:+)
end

s = '(()(()))'
s = '()()'
p score_of_parentheses(s)
