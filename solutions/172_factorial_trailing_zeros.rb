# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.

# @param {Integer} n
# @return {Integer}
def trailing_zeroes(n)
  r = 0
  while n > 0
    r += n / 5
    n /= 5
  end
  r
end

def trailing_zeroes_2(n)
  n.zero? ? 0 : n / 5 + trailing_zeroes_2(n / 5)
end

n = 50
p trailing_zeroes(n)
p trailing_zeroes_2(n)
