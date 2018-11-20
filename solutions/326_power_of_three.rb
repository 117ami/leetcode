# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
# Input: 27
# Output: true

# @param {Integer} n
# @return {Boolean}
def is_power_of_three(n)
  return true if n == 1
  r = 1
  r *= 3 while r < n
  r == n
end

(1..29).each do |i|
  p [i, is_power_of_three(i)]
end
