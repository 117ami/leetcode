# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
# Example 1:
# Input: &quot;3+2*2&quot;
# Output: 7
# Example 2:
# Input: &quot; 3/2 &quot;
# Output: 1
# Example 3:
# Input: &quot; 3+5 / 2 &quot;
# Output: 5
# Note:
#   You may assume that the given expression is always valid.
#   Do not use the eval built-in library function.
#

# @param {String} s
# @return {Integer}
def calculate(s)
  stack = s.split(/\s|(\d+)/).reject { |i| i == '' }
  (1..stack.size - 1).step(2) do |i|
    next if stack[i] == '+' || stack[i] == '-'
    stack[i + 1] = if stack[i] == '*'
                     stack[i - 1].to_i * stack[i + 1].to_i
                   else
                     (stack[i - 1].to_f / stack[i + 1].to_f).to_i
                   end
    stack[i - 1] = 0
    stack[i] = i > 2 ? stack[i - 2] : '+'
  end
  (1..stack.size - 1).step(2) do |i|
    stack[i + 1] = if stack[i] == '+'
                     stack[i - 1].to_i + stack[i + 1].to_i
                   else
                     stack[i - 1].to_i - stack[i + 1].to_i
                   end
  end
  stack[-1].to_i
end

s = '4 * 2 + 4 *4 -2 * 4/ 5'
#s = '3+2*2'
#s = ' 3/2 '
#s = ' 3+5 / 2 '
#s = '12-3*4'
p calculate(s)
