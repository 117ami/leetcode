#
# Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.
# If there is no solution for the equation, return "No solution".
# If there are infinite solutions for the equation, return "Infinite solutions".
# If there is exactly one solution for the equation, we ensure that the value of x is an integer.
# Example 1:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:
# Input: "x=x"
# Output: "Infinite solutions"
# Example 3:
# Input: "2x=x"
# Output: "x=0"
# Example 4:
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
# Example 5:
# Input: "x=x+2"
# Output: "No solution"
#
#  https://leetcode.com/problems/solve-the-equation/description/
require './aux.rb'

# @param {String} equation
# @return {String}
def solve_equation(equation)
  ss = equation.split('=')
  lxn, ln = parse_formula(ss.first)
  rxn, rn = parse_formula(ss.last)
  xn = lxn - rxn
  n = rn - ln
  return 'Infinite solutions' if xn.zero? && n.zero?
  return 'No solution' if xn.zero?
  sol = n / xn
  "x=#{sol}"
end

def parse_formula(s)
  xn = n = 0
  symbols = s.scan(/[-+]/)
  symbols.unshift('+')
  s.split(/[+-]/).each_with_index do |item, idx|
    if item.end_with?('x')
      co = item.scan(/\d+/)
      co = co.empty? ? 1 : co.first.to_i
      co *= -1 if symbols[idx] == '-'
      xn += co
    else
      n += symbols[idx] == '+' ? item.to_i : item.to_i * -1
    end
  end
  [xn, n]
end

s = '7+x-3x+9-3+9x-23+x=-2+-9x+3'
s = '3x=x'
s = '2x+3x-6x=x+2'
# s = "x+5-3+x=6+x-2"
p solve_equation(s)
