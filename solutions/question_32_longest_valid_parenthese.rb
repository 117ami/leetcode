#!/usr/bin/ruby -w
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# @param {String} s
# @return {Integer}
def longest_valid_parentheses(s)
  stack = []
  leftnum, lastid = 0, 0
  s.chars.each do |c|
    if c == '('
      stack.push(c)
      leftnum += 1
      lastid = stack.size - 1
    elsif leftnum.zero?
      stack.push(')')
    else
      stack[lastid] = '*'
      leftnum -= 1
    end
  end

  p stack.join.split('(').map { |v| v.length }.max * 2
end

s = '(())()((((())))))(())(()))'
longest_valid_parentheses(s)
longest_valid_parentheses('()')
longest_valid_parentheses(')()())()()(')
