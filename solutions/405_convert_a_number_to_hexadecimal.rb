# coding: utf-8
#
# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
# Note:
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:
# Input:
# 26
# Output:
# "1a"
# Example 2:
# Input:
# -1
# Output:
# "ffffffff"
#
# @param {Integer} num
# @return {String}
def to_hex(num)
  return '0' if num.zero?
  hex = '0123456789abcdef'
  cter = 0
  res = []
  while !num.zero? && cter < 8
    cter += 1
    res << hex[num & 0xf]
    num = num >> 4
  end
  res.reverse.join
end

[0, 1, -1, 2_147_483_647, -2, 2].each do |i|
  p [i, to_hex(i)]
end
