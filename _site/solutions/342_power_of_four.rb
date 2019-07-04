# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?

# @param {Integer} num
# @return {Boolean}
def is_power_of_four(num)
  num & (num - 1) == 0 && (num - 1) % 3 == 0
end

(0..10_000).each do |i|
  p i if is_power_of_four(i)
end
