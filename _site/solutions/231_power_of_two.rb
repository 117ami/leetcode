# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
# Input: 1
# Output: true
# Example 2:
#
# Input: 16
# Output: true

# @param {Integer} n
# @return {Boolean}
def is_power_of_two(n)
  return true if n == 1
  r = 2
  r *= 2 while r < n
  r == n
end

def is_power_of_two2(n)
  return true if n < 1
  n & (n - 1) == 0
end

(1..20).each do |i|
  p [i, is_power_of_two(i)]
  p [i, is_power_of_two2(i)]
end

p 3 & 2
