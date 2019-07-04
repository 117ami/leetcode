#
# @lc app=leetcode id=224 lang=ruby
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
# @param {String} s
# @return {Integer}
def calculate(s)
  unless s.include?('(')
    arr = s.gsub('--', '+').gsub('+', '=+=').gsub('-', '=-=').split('=')
    res = arr.shift.to_i
    until arr.empty?
      res += arr.first == '+' ? arr[1].to_i : -1 * arr[1].to_i
      arr.shift(2)
    end
    return res
  end

  stack = []
  s.each_char do |c|
    stack << c
    next unless c == ')'

    stack.pop
    next_s = ''
    next_s = stack.pop + next_s while stack.last != '('
    stack[-1] = calculate(next_s).to_s
  end
  calculate(stack.join)
end

s = '265 + (98 - 99)'
s = '(1+(4+5+2)-3)+(6+8)'
s = '(1-(5-6))'
p calculate(s)
