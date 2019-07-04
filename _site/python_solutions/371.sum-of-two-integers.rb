#
# @lc app=leetcode id=371 lang=ruby
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.97%)
# Total Accepted:    132.9K
# Total Submissions: 260.8K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
#
#
# Example 1:
#
#
# Input: a = 1, b = 2
# Output: 3
#
#
#
# Example 2:
#
#
# Input: a = -2, b = 3
# Output: 1
#
#
#
#
#
# @param {Integer} a
# @param {Integer} b
# @return {Integer}

# def get_sum(a, b)
#   maxn = 0x7FFFFFFF
#   mask = 0xFFFFFFFF
# 	p Array(a).pack('l').unpack('l')#.first  
# 	p Array(b).pack('l').unpack('l')#.first  	
#   until b.zero?
#     t = a
#     a = (a ^ b) & mask
#     b = ((t & b) << 1) & mask
#   end
#   a <= maxn ? a : ~(a ^ mask)
# end

def get_sum(a, b)
 p [a, b]	
    a = Array(a).pack('l').unpack('l').first
    b = Array(b).pack('l').unpack('l').first
    
    return b if a.zero?
    return a if b.zero?
    
    return get_sum(a^b, (a&b) << 1)
end
a = -1
b = 1

p get_sum(a, b)

