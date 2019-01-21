#
# @lc app=leetcode id=717 lang=ruby
#
# [717] 1-bit and 2-bit Characters
#
# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (48.65%)
# Total Accepted:    33.9K
# Total Submissions: 69.5K
# Testcase Example:  '[1,0,0]'
#
# We have two special characters. The first character can be represented by one
# bit 0. The second character can be represented by two bits (10 or 11).
#
# Now given a string represented by several bits. Return whether the last
# character must be a one-bit character or not. The given string will always
# end with a zero.
#
# Example 1:
#
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character. So the
# last character is one-bit character.
#
#
#
# Example 2:
#
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character. So the
# last character is NOT one-bit character.
#
#
#
# Note:
# 1 .
# bits[i] is always 0 or 1.
#
#
# @param {Integer[]} bits
# @return {Boolean}
def is_one_bit_character(bits)
  bits.shift if bits.shift == 1 while bits.size > 1
  !bits.empty?
end

bits = [1, 1, 1, 0, 0]
p is_one_bit_character(bits)
