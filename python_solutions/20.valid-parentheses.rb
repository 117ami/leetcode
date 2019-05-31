#
# @lc app=leetcode id=20 lang=ruby
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.49%)
# Total Accepted:    593.6K
# Total Submissions: 1.6M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#
# @param {String} s
# @return {Boolean}
def is_valid(s)
  stack = []
  s.each_char do |c|
    if c == ')'
      return false if stack.empty? || stack.pop != '('
    elsif c == ']'
      return false if stack.empty? || stack.pop != '['
    elsif c == '}'
      return false if stack.empty? || stack.pop != '{'
    else
      stack << c
    end
  end
  stack.empty?
end

s = '([])'
p is_valid(s)
