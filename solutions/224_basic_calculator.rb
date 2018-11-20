# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
# Example 1:
# Input: &quot;1 + 1&quot;
# Output: 2
# Example 2:
# Input: &quot; 2-1 + 2 &quot;
# Output: 3
# Example 3:
# Input: &quot;(1+(4+5+2)-3)+(6+8)&quot;
# Output: 23
# Note:
#   You may assume that the given expression is always valid.
#   Do not use the eval built-in library function.
#

# @param {String} s
# @return {Integer}
def calculate(s)
  stack = []
  s.split(/(\+|\-|\(|\)|\s)/).each do |e|
    next if e == '' || e == ' '
    if e == ')'
      j = -1
      j -= 1 while stack[j] != '('
      stack[j..-1] = domath(stack[j + 1..-1])
    else
      stack << e
    end
  end
  return domath(stack) if stack.size > 1
  stack.first
end

def domath(arr)
  r = arr[0].to_i
  (1..arr.size - 1).step(2).each do |i|
    r = arr[i] == '+' ? r + arr[i + 1].to_i : r - arr[i + 1].to_i
  end
  r
end

def domath2(arr)
  until arr.size == 1
    arr[2] = arr[1] == '+' ? arr[0].to_i + arr[2].to_i : arr[0].to_i - arr[2].to_i
    arr.shift(2)
  end
  arr.first.to_i
end

s = '(1+(4+5+2)-3)+ ( 6+8)'
s = ' 2-1 + 2 '
s = '1 + 1'

p calculate(s)
